---
id: https://agentic-knowledge-base.dev/id/chunk/072c3853-c694-43fd-a8b9-c834aa2e363e
type: artifact
level: executable
title_ko: 파일 tools/chunk2kg.py
title: file tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce, title_ko: 파일 복합체 tools/chunk2kg.py, title: file composite tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24, https://agentic-knowledge-base.dev/id/composite/d2327845-e19c-432e-bef7-b5d429601fb6, https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e, https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a, https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94, https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0, https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2, https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828, https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72]}
---
**파일** — `tools/chunk2kg.py` 다. 979줄 · 최상위 정의 27개 · 최상위 절 9개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:lineCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식 (YAML 부분집합 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}).
OKF v0.2 번들이므로 type·status·generated·verified 는 그 스펙의 필드명을 쓴다:
  iri:          항목 IRI (필수)
  type:         requirement | decision | contract | schema | artifact | annotation | memory (필수, OKF).
                예외 하나가 `agt:Space` 다 — plane 이름이 아니라 온톨로지 클래스 이름이고, 그 청크는 설계 공간(`-space`)이라
                본문의 후보·제약까지 읽어야 그래프가 된다. 여기서는 frontmatter 만 판정하고(level 은 logical 고정) 방출은
                tools/space2kg.py 가 한다 — 이 도구에 넘기면 `FAIL [space]` 다 (결정 p9-candidate-storage)
  level:        functional | abstract | logical | concrete | executable (필수)
  title_ko:     한글 라벨 (필수) — OKF 확장 키
  title:        영어 라벨 (필수) — OKF title
  status:       draft | stable | suspect | invalidated | deprecated (필수, OKF + 확장 2)
  generated:    {by: <행위자>, at: <ISO 8601>} (필수, OKF)
  verified:     [{by: <행위자>, at: <ISO 8601>}, ...] (선택, OKF) — human: 접두어가 사람 검토
  assumes:      가정 IRI 목록 (선택)
  sources:      OKF v0.2 sources — [{resource: IRI, id?, title?, author?}] (선택). resource → prov:wasDerivedFrom
  refines:      이 항목이 정제하는 상위 항목 IRI 목록 (선택, 수직 링크 9.2절)
  supersedes:   이 항목이 대체하는 항목 IRI 목록 (선택)
  serves·verifies·derivesFrom·satisfies·constrains·allocates·generates·overlapsWith: 그 밖의 링크 키(LINK_KEYS) — 대상 IRI 목록 (선택).
                모든 링크 키는 직접 트리플(agt:<key>)과 링크 개체(agt:Link, emit_links) 둘로 나간다. verifies 의 주어는 kb/vv 청크뿐 (defs/kb.bzl).
                overlapsWith 는 relatedTo 족의 약한 잎이다 — 추적 매트릭스에 칸이 없어 어느 잎도 이름을 주지 못하는 관계의 자리이고,
                Bazel deps 가 되지 않는다(gen_build.LINKS 밖) 대신 링크 개체와 복원 표시를 받는다 (overlap-ontology)
  uses:         이 정의가 이름으로 쓰는 **같은 모듈의 최상위 정의** 청크 IRI 목록 (선택, type: artifact 에서만 —
                agt:usesDefinition 의 정의역이 agt:ArtifactChunk 다). agt:usesDefinition 으로 나간다. 링크 키가 아니다 —
                Bazel deps 도 링크 개체도 되지 않는다(링크는 파일 복합체의 것이다, p7-code-links-on-file-composite).
                값의 원본은 손이 아니라 tools/extract.py 이고 대상 실재는 validate check_dangling 이 본다
  exposes:      이 항목이 노출하려는 결함 요인(현상) 개체의 agt: IRI 목록 (선택, 위험 분석 G5 — 노트 8.21절).
                agt:exposesFactor 로 나간다. 링크 키가 아니다 — 대상이 청크가 아니라 온톨로지 개체이므로 링크 개체의
                치역 밖이고 Bazel deps 도 되지 않는다. 대상의 종류는 shape exposes-factor-shapes.ttl 이 판정한다
  restored:     복원 링크의 표시 — 같은 청크의 링크 키(LINK_KEYS) 어딘가에 대상으로 있는 IRI 목록 (선택, p10-restored-link-marking).
                그 (주어, 링크 키, 대상)의 agt:Link 개체에 증거가 두 줄 붙는다 — 확정 기록 constructionRecord(사람이 frontmatter 에 적은
                편집 시점 기록; 9.11절 규칙 "구축(+) 또는 실행(+) 없이 확정 불가"를 verify 질의 confirmed-without-evidence 가 강제한다)와
                후보의 출처 proposal(도구·에이전트가 제안하고 사람이 확정). 구축 링크는 constructionRecord 한 줄뿐이므로 proposal 의 유무가
                복원의 표지다. linkState 는 그대로 confirmed 다 — frontmatter 에 적힌 것은 확정이다. 링크 대상에 없는 IRI 는
                `FAIL [restored] <파일>: 복원 표시 <IRI> 가 링크 대상에 없다` 로 거부. 복원 비율(metrics·audit)은 증거 종류로 센다 (kb_lib.link_origins)
  specializationOf: 분할로 생긴 조각이 원 청크를 가리키는 단일 IRI (선택, p10-split-keeps-work-identity) → prov:specializationOf (PROV-O).
                청크 uuid 는 work-id 다: 분할 시 조각 하나가 원 uuid 를 승계하고 나머지는 새 uuid + 이 키로 잇는다. 자기 자신은 거부.
                대상 실재는 validate dangling, 같은 plane·살아 있음·사슬 비순환은 validate check_specialization(FAIL [specialization])이
                판정한다. 순환은 이 도구도 뿌리를 계산할 수 없으므로 같은 게이트 id 로 거부한다
  링크 IRI:     id/link/<sha256(뿌리(출발)|종류|뿌리(도착))[:12]> — 양 끝은 specializationOf 사슬을 따라 올라간 뿌리 uuid(work-id)다.
                그래서 조각을 가리키는 링크와 원본을 가리키던 링크가 같은 개체가 되어 증거·이력이 이어진다. 뿌리는 묶음 전체를 알아야
                계산되므로 --fragment 는 원 IRI 로 해시하고 --merge(와 단일 실행)가 rebase_links 로 다시 계산해 같은 IRI 의 링크·증거
                블록을 하나로 합친다(양 끝·증거의 합집합). 증거 IRI 는 같은 해시에 접미(-proposal)다
  coUpdatesWith: 같은 내용을 담아 함께 갱신되어야 하는 청크 IRI 목록 (선택, relatedTo 족 — 안전율 중복의 표시)
  part_of:      소속 복합체 IRI (선택) — 복합체는 멤버 중 하나가 composite: 로 선언
  composite:    {id: …, title_ko: …, title: …, ordered: [<부분 IRI>…], part_of: <상위 복합체 IRI>} (선택) — 복합체 개체 선언.
                `part_of` 는 선택 키이며 **선언된 복합체**가 다른 복합체의 직접 부분임을 적는다 (p4-composite-as-part-of —
                복합체는 청크 또는 다른 복합체를 부분으로 갖는다). 청크의 최상위 `part_of` 와 자리가 다르다: 앞은 청크의
                소속, 뒤는 복합체의 소속이다. 상위 복합체도 같은 실행의 입력 집합 안에서 선언돼야 하고 사슬은 순환하지
                않는다. 코드 추출(p7-code-links-on-file-composite)의 파일 → 장·절 → 함수 세 층이 이 키로 선다. `ordered` 는 선택 키이고
                순서가 뜻을 갖는 복합체만 적는다 (결정 p4-composite-order-is-declared). 있으면 `agt:Composite , co:List` 로
                타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`
                을 그 순서로 낸다. 없으면 `agt:hasDirectPart` 만 낸다(순서 없음) — 순서를 요구하지 않는 것에 순서를 붙이면
                거짓 정보다. 목록이 부분 전부를 빠짐없이 한 번씩 담지 않으면 거부한다. **예외는 없다** — 결정 복합체도 선언으로만
                순서를 갖고(유저 승인 2026-09-29) 그 선언은 `--ordered` 인자로 들어온다. 이 도구는 역할 이름으로 순서를 추측하지 않는다.
                **묶음의 단위는 파일이 아니라 이 실행의 입력 집합**이다 (2026-09-26 반영). part_of 대상은 같은 실행의 파일 어딘가에서
                composite: 로 선언돼야 한다. 그 입력 집합을 만드는 것이 defs/kb.bzl 의 kb_decision(결론·근거·대안 셋)과
                kb_composite(부분 2~9 가변)이고, 청크 하나만 받는 kb_chunk 로는 복합체가 서지 않는다
  pattern:      ubiquitous | event-driven | state-driven | unwanted-behaviour | optional | complex (선택, type: requirement 에서만) —
                요구 문장의 EARS 패턴 (Mavin RE'09, 결정 p7-dev-plane-substance) → agt:pattern agt:<camelCase 개체>. 다른 plane 에 있으면 거부
  targets:      주석이 관찰하는 대상 IRI 목록 (선택, type: annotation 에서만) → agt:targets 직접 트리플.
                **링크 키가 아니다** — 링크 개체(agt:Link)도 Bazel deps(gen_build.LINKS)도 만들지 않는다. 주석이 대상의 deps 가
                되면 주석 하나가 대상의 재빌드를 유발해 리뷰가 빌드 그래프를 오염시킨다. 주석은 대상을 관찰하지 구성하지 않는다
  주석의 본문:   type: annotation 의 본문은 주석이다 (p7-commentary-form). 첫 줄 `<라벨> (<장식>): <요지>` 와 줄 머리 슬롯 넷
                (`대상:`·`본문:`·`제안:`·`해소:`)에서 agt:commentLabel·agt:commentDecoration·agt:resolutionState·
                agt:commentSentenceCount 를 낸다. 닫힌 어휘와 문장 상한의 판정은 shape(review-comment-body-shapes.ttl)이고
                여기서 거부하는 것은 `대상:` 과 frontmatter `targets` 의 불일치 하나뿐이다
  프로파일 타이핑: 청크마다 plane 클래스 뒤에 개발 프로파일의 실체 클래스를 더 붙인다 (`a agt:RequirementChunk , agt:RequirementStatement`,
                PROFILE_SUBSTANCE). 살아 있는 청크든 폐기된 청크든 같다 — 폐기된 요구 문장도 요구 문장이다
  라벨 언어:    title 에 한글([ㄱ-ㆎ가-힣])이 있거나 title_ko 에 한글이 없으면 거부 — 영문 라벨에 한글을 섞지 않는다(0.6절).
                composite 의 title·title_ko 도 같은 @en/@ko 라벨이므로 같은 규칙으로 거부한다
  --ordered:    묶음의 복합체가 선언한 부분의 순서 (인자, 선택) — 생성 BUILD 의 `kb_decision.ordered`·`kb_composite.ordered` 가 넘긴다.
                결정 복합체 205개의 선언이 이 자리다 (유저 승인 2026-09-29: 예외 없음, 손으로 frontmatter 를 고치지 않는다).
                frontmatter `composite.ordered` 와 함께 있으면 같아야 한다 — BUILD 는 뷰이고 frontmatter 가 원본이다
  인용원:       본문(frontmatter 제외, **코드 펜스 밖**)에 소멸성 채널 경로 `docs/feedback/` 가 있으면 거부 — 규칙·근거는 영속 지식
                (노트·결정)에 둔다 (agrtls-practices-review P). status: deprecated 청크는 제외

출력·종료: 위반은 `FAIL [chunk2kg] <경로>: <메시지>` (병합은 `FAIL [chunk2kg-merge]`, 특수화 사슬은 `FAIL [specialization]`) + EXIT_FAIL,
           읽을 수 없는 입력은 EXIT_CONFIG. 생성기이므로 입력 0건은 빈 그래프(SKIP 아님).
사용: chunk2kg.py --out <생성.ttl> --residency defs/kb.bzl <청크 파일들...> (--merge 는 --residency 없이 조각을 잇기만 한다)
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import re
import sys
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 이 도구는 rdflib 없이 돌므로(타깃마다 실행) 없으면 같은 값의 폴백
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
