---
id: https://agentic-knowledge-base.dev/id/chunk/44a05a81-0490-4725-a114-8d42143fdc0e
type: artifact
level: executable
title_ko: 파일 tools/metrics.py
title: file tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f, https://agentic-knowledge-base.dev/id/chunk/1f7d15d7-e85d-42dd-bef3-fb9c9a6d0365]
composite: {id: https://agentic-knowledge-base.dev/id/composite/3c529991-238b-41b3-abc4-9d4e944f0a32, title_ko: 파일 복합체 tools/metrics.py, title: file composite tools/metrics.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e2d8a9c4-074b-4ff9-89a7-92e76bd285fb, https://agentic-knowledge-base.dev/id/composite/90bd15d5-e388-4dc6-b7d0-0e639fe85f3f, https://agentic-knowledge-base.dev/id/composite/c6d68e53-8445-4ac7-a4d6-7d59dd3b3ca6, https://agentic-knowledge-base.dev/id/composite/608921b6-11ac-4736-ae95-09ee84f21b74, https://agentic-knowledge-base.dev/id/composite/2bd326ae-1255-4621-b93d-03485668c5b1]}
---
**파일** — `tools/metrics.py` 다. 423줄 · 최상위 정의 18개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""코어 지표 뷰 — 그래프에서 metrics.md를 생성한다 (노트 4.13절, 10.14절, 12.3절, 14.1절).

문서에 수치를 적으면 반드시 낡으므로(4.6절 뷰 원칙) 지표는 이 생성물을 인용한다.
  청크 수(plane·level·status) · 고아율(복합체 부분도 링크도 없는 청크, 4.13절) · 크기 분포 ·
  링크 밀도 · 가정 · 신뢰 등급(사람 검토) · CQ19 전방 추적 커버리지 · CQ20 후방 추적 커버리지 · 도입 1단계 통과 조건.
사용: metrics.py --out metrics.md --residency defs/kb.bzl <TTL...>
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, RDF, RDFS, URIRef

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
