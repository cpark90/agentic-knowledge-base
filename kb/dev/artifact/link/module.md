---
id: https://agentic-knowledge-base.dev/id/chunk/2ed70acf-5e27-4d27-986f-458977bf1974
type: artifact
level: executable
title_ko: 파일 tools/link.py
title: file tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/8d09b0e4-44b4-47b2-9ff6-5da9f3b22e12, https://agentic-knowledge-base.dev/id/chunk/5287133e-f7a3-4913-8aaf-062647cf5491, https://agentic-knowledge-base.dev/id/chunk/6321bf38-7026-4c60-b4fb-7cf3a956b35b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b28a66c9-4140-4beb-bb95-69e12a91e607, title_ko: 파일 복합체 tools/link.py, title: file composite tools/link.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d456c76a-43ad-49f5-b73e-ca32721dd5ec, https://agentic-knowledge-base.dev/id/composite/570df80b-916d-466e-a9fe-8a9ac66eea54, https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d]}
---
**파일** — `tools/link.py` 다. 459줄 · 최상위 정의 9개 · 최상위 절 3개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""복원 후보 생성기 뷰 — frontmatter 링크가 없는 단위 지식 쌍의 링크 후보를 체계 안 증거만으로 낸다 (로드맵 8단계 복원,
p10-link-by-construction · p10-candidate-and-confirmed-link · p10-link-judgement-evidence).

게이트가 아니라 **후보 생성기**다. 입력은 그래프 union 뿐이고(체계 밖 정보 0) 판정은 사람이 후보마다 한다 — 채택하면 앵커 단위 지식의
frontmatter 에 링크 키와 `restored:` 를 적는다 (p10-restored-link-marking). 결과는 저장하지 않는다 (4.6절 뷰 원칙).
  단위  살아 있는 단위 지식(status ≠ deprecated). 결정 기록(conclusion·rationale·alternatives)은 한 단위이고 앵커는 결론이다 — 링크 키는
        결론에 적는다. 손으로 쓴 복합체(kg/composite-kg.ttl)의 부분은 각각 단위이되 형제끼리는 후보가 아니다
  근거  체계 안 증거만, 검사 가능성 순 (kb/ontology/related/trace/evidence-ontology.ttl):
        (a) 본문 식별자 — A 본문이 B 를 agt:cites 하는데 frontmatter 링크가 없다 → constructionRecord (본문 식별자는 구축 기록이다)
        (b) 테스트 공동 커버 — `verifies`(V&V → 개발)의 근거다 (p10-link-judgement-evidence). 테스트 케이스 C 가 개발 항목 D 를 verifies 하고
            같은 합격 기준의 검증기 W 가 C 를 돌리며 개발 항목 A 가 D 를 refines 하면 W→A `verifies` 후보 → testCoverage, 값은 테스트 케이스.
            정의는 kb_lib.co_cover 하나다. 같은 V&V 항목이 함께 덮는 개발 항목 두 개의 쌍으로 읽지 않는다
        (c) 개념 공유 — agt:usesConcept 교집합 ≥ --min-shared (기본 3) → proposal (도구 제안 — 확정 근거가 아니며 동률만 깬다)
        (d) 승계 — 조각 F 가 prov:specializationOf O 이면 O 를 가리키던 확정 링크(linkState confirmed, 종류는 LINK_KEYS) X→O 마다
            X→F 후보 → constructionRecord, 값 "승계: O" (p10-split-keeps-work-identity). 종류는 원 링크의 종류를 우선한다
        (e) 동시 편집 — 동시 편집 관측(`--coedit`, kb_lib.coedit_pairs)의 쌍 → coEditHistory, 값은 관측 파일 이름. git 은 읽지 않는다 —
            쌍은 `bazel run //tools:run_evidence -- --coedit-record` 가 고정한 관측에만 있다 (p10-co-edit-evidence-from-small-commits)
        (f) 판정 — 판정자 둘이 쌍 판정지(`label_sample.py --pair-sheet`)로 판정하고 `run_evidence` 가 판정 로그에서 후보 링크 개체에 붙인
            agt:judgement 증거(극성 yes=+ no=−). 같은 쌍·같은 종류의 후보에만 붙고 값은 극성들이다. 동시 편집이 첫 근거인 후보만 판정 대상이다
        임베딩 유사도는 쓰지 않는다 (ODD 가 학습 임베딩을 명시 제외). 같은 세션 읽음은 하네스가 아직 기록하지 않는다
  종류  TIM 허용 칸(kb_lib.TIM_CELLS)에서 고른다 — 인용 방향(대칭 근거는 IRI 순)을 먼저, 다음 역방향, 칸이 없으면 overlapsWith
        (relatedTo 족의 약한 잎 — 관계는 있으나 이름이 아직 없는 자리, overlap-ontology). 그것은 링크 키라 채택이 복원 비율에 든다.
        supersedes 는 시간축이라 후보가 아니다. 한 칸에 종류가 여럿이면 refines > derivesFrom > satisfies > constrains > serves > verifies 순.
        승계 후보는 원 링크의 종류가 제약을 통과하면 그것을 쓴다
  제약  defs/kb.bzl _check_links 와 같은 규칙 — refines·serves 는 더 높은 수준으로·지식 종류 순서 역행 금지, serves 대상은 요구,
        verifies 는 주어 kb/vv·대상 개발 KB·같은 수준. 자기 자신·deprecated·복합체 형제·이미 링크된 쌍·KB 를 가로지르는 overlapsWith 는 탈락.
        구조상 채택될 수 없는 후보 셋을 더 거른다 — `_check_links` 는 Bazel deps(refines·serves·supersedes·verifies)만 보므로
        나머지 키는 여기서 걸러야 후보가 준다:
        (가) KB 가로지름 — verifies 밖의 모든 종류(satisfies·derivesFrom 포함). KB 사이 링크는 verifies 하나다
             (p6-executable-splits-by-kb). 예외는 정제 계층의 functional 행 하나 — V&V 검증 목표(kb/vv requirement, functional)
             → 개발 요구 derivesFrom (p8-scenario-ladder-rungs). 판정은 kb_lib.cross_kb_link 이고 저작된 링크는 같은 함수로
             게이트 `cross-kb-link`(validate)가 거부한다
        (나) 코드 부분 끝점 — 추출 트리(kb_lib.EXTRACT_ROOT) 안에서 복합체의 부분인 단위 지식(정의·절·장·모듈 머리)은 끝점이 아니다.
             링크는 파일 복합체의 선언 단위 지식(module.md)과 질의 단위 지식이 갖는다 (p7-code-links-on-file-composite)
        (다) 테스트 케이스의 derivesFrom — 테스트 케이스(generated.by = kb_lib.CASE_GEN_ACTOR)의 derivesFrom 은 생성기가 자기 시나리오로 쓴다
             (tools/case_gen.py). 그 밖의 대상은 후보가 아니다
  상한  앵커(주어)당 k ≤ --k (기본 7, 로드맵 입력표) — 근거 강도 → 공유 개념 수 → 대상 IRI 순으로 자르고 넘치는 것은 탈락으로 센다.
        라벨은 자르는 데 쓰지 않고 자른 뒤 표시 순서에만 쓴다 — 라벨을 바꿔도 상한 안의 후보는 같다 (p9-candidate-generation-limits, Q169-a)
  큐    첫 근거가 동시 편집인 후보는 판정 넷(kb_lib.judged_class)으로 가른다 — 일치(+,+) · 일치(−,−) · 불일치 · 판정 없음 (task 0262,
        Q-0061 Q145-a). 사람 확인 큐(후보 표)에는 첫 근거가 동시 편집이 아닌 후보와 일치(+,+) 전부, 일치(−,−) 의 표본(kb_lib.JUDGED_NO_SAMPLE_SIZE,
        시드 kb_lib.JUDGED_NO_SAMPLE_SEED 의 sha256 순위)이 판정자 값과 함께 오른다 (task 0303, Q165-c). 표본 밖 일치(−,−)·불일치·판정 없음은
        따로 절을 세운다. 판정은 후보를 확정하지도 무효로 만들지도 않는다 — 확정은 언제나 사람이 frontmatter 에 적는 행위다
사용: link.py --out link-candidates.md [--k 7] [--min-shared 3] [--coedit <관측 .md...>] <TTL...>   (bazel build //kg:link_candidates)
종료: 0 생성됨 · 2 입력 문제(그래프 파일 없음·파싱 불가) — 뷰라 판정 실패(1)는 없다. 후보 0건은 빈 표이지 실패가 아니다
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from collections import Counter, defaultdict

from pathlib import Path
```
<!-- 인용 끝 -->
