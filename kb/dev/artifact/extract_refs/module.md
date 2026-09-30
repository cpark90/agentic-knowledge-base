---
id: https://agentic-knowledge-base.dev/id/chunk/b99b53d3-521e-493b-861d-d2cb73fba546
type: artifact
level: executable
title_ko: 파일 tools/extract_refs.py
title: file tools/extract_refs.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract-refs}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-19T14:57:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/55535378-f5cd-4f01-a5ce-54d438529104, https://agentic-knowledge-base.dev/id/chunk/8d09b0e4-44b4-47b2-9ff6-5da9f3b22e12]
composite: {id: https://agentic-knowledge-base.dev/id/composite/1ddb8a02-e2d5-48e7-a66d-3c960e6a523a, title_ko: 파일 복합체 tools/extract_refs.py, title: file composite tools/extract_refs.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/1a3482f6-0687-482a-848a-544cab7ed57b, https://agentic-knowledge-base.dev/id/composite/444fc7bd-680b-4c09-aec8-0e5de0cc1175]}
---
**파일** — `tools/extract_refs.py` 다. 202줄 · 최상위 정의 3개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""청크 본문의 명시적 인용·개념 사용 → 참조 그래프(-kg) 생성.

링크는 편집의 부산물로 만든다(8.3절). 본문이 다른 항목의 식별자를 적어 가리키는
것은 가장 검사 가능성이 높은 근거이므로, 그 인용을 기계로 뽑아 agt:cites 링크로
방출한다 — 손으로 쓰지 않는 생성물이다 (8.2절, 8.8절).

인용 표기: 본문의 `d-NNNN` (자기 자신은 제외). 대상이 실재하지 않으면 비영 종료 —
"인용한 타깃이 존재하는가"가 여기서 강제된다 (참조 무결성).

개념 사용 표기 (--ontology 를 줄 때만, dependency-graph-design §6 복원 경로):
본문의 `agt:<Term>` 이 온톨로지 union이 정의하는 agt: 클래스·속성·개체이면
agt:usesConcept 링크로 방출한다 (청크당 용어당 1). 온톨로지에 없는 표기는 링크로
만들지 않고 stderr 에 `info [usesConcept]` 로 센다 — 본문의 오타·예시일 수 있으므로
게이트 실패가 아니다. 폐기된 용어 참조의 경고는 validate.py 가 낸다.

후보 링크 개체 (p10-extracted-references-are-candidates, 유저 승인 2026-09-19): 인용(agt:cites)마다 직접 트리플에 더해
agt:CandidateLink 개체를 낸다 — linkState "candidate", 양 끝, linkKind agt:cites, 증거 constructionRecord(저자가 본문에 적은
식별자는 구축 기록이다 — p10-link-by-construction) + evidenceRef 그 청크, 극성 "+". 확정은 사람이 앵커 청크의 frontmatter 링크 키에
적는 행위이고(chunk2kg 가 ConfirmedLink 를 낸다) 후보 생성기 link 가 판정 대상을 낸다. 링크 IRI 는 chunk2kg 와 같은 규칙 —
양 끝의 뿌리 uuid(specializationOf 사슬, chunk2kg.work_id)의 link_hash — 라 한 청크가 원본과 조각을 함께 인용하면 후보 하나에
linkTo 둘이 붙는다. usesConcept 는 후보로 만들지 않는다: agt:linkTo 의 치역은 agt:KnowledgeItem 인데 대상이 온톨로지 용어
(owl:Class·속성·개체)라 치역 밖이다 (link-ontology · usesConcept 정의 "치역이 지식 항목이 아니라 어휘의 개념").

출력·종료: 위반은 `FAIL [extract-refs] <경로>: …` + EXIT_FAIL. 읽을 수 없는 입력은 EXIT_CONFIG.
사용: extract_refs.py --out <생성.ttl> [--ontology <온톨로지.ttl...> --] <청크 파일들...>
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
```
<!-- 인용 끝 -->
