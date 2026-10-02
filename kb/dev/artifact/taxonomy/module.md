---
id: https://agentic-knowledge-base.dev/id/chunk/421c8a5d-8d5a-414c-8938-2865c45df8ef
type: artifact
level: executable
title_ko: 파일 tools/taxonomy.py
title: file tools/taxonomy.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/870158d1-2a3e-4b89-b721-7afb4d7a095d, https://agentic-knowledge-base.dev/id/chunk/40abcad5-6a9c-4233-99d3-0b7ceeafb06b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/5cd36157-e133-4ff0-bb51-ba6848ba0fbd, title_ko: 파일 복합체 tools/taxonomy.py, title: file composite tools/taxonomy.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/205f5607-e950-444d-b697-1bf3f4449223, https://agentic-knowledge-base.dev/id/composite/9027036d-a39d-4b9e-b7c2-40b3cddb625f]}
---
**파일** — `tools/taxonomy.py` 다. 59줄 · 최상위 정의 1개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""ODD 택소노미 뷰 — related/condition 온톨로지에서 OpenODD 택소노미 YAML(taxonomy.yml)을 생성한다 (부록 E.4).

OpenODD YAML 매핑 참조: 최상위 `TAXONOMY:` 아래 개념 레코드. 이 체계에서 범주(정적 요소·환경 조건·동적 요소)는
온톨로지의 agt:Condition 하위 클래스이고, 속성은 프로젝트의 ODD 문서가 같은 범주 키 아래에 확장한다.
손으로 쓰지 않는다. 사용: taxonomy.py --out taxonomy.yml <condition 모듈 TTL...>
출력·종료: 읽을 수 없거나 파싱되지 않는 입력은 `FAIL [taxonomy] <경로>: …` + EXIT_CONFIG (판정 규칙은 없다 — 생성기).
"""
import argparse
import sys
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
