---
id: https://agentic-knowledge-base.dev/id/chunk/db6433c7-428f-434f-8aa1-abbcaec51063
type: artifact
level: executable
title_ko: 파일 tools/handoff.py
title: file tools/handoff.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-handoff}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-11T09:15:09Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/92762c1c-18df-4b8e-9b9d-9d43e4811e0f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b1ea15c6-7e5e-4365-91b4-7b2f4ad29839, title_ko: 파일 복합체 tools/handoff.py, title: file composite tools/handoff.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e027fd98-2f7d-435e-92e6-27671aefb3ca, https://agentic-knowledge-base.dev/id/composite/0b8984a8-4b3a-4b30-9c38-041302b18093]}
---
**파일** — `tools/handoff.py` 다. 36줄 · 최상위 정의 1개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""읽기 집합 인수인계 — 작업 집합 뷰에서 펼쳐 읽은 청크를 새 청크의 OKF `sources` 로 옮긴다 (노트 10.3절, 부록 E.2).

`sources` 는 "편집 시 읽은 것"의 산출이며 하네스가 채워야 한다. 하네스가 읽기 집합을 기록하기 전까지의 첫 형태:
workset 뷰(bazel-bin/kg/workset-<role>.md)의 `<!-- iri: … -->` 줄이 읽기 집합이고, 이 도구가 대상 청크의 frontmatter
`sources` 에 병합한다 (기존 항목 유지). 사용: handoff.py --workset bazel-bin/kg/workset-developer.md <청크 파일...>
"""
import argparse
import re
from pathlib import Path
```
<!-- 인용 끝 -->
