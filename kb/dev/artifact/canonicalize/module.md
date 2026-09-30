---
id: https://agentic-knowledge-base.dev/id/chunk/79933019-87fe-4c4c-9d44-0b76b96a2cb3
type: artifact
level: executable
title_ko: 파일 tools/canonicalize.py
title: file tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/a9cc1a02-29b3-4f53-8711-8d60a4bea3cf]
composite: {id: https://agentic-knowledge-base.dev/id/composite/cf91a784-b983-40fa-afff-ff9105164656, title_ko: 파일 복합체 tools/canonicalize.py, title: file composite tools/canonicalize.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/811c8a9a-7991-488b-927b-a703841a532b, https://agentic-knowledge-base.dev/id/composite/29d788bd-8690-47f5-8a29-184a6e40d389]}
---
**파일** — `tools/canonicalize.py` 다. 160줄 · 최상위 정의 4개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""정규화 직렬화 (노트 2.5절) — diff가 의미 변화만 보여주도록 출력 순서를 고정한다.

  canonicalize.py --check <files>   파일이 정규형과 일치하는지 검사 (비영 종료)
  canonicalize.py --write <files>   파일을 정규형으로 다시 쓴다 (주석은 사라진다)

정규형: 정렬된 @prefix 블록 + 주어(subject) 정렬 블록, 술어는 rdf:type 우선 후 정렬,
목적어 정렬. 익명 노드는 rdflib 정준화(canonicalization)로 라벨을 고정한다.
출력·종료: --check 위반은 `FAIL [canon] <경로>: …` + EXIT_FAIL. 읽을 수 없거나 파싱되지 않는 입력은 EXIT_CONFIG.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import re

from rdflib import BNode, Graph, Literal, RDF, URIRef
from rdflib.compare import to_canonical_graph

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
