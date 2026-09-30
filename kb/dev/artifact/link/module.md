---
id: https://agentic-knowledge-base.dev/id/chunk/2ed70acf-5e27-4d27-986f-458977bf1974
type: artifact
level: executable
title_ko: 파일 tools/link.py
title: file tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/8d09b0e4-44b4-47b2-9ff6-5da9f3b22e12, https://agentic-knowledge-base.dev/id/chunk/5287133e-f7a3-4913-8aaf-062647cf5491, https://agentic-knowledge-base.dev/id/chunk/6321bf38-7026-4c60-b4fb-7cf3a956b35b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b28a66c9-4140-4beb-bb95-69e12a91e607, title_ko: 파일 복합체 tools/link.py, title: file composite tools/link.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d456c76a-43ad-49f5-b73e-ca32721dd5ec, https://agentic-knowledge-base.dev/id/composite/570df80b-916d-466e-a9fe-8a9ac66eea54, https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d]}
---
**파일** — `tools/link.py` 다. 327줄 · 최상위 정의 7개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""복원 후보 생성기 뷰 — frontmatter 링크가 없는 청크 쌍의 링크 후보를 체계 안 증거만으로 낸다 (로드맵 8단계 복원,
p10-link-by-construction · p10-candidate-and-confirmed-link · p10-link-judgement-evidence).

게이트가 아니라 **후보 생성기**다. 입력은 그래프 union 뿐이고(체계 밖 정보 0) 판정은 사람이 후보마다 한다 — 채택하면 앵커 청크의
frontmatter 에 링크 키와 `restored:` 를 적는다 (p10-restored-link-marking). 결과는 저장하지 않는다 (4.6절 뷰 원칙).
  단위  살아 있는 청크(status ≠ deprecated). 결정 복합체(conclusion·rationale·alternatives)는 한 단위이고 앵커는 결론이다 — 링크 키는
        결론에 적는다. 손으로 쓴 복합체(kg/composite-kg.ttl)의 부분은 각각 단위이되 형제끼리는 후보가 아니다
  근거  체계 안 증거만, 검사 가능성 순 (kb/ontology/related/trace/evidence-ontology.ttl):
        (a) 본문 식별자 — A 본문이 B 를 agt:cites 하는데 frontmatter 링크가 없다 → constructionRecord (본문 식별자는 구축 기록이다)
        (b) 테스트 공동 커버 — 같은 V&V 청크가 verifies 하는 두 개발 청크 → testCoverage
        (c) 개념 공유 — agt:usesConcept 교집합 ≥ --min-shared (기본 3) → proposal (도구 제안 — 확정 근거가 아니며 동률만 깬다)
        (d) 승계 — 조각 F 가 prov:specializationOf O 이면 O 를 가리키던 확정 링크(linkState confirmed, 종류는 LINK_KEYS) X→O 마다
            X→F 후보 → constructionRecord, 값 "승계: O" (p10-split-keeps-work-identity). 종류는 원 링크의 종류를 우선한다
        임베딩 유사도는 쓰지 않는다 (ODD 가 학습 임베딩을 명시 제외). 같은 세션 읽음은 하네스가 아직 기록하지 않는다
  종류  TIM 허용 칸(kb_lib.TIM_CELLS)에서 고른다 — 인용 방향(대칭 근거는 IRI 순)을 먼저, 다음 역방향, 칸이 없으면 overlapsWith
        (relatedTo 족의 약한 잎 — 관계는 있으나 이름이 아직 없는 자리, overlap-ontology). 그것은 링크 키라 채택이 복원 비율에 든다.
        supersedes 는 시간축이라 후보가 아니다. 한 칸에 종류가 여럿이면 refines > derivesFrom > satisfies > constrains > serves > verifies 순.
        승계 후보는 원 링크의 종류가 제약을 통과하면 그것을 쓴다
  제약  defs/kb.bzl _check_links 와 같은 규칙 — refines·serves 는 더 높은 수준으로·plane 순서 역행 금지·같은 KB, serves 대상은 요구,
        verifies 는 주어 kb/vv·대상 개발 KB·같은 수준. 자기 자신·deprecated·복합체 형제·이미 링크된 쌍·KB 를 가로지르는 overlapsWith 는 탈락
  상한  앵커(주어)당 k ≤ --k (기본 7, 로드맵 입력표) — 근거 강도 → 공유 개념 수 → 대상 라벨 순. 넘치는 것은 탈락으로 센다
사용: link.py --out link-candidates.md [--k 7] [--min-shared 3] <TTL...>   (bazel build //kg:link_candidates)
종료: 0 생성됨 · 2 입력 문제(그래프 파일 없음·파싱 불가) — 뷰라 판정 실패(1)는 없다. 후보 0건은 빈 표이지 실패가 아니다
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict

from pathlib import Path
```
<!-- 인용 끝 -->
