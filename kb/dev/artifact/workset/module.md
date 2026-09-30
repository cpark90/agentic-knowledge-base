---
id: https://agentic-knowledge-base.dev/id/chunk/ea192023-b5a0-4dbe-bb2f-8b507575633c
type: artifact
level: executable
title_ko: 파일 tools/workset.py
title: file tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c, https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320]
composite: {id: https://agentic-knowledge-base.dev/id/composite/daba0b21-4c2e-4be6-8cc6-9cef10baa82f, title_ko: 파일 복합체 tools/workset.py, title: file composite tools/workset.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/58ca0301-520d-4ec2-848b-bfea07859eab, https://agentic-knowledge-base.dev/id/composite/efdb6344-03eb-4727-97ba-fe8aadcc7424]}
---
**파일** — `tools/workset.py` 다. 179줄 · 최상위 정의 3개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""작업 집합 뷰 — 스코프 × 수준 창으로 거른 라벨 목록과 앵커 이웃을 예산 안에 담는다 (노트 0.5절, 5.6절, 11.3절).

작업 집합은 질의 결과이며 저장하지 않는다. 읽기 응답의 기본은 라벨 목록이고 본문은 앵커 이웃만 펼친다.
이웃은 앵커에서 k홉 안의 청크(upstream ∪ downstream, 직접 트리플과 agt:Link 개체 둘 다)이며, 펼치는 순서는
링크 족의 우선순위다 — 앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo
(dependency-graph-design §4, p0-workset-anchor-neighbourhood). 예산을 넘는 이웃은 라벨만 남는다.
사용: workset.py --role developer [--levels logical,concrete] [--anchor <IRI|라벨 부분>] [--budget 200] --out workset.md <TTL...>
종료: 앵커가 있을 때만 예산 판정이 게이트다 — 문서 전체(라벨 목록 + 펼친 본문)가 예산을 넘으면
  `FAIL [workset-budget]` + 1(도입 2단계 구체화 조건, handoff/workset-budget-gate-2026-09-22). 앵커가 없으면
  지금처럼 뷰에 판정만 적고 0 — 앵커 없는 뷰(스코프 전체 라벨 목록)는 구조적으로 예산을 넘어 판정 대상이 아니다.
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
