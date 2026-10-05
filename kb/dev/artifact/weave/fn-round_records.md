---
id: https://agentic-knowledge-base.dev/id/chunk/12df4a74-89e1-4884-b0dc-b7c7f375d8e0
type: artifact
level: executable
title_ko: 함수 round_records (tools/weave.py)
title: function round_records in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4600b6bb-eddb-4832-9854-1c587f7929d9, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `round_records(m, by_gen)` 다. 라운드 기록 → [(시각, 청크, 종료 사유)] 오름차순 (유저 답 Q39-c).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def round_records(m: Model, by_gen) -> list:
    """라운드 기록 → [(시각, 청크, 종료 사유)] 오름차순 (유저 답 Q39-c). verify 질의 `round-stop-rule-violated` 와 같은 정의다 —
    `vv_run` 의 관측(memory) 중 본문이 종료 사유(`agt:RoundEndReason`) 하나를 인용한(`agt:usesConcept`) 것. 시각을 읽을 수 없으면 뺀다."""
    reasons = set(m.g.subjects(RDF.type, AGT.RoundEndReason))
    out = []
    for c in m.chunks:
        if m.plane[c] != "memory" or by_gen(c) != kb_lib.RUN_GENERATOR:
            continue
        cited = sorted((r for r in m.g.objects(c, AGT.usesConcept) if r in reasons), key=str)
        at = as_dt(m.at(c))
        if cited and at:
            out.append((at, c, cited[0]))
    return sorted(out, key=lambda x: (x[0], str(x[1])))
```
<!-- 인용 끝 -->
