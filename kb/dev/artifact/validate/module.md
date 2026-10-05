---
id: https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1
type: artifact
level: executable
title_ko: 파일 tools/validate.py
title: file tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/f7ac5761-e5da-4a34-8beb-f661f8164328, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/cdf76c66-5003-405d-8fc1-4fbcafb8c586, https://agentic-knowledge-base.dev/id/chunk/14782c7c-bf50-47a8-ab11-62715aeeb63e]
composite: {id: https://agentic-knowledge-base.dev/id/composite/fb7cffc9-e5b5-4ed5-af22-40aa50e3c6aa, title_ko: 파일 복합체 tools/validate.py, title: file composite tools/validate.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/f78b9e0e-d84b-4087-9f1d-29bcf769d844, https://agentic-knowledge-base.dev/id/composite/56ab8e29-8a32-4148-bee8-85b8eabe8488, https://agentic-knowledge-base.dev/id/composite/dfafb084-58ea-49a9-9fe2-20457fba4997, https://agentic-knowledge-base.dev/id/composite/4d158385-e139-4042-8477-a87c3deeefe2]}
---
**파일** — `tools/validate.py` 다. 1043줄 · 최상위 정의 34개 · 최상위 절 4개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""검사 게이트 (노트 6.7절) — 온톨로지 품질 검사(2.5절) + SHACL(4.4절) + ODD 참조(3.3절).

검사 항목
  syntax      모든 TTL이 파싱된다
  labels      온톨로지가 정의한 모든 agt: 용어에 rdfs:label 한/영 + skos:definition (2.5절)
  boundary    한 agt: 용어는 정확히 한 모듈 파일에서만 정의된다 (2.3절 경계 규칙)
  vocab       데이터 그래프의 술어는 온톨로지 정의 또는 표준 어휘 안에 있다 (4.4절 일관성,
              Part XIII "어휘 우회" 리스크). --standard-vocab <원문...> 을 주면 그 원문
              (PROV-O·SKOS, MODULE.bazel http_file 해시 고정)의 네임스페이스에 속한 용어가
              실제로 거기 정의돼 있는지까지 본다 — 접두사만 맞는 오타를 잡는다
  odd-ref     agt:refersTo 의 대상은 ODD 그래프에 존재한다 — "ODD에 없는 속성을 참조하는
              스코프나 가정은 존재할 수 없다" (0.4절)
  dangling    저장소 안을 가리키는 링크의 대상이 실재한다. 주석의 대상(agt:targets)과 정의의 호출 대상
              (agt:usesDefinition — 추출기가 낸 frontmatter `uses`)도 본다 — 링크 개체가
              아니라 직접 트리플뿐이므로 여기가 유일한 실재 검사다. agt:usesConcept 의 대상은
              온톨로지가 정의한 용어여야 한다 (dependency-graph-design §5 참조 무결성).
              prov:specializationOf(분할 조각 → 원본)의 대상도 포함한다
  space       설계 공간(agt:Space)의 규율 (p9-candidate-storage, 요구 r-011): 변수의 출발 항목과 후보의 대상이
              실재하고 · 후보의 출발점·링크 타입이 그 공간의 변수와 같고 · spaceStatus resolved 면 확정 후보가
              정확히 하나이며 · 배제된 후보에 (−) 증거, 확정된 후보에 구축·실행 (+) 증거가 있다
  specialization  prov:specializationOf 의 대상은 살아 있는(deprecated 아닌) 같은 plane 의 청크이고 사슬은 순환하지
              않는다 (p10-split-keeps-work-identity — 청크 uuid 는 work-id, 링크 IRI 는 뿌리 uuid 로 계산)
  cross-kb-link  frontmatter 링크 키(chunk2kg.LINK_KEYS)의 링크가 verifies 밖이면서 두 KB(kb/dev ↔ kb/vv)를 가로지르지
              않는다. 예외는 검증 목표(kb/vv requirement, functional) → 개발 요구 derivesFrom 하나다 (p6-executable-splits-by-kb ·
              p8-scenario-ladder-rungs). 판정은 복원 후보 생성기(tools/link.py)와 같은 함수 kb_lib.cross_kb_link 다
  rung-before-descent  같은 높이의 V&V 대응물 없이 다음 높이로 내려간 하강이 없다 (요구 r-023, 유저 결정 Q51-a 의 R1 사다리
              사슬) — functional→abstract 는 목표, logical→concrete 는 기준, concrete→executable 은 검증기가 바인딩한 기준(사람
              확인 기준만 가진 요구는 면제)이다. 판정은 지표와 같은 함수 kb_lib.rung_violations 다
  catalog     (--data 에 agt:Harness 가 있을 때) 카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 9.2·9.6절):
              하네스가 hasRole 하는 역할마다 대응 스코프(id:role-<x> ↔ id:scope-<x>)가 있고 하네스가 grants 한다 ·
              역할마다 read plane ≥ 1 · write plane 은 역할 사이에 겹치지 않는다 · maxConcurrent 합 ≤ ODD 동적 요소
              id:cond-concurrent-agents 의 상한(--odd 의 agt:conditionValue). 상한을 못 뽑으면 EXIT_CONFIG ·
              스코프는 ODD 의 부분집합이다 — agt:subsetOf 대상이 ODD 그래프의 agt:ODD 이고 include/exclude 조건이
              그 ODD 의 agt:hasCondition 에 등록돼 있다 (0.4절, 2026-09-26 metrics 지표에서 게이트로 승격)
  element-drop 소스 요소의 전수와 방출 전수의 차가 공집합이다 (현상 P19 의 관측 수단, 8.21절 G1). 둘을 본다 —
              (a) --chunk-files 를 주면 청크 frontmatter 의 최상위 키 집합에서 chunk2kg 가 소비하는 키 집합
              (REQUIRED ∪ LINK_KEYS ∪ kb_lib.CHUNK_OPTIONAL_KEYS)을 뺀 차. 모르는 키는 조용히 버려지는 요소다.
              (b) 프로파일이 선언한 plane 실체 클래스 집합과 chunk2kg.PROFILE_SUBSTANCE 치역의 대칭차. 어휘에만
              있으면 데이터가 그 클래스를 못 받고, 생성기에만 있으면 정의 없는 클래스가 그래프에 나타난다
  residency   (--shapes --residency defs/kb.bzl) 수준 허용표가 한 곳에만 적혀 있다 — shape `residency-shapes.ttl` 의
              plane × level 구간이 `defs/kb.bzl` 의 `RESIDENCY` 와 같다. 원본은 Starlark 리터럴이다(분석 시점
              판정이 파일을 읽지 못하므로). 갈리면 shape 를 맞춘다 (M1 단일 정의처, 2026-09-26)
  shacl       (--shapes) OWL-RL 추론 후 pySHACL 적합성 (--reason 시 추론 적용). --waivers <docs/waivers.md>
              를 주면 위반의 focus node 를 agt:assertionLocation 으로 파일에 사상해 게이트 id `shacl`
              (축 `파일`)로 선언된 면제를 집계에서 빼고 `WAIVED [shacl]` 줄로 남긴다 — shape 는 그대로다

경고(비영 종료 아님, `warn [검사명]` 접두사)
  usesConcept-deprecated  agt:usesConcept 의 대상이 폐기된 용어(owl:deprecated true 또는
              라벨의 "(deprecated)"/"(폐기)")다 — 용어 일관성 (dependency-graph-design §5)

출력·종료 (agrtls-practices-review A): 위반은 `FAIL [<검사명>] <경로>: <메시지>` 한 줄씩 + EXIT_FAIL.
  파싱되지 않는 입력(syntax)·파일 없음은 게이트가 판정을 내릴 수 없는 상태이므로 EXIT_CONFIG,
  그래프 파일 0건은 EXIT_SKIP — SKIP 은 PASS 가 아니다. bazel test 가 곧 게이트다.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from rdflib import OWL, RDF, RDFS, XSD, Graph, URIRef
from rdflib.namespace import SKOS

try:
    from tools import chunk2kg  # 소비되는 frontmatter 키·plane 실체 사상의 정의처 (element-drop)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import chunk2kg
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
