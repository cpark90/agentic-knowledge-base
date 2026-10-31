# glossary — 용어집 (표준 용어의 원본)

이 문서는 산문에 쓰는 한글 용어의 원본이다(유저 결정 2026-09-10, 원장 19). **여기 없는 조어를 새로 만들지
않는다.** 표준어가 있으면 그것을 쓰고, 없으면 서술어로 풀어 쓴다(0.0절, STYLEGUIDE §0).

2026-10-23부터 저장소 고유 용어를 분야 표준 용어로 바꾼다. 이 변경은 한글 산문과 한글 제목에만 적용한다. 반면
영문 식별자(`chunk`, `plane`, `level`, `refines`, `serves`, `Composite`)는 온톨로지에 속하므로 바꾸지 않는다(유저
답 Q98, Q99-a, Q103-b, 2026-10-23). 핵심 용어 셋인 청크와 plane, 수준의 개명은 이전 결정(2026-09-02와 2026-09-04)을
개정한 것이다(유저 답 Q99-a, 2026-10-23). 그 가운데 "수준"은 온톨로지의 라벨과 같은 "정제 수준"으로 쓴다(유저 답
Q106-a, 2026-10-23).

한국어 표기는 출처를 확인한 행만 표준 용어로 올린다. 출처는 KS X ISO/IEC 번역과 TTA 정보통신용어사전, 학회나 자격
기구의 용어집, 관용의 순서로 고른다. 표준이 없어 관용으로 올린 행은 출처 열에 '관용'이라고 적는다. 2026-10-23
조사에서는 TTA 정보통신용어사전에 접속하지 못했으므로, TTA 표기는 확인하지 못한 상태다.

노트 v5(`docs/agent-knowledge-system-notes.md`)는 동결되어 있어 고치지 않는다. 따라서 노트 v5와 그 이전 기록은 이
표의 옛 표기로 읽는다(유저 답 Q101-a, 2026-10-23). 2026-09-10 이전 기록, 곧 `harness/user/archive/legacy/`와 git
역사에 남은 옛 결정 트리도 당시 어휘 그대로이므로 같은 방식으로 읽는다.

| 표준 용어 (ko) | en | 옛 표기 | 출처 | tier |
|---|---|---|---|---|
| 단위 지식 | chunk (`agt:Chunk`, 식별자 `chunk`) | 지식 항목 · 청크 | 유저 답 Q163(b·c, 2026-10-25)이 Q99-a(2026-10-23)의 "지식 항목"을 개정했다. Q99-a는 이전 결정(2026-09-02와 2026-09-04)의 "청크"를 "지식 항목"으로 바꿨다. Q160(2026-10-25)은 `agt:Chunk`의 한글 라벨을 "단위 지식"으로, `agt:KnowledgeItem`(knowledge item)의 한글 라벨을 "지식"으로 정했고, Q163은 이 이름을 산문까지 넓혔다. 그래서 옛 표기 "지식 항목"은 자리마다 뜻을 읽어 바꾼다. 파일 하나인 뜻은 "단위 지식"으로, 복합체와 묘비까지 묶는 최상위 뜻은 "지식"으로 쓴다. 영문은 OASIS DITA topic과 ISO/IEC/IEEE 15289 information item에 대응한다. 15289의 KS 부합화는 없고(KSSN 검색, 2026-10-23) TTA는 미확인이므로 한국어는 관용이다 | 2 |
| 지식 종류 | knowledge kind (식별자 `plane`) | plane | 유저 답 Q99-a(2026-10-23)가 이전 결정(2026-09-02와 2026-09-04)을 개정했다. 이 뜻의 표준 용어는 없으므로 서술어로 지었고, 한국어는 관용이다. 옛 표기 `plane`은 식별자로 남으므로 문맥 공존이다 | 3 |
| 정제 수준 (단축형 수준) | refinement level (식별자 `level`) | 추상화 수준 | 아래 "정제 · 정제 계층 · 정제 수준" 행과 같은 말이다. 유저 답 Q99-a(2026-10-23)는 "추상화 수준"으로 바꾸기로 했으나, 온톨로지 `level-ontology`의 라벨과 정의가 "정제 수준"이므로 유저 답 Q106-a(2026-10-23)가 그것을 "정제 수준"으로 바꿨다. 한 문서에서 처음 쓸 때 "정제 수준"으로 적고, 그 뒤에는 "수준"으로 줄여 쓴다. 다섯 수준의 한글 이름(기능·추상·논리·구체·실행 수준)은 그대로다 | 2 |
| 지식 종류별 허용 수준 표 | allowed-level matrix (plane × level) | 수준 허용표 | 서술어이고 관용이다 | 2 |
| 지식 종류별 허용 수준 표 | allowed-level matrix (plane × level) | 거주표 · 상주표 | 서술어 | 1 |
| 결정 기록 | architecture decision record (`agt:Composite` 결정) | 결정 복합체 | ISO/IEC/IEEE 42010. 한국어는 관용이다("아키텍처 결정 레코드", AWS 권장 가이드 한국어판). 지금까지 "결정 기록(ADR)"은 생성 문서 `//kb/dev:adr`의 이름이었으므로 그 문서는 "결정 기록 문서"로 풀어 쓴다 | 2 |
| 테스트 케이스 | test case | 케이스 | KS X ISO/IEC/IEEE 29119-1~4(KSSN 표준명 "소프트웨어 테스팅", "테스트 문서화", 2023 확인)와 ISTQB 용어집 한국어판 "테스트 케이스(test case)". 새 용어가 옛 표기를 포함하므로 잔존은 정규식 기준선으로 센다 | 2 |
| 측정 · 측정치 | measurement · measure | 실측 | ISTQB 용어집 한국어판 "측정(measurement)"·"측정치(measure)" | 2 |
| 해시값 | hash value (digest) | 지문 | ISTQB 용어집 한국어판 "해싱(hashing)" 정의의 "해시된 값(해시)". 항목명이 아니라 정의 안의 표기이므로 관용으로 본다 | 2 |
| 판정 술어 | predicate | 판정식 | 논리학의 술어(predicate). 한국어 사전 대조는 미확인이므로 관용이다 | 2 |
| 재검증 | revalidation | 재판정 | ISO/IEC/IEEE 24765 revalidation. 한국어는 관용이고 아래 "재검증 시점" 행과 같은 낱말이다 | 2 |
| 재검증 시점 | revalidation point | 재판정 경계 | 24765 revalidation | 1 |
| 단일 정의 위치 | single point of definition | 정의처 | 표준이 없으므로 서술어이고 관용이다 | 2 |
| 적용 범위 | scope (`agt:Scope`) | 스코프 | KS 상세정보의 scope 필드 표기 "적용 범위"(KSSN, KS X ISO/IEC/IEEE 29119-1 IDT) | 2 |
| 후보 링크 · 확정 링크 | candidate trace link · confirmed trace link | 없음 | Antoniol 외 2002(IEEE TSE 28(10), 정보 검색 기반 추적 링크 복구). "추적성"은 ISTQB 용어집 한국어판 "추적성(traceability)" | — |
| 설계 공간 | design space | 없음 | MacLean 외 1991 "Questions, Options, and Criteria: Elements of Design Space Analysis". 한국어는 관용이다 | — |
| 겹침 | overlaps | 없음 | 추적성 관계 분류(Ramesh & Jarke) | — |
| 결함 요인 | defect factor | 없음 | ODC v5.2 (Chillarege, IBM) | — |
| 현상 | phenomenon | 없음 | 위험 분석 G1 (HARA 골격) | — |
| 피해 | harm | 없음 | HARA (ISO 26262) | — |
| 한정자 | qualifier | 없음 | ODC v5.2 | — |
| 영향 차원 | impact dimension | 없음 | ODC v5.2 | — |
| 트리거 | trigger | 없음 | ODC v5.2 | — |
| 심각도 · 노출 · 탐지가능성 | severity · exposure · detectability | 없음 | HARA(S·E) · 소프트웨어 FMEA(D) | — |
| 시나리오 부류 | scenario class | 없음 | 위험 분석 G5 | — |
| 관측 수단 | observation means | 없음 | 서술어 | — |
| 검증 대응물 | verification counterpart | 가로대 | V-모델 | 1 |
| 정제 · 정제 계층 · 정제 수준 | refinement · refinement hierarchy · refinement level | 하강 · 사다리 · 정제 높이 | ISO/IEC/IEEE 24765 | 1 |
| 분류 단계 | classification level | 수준(조건 분류의 깊이, 예: 조건 셋째 수준) | 유저 답 Q149-a(2026-10-24). 조건 분류의 깊이를 가리킨다. 첫째 분류 단계가 세 갈래이고, 둘째 분류 단계는 코어 `related/condition`에, 셋째 분류 단계 이하는 프로젝트에 둔다. "수준"은 정제 수준만 뜻하므로 조건 분류에는 쓰지 않는다(`p0-one-word-one-concept`). 동결된 노트 v5의 "셋째 수준"은 그대로 둔다 | 2 |
| 일반화 | generalization | 상승 | 온톨로지 학습 | 3 |
| 전방 추적 커버리지 · 후방 추적 커버리지 | forward · backward traceability coverage | 하강 완주율 · 상향 귀속률 | ISO/IEC/IEEE 29148 | 1 |
| 증거 기록 | evidence record | 장부 · 증거 장부 | ISO/IEC 15026 | 1 |
| 극성 · 지지 · 반박 | polarity · supporting (+) · refuting (−) | 긍정 · 부정 | 증거 기록 항목의 극성이다. 온톨로지 `agt:polarity`의 정의("지지(+) 또는 반박(−)")와 `//kg:audit`의 극성 표가 이 말을 쓴다. 지시 0207(2026-10-24)이 규범 원본의 "긍정·부정"을 이 말로 맞췄다. 한국어는 관용이다. "부정"은 판정 값 같은 다른 뜻으로도 쓰이므로 문맥 공존이다 | 3 |
| 뷰 | view (generated, never stored) | 없음 | ISO/IEC/IEEE 42010. 투영의 하위 종류다(`agt:View`) | — |
| 투영 | projection | 없음 | 원본 지식에서 결정론적으로 생성되는 것이고, 서비스 층을 갖지 않는다. 뷰와 skill이 그 종류다(`agt:Projection`, 유저 답 Q9-a 2026-10-03). 2026-10-03 전에는 "뷰"의 옛 표기로 금지 목록에 있었다 | 2 |
| 기여(하다) | contributes to (`serves`) | 봉사(하다) | 요구 추적 | 1 |
| 할당 · 할당 근거 | allocation · allocation rationale | 배정 · 배정 근거 | ISO 29148. "배정"은 서비스 층이나 값을 정해 주는 다른 뜻(층 배정 · 값 배정)으로도 쓰여 문맥 공존이다(유저 답 Q73-b, 2026-10-07) | 3 |
| 지침 | guidance | 지도 청크 | — | 1 |
| 온톨로지 검사 3단계 · 온톨로지 검사기 | three-stage ontology check (lint · verify · reason) | 컴파일러 3계층 · 3계층 · 온톨로지 컴파일러 | — | 1 |
| 온톨로지 품질 검사 | ontology quality check | 위생 | — | 1 |
| 통제 어휘 | controlled vocabulary | 어휘 폐쇄 | ISO 25964 | 1 |
| ODD 모니터링 | ODD monitoring | ODD 대조 | ISO 34503 | 1 |
| 역량 질문 | competency question | 경쟁 질문 | 온톨로지 공학 (Grüninger & Fox 1995). **국문 정역은 확인하지 못했다.** 국내 문헌은 역량 질문과 능력 질문을 섞어 쓴다 | 1 |
| 검증 · 확인 | verification · validation | 검증 · 평가 | ISO/IEC/IEEE 24765, ISO 9000. 국문에서는 확인과 유효성 확인, 타당성 확인이 섞여 쓰이고, 이 체계는 "확인"을 쓴다. ISTQB 용어집 한국어판에는 두 항목이 없다(2026-10-23) | 3 |
| 평가 | evaluation (지표 측정, 12.3절) | 평가 | 24765 | — |
| 주석 | annotation | 논평 | 표준 번역 | 1 |
| 복합체 | composite | 구성체 | GoF 국문판(김정아 역, 프로텍미디어 2015) "복합체" — 확인됨 | 1 |
| 코어 온톨로지 · 코어 | core ontology | 골격 | 온톨로지 공학 core/domain. "골격"은 규범 문서의 뼈대(`norm` 지식 종류의 절 항목)라는 다른 뜻으로도 쓰여 문맥 공존이다(유저 답 Q73-b, 2026-10-07) | 3 |
| 도메인 프로파일 (단축형: 프로파일) | domain profile | — (단축형 인정, 유저 결정 2026-09-12) | OWL 2 profile, ISO 34503. 첫 언급에 한정(도메인·개발·V&V·참조)을 붙이고 이후 단축한다 | — |
| 신뢰 등급 | trust tier | 트러스트 (티어) | OKF v0.2 | 1 |
| 검증기 | verifier | verifier | 한글 산문 안의 영문 표기가 옛 표기다. 영문 라벨과 식별자(`title`, 디렉토리명 `verifier/`, `verifier_bind`)는 `verifier` 그대로 두고, 치환 대상은 한글 필드뿐이다(유저 결정 2026-09-12). 식별자에 걸린 것은 `waivers.md`로 면제한다. "verifier"는 경로·플래그·영문 문장의 식별자로 다른 뜻으로 쓰여 문맥 공존이다(유저 답 Q73-b, 2026-10-07) | 3 |
| 규칙 | rule (구조 규칙, 42줄 규칙) | 규율 | — | 1 |
| 판정 · 합격 판정 기준 · 판정자 | judgement · pass/fail criteria · judge | (유지) | ISTQB. 용어집 한국어판에는 pass/fail criteria 항목이 없다(2026-10-23). 29148 검증 방법 4종과의 대응은 references §1.1 | — |
| ODD 이탈 · 운영 설계 영역 | ODD exit · operational design domain | (유지) | ISO 34503 (최상위 3범주 scenery·environmental·dynamic). 국문 명칭·"ODD exit" 표기는 미확인 | — |
| 되먹임 | feedback | (유지) | 제어공학 | — |
| 앵커 (두 역할) | anchor | (유지) | 두 역할이 있다. 첫째는 링크가 가리키는 기준점이고, 그 값은 지식 IRI다(4.8절, Eclipse Capra 앵커 해석기). 둘째는 작업 집합의 출발점이고, 지금 작업이 가리키는 지식에서 이웃을 펼친다(0.5절 2026-09-11, LEDGER와 LARGER) | — |
| 안전율 (중복의) | safety margin (redundancy) | (신설 2026-09-11) | 공학 일반의 safety factor/margin. 본문 중복을 용인하는 근거이고([`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)), 경계는 `coUpdatesWith`로 묶는다 | — |
| 작업 집합 · 읽기 집합 · 인수인계 · 게이트 · 승격 | working set · read set · handoff · anchor · gate · promotion | (유지) | OS·DB·품질 관용 | — |
| 하네스 | harness | (유지) | 정의는 유저 문장 그대로다(Q18-a, 2026-10-03): "하네스는 에이전트를 형성하기 위해서 필요한 행동방침, 도구, 정체성 등이다." 목록은 열려 있다. 기록의 주체는 에이전트이고 하네스의 도구가 기록 수단이다(Q17-b, `r-019`). ISTQB의 테스트 하네스(스텁·드라이버 모음)와 다른 뜻이다 | 2 |
| 서비스 층 (단축형: 층) | layer | 요구 층 · development 층 · V&V 층 · 코어 층 · 세 층 바인딩 | 결정 [`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md), 유저 답 Q69-a(2026-10-06). 서비스의 세 층(지식·방법론·프로세스, `agt:Layer`, 키 `layer`)에만 쓴다. 다른 뜻은 새 낱말 없이 풀어 쓴다 | 1 |
| 실행 계층 | gate tier | 없음 | `defs/kb.bzl` 의 `GATE_TIERS` · 결정 [`p6-gate-catalogue`](../kb/dev/decision/p6-gate-catalogue/conclusion.md). 게이트를 어느 기계가 판정하는가의 다섯(shape·verify·analysis·test·human)에만 쓴다. 하나를 가리키면 "verify 실행 계층"이다 | 2 |
| 분류 계층 | class hierarchy | 없음 | OWL 2 (`rdfs:subClassOf` 의 상하 관계). 태그 분류와 맞서는 뜻도 이 낱말이다 | 2 |
| 검증 환경 계층 | test environment level | 없음 | 결정 [`p8-verification-environment-ladder`](../kb/dev/decision/p8-verification-environment-ladder/conclusion.md), 노트 8.9절. 여섯 단계(단위 ~ 실환경)에 쓴다 | 2 |
| 제목 계층 | heading hierarchy | 없음 | markdownlint MD001 · WCAG 2.2 SC 1.3.1. 마크다운 제목 수준(h1~h6)의 차례에만 쓴다 | 2 |
| 작업 메모리 (`memory`) | working memory plane | 없음 | 결정 [`p5-plane-by-verification`](../kb/dev/decision/p5-plane-by-verification/conclusion.md) 결론의 지식 종류 표. 항목은 관측(실행 기록 `agt:Run`, [`p0-run-is-an-append-only-memory-chunk`](../kb/dev/decision/p0-run-is-an-append-only-memory-chunk/conclusion.md))이다 | 2 |
| 단기기억 · 장기기억 | short-term memory · long-term memory | 없음 | 결정 [`p11-memory-promotion-rule`](../kb/dev/decision/p11-memory-promotion-rule/conclusion.md). 단기기억은 `memory` 지식 종류(작업 메모리)에 두고, 장기기억은 주제 지식 종류로 승격한다. 승격 규칙은 체계가 고정하지 않는 입력이다 | 2 |
| 역할 메모리 | role memory | 없음 | [`harness/agents/interpreter.md`](../harness/agents/interpreter.md)의 "역할 메모리" 절과 `.claude/agent-memory/<역할>/`. 세션 역할이 재사용 지식을 남기는 그래프 밖의 자리다. 결정 `p11-memory-promotion-rule`은 역할 메모리를 단기기억·장기기억 어느 쪽으로도 정하지 않는다 | 2 |
| 확률적 지식 모델 [후보] | probabilistic knowledge model | 없음 | 유저 지시 2026-10-22·2026-10-24(Q-0063 Q153), 요구 r-032(draft), Q87-b. 지식을 확률 구조적으로 모델링한 결과물이다. 링크와 결정 후보가 증거에서 계산한 믿음 정도를 갖는 지식 베이스 자체를 가리킨다. "학습 기반 방법에서의 주요요소인 모델"이 아니다(유저 지시 2026-10-24). 단독 "모델"은 쓰지 않는다 | — |
| 믿음 정도 [후보] | degree of belief | 없음 | 베이즈 확률의 관용 번역, 요구 r-032(draft), Q88. 링크·결정 후보가 증거에서 계산해 갖는 확률이다. 노트 1.6절의 "신념 상태"(belief state, `memory` 지식 종류)와 다른 말이다 | — |
| 인터프리터 | interpreter | 없음 | 유저 답 Q123-b(2026-10-24). 유저 설명 원문은 "interpreter는 프로그래밍 언어의 해석기에서 차용한 용어임. 그와 유사한 역할을 할 예정임."이다. 외부 대상의 요청을 해석해 지식 베이스에 대한 동작으로 옮기는 에이전트 역할에만 쓰고, 정의는 결정 [`p11-interpreter-generalizes-hci`](../kb/dev/decision/p11-interpreter-generalizes-hci/conclusion.md)에 있다 | — |

**tier** 열은 옛 표기를 어떻게 다루는가를 적는다(agrtls B, 유저 채택 2026-09-12).

- tier 1은 기계 치환이다. `consistency` ⑥이 옛 표기의 잔존을 센다.
- tier 2는 유저 결정이다.
- tier 3은 문맥 공존이다. 옛 표기가 다른 뜻으로도 쓰이므로 바꾸지 않는다. 증가를 뜻하는 "상승"과 지표 측정의 "평가",
  식별자 `plane`이 그 예다.
- 대시(—)는 옛 표기가 없다는 뜻이다.

2026-10-23에 올린 개명 행은 이행 단계 동안 tier 2로 둔다. 본문 이행(Q100의 5단계)을 아직 승인받지 않았기 때문이다.
지금 tier 1로 두면 ⑥이 이행 전의 잔존 수천 건을 보고해, 기존 tier 1 행의 표류를 가린다. 5단계를 시작할 때는 새 용어가
옛 표기를 포함하지 않는 행을 tier 1로 올린다. 그런 행은 단위 지식과 결정 기록, 측정, 해시값, 판정 술어, 재검증, 단일
정의 위치, 적용 범위, 지식 종류별 허용 수준 표다. 반면 새 용어가 옛 표기를 포함하는 행은 tier 2에 남긴다. 테스트
케이스는 케이스를 포함하고 정제 수준은 수준을 포함하므로, ⑥의 부분 문자열 계수로는 잔존이 0이 되지 않기 때문이다.
이 두 행의 잔존은 기준선 정규식 `(?<!테스트 )케이스`와 `(?<!정제 )수준`으로 따로 센다. 다만 "수준"은 단축형으로
허용되므로, 그 수는 줄일 목표가 아니라 참고값이다.
