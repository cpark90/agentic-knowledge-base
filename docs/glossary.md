# glossary — 용어집 (표준 용어의 원본)

산문에 쓰는 한글 용어의 원본이다 (유저 결정 2026-09-10, 원장 19). **여기 없는 조어를 새로 만들지
않는다** — 표준어가 있으면 그것을 쓰고, 없으면 서술어로 풀어 쓴다 (0.0절, STYLEGUIDE §0). 영문
식별자(`refines`·`serves`·`Composite`·`plane`·`level`)는 온톨로지의 것이며 바꾸지 않는다.
2026-09-10 이전 기록(`docs/feedback/`, deprecated `chunks/`)은 당시 어휘 그대로다 — 이 표로 읽는다.

| 표준 용어 (ko) | en | 옛 표기 (2026-09-10 이전) | 출처 | tier |
|---|---|---|---|---|
| 검증 대응물 | verification counterpart | 가로대 | V-모델 | 1 |
| 정제 · 정제 계층 · 정제 수준 | refinement · refinement hierarchy · refinement level | 하강 · 사다리 · 정제 높이 | ISO/IEC/IEEE 24765 | 1 |
| 일반화 | generalization | 상승 | 온톨로지 학습 | 3 |
| 전방 추적 커버리지 · 후방 추적 커버리지 | forward · backward traceability coverage | 하강 완주율 · 상향 귀속률 | ISO/IEC/IEEE 29148 | 1 |
| 수준 허용표 | allowed-level matrix (plane × level) | 거주표 · 상주표 | — (서술어) | 1 |
| 재검증 시점 | revalidation point | 재판정 경계 | 24765 revalidation | 1 |
| 증거 기록 | evidence record | 장부 · 증거 장부 | ISO/IEC 15026 | 1 |
| 뷰 | view (generated, never stored) | 투영 | ISO/IEC/IEEE 42010 | 1 |
| 기여(하다) | contributes to (`serves`) | 봉사(하다) | 요구 추적 | 1 |
| 할당 · 할당 근거 | allocation · allocation rationale | 배정 · 배정 근거 | ISO 29148 | 1 |
| 지침 | guidance | 지도 청크 | — | 1 |
| 온톨로지 검사 3단계 · 온톨로지 검사기 | three-stage ontology check (lint · verify · reason) | 컴파일러 3계층 · 온톨로지 컴파일러 | — | 1 |
| 온톨로지 품질 검사 | ontology quality check | 위생 | — | 1 |
| 통제 어휘 | controlled vocabulary | 어휘 폐쇄 | ISO 25964 | 1 |
| ODD 모니터링 | ODD monitoring | ODD 대조 | ISO 34503 | 1 |
| 역량 질문 | competency question | 경쟁 질문 | 온톨로지 공학 (Grüninger & Fox 1995). **국문 정역 미확인** — 국내 문헌은 역량/능력 질문 혼용 | 1 |
| 검증 · 확인 | verification · validation | 검증 · 평가 | ISO/IEC/IEEE 24765, ISO 9000. 국문은 확인·유효성 확인·타당성 확인이 혼용 — 이 체계는 "확인" | 3 |
| 평가 | evaluation (지표 측정, 12.3절) | 평가 | 24765 | — |
| 주석 | annotation | 논평 | 표준 번역 | 1 |
| 복합체 | composite | 구성체 | GoF 국문판(김정아 역, 프로텍미디어 2015) "복합체" — 확인됨 | 1 |
| 코어 온톨로지 · 코어 | core ontology | 골격 | 온톨로지 공학 core/domain | 1 |
| 도메인 프로파일 (단축형: 프로파일) | domain profile | — (단축형 인정, 유저 결정 2026-09-12) | OWL 2 profile, ISO 34503. 첫 언급에 한정(도메인·개발·V&V·참조)을 붙이고 이후 단축한다 | — |
| 신뢰 등급 | trust tier | 트러스트 (티어) | OKF v0.2 | 1 |
| 검증기 | verifier | verifier | 한글 산문 안의 영문 표기가 옛 표기다. 영문 라벨·식별자(`title`, 디렉토리명 `verifier/`, `verifier_bind`)는 `verifier` 그대로 — 치환 대상은 한글 필드뿐 (유저 결정 2026-09-12); 식별자 히트는 `waivers.md`로 면제 | 1 |
| 규칙 | rule (구조 규칙, 42줄 규칙) | 규율 | — | 1 |
| 판정 · 합격 판정 기준 · 판정식 · 판정자 | judgement · pass/fail criteria · predicate · judge | (유지) | ISTQB (국문 용어집 표기는 미확인). 29148 검증 방법 4종과의 대응은 references §1.1 | — |
| 청크 · 지식 종류(plane) · 수준(level) | chunk · plane · level | (유지) | 유저 결정 2026-09-02·04 | — |
| ODD 이탈 · 운영 설계 영역 | ODD exit · operational design domain | (유지) | ISO 34503 (최상위 3범주 scenery·environmental·dynamic). 국문 명칭·"ODD exit" 표기는 미확인 | — |
| 되먹임 | feedback | (유지) | 제어공학 | — |
| 앵커 (두 역할) | anchor | (유지) | ① 링크가 가리키는 기준점 = 청크 IRI (4.8절, Eclipse Capra 앵커 해석기) ② 작업 집합의 출발점 = 지금 작업이 가리키는 청크, 이웃을 펼친다 (0.5절 2026-09-11, LEDGER·LARGER) | — |
| 안전율 (중복의) | safety margin (redundancy) | (신설 2026-09-11) | 공학 일반 safety factor/margin. 본문 중복을 용인하는 근거 — [`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md), 경계는 `coUpdatesWith` | — |
| 작업 집합 · 읽기 집합 · 인수인계 · 게이트 · 승격 | working set · read set · handoff · anchor · gate · promotion | (유지) | OS·DB·품질 관용 | — |

표기: **tier** 1 = 기계 치환(`consistency` ⑥이 옛 표기 잔존으로 센다) · 2 = 유저 결정 · 3 = 문맥 공존(바꾸지 않는다 — 옛 표기가 다른 뜻으로도 쓰인다: 증가 의미의 "상승", 지표 측정의 "평가") · — = 옛 표기 없음 (agrtls B, 유저 채택 2026-09-12).
