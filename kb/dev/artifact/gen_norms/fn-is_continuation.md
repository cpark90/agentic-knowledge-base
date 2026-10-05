---
id: https://agentic-knowledge-base.dev/id/chunk/49271822-40b4-4cdd-9e5c-c787b7bd458a
type: artifact
level: executable
title_ko: 함수 is_continuation (tools/gen_norms.py)
title: function is_continuation in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `is_continuation(meta)` 다. 이어짐 절 청크(`continues: true`)인가 — 제목·깊이가 없고 번호를 소비하지 않으며 본문은 앞 묶음 뒤의 산문이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def is_continuation(meta: dict) -> bool:
    """이어짐 절 청크(`continues: true`)인가 — 제목·깊이가 없고 번호를 소비하지 않으며 본문은 앞 묶음 뒤의 산문이다."""
    return meta.get(NORM_CONTINUES_KEY) == "true"
```
<!-- 인용 끝 -->
