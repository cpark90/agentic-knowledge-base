---
id: https://agentic-knowledge-base.dev/id/chunk/92ac1970-f252-48a0-b11a-fbaa774b2f4a
type: artifact
level: executable
title_ko: 함수 human_check_criteria (tools/kb_lib.py)
title: function human_check_criteria in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/45dfc4dd-c694-47a7-9a8c-6398612879db
---
**함수** — `human_check_criteria(g, plane)` 다. 가운데 슬롯이 `HUMAN_CHECK_SLOT` 인 합격 기준(contract 청크)의 집합 — 사람 확인 기준이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def human_check_criteria(g: Graph, plane: dict) -> set:
    """가운데 슬롯이 `HUMAN_CHECK_SLOT` 인 합격 기준(contract 청크)의 집합 — 사람 확인 기준이다."""
    return {c for c, v in g.subject_objects(AGT.bodySlot) if plane.get(c) == "contract" and str(v) == HUMAN_CHECK_SLOT}
```
<!-- 인용 끝 -->
