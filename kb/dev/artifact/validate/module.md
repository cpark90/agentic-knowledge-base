---
id: https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1
type: artifact
level: executable
title_ko: 파일 tools/validate.py
title: file tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/f7ac5761-e5da-4a34-8beb-f661f8164328, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/cdf76c66-5003-405d-8fc1-4fbcafb8c586, https://agentic-knowledge-base.dev/id/chunk/14782c7c-bf50-47a8-ab11-62715aeeb63e]
---
**파일** — `tools/validate.py` 다. 1659줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

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
              적용 범위나 가정은 존재할 수 없다" (0.4절)
  dangling    저장소 안을 가리키는 링크의 대상이 실재한다. 주석의 대상(agt:targets)과 정의의 호출 대상
              (agt:usesDefinition — 추출기가 낸 frontmatter `uses`)도 본다 — 링크 개체가
              아니라 직접 트리플뿐이므로 여기가 유일한 실재 검사다. agt:usesConcept 의 대상은
              온톨로지가 정의한 용어여야 한다 (dependency-graph-design §5 참조 무결성).
              prov:specializationOf(분할 조각 → 원본)의 대상도 포함한다
  space       설계 공간(agt:Space)의 규칙 (p9-candidate-storage, 요구 r-011): 변수의 출발 항목과 후보의 대상이
              실재하고 · 후보의 출발점·링크 타입이 그 공간의 변수와 같고 · spaceStatus resolved 면 확정 후보가
              정확히 하나이며 · 배제된 후보에 (−) 증거, 확정된 후보에 구축·실행 (+) 증거가 있다
  specialization  prov:specializationOf 의 대상은 살아 있는(deprecated 아닌) 같은 지식 종류의 단위 지식이고 사슬은 순환하지
              않는다 (p10-split-keeps-work-identity — 단위 지식 uuid 는 work-id, 링크 IRI 는 뿌리 uuid 로 계산)
  cross-kb-link  frontmatter 링크 키(chunk2kg.LINK_KEYS)의 링크가 verifies 밖이면서 두 KB(kb/dev ↔ kb/vv)를 가로지르지
              않는다. 예외는 검증 목표(kb/vv requirement, functional) → 개발 요구 derivesFrom 하나다 (p6-executable-splits-by-kb ·
              p8-scenario-ladder-rungs). 판정은 복원 후보 생성기(tools/link.py)와 같은 함수 kb_lib.cross_kb_link 다
  rung-before-descent  같은 정제 수준의 V&V 대응물 없이 다음 정제 수준으로 내려간 정제가 없다 (요구 r-023, 유저 결정 Q51-a 의 R1 정제 계층
              사슬) — functional→abstract 는 목표, logical→concrete 는 기준, concrete→executable 은 검증기가 바인딩한 기준(사람
              확인 기준만 가진 요구는 면제)이다. 판정은 지표와 같은 함수 kb_lib.rung_violations 다
  draft-end   살아 있는(deprecated 아닌) 단위 지식의 frontmatter 링크 키(chunk2kg.LINK_KEYS) 링크가 status draft 인 단위 지식을 끝으로
              두지 않는다 (p4-chunk-state-machine, 유저 답 Q108-a 3단계). 판정은 감사 보고의 지표와 같은 함수 kb_lib.draft_end_links 다
  catalog     (--data 에 agt:Harness 가 있을 때) 카탈로그 정합성 (AGENTS.md 역할 절 · STYLEGUIDE §5 · 9.2·9.6절):
              하네스가 hasRole 하는 역할마다 대응 적용 범위(id:role-<x> ↔ id:scope-<x>)가 있고 하네스가 grants 한다 ·
              역할마다 읽기 지식 종류 ≥ 1 · 쓰기 지식 종류는 역할 사이에 겹치지 않는다 · maxConcurrent 합 ≤ ODD 동적 요소
              id:cond-concurrent-agents 의 상한(--odd 의 agt:conditionValue). 상한을 못 뽑으면 EXIT_CONFIG ·
              적용 범위는 ODD 의 부분집합이다 — agt:subsetOf 대상이 ODD 그래프의 agt:ODD 이고 include/exclude 조건이
              그 ODD 의 agt:hasCondition 에 등록돼 있다 (0.4절, 2026-09-26 metrics 지표에서 게이트로 승격) ·
              하위 역할(agt:subRoleOf)의 상위 역할은 같은 하네스의 역할이고 하위 역할의 maxConcurrent 는 0 이다(상위 역할의 세션이 맡는다)
  element-drop 소스 요소의 전수와 방출 전수의 차가 공집합이다 (현상 P19 의 관측 수단, 8.21절 G1). 둘을 본다 —
              (a) --chunk-files 를 주면 단위 지식 frontmatter 의 최상위 키 집합에서 chunk2kg 가 소비하는 키 집합
              (REQUIRED ∪ LINK_KEYS ∪ kb_lib.CHUNK_OPTIONAL_KEYS)을 뺀 차. 모르는 키는 조용히 버려지는 요소다.
              (b) 프로파일이 선언한 지식 종류 실체 클래스 집합과 chunk2kg.PROFILE_SUBSTANCE 치역의 대칭차. 어휘에만
              있으면 데이터가 그 클래스를 못 받고, 생성기에만 있으면 정의 없는 클래스가 그래프에 나타난다
  belief-consistency (--chunk-files) 믿음 정도가 상태 전이와 선호의 동률 깨기에 새지 않았다 (요구 r-032, 설계 공간
              degree-of-belief-space 닫기 기준 3). 코드 단위 지식(kb/dev/artifact/ 의 인용 코드)을 읽는다 — (i) 상태 전이 결정을
              refines 로 구현한다고 선언하고 상태의 어휘를 쓰는 단위와 그 uses 폐포는 믿음 정도의 어휘를 쓰지 않는다(Q90-a),
              (ii) 설계 공간에 닫힌 계산 규칙이 없는 동안 선호의 동률 깨기 단위와 그 uses 폐포는 믿음 정도의 어휘를 쓰지 않는다(Q137-a)
  residency   (--shapes --residency defs/kb.bzl) 수준 허용표가 한 곳에만 적혀 있다 — shape `residency-shapes.ttl` 의
              plane × level 구간이 `defs/kb.bzl` 의 `RESIDENCY` 와 같다. 원본은 Starlark 리터럴이다(분석 시점
              판정이 파일을 읽지 못하므로). 갈리면 shape 를 맞춘다 (M1 단일 정의 위치, 2026-09-26)
  shacl       (--shapes) pySHACL 적합성 — RDFS 추론을 얹어 본다. --reason 이면 OWL 2 RL 폐포 위에서 추론 없이 본다.
              --waivers <docs/waivers.md>
              를 주면 위반의 focus node 를 agt:assertionLocation 으로 파일에 사상해 게이트 id `shacl`
              (축 `파일`)로 선언된 면제를 집계에서 빼고 `WAIVED [shacl]` 줄로 남긴다 — shape 는 그대로다
  logical-consistency  (--reason) 온톨로지 검사 3단계의 셋째 단계(p2-ontology-compiler-three-tiers). 온톨로지·ODD·A-Box 의
              병합에 OWL 2 RL 폐포(owlrl OWLRL_Semantics, 결정 p2-owl2-rl-profile)를 한 번 만들고 모순을 거부한다 — 추론기가
              그래프에 더한 오류 노드(서로소 클래스의 공통 개체 등)와 owl:Nothing 소속이다. FAIL 줄은 개체 IRI 와 그 모순을 낳은
              공리·클래스·단언 유형을 적는다. 같은 폐포에 shape 를 적용한다(shacl). 추론 모드는 이 둘과 아래 셋만 돌린다 — 나머지
              검사는 --reason 없는 게이트 테스트가 이미 돌리므로 다시 돌리지 않는다 (유저 결정 Q174-a, //kg:reason_test)
  cyclic-hierarchy · unsatisfiable-class · unintended-equivalence  (--reason) 분류 계층의 셋째 단계 검사 (유저 결정 Q179-a).
              대상은 --ontology 파일이 owl:Class 로 선언한 이름 IRI 다. 순환은 단언된 rdfs:subClassOf 에서 찾는다. 불만족은 클래스마다
              프로브 개체를 넣은 온톨로지 사본의 OWL 2 RL 폐포로 판정하는 RL 근사라 놓치는 불만족이 있다. 동치는 폐포에서 서로 하위인
              쌍 중 단언된 owl:equivalentClass 의 사슬 밖이고 순환·불만족이 아닌 쌍이다. 한 결함에 한 줄이다

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
    from tools import chunk2kg  # 소비되는 frontmatter 키·지식 종류 실체 사상의 단일 정의 위치 (element-drop)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
except ImportError:
    import chunk2kg
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
