---
id: https://agentic-knowledge-base.dev/id/chunk/ab2cbe51-0701-4753-859c-1019a3b9808f
type: artifact
level: executable
title_ko: 함수 pair_judge_targets (tools/label_sample.py)
title: function pair_judge_targets in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `pair_judge_targets(rows)` 다. 판정 대상 — 첫 근거가 동시 편집이고 판정자 둘의 판정이 아직 없는 후보(뷰의 판정 없음 절: 단독 판정·낡은 판정 포함).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_judge_targets(rows: list[dict]) -> list[dict]:
    """판정 대상 — 첫 근거가 동시 편집이고 판정자 둘의 판정이 아직 없는 후보(뷰의 판정 없음 절: 단독 판정·낡은 판정 포함)."""
    return [r for r in rows if r["근거 종류"].split(" · ")[0] == "coEditHistory"
            and (r["판정자 값"] == kb_lib.EMPTY_NOT_APPLICABLE or kb_lib.JUDGED_NONE in r["판정자 값"])]
```
<!-- 인용 끝 -->
