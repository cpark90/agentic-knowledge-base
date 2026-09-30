---
id: https://agentic-knowledge-base.dev/id/chunk/e4926f66-ff93-4656-be1b-63dbed7f8e90
type: artifact
level: executable
title_ko: 파일 tools/community.py
title: file tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/822db955-483e-47ed-ad68-fec783bc825b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/0ef43353-941b-4b48-b8b1-2ef9a8eacf53, title_ko: 파일 복합체 tools/community.py, title: file composite tools/community.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/13568c50-9137-4cc7-82ab-dc6e233c5bcc, https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5, https://agentic-knowledge-base.dev/id/composite/09eb4947-176f-41ad-92ee-7632b5240022]}
---
**파일** — `tools/community.py` 다. 277줄 · 최상위 정의 7개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""커뮤니티 탐지 뷰 — 링크 구조의 군집을 복합체 후보와 relatedTo 링크 후보로 보고한다
(p4-community-detection-proposes-composites, dependency-graph-design §7 (h)).

게이트가 아니라 **후보 생성기**다: 채택(복합체 선언)·묶기(relatedTo 링크)·기각은 사람이 후보마다 판정하고,
결과는 저장하지 않는다 (4.6절 뷰 원칙). 판정란은 비워 둔다.

  입력  살아 있는 청크(status ≠ deprecated)와 링크 — refines·serves·cites·usesConcept·coUpdatesWith·conflictsWith
        (직접 트리플과 agt:Link 개체 둘 다) + 구성 관계 hasDirectPart. supersedes 는 시간축이라 제외한다.
  계산  결정론적 Louvain (외부 의존 없음). 노드·이웃·군집 순회를 IRI 정렬로 고정하고 동점은 작은 IRI 가 이기므로
        같은 입력이면 같은 출력이다. 이미 선언된 복합체의 부분은 처음부터 한 단위로 묶어 계산이 선언을 쪼개지 않는다
        — 복합체는 선언이고 커뮤니티는 계산이다 (근거 청크). 복합체의 수준은 결론의 수준이다 (defs/kb.bzl ChunkInfo).
  판정  같은 plane·level 안의 군집(청크 2~9, 아직 복합체가 아닌 것)만 복합체 후보,
        plane 또는 level 을 넘는 군집은 relatedTo 링크 후보 — 쌍이 아니라 군집 단위.

사용: community.py --out communities.md <TTL...>   (bazel build //kg:communities)
"""
import argparse
from collections import Counter, defaultdict
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
