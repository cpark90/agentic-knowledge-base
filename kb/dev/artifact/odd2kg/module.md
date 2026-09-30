---
id: https://agentic-knowledge-base.dev/id/chunk/195a3146-351c-4ae5-bea7-61bc6edf7704
type: artifact
level: executable
title_ko: 파일 tools/odd2kg.py
title: file tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/3d66b1bc-0e65-4e62-9654-fc0ddb6b7d20, https://agentic-knowledge-base.dev/id/chunk/40abcad5-6a9c-4233-99d3-0b7ceeafb06b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/50c525bb-02f0-4c2b-a9e0-1a3b666fbd3c, title_ko: 파일 복합체 tools/odd2kg.py, title: file composite tools/odd2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fb4cc423-29a9-4491-a1e8-a630c1b5a123, https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d]}
---
**파일** — `tools/odd2kg.py` 다. 133줄 · 최상위 정의 4개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""OpenODD 문서(YAML 매핑 참조) → ODD 그래프(-odd.ttl) 생성기 (노트 3.2절, 부록 E.4).

원본은 kb/odd/*.yml, TTL은 생성물. 생성 = 검사:
  - TAXONOMY 확장의 범주 키가 생성된 taxonomy.yml 의 범주 안에 있다 (어휘는 온톨로지에서)
  - MODULES 의 모든 조건 속성이 TAXONOMY 에 선언되어 있고, 식이 OpenODD 식(리터럴·"< n"·"> n"·"[a .. b]"·unknown)이다
  - 범주 리터럴은 선언된 목록 안, 수치 식은 수치 속성에만
  - 모든 속성에 ATTRIBUTES(IRI·라벨)와 CHECKS(방법·등급)가 있다 — 판정 방법 없는 조건은 ODD에 둘 수 없다 (0.4절)
출력·종료: 위반은 `FAIL [odd2kg] <원본 yml>: <메시지>` + EXIT_FAIL. 읽을 수 없거나 YAML 로 파싱되지 않는 입력은 EXIT_CONFIG.
사용: odd2kg.py --taxonomy taxonomy.yml --out project-odd.ttl project-odd.yml
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 이 도구는 rdflib 없이 돌므로 없으면 같은 값의 폴백
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
