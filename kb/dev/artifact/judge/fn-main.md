---
id: https://agentic-knowledge-base.dev/id/chunk/988b5551-bcb2-4776-83ce-290f44c435f7
type: artifact
level: executable
title_ko: 함수 main (tools/judge.py)
title: function main in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0b44a7ed-753e-4f76-bfba-efd520b3c3f1, https://agentic-knowledge-base.dev/id/chunk/136a10e2-560c-4817-b3e1-630cbe303a57, https://agentic-knowledge-base.dev/id/chunk/21357a69-21e9-470e-8d6c-43908a9308d7, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/39f2a0d8-63e6-48ef-a57b-5291a656e915, https://agentic-knowledge-base.dev/id/chunk/473ab4af-5806-45ea-a923-d7f635544fdb, https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb, https://agentic-knowledge-base.dev/id/chunk/568c9c47-0d5f-4372-a395-b07605eaeedd, https://agentic-knowledge-base.dev/id/chunk/8a58cf85-fc7e-418d-91fc-ce025cf2cff9, https://agentic-knowledge-base.dev/id/chunk/8d5e7694-cb0b-42c7-a734-a6f0e8782caf, https://agentic-knowledge-base.dev/id/chunk/d1ca967e-c2f5-4f0e-8d10-03adbb6b5c13, https://agentic-knowledge-base.dev/id/chunk/f804ba0b-8ec8-42b5-b53e-733d51e50546]
part_of: https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--question", default="", help="질문 id — 프로파일의 `agt:` 지역명 또는 전체 IRI (`--list` 에는 필요 없다)")
    ap.add_argument("--responses", action="append", default=[], metavar="JSON",
                    help="세션 판정자의 응답 — {judge, responses: [{question, fingerprint, value, confidence}]}. "
                         "판정자마다 한 번씩 반복한다 — 둘 이상이면 일치를 계산한다 (옛 --fixture 의 승격)")
    ap.add_argument("--decoys", default="", metavar="JSON",
                    help="label_sample.py --decoys 가 낸 key.json — 미끼 항목의 검출률을 보고 요약에 낸다(라벨 대표성 실험 전용)")
    ap.add_argument("--record", action="store_true",
                    help=f"판정 로그({kb_lib.JUDGE_LOG_DIR}/judge-<UTC>.md)와 결과 주석({kb_lib.JUDGE_VERDICT_DIR}/)을 쓴다")
    ap.add_argument("--into", default="", metavar="DIR", help="기록의 뿌리 — 기본은 워크스페이스다. 시험물을 밖에 두는 수단이다")
    ap.add_argument("--out", default="", metavar="FILE", help="보고를 파일로도 쓴다")
    ap.add_argument("--profile", default=PROFILE_DIR, help="질문·척도·임계의 원본 디렉토리")
    ap.add_argument("--list", action="store_true", help="등록된 질문만 나열하고 멈춘다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 판정 로그를 `memory` 상한 안으로 가르는 데 쓴다. "
                                               "없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("chunks", nargs="*", help="판정 대상 청크 파일 — 라벨 대표성 실험(`--decoys`)만 쓰면 생략할 수 있다")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))

    try:
        try:
            apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
        except (OSError, ValueError) as e:
            raise JudgeError(f"{a.residency or root / 'defs/kb.bzl'}: 값 어휘의 원본을 읽을 수 없다 — {e}")
        g = load_profile(root, a.profile, SHAPES)
        qs = questions(g)
        if a.list:
            for k, q in sorted(qs.items()):
                print(f"agt:{k} ({q['form']}) — {q['label']}")
            return EXIT_OK
        if not a.question:
            raise JudgeError("`--question <질문 id>` 가 없다 — 등록된 질문은 `--list` 가 낸다")
        name = a.question.rsplit("/", 1)[-1].removeprefix("agt:")
        if name not in qs:
            raise JudgeError(f"질문 {a.question!r} 이 프로파일에 없다 — 등록된 것은 "
                             + " · ".join(f"`agt:{k}`" for k in sorted(qs)) + f". 새 질문은 {a.profile} 에 파일로 더한다")
        q = qs[name]
        check_question(q, name)

        decoys_raw = None
        if a.decoys:
            try:
                decoys_raw = json.loads(at(root, a.decoys).read_text(encoding="utf-8"))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{a.decoys}: 미끼 목록을 읽을 수 없다 — {e}")
            if not isinstance(decoys_raw, list):
                raise JudgeError(f"{a.decoys}: label_sample.py 의 key.json 은 목록이다")
        decoy_items = [it for it in decoys_raw if isinstance(it, dict) and it.get("decoy")] if decoys_raw else []
        # 대조 지문의 원본 — key.json 은 실표본·미끼를 다 담으므로 실표본 지문도 여기서 스스로 대조한다
        # (2026-09-30 vnv 결함 보고 ①). 경로가 곧 색인 키다 — label_sample.py 가 낸 path 그대로다
        sheet_index = {it["path"]: it for it in (decoys_raw or []) if isinstance(it, dict) and it.get("path")}

        if not a.chunks and not decoy_items:
            print(f"SKIP [{TAG}] 판정 대상 0건 — PASS 가 아니다")
            return EXIT_SKIP
        if not a.responses:
            raise JudgeError("`--responses <json>` 이 없다 — 외부 서비스가 없으므로 세션 판정자의 응답을 오프라인으로 받는다")
        resp_sets = [load_responses(at(root, p)) for p in a.responses]

        th = thresholds(g)
        now = datetime.now(timezone.utc)
        rows = judge_rows(root, a.chunks, q, name, th, resp_sets, sheet=sheet_index) if a.chunks else []
        if rows:
            agreement(rows)
        decoy_hit, decoy_seen = decoy_detection_rate(decoy_items, q, resp_sets) if decoy_items else (0, 0)
        # 응답 파일의 이름만 적는다(basename) — 절대 경로는 판정 로그에 실리지 않는다(2026-09-30 vnv 결함 보고 ⑤)
        source = "세션 판정자 응답 " + " · ".join(f"`{Path(p).name}`(판정자 `{d.get('judge')}`)"
                                               for p, d in zip(a.responses, resp_sets))
        text = report(rows, q, name, th, source, now, decoy_hit, decoy_seen, len(decoy_items))
        print(text)
        if a.out:
            at(root, a.out).write_text(text, encoding="utf-8")
        if a.record:
            if not rows:
                raise JudgeError("기록할 판정 행이 없다 — `--decoys` 만으로는 판정 로그를 남기지 않는다(청크 대상이 없다)")
            try:  # 로그를 가르는 상한이 토큰이므로 계수기가 기록의 입력이다 (ODD id:cond-tokenizer-lock)
                enc = kb_lib.load_tokenizer(a.vocab or None)
            except (FileNotFoundError, ValueError) as e:
                raise JudgeError(f"어휘 파일 — {e}") from e
            written = write_records(at(root, a.into) if a.into else root, rows, q, name, th, source, now, enc)
            print("기록: " + " · ".join(p.as_posix() for p in written) +
                  " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    except JudgeError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_CONFIG
    return EXIT_OK
```
<!-- 인용 끝 -->
