---
id: https://agentic-knowledge-base.dev/id/chunk/4968c95b-0d6d-4a5c-89d6-485cfc822180
type: artifact
level: executable
title_ko: 파일 tools/consistency.py
title: file tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9d3f4240-66d0-4dfd-9124-9499e65cb57a, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97, https://agentic-knowledge-base.dev/id/chunk/5287133e-f7a3-4913-8aaf-062647cf5491]
composite: {id: https://agentic-knowledge-base.dev/id/composite/6cf102de-daa9-4edc-bd55-b2dab0f902b8, title_ko: 파일 복합체 tools/consistency.py, title: file composite tools/consistency.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fa1732a8-9290-48de-8e7f-90f31527d6e6, https://agentic-knowledge-base.dev/id/composite/d7a2d774-2413-46e9-bd6d-6281509faf4c, https://agentic-knowledge-base.dev/id/composite/65bc7b55-1885-496f-8600-24e609326f5f, https://agentic-knowledge-base.dev/id/composite/cad544bc-3441-4d9e-849e-71609044a7e7]}
---
**파일** — `tools/consistency.py` 다. 608줄 · 최상위 정의 27개 · 최상위 절 4개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 청크 파일에서 보고한다 (p4-redundancy-as-safety-margin).

게이트가 아니라 **보고**다: 병합·묶기·유지의 판정은 사람 또는 승인된 판정자가 하고(9.8절), 이 도구는
후보를 추린다. 재검증 시점(커밋)마다 생성하고 저장하지 않는다 (4.6절 뷰 원칙).

  ① 정확 중복 — 본문 sha256 앞 12자(contentHash)가 같은 살아 있는 청크 쌍
  ② 라벨 중복 — title_ko 또는 title 이 같은 청크 (용인 불가: 라벨은 인터페이스)
  ③ 근사 중복 후보 — 본문 문자 5-gram 집합의 Jaccard ≥ θ (기본 0.5). 유사도는 후보 추림에만 쓴다
  ④ 묶임과 응집 — ①·③ 쌍이 coUpdatesWith 로 묶여 있는가(안 묶인 중복이 드리프트 후보), 그리고 묶인 쌍의 현재 본문
     Jaccard 가 θ_cohesion(기본 θ/2) 미만인가 — 응집 저하 후보: 묶었으나 본문이 갈라짐, suspect 판정 대상.
     저장된 이전 값과의 비교가 아니라 절대 임계다 — 뷰는 저장하지 않으므로(4.6절) 비교할 캐시가 없다.
     학습 모델 임베딩은 ODD 명시 제외(project-odd.yml EXCLUSIONS_REVIEWED)라 유사도는 문자 n-gram 으로만 잰다
  ⑤ 결론 라벨 형식 — 결정의 결론(conclusion.md 또는 단일 파일 결정)의 title_ko 가 문장형(…다)으로 끝나는가.
     근거·대안 라벨은 명사구가 관례라 보지 않는다 (label-representativeness-protocol (c) ④: "결정 라벨은 결론 문장형")
  ⑥ 용어 — docs/glossary.md 의 "옛 표기"가 살아 있는 청크 본문에 남아 있는가. **tier 1 (기계 치환)만** 위반이다 —
     tier 2 는 유저 결정, tier 3 은 문맥 공존(바꾸지 않음), — 는 옛 표기 없음. tier 열이 없으면 전부 1 로 보고 info 를 남긴다.
     docs/waivers.md 의 게이트 id `term-drift`(축 파일)에 면제된 파일의 히트는 집계에서 빼되 목록에 남긴다 (C)
  ⑦ 단정성 — STYLEGUIDE §0 "산문은 단정 서술형"(유저 결정 2026-09-13) 가운데 게이트 `prose`(chunk_lint·doccheck: 경어·감탄)가
     거부하지 않는, 판단이 필요한 나머지: 추측 표현(것 같·듯하·수도 있·아마 …)·구어 후보(근데·그냥·좀·엄청·뭔가·약간)의
     파일·줄·표현 목록과, 대시 밀도(문장당 " — " 수; 문장 = 마침표 종결 또는 마침표 없는 종결 "다" 뒤에 `|`·`)`·닫는 따옴표·
     줄끝이 오는 곳 — 명사형 종결 "기각." 과 표 셀 "…다 |" 를 다 센다; 줄·불릿·셀 첫머리의 종결 없는 짧은 라벨 뒤의
     라벨 대시 "**결론** — "·"- 라벨 — " 는 구조적 구분자라 세지 않는다)가 1.0 을 넘는 청크(상위 20). 목록·정규식의 단일 정의처는 kb_lib(PROSE_HEDGES·PROSE_COLLOQUIAL·PROSE_SENTENCE_END·prose_segments).
     대시·문장 모두 산문 조각(prose_segments) 안에서만 센다 — 코드·따옴표 안은 산문이 아니다
  ⑧ 첨가 — 슬롯의 질문에 답하지 않는 문장과 빈 값의 이상 표기(명세 문서 작성 규격 4.1·9.4절, 유저 승인 2026-09-22;
     결정 p4-three-empty-values). 셋을 본다: 메타 문장(다음과 같다·이 절에서는 …), 채움 문구(특이사항 없음·추후 결정한다 …),
     세 빈 값(`없음`·`해당 없음`·`미확정`) 밖의 표기(`N/A`·`TBD`·`미정`·표의 단독 대시 셀). 정의처는 kb_lib
     (PROSE_META·PROSE_FILLER·EMPTY_VALUE·EMPTY_VALUE_REJECTED·check_addition)
  ⑨ 목록 — 목록 규칙(같은 규격 4.3절): 손 번호(`2.` 이상 — 순서 목록의 항목은 모두 `1.` 로 쓴다) · 항목 9개 초과 ·
     중첩 3단계 이상 · 항목당 240자 초과 · 빈 항목. 같은 문법 형은 기계 판정이 되지 않아 보지 않는다. 항목 길이는
     소스 줄이 아니라 **글자**로 잰다 — 이어지는 들여쓴 줄을 합치고 연속 공백을 하나로 줄인 뒤 센다. 손 줄바꿈이
     110~120자라 소스 줄을 세면 접힌 자리가 그대로 위반이 된다 (STYLEGUIDE §0, 유저 승인 2026-09-22). 정의처는
     kb_lib(LIST_MAX_ITEMS·LIST_MAX_DEPTH·LIST_MAX_ITEM_CHARS·check_lists)
  ⑩ 중복 확정 후보 — ③의 근사 중복 중 `coUpdatesWith` 미묶음 쌍(+①의 미묶음 정확 중복)을 판정자 질문("이 두 블록은
     같은 주장을 담는가?")의 입력 후보로 다시 낸다(judge-without-service-2026-09-30 기계 환원 ②). 후보 생성까지이고
     병합·묶기·유지의 확정은 판정자(사람 또는 세션 판정자) 몫이다 — ③과 같은 데이터를 판정 관점으로 다시 읽은 것이라
     수치가 갈리지 않는다.
  ⑪ 자리 후보 — 둘 이상의 등록 본문 슬롯(`agt:bodySlot`)을 가진 청크에서, 한 슬롯의 영역 안에 **다른** 슬롯의 표지
     낱말이 한글 음절 경계 밖(조사가 붙지 않은 자리)으로 등장하면 후보로 낸다 — "이 문장이 그 슬롯에 있어야 하는가"의
     판정자 질문 입력이다(judge-without-service-2026-09-30 기계 환원 ②). 슬롯이 하나뿐인 청크(결정 세 청크·V&V
     시나리오 세 청크)는 대상이 아니다. 확정은 판정자 몫이고 이 축은 후보만 낸다 — 낱말 재등장이 전부 오배치는
     아니므로 오탐이 있을 수 있다(게이트가 아니라 보고인 이유).

⑧·⑨ 의 **판정은 게이트 `chunk_lint`** 가 한다 — 게이트 id 는 `addition`(메타 문장·채움 문구)·`empty-value`(빈 값 표기)·
`list-rules`(목록 규칙)이고, 보고 수치가 0 이 된 2026-09-22 에 올렸다(반영 계획 7번, STYLEGUIDE §2 — 강화는 약화가 아니다).
이 절은 목록과 맥락을 주는 보고로 남는다. 둘이 같은 함수(kb_lib.check_addition·check_lists)를 쓰므로 수치가 갈리지 않는다.
⑥ 과 같은 규약으로 waivers.md 의 면제는 집계에서 빼되 목록에 남긴다. ⑩·⑪ 은 후보 생성까지이고 게이트가 아니다 —
확정에는 판정자(세션 판정자 또는 사람)가 필요하다(`tools/judge.py`).

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(용어집·waiver 표·청크 파싱 불가). 보고 뷰라 판정 실패(1)는 없다
사용: consistency.py --out consistency.md [--theta 0.5] [--theta-cohesion θ/2] [--glossary docs/glossary.md] [--waivers docs/waivers.md] <청크 .md …>
"""
import argparse
import os
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path
```
<!-- 인용 끝 -->
