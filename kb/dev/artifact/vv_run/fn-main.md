---
id: https://agentic-knowledge-base.dev/id/chunk/9f97f1c4-3974-4cf9-a2d7-d09597311cae
type: artifact
level: executable
title_ko: 함수 main (tools/vv_run.py)
title: function main in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07ed26ac-e215-4583-8d9d-10f93fe1eed9, https://agentic-knowledge-base.dev/id/chunk/4819f0e8-1ed9-43cb-b206-366b65a7f00f, https://agentic-knowledge-base.dev/id/chunk/4dc64a35-fb4f-4396-838d-acef3f4e186c, https://agentic-knowledge-base.dev/id/chunk/5f53b16a-56e0-4dc8-886e-c0e202e515c8, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/b79a944c-fcdd-4100-baf7-9f03da3576b1, https://agentic-knowledge-base.dev/id/chunk/c4812ae0-4745-4e23-bcd2-a72f82d600fd, https://agentic-knowledge-base.dev/id/chunk/d213b57a-b3ec-4271-aba1-114f98f7a4c7, https://agentic-knowledge-base.dev/id/chunk/ddab0191-16a5-4584-9734-a7d026cb29f8, https://agentic-knowledge-base.dev/id/chunk/de4671f1-1f9f-4715-a852-ab91c7368807]
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", action="append", default=[], metavar="SLUG", help="이 케이스(파일 stem)만 — 반복 가능")
    ap.add_argument("--verifier", action="append", default=[], metavar="SLUG",
                    help=f"이 검증기({VERIFIER_DIR} 의 파일 stem)만 — 반복 가능. `--case`·`--verifier` 를 둘 다 안 주면 전부다")
    ap.add_argument("--record", action="store_true", help=f"결과를 실행 기록으로 {RUN_DIR}/run-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--round", choices=tuple(ROUND_REASONS), default="", metavar="REASON",
                    help=f"검증 라운드 하나를 닫는다 — {RUN_DIR}/{ROUND_PREFIX}<UTC>.md 를 append-only 로 쓰고 케이스는 돌리지 않는다. "
                         f"종료 사유는 {' · '.join(ROUND_REASONS)} 중 하나다 (유저 답 Q39-c)")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    ap.add_argument("--waivers", default=WAIVERS, metavar="FILE",
                    help=f"docs/waivers.md — 게이트 id `{CASE_GATE}`(축 파일·stem)로 면제된 케이스의 형식 오류는 집계에서 빼되 목록에 남긴다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("--vocab", default="", metavar="FILE",
                    help=f"토큰 계수기 어휘 파일 — 검증기 명령에 {kb_lib.TOKENIZER_VOCAB_ENV} 로 넘긴다. "
                         "타깃이 `--vocab=$(rootpath @tiktoken_o200k_base//file)` 로 준다. 못 찾으면 돌지 않는다")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    if not (root / CASE_DIR).is_dir():
        print(f"FAIL [vv_run] {CASE_DIR}: 케이스 디렉토리가 없다 — 워크스페이스 루트에서 돌린다")
        return EXIT_CONFIG
    if a.round:  # 라운드 경계 기록 — 케이스를 돌리지 않으므로 어휘가 필요 없다. 다른 선택과 섞지 않는다
        if a.case or a.verifier or a.record or a.out:
            print("FAIL [vv_run] `--round` 는 라운드 경계만 기록한다 — `--case`·`--verifier`·`--record`·`--out` 과 함께 쓰지 않는다")
            return EXIT_CONFIG
        try:
            apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
        except (OSError, ValueError) as e:
            print(f"FAIL [vv_run] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        return record_round(root, a.round)
    try:  # 어휘 해소는 여기 한 자리다 — 못 찾으면 케이스를 하나도 돌리지 않는다. 건너뜀은 판정의 공백이다
        vocab = tokenizer_vocab_path(a.vocab or None).resolve()
    except FileNotFoundError as e:
        print(f"FAIL [vv_run] 토큰 계수기 어휘 — {e}. 허용 목록의 검증기(`chunk_lint` 등)는 이 어휘로 토큰을 세므로 "
              f"경로 없이는 자극에 닿지 못한다 — `bazel run //tools:vv_run`(타깃이 --vocab 을 준다) 또는 "
              f"`--vocab <경로>` 로 돌린다")
        return EXIT_CONFIG
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [vv_run] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    waiver_path = root / a.waivers
    try:
        waivers = kb_lib.load_waivers(waiver_path) if waiver_path.is_file() else []
    except ValueError as e:  # 표의 열·축이 규약 밖이면 설정 문제다 — 판정 실패가 아니다
        print(f"FAIL [vv_run] waiver 표 — {e}")
        return EXIT_CONFIG
    # 선택 — 둘 다 없으면 전부, 하나라도 있으면 준 쪽만 돈다. `--case` 만 준 실행은 검증기를 싣지 않아 케이스만의 보고·기록 꼴 그대로다
    everything = not a.case and not a.verifier
    try:
        cases, missing = load_cases(root, a.case, waivers) if everything or a.case else ([], [])
        verifiers, idle = load_items(root, "verifier", a.verifier, waivers) if everything or a.verifier else ([], [])
    except ValueError as e:  # parse_chunk 의 frontmatter 규칙 — 케이스가 청크가 아니면 실행할 수 없다
        print(f"FAIL [vv_run] {e}")
        return EXIT_CONFIG
    unknown = sorted(set(a.case) - {c["slug"] for c in cases} - set(missing))
    if unknown:
        print(f"FAIL [vv_run] --case 대상이 {CASE_DIR} 에 없다: {', '.join(unknown)}")
        return EXIT_CONFIG
    unknown = sorted(set(a.verifier) - {c["slug"] for c in verifiers} - set(idle))
    if unknown:
        print(f"FAIL [vv_run] --verifier 대상이 {VERIFIER_DIR} 에 없다: {', '.join(unknown)}")
        return EXIT_CONFIG
    if not cases and not verifiers:
        print(f"SKIP [vv_run] {CASE_DIR}: 실행할 케이스가 없다")
        return EXIT_SKIP
    # 케이스 형식 검사 — 규약 펜스를 둔 케이스만 대상이다. 형식이 깨진 케이스는 실행 전에 거부한다. 자극·기대가
    # 명령과 어긋난 채 도는 실행은 판정이 아니라 소음이다 (STYLEGUIDE §7 — 메시지가 곧 수정 안내다)
    items = cases + verifiers
    for c in items:
        if c["errors"] and c["waived"]:
            for e in c["errors"]:
                print(f"WAIVED [{CASE_GATE}] {c['path']}: {e} (waivers.md — 집계에서 뺐고 펜스를 읽지 않았다)")
    broken = [c for c in items if c["errors"] and not c["waived"]]
    if broken:
        for c in broken:
            for e in c["errors"]:
                print(f"FAIL [{CASE_GATE}] {c['path']}: {e}")
        print(f"FAIL [{CASE_GATE}] 케이스 {len(broken)}건의 형식이 규약 밖이다 — 규약은 결정 `p8-machine-readable-case` 다. "
              f"면제는 `{a.waivers}` 에 게이트 id `{CASE_GATE}` 로 선언한다")
        return EXIT_CONFIG

    now = datetime.now(timezone.utc).replace(microsecond=0)
    rev, dirty = revision(root)
    env = environment(root)
    execute(items, root, vocab)
    text = report(now, cases, missing, rev, dirty, env, verifiers, idle)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")

    if a.record:
        run_dir = root / RUN_DIR
        run_dir.mkdir(parents=True, exist_ok=True)
        target = run_dir / f"run-{now.strftime('%Y%m%dT%H%M%SZ')}.md"
        if target.exists():
            print(f"FAIL [vv_run] {target.relative_to(root)}: 이미 있다 — 실행 기록은 append-only 다 (r-026)")
            return EXIT_CONFIG
        target.write_text(observation(now, cases, rev, dirty, env, verifiers), encoding="utf-8")
        print(f"실행 기록: {target.relative_to(root)} — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    n = counts(items)
    return EXIT_FAIL if n["fail"] else EXIT_OK if n["pass"] else EXIT_SKIP
```
<!-- 인용 끝 -->
