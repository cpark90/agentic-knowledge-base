---
id: https://agentic-knowledge-base.dev/id/chunk/79933019-87fe-4c4c-9d44-0b76b96a2cb3
type: artifact
level: executable
title_ko: 파일 tools/canonicalize.py
title: file tools/canonicalize.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-canonicalize}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a9cc1a02-29b3-4f53-8711-8d60a4bea3cf]
---
**파일** — `tools/canonicalize.py` 다. 252줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""정규화 직렬화 (노트 2.5절) — diff가 의미 변화만 보여주도록 출력 순서를 고정한다.

  canonicalize.py --check <files>   파일이 정규형과 일치하는지 검사 (비영 종료)
  canonicalize.py --write <files>   파일을 정규형으로 다시 쓴다 (주석은 사라진다)
  canonicalize.py --catalog <dir> --root <ttl> --module <iri> <name> <files...> [--module-import <iri> <iri>]
                                    표준 OWL 도구용 OASIS XML Catalog 와 모듈 합본을 <dir> 에 쓴다 (Q176-a·Q177-c)

정규형: 정렬된 @prefix 블록 + 주어(subject) 정렬 블록, 술어는 rdf:type 우선 후 정렬,
목적어 정렬. 익명 노드는 rdflib 정준화(canonicalization)로 라벨을 고정한다.
출력·종료: --check 위반은 `FAIL [canon] <경로>: …` + EXIT_FAIL. 읽을 수 없거나 파싱되지 않는 입력은 EXIT_CONFIG.
--catalog 는 빌드 액션(`kb_owl_catalog`)의 실행 경로다. 최상위 파일의 owl:imports 가 대응표 밖이면 `FAIL [canon]` + EXIT_FAIL.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import re

from xml.sax.saxutils import quoteattr

from rdflib import BNode, Graph, Literal, OWL, RDF, URIRef
from rdflib.compare import to_canonical_graph

try:  # 종료 코드 규약의 단일 정의 위치는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
