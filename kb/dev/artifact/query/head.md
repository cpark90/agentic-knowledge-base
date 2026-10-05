---
id: https://agentic-knowledge-base.dev/id/chunk/8952bd20-8b9b-4bd8-916d-669341f4c67e
type: artifact
level: executable
title_ko: 모듈 머리 default-query-dir (tools/query.py)
title: module head default-query-dir in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/f0c1bfd1-a5d5-4710-83ce-f8ca7018e21b
---
**모듈 머리** — `tools/query.py` 의 모듈 머리 `default-query-dir` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT, ID = kb_lib.AGT, kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
DEFAULT_QUERY_DIR = "tools/cq-queries"
DEFAULT_LIMIT = 50      # 표 상한 — 컨텍스트 예산(anti-rot). 0 이면 전부
REPORT_TOP = 5          # 뷰 cq.md 의 CQ 별 상위 행 수
REPORT_CELL = 100       # 뷰의 셀 폭 상한 (문자) — CLI 는 자르지 않는다
CQ_ID = re.compile(r"^CQ-\d+$")
FORM_PREFIX = "행 = "  # .rq 머리 주석 둘째 줄의 접두 — 원문에 이미 있으므로 읽을 때 떼고 출력에서 한 번만 붙인다
```
<!-- 인용 끝 -->
