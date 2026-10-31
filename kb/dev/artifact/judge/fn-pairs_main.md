---
id: https://agentic-knowledge-base.dev/id/chunk/37cdc474-ee6d-4363-a323-e1a7ea998ddc
type: artifact
level: executable
title_ko: 함수 pairs_main (tools/judge.py)
title: function pairs_main in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0b44a7ed-753e-4f76-bfba-efd520b3c3f1, https://agentic-knowledge-base.dev/id/chunk/21357a69-21e9-470e-8d6c-43908a9308d7, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/39f2a0d8-63e6-48ef-a57b-5291a656e915, https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb, https://agentic-knowledge-base.dev/id/chunk/5e8f0410-5a7f-4fe4-848c-4414e21924d0, https://agentic-knowledge-base.dev/id/chunk/69ceb5b2-0e90-45f9-983b-c8a56c9fda09, https://agentic-knowledge-base.dev/id/chunk/8361deae-2526-4bb1-9fd9-bb8b6899d0f2, https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/d1ca967e-c2f5-4f0e-8d10-03adbb6b5c13, https://agentic-knowledge-base.dev/id/chunk/d5ec017d-0162-43dd-bd2e-06bb28ffe5d2, https://agentic-knowledge-base.dev/id/chunk/f7d7344d-7095-485f-976f-8de7b92e5e4d]
part_of: https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac
---
**함수** — `pairs_main(a, root, qs)` 다. 쌍 모드 — key 의 쌍마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pairs_main(a, root: Path, qs: dict) -> int:
    """쌍 모드 — key 의 쌍마다 판정자 응답을 찾아 질문별로 보고하고, `--record` 면 질문마다 판정 로그와 쌍마다 결과 주석을 쓴다."""
    pairs = load_pairs(at(root, a.pairs))
    if a.question:
        name = a.question.rsplit("/", 1)[-1].removeprefix("agt:")
        pairs = [p for p in pairs if p["question"] == name]
    if not pairs:
        print(f"SKIP [{TAG}] 판정 대상 쌍 0건 — PASS 가 아니다")
        return EXIT_SKIP
    if not a.responses:
        raise JudgeError("`--responses <json>` 이 없다 — 외부 서비스가 없으므로 세션 판정자의 응답을 오프라인으로 받는다")
    resp_sets = [load_responses(at(root, p)) for p in a.responses]
    rows, tally = pair_rows(root, pairs, qs, resp_sets)
    decoy = pair_decoy_summary(tally)
    source = "세션 판정자 응답 " + " · ".join(f"`{Path(p).name}`(판정자 `{d.get('judge')}`)" for p, d in zip(a.responses, resp_sets))
    now = datetime.now(timezone.utc)
    by_q: dict = defaultdict(list)
    for r in rows:
        by_q[r["question"]].append(r)
    texts = []
    for name in sorted(by_q):
        by_q[name].sort(key=lambda r: (r["iri"], r["judge"]))  # 한 쌍의 판정자 행을 붙여 둔다 — 로그를 토큰 상한으로 갈라도 묶음마다 판정자 둘이 있다
        agreement(by_q[name])
        texts.append(report(by_q[name], qs[name], name, source, now, 0, 0, 0, pair_decoy=decoy))
    print(f"[{TAG}] 쌍 {len({p['fingerprint'] for p in pairs if not p.get('decoy')})} · 판정 행 {len(rows)} · 응답 없음 {tally['missing']} · "
          f"낡은 판정 {tally['stale']} · 미끼 — {decoy}")
    for text in texts:
        print(text)
    if a.out:
        at(root, a.out).write_text("\n".join(texts), encoding="utf-8")
    if a.record:
        if not rows:
            raise JudgeError("기록할 판정 행이 없다 — 미끼만으로는 판정 로그를 남기지 않는다")
        into, enc, shapes = record_args(a, root)
        stamp = kb_lib.utc_stamp(now)
        counts_q = {name: len(log_texts(by_q[name], qs[name], name, decoy, source, stamp, enc, shapes)[1]) for name in sorted(by_q)}
        written, first = [], 0   # 모든 질문의 로그가 shape 를 지킨 뒤에만 쓴다 — 한 질문만 쓰이고 멈추지 않는다
        for name in sorted(by_q):
            written += write_records(into, by_q[name], qs[name], name, decoy, source, now, enc, shapes, first)
            first += counts_q[name]
        print("기록: " + " · ".join(p.as_posix() for p in written) +
              " — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    return EXIT_OK
```
<!-- 인용 끝 -->
