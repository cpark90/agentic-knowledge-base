---
id: https://agentic-knowledge-base.dev/id/chunk/ebf3db88-a177-4d7c-8441-992719f174d9
type: artifact
level: executable
title_ko: 파일 tools/query.py
title: file tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/0c829785-f155-4ab8-bf9a-1f69b0d3e85d, https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4, https://agentic-knowledge-base.dev/id/chunk/595590fa-f40a-4008-92c0-f971f574111b]
---
**파일** — `tools/query.py` 다. 243줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""일반 질의 도구 — 역량 질문(질의는 tools/cq-queries/*.rq 에 등재하고 질의가 아직 없는 질문은 docs/competency-questions.md 에 둔다)을 SPARQL 로 노출한다 (로드맵 다음 산출 4, 노트 2.7절).

질의 하나 = 파일 하나 tools/cq-queries/CQ-NN.rq. 머리 주석 첫 줄이 질문 원문, 둘째 줄이 답의 형태(행 = 무엇)다.
그래프는 metrics 와 같은 union(head·참조·시드·카탈로그·복합체·ODD)에 온톨로지 모듈을 더해 rdflib 에 **한 번** 올린다 (kb_lib.load_union).
캐시·직렬화는 두지 않는다 — 원본은 그래프 파일이고 결과는 저장하지 않는 질의 결과다 (docs/competency-questions.md 쓰는 법 4번 "답은 저장하지 않는다").
결과는 표이고 --labels 가 IRI 열을 rdfs:label@ko 로 바꾼다 — 라벨이 인터페이스다 (p4-label-is-the-interface,
p12-knowledge-retrieval-by-label: 결과는 라벨 목록).

사용:
  bazel run //tools:query -- CQ-07 [--limit N] [--labels] [--bind ?x=<IRI|id:슬러그|agt:용어|라벨>]
  bazel run //tools:query                       # 전체 CQ 의 행 수 요약표
  query.py --report cq.md --queries <dir|*.rq> --ttl <TTL...>    # 뷰 //kg:cq 의 생성기
종료 코드는 kb_lib 상수 — 질의 파일 없음·SPARQL 파싱 실패·그래프 파일 없음·--bind 해석 실패는 EXIT_CONFIG, 질의 0건은 EXIT_SKIP.
행 0 은 답이지 실패가 아니다 (게이트가 아니다).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from rdflib import Graph, Literal, URIRef, RDFS
from rdflib.plugins.sparql import prepareQuery

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
