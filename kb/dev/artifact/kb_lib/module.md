---
id: https://agentic-knowledge-base.dev/id/chunk/f27e3bb2-85d8-43e1-9020-f659f1d58743
type: artifact
level: executable
title_ko: 파일 tools/kb_lib.py
title: file tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
composite: {id: https://agentic-knowledge-base.dev/id/composite/dca529bc-79c6-4569-af4c-122c0d736686, title_ko: 파일 복합체 tools/kb_lib.py, title: file composite tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/composite/7aee7ddf-f82b-4788-88ce-b27bd5290481, https://agentic-knowledge-base.dev/id/composite/ff9d354a-d261-44a5-b7cd-7dd050de0370, https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211, https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2, https://agentic-knowledge-base.dev/id/composite/9eb3404e-6904-4245-8c6b-5fcc2cc9f893, https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed, https://agentic-knowledge-base.dev/id/composite/2fee8437-c9b3-4f23-a1d9-a0ec5e3891b0, https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a]}
---
**파일** — `tools/kb_lib.py` 다. 1829줄 · 최상위 정의 65개 · 최상위 절 8개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
"""공용 그래프 적재·어휘 헬퍼.

접미사 규약(노트 0.2절)과 네임스페이스(0.3절, 0.7절)의 단일 정의처.
"""

from __future__ import annotations

import hashlib
import os
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef
from rdflib.namespace import SKOS

try:  # PLANES·LEVELS·STATES 리터럴 읽기 함수의 정의처는 chunk2kg 하나다(오케스트레이터 판정, 2026-09-27) —
    from tools.chunk2kg import load_plane_level_state  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
    from tools.chunk2kg import BODY_SLOT_MARKERS  # 본문 슬롯 표지 낱말의 정의처(단일) — 겹침 검사(아래)의 입력
except ImportError:
    from chunk2kg import load_plane_level_state  # 직접 실행: 스크립트 디렉토리 기준 (chunk2kg.py 가 같은 srcs 에 있어야 한다)
    from chunk2kg import BODY_SLOT_MARKERS
```
<!-- 인용 끝 -->
