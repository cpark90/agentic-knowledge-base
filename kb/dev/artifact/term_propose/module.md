---
id: https://agentic-knowledge-base.dev/id/chunk/f0e34a95-761c-4513-8c4a-a3c779e351c8
type: artifact
level: executable
title_ko: 파일 tools/term_propose.py
title: file tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-10T17:03:35Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/4754eb68-ad27-45ad-912c-0385087cd063, https://agentic-knowledge-base.dev/id/chunk/b136d285-c4ba-461b-99cf-bda07c2243d8]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f141ce57-8f04-4bda-a9ff-756f81f57846, title_ko: 파일 복합체 tools/term_propose.py, title: file composite tools/term_propose.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c730fd69-c542-4d85-92ae-38125ac16f18, https://agentic-knowledge-base.dev/id/composite/f37f3044-d076-4e57-b68f-4a03d2ad16d5]}
---
**파일** — `tools/term_propose.py` 다. 116줄 · 최상위 정의 1개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""용어 제안 워크플로 (노트 2.5절) — 일반화가 온톨로지에 닿을 때의 절차.

에이전트는 신뢰할 수 없는 센서다: 제안은 하되 판정하지 않는다. 이 도구는
template 행(ID·라벨 ko/en·정의·상위·역량 질문 기여)을 받아 검사를 통과한
제안만 승인 큐(kb/ontology/proposals/)에 남긴다. 승인 큐는 //kb/ontology:modules
밖이라 병합 전에는 그래프에 들어가지 않는다.

  1. 에이전트가 관측에서 개념 후보를 뽑아 이 도구로 제안
  2. 검사: 상위 개념 실재, 라벨 중복 없음, 정의 존재, 케밥 ID
  3. 통과한 것만 proposals/<slug>-proposal.ttl 로 (실패는 비영 종료)
  4. 유저 승인 → 해당 모듈 파일로 이동 + prov:wasDerivedFrom 으로 관측에 연결

사용: term_propose.py --id retry-policy --kind class --parent agt:Condition \\
        --label-ko "재시도 정책" --label-en "retry policy" \\
        --definition "…인 조건. (속+종차)" --cq CQ12 [--derived-from <관측 IRI>]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from rdflib import Graph, RDFS

try:
    from tools import kb_lib
except ImportError:
    import kb_lib
```
<!-- 인용 끝 -->
