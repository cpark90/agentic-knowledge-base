# ontology — 지식의 코어과 분야 프로파일

구조도 v5에 따라 **코어 / development / V&V** 세 층으로 적는다. 온톨로지는 이 체계의 **어휘**다. 계층의 한 단계가 아니라 계층 전체가 쓰는 어휘이며,
이 어휘 밖에서 쓴 지식은 이 체계에 존재하지 않는다
([`id:chunk-d0046`](../chunks/decision/d-0046-ontology-as-vocabulary.md)).

## 코어 — 두 층(코어·프로파일)

| 층 | 담는 것 | 누가 만드나 | 위치 |
|---|---|---|---|
| **코어** | 분야와 무관한 것 — plane, level, 조건, 가정, 역할, 청크·복합체, 링크 타입 | 이 저장소 | `kb/ontology/` (`agt:`) |
| **분야 프로파일** | 각 plane의 실체와 판정 도구, 조건 어휘 셋째 수준, 도메인 결함 하위 유형, 앵커 해석기 | 분야마다 | `profile/<분야>` (미구현) |

프로파일은 별도 장치가 아니라 **코어을 확장만 하는 온톨로지 모듈**이다. 코어 클래스의
하위 클래스와 shape만 추가하며, 코어을 수정하는 프로파일은 검사 실패다
([`id:chunk-d0057`](../chunks/decision/d-0057-profile-extension-only-module.md)). 한 프로젝트가
프로파일을 여럿 가질 수 있고, 링크는 프로파일을 넘는다.

**현재 `profile/` 디렉토리는 없다.** 프로파일 구축 절차도 아직 없다 —
[`method.md §1`](method.md#1-프로파일-구축)이 그 자리이고, 첫 프로파일 작성이 다음 산출이다
([`roadmap.md`](roadmap.md)).

## 코어의 구성

```
kb/ontology/
  project-ontology.ttl          # 최상위. import만 하는 얇은 파일
  entity/                       # plane으로 분류 가능한 개념
    knowledge-item/             #   KnowledgeItem · Chunk · Composite · plane 7종 · level · 속성
  related/                      # 횡단 개념 — 어느 plane에도 속하지 않는다
    condition/  scope/  assumption/  channel/  harness/  trace/  trust/  state/  tag/
  shapes/                       # SHACL — 원칙의 검사 가능한 형태 (plane×level 수준 허용표 포함)
  proposals/                    # 용어 제안 승인 큐 — //kb/ontology:modules 밖 (2.5절)
```

모듈 = 디렉토리 = Bazel 패키지이고, 한 파일이 한 주제다. 분할 축은 둘 — **plane으로
분류되는 개념(`entity/`)과 횡단 개념(`related/`)**, 그리고 **어휘(`-ontology`)와
형식화(`-rules`·`-shapes`)** ([`id:chunk-d0048`](../chunks/decision/d-0048-ontology-module-structure.md)).

`related/trace`(링크 타입·링크 개체·판정 근거, 파일 8개)가 2026-09-04에 추가되었다 — 설계는
[`feedback/dependency-graph-design.md`](feedback/dependency-graph-design.md).

`related/trust`(생성·검증 주체)가 2026-09-07에 추가되었다 — OKF v0.2의 신뢰 등급.

노트 v3 반영(2026-09-10)으로 추가된 것: `related/state`(Workset·Run·Runbook),
`related/tag`(태그 범주 9종), `related/condition/temporal-ontology.ttl`(precedes·
mutuallyExclusiveWith·withinDeadline), `entity/knowledge-item`의 `RequirementChunk`,
`shapes/residency-shapes.ttl`(plane×level 수준 허용표), trace의 `allocates`·`generates`·
`CandidateLink`·`ConfirmedLink`, `agt:contentHash`.

설계가 요구하나 아직 없는 모듈: `upper`(상위 온톨로지 정렬), `related/policy`,
`profile/`, `defect`·`defect-rules`.

## 확장 규칙

1. **기존 어휘를 먼저 찾는다** (`grep -r "찾는개념" kb/ontology/`). 같은 뜻의 개념을 둘
   만드는 것이 이 체계가 막는 드리프트다 ([`id:chunk-d0160`](../chunks/decision/d-0160-search-before-authoring.md)).
2. 주제가 맞는 **기존 모듈 디렉토리에 새 파일 하나**, 새 주제면 **새 모듈 디렉토리**
   + `BUILD.bazel` + `//kb/ontology:modules` 등록.
3. 한 개념은 정확히 한 파일에서 정의된다 — 다른 파일에서 재정의하면 boundary 게이트가
   거부한다.
4. 모든 `agt:` 용어에 한/영 `rdfs:label`과 `skos:definition`. 정의는 속 + 종차로 쓰고
   ([`id:chunk-d0034`](../chunks/decision/d-0034-genus-differentia-definition.md)), 그래프가
   보여주지 못하는 것만 서술한다 ([`id:chunk-d0161`](../chunks/decision/d-0161-definition-says-why-and-when.md)).
5. **지어낸 용어를 쓰지 않는다.** 확립된 표준어가 있으면 그것을 쓰고, 고유 관계가
   필요하면 표준 관계의 하위 속성으로 매단다 (d-0024 · d-0053). 어디서 가져왔는지는
   [`references.md`](references.md)에 기록한다.
6. 폐기는 삭제가 아니다 — `owl:deprecated` + `agt:replacedBy` (d-0035).
7. **에이전트는 제안만 한다** — 일반화이 온톨로지에 닿을 때는 `bazel run //tools:term_propose`로
   제안을 승인 큐(`kb/ontology/proposals/`)에 올리고, 유저 승인 뒤에만 모듈 파일로 옮긴다
   (노트 2.5절). 큐는 `//kb/ontology:modules` 밖이라 승인 전에는 그래프에 들어가지 않는다.

## 역량 질문 — 온톨로지의 요구사항이자 완료 판정

온톨로지가 답해야 하는 질문 목록이 그 온톨로지의 요구사항이다
([`id:chunk-d0052`](../chunks/decision/d-0052-competency-questions.md)). 질문에 기여하지 않는
개념은 과설계이고, 질문이 질의로 답해지면 그 부분은 완성이다.

목록과 현재 답할 수 있는 것의 실측은 [`competency-questions.md`](competency-questions.md) —
노트 v3의 CQ1~20과 이 저장소 등록분 CQ-01~32의 대응표도 거기에 있다. 답할 수 없는
질문이 어휘 확장의 우선순위다.

## development 층 — 개발 KB의 어휘 (노트 7.2)

| 항목 | 설계 | 이 저장소 |
|---|---|---|
| plane 실체 | `RequirementChunk`(EARS 패턴·이해관계자·관심사) · `DecisionChunk`(결론/근거/대안, `serves`) · `ContractChunk`(시그니처, 사전·사후조건) · `SchemaChunk`(호환 관계) · `ArtifactChunk`(앵커) · `AnnotationChunk` · `MemoryChunk` | 클래스 7 **있음**(`entity/knowledge-item`). `serves ⊑ refines` 있음. EARS 패턴·관심사·호환성·표본 근거 유형 어휘 **없음** |
| 역량 질문 | CQ1 충족 · CQ3 배제 대안 · CQ4 무효 범위 · CQ7 고아 · CQ16 할당 · **CQ19 정제 완주** · **CQ20 후방 추적 귀속** | [competency-questions](competency-questions.md) |

## V&V 층 — V&V KB의 어휘 (노트 8.2, 8.16~8.21, 부록 E.5)

| 항목 | 설계 | 이 저장소 |
|---|---|---|
| `vv/` 모듈 | 일곱 plane의 V&V 실체 — 검증 목표 · 시나리오(자극·요인·배제 자극) · 합격 기준(판정식) · 케이스 · 검증기 · 판정 주석 · 실행 기록 | **없음** — plane 클래스는 코어을 그대로 쓴다 ([p8-vv-plane-instances](../kb/dev/decision/p8-vv-plane-instances/conclusion.md)) |
| 위험 분석 산출 | 현상(ODD 조건 + `defect` 요인) · 인과(`defect-rules`) · 지표 · 시나리오 부류 abstract 라이브러리 · 목표 거동(Runbook) | `Runbook`만 있음(`related/state`). `defect`·`defect-rules` **없음** |
| 시나리오 도메인 모델 | actor(에이전트·유저·서비스) · action — OpenSCENARIO 코어 구조 위 | **없음** (도입 7단계, [pe-scenario-is-openscenario](../kb/dev/decision/pe-scenario-is-openscenario/conclusion.md)) |
| 결함 어휘 | 3갈래 × ODC 유형 × 한정자 × 트리거 × 발견 단계 | **없음** |
| 역량 질문 | CQ5 작업 집합 · CQ6 ODD 안팎 · CQ10 결함 요인 · **CQ11 무엇을 검증하는가** · CQ17 양립 후보 | [competency-questions](competency-questions.md) |

## 참조 프로파일 — 소프트웨어 개발

코어을 개발 작업에 특수화한 결정들이며, 다른 프로파일의 템플릿이다. 이 저장소는 이
프로파일의 부분집합만 쓴다 — 현재 `requirement`·`decision` plane이 채워져 있고, 역할은
노트 10.2절 9역할 중 5개다(design은 developer가 겸함 — 유저 결정 C4).

| 코어 항목 | 개발 프로파일의 결정 |
|---|---|
| `requirement` | EARS 문장. 이해관계자 관심사에서 도출 |
| `decision` | 설계 결정. 결론(concrete)·근거·대안(logical) 세 청크의 복합체 |
| `schema` | 프로토콜 메시지·필드. 스키마 언어 |
| `contract` | 인터페이스 시그니처. 언어 네이티브 선언 |
| `artifact` | **함수.** 42줄 초과 함수는 분할 |
| `annotation` | 코드 주석·리뷰 코멘트. 코드 밖에 저장 |
| 앵커 해석 | 심볼 ID → 파일 내 범위 |
| 판정 도구 | 컴파일러, 타입 체커, 스키마 검사기, 테스트, 린터 |
| 뷰 | tangle(코드 파일), weave(문서) |
| 결함 하위 유형 | ODC 8유형 |
| 조건 셋째 수준 | 언어·런타임, 빌드 체계, 저장소 구조, 의존성 버전 |
| 검증 환경 | 단위 → 계약 → mock 통합 → 실제 인프라 → 스테이징 → 운영 |
