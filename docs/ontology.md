# ontology — 지식의 코어와 분야 프로파일

온톨로지는 이 체계의 **어휘**다. 온톨로지는 정제 계층의 한 단계가 아니라 정제 계층 전체가 쓰는 어휘이고, 그래서
이 어휘 밖에서 쓴 지식은 이 체계에 존재하지 않는다([`p2-ontology-as-vocabulary`](../kb/dev/decision/p2-ontology-as-vocabulary/conclusion.md)).
이 문서는 구조도 v5에 따라 온톨로지를 **코어, development, V&V**의 셋으로 나눠 적는다.

## 코어 — 코어와 프로파일

| 구분 | 담는 것 | 누가 만드나 | 위치 |
|---|---|---|---|
| **코어** | 분야와 무관한 것. 지식 종류(`plane`)와 정제 수준(`level`), 조건, 가정, 역할, 단위 지식(`chunk`)과 복합체, 링크 타입 | 이 저장소 | `kb/ontology/` (`agt:`) |
| **분야 프로파일** | 각 지식 종류의 실체와 판정 도구, 조건 어휘의 셋째 분류 단계, 도메인 결함 하위 유형, 앵커 해석기 | 분야마다 | `profile/development`. 첫 형태(2026-09-18)는 실체 7개와 판정 도구 6개, EARS 패턴 6개다 |

프로파일은 별도 장치가 아니라 **코어를 확장만 하는 온톨로지 모듈**이다. 프로파일은 코어 클래스의 하위 클래스와
shape만 추가하고, 코어를 수정하는 프로파일은 검사에서 실패한다
([`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md)). 한 프로젝트가
프로파일을 여럿 가질 수 있고, 링크는 프로파일의 경계를 넘을 수 있다.

첫 프로파일 `kb/ontology/profile/development/`는 2026-09-18에 생겼다. 이 프로파일은 네 부분으로 이루어진다. 첫째는
`norm`을 뺀 일곱 지식 종류의 실체 하위 클래스이고, 둘째는 판정 도구 개체 6개와 그 `judgedBy` 바인딩(값 제약)이다.
셋째는 EARS 패턴 어휘와 요구의 `pattern` 필드이고, 넷째는 shape(`profile-development-shapes.ttl`)다. `chunk2kg`는
지식 종류를 보고 단위 지식에 실체 클래스를 붙인다. 구축 절차는 [`method.md §1`](method.md#1-프로파일-구축)에 있고,
아직 채우지 않은 확장점인 조건 어휘의 셋째 분류 단계와 결함 하위 유형은 그 절의 표에 있다.

## 코어의 구성

```
kb/ontology/
  project-ontology.ttl          # 최상위. import만 하는 얇은 파일
  entity/                       # 지식 종류(plane)로 분류할 수 있는 개념
    knowledge-item/             #   KnowledgeItem · Chunk · Composite · 지식 종류(plane) · 정제 수준(level) · 속성
  related/                      # 횡단 개념 — 어느 지식 종류에도 속하지 않는다
    condition/  scope/  assumption/  channel/  harness/  trace/  trust/  state/  tag/
    layer/  defect/  defect-rules/
  profile/development/          # 개발 프로파일 — 코어를 확장만 한다
  shapes/                       # SHACL — 원칙을 검사할 수 있는 형태 (지식 종류별 허용 수준 표 포함)
  proposals/                    # 용어 제안 승인 큐 — //kb/ontology:modules 밖 (2.5절)
```

모듈 하나는 디렉토리 하나이고 Bazel 패키지 하나이며, 한 파일은 한 주제를 담는다. 모듈을 나누는 축은 둘이다.
하나는 **지식 종류로 분류되는 개념(`entity/`)과 횡단 개념(`related/`)**의 구분이고, 다른 하나는 **어휘(`-ontology`)와
형식화(`-rules`, `-shapes`)**의 구분이다 ([`p2-ontology-module-structure`](../kb/dev/decision/p2-ontology-module-structure/conclusion.md)).

`related/trace`는 2026-09-04에 추가되었고, 링크 타입과 링크 개체, 판정 근거를 담는다. 링크 타입은 네 족으로
나뉜다. 네 족은 `references`와 `semanticallyDependsOn`, `relatedTo`, 그리고 구성 관계다. 표준 어휘와의 정렬은
`dcterms:references`와 `skos:related`다. 네 족과 표준 정렬의 근거는 결정
[`p10-link-types`](../kb/dev/decision/p10-link-types/conclusion.md)와
[`p10-traceability-information-model`](../kb/dev/decision/p10-traceability-information-model/conclusion.md)에 있다.
LEDGER와 LARGER에 대응시킨 원안은 채널 항목 `dependency-graph-design`이었고, 반영을 마친 그 항목은 git 이력에 있다.

`related/trust`는 2026-09-07에 추가되었다. 이 모듈은 단위 지식을 생성하고 검증한 주체를 담고, 그 내용은 OKF v0.2의
신뢰 등급이다.

2026-09-10에 노트 v3을 반영하면서 다음이 추가되었다.

- `related/state`의 `Workset`, `Run`, `Runbook`
- `related/tag`의 태그 범주 9종
- `related/condition/temporal-ontology.ttl`의 `precedes`, `mutuallyExclusiveWith`, `withinDeadline`
- `entity/knowledge-item`의 `RequirementChunk`
- 지식 종류별 허용 수준 표를 담은 `shapes/residency-shapes.ttl`
- trace의 `allocates`, `generates`, `CandidateLink`, `ConfirmedLink`
- `agt:contentHash`

`related/defect`(결함 요인과 현상, 한정자, 트리거, 영향, 위험 등급)와 `related/defect-rules`(인과와 ODC 차원 규칙)는
2026-09-29에 추가되었다. 설계가 요구하지만 아직 없는 모듈은 `upper`(상위 온톨로지 정렬)와 `related/policy`다.
지금 있는 모듈 목록의 원본은 생성 파일 `kb/ontology/modules.bzl`이다.

## 확장 규칙

1. **기존 어휘를 먼저 찾는다**. 찾는 명령은 `grep -r "찾는개념" kb/ontology/`이다. 같은 뜻의 개념이 둘 생기는 것이
   이 체계가 막는 드리프트다 ([`p4-search-before-authoring`](../kb/dev/decision/p4-search-before-authoring/conclusion.md)).
2. 주제가 맞는 **기존 모듈 디렉토리에 새 파일 하나**를 만든다. 새 주제이면 **새 모듈 디렉토리**를 만들고, 그
   디렉토리에 `BUILD.bazel`을 두며, `//kb/ontology:modules`에 등록한다.
3. 한 개념은 정확히 한 파일에서 정의된다. 다른 파일에서 재정의하면 boundary 게이트가 거부한다.
4. 모든 `agt:` 용어에 한/영 `rdfs:label`과 `skos:definition`을 단다. 정의는 속과 종차로 쓴다
   ([`p0-genus-differentia-definition`](../kb/dev/decision/p0-genus-differentia-definition/conclusion.md)). 서술은
   그래프가 보여주지 못하는 것만 적는다 ([`p0-description-says-what-graph-cannot`](../kb/dev/decision/p0-description-says-what-graph-cannot/conclusion.md)).
5. **지어낸 용어를 쓰지 않는다.** 확립된 표준어가 있으면 그것을 쓰고, 고유 관계가 필요하면 표준 관계의 하위
   속성으로 정의한다(`p0-no-invented-terms`, `p2-standard-relation-vocabulary`). 어디서 가져왔는지는
   [`references.md`](references.md)에 기록한다.
6. 폐기는 삭제하지 않고 `owl:deprecated`와 `agt:replacedBy`를 다는 것으로 한다(`p0-deprecate-not-delete`).
7. **에이전트는 제안만 한다.** 일반화가 온톨로지에 닿을 때는 `bazel run //tools:term_propose`로
   제안을 승인 큐(`kb/ontology/proposals/`)에 올리고, 유저가 승인한 뒤에만 모듈 파일로 옮긴다(노트 2.5절). 큐는
   `//kb/ontology:modules` 밖에 있으므로, 제안은 승인 전에 그래프에 들어가지 않는다.

## 역량 질문 — 온톨로지의 요구사항이자 완료 판정

역량 질문은 온톨로지가 답해야 하는 질문이고, 그 목록이 온톨로지의 요구사항이다
([`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md)). 질문에 기여하지 않는
개념은 과설계다. 반면 질문이 질의로 답해지면 그 부분은 완성된 것이다.

목록과, 지금 답할 수 있는 질문의 측정은 [`competency-questions.md`](competency-questions.md)에 있다. 노트 v3의
CQ1~CQ20과 이 저장소에 등록한 질문(`tools/cq-queries/`의 CQ 질의)의 대응표도 그 문서에 있다. 등록한 질문의 현재
답은 생성 뷰 `bazel build //kg:cq`가 낸다. 어휘를 확장할 때는 답할 수 없는 질문부터 다룬다.

## development — 개발 KB의 어휘 (노트 7.2)

| 항목 | 설계 | 이 저장소 |
|---|---|---|
| 지식 종류의 실체 | `RequirementChunk`(EARS 패턴, 이해관계자, 관심사), `DecisionChunk`(결론과 근거, 대안, `serves`), `ContractChunk`(시그니처, 사전조건과 사후조건), `SchemaChunk`(호환 관계), `ArtifactChunk`(앵커), `AnnotationChunk`, `MemoryChunk` | 실체 클래스와 `serves`가 `refines`의 하위 속성이라는 정의는 있다(`entity/knowledge-item`). EARS 패턴 어휘는 개발 프로파일에 있다(`profile/development/ears-pattern-ontology.ttl`). 관심사와 호환성, 표본 근거 유형의 어휘는 없다 |
| 역량 질문 | CQ1 충족, CQ3 배제 대안, CQ4 무효 범위, CQ7 고아, CQ16 할당, **CQ19 정제 완주**, **CQ20 후방 추적 귀속** | [competency-questions](competency-questions.md) |

## V&V — V&V KB의 어휘 (노트 8.2, 8.16~8.21, 부록 E.5)

| 항목 | 설계 | 이 저장소 |
|---|---|---|
| `vv/` 모듈 | `norm`을 뺀 지식 종류마다의 V&V 실체. 검증 목표와 시나리오(자극, 요인, 배제 자극), 합격 기준(판정 술어), 테스트 케이스, 검증기, 판정 주석, 실행 기록이다 | **없음**. V&V KB는 지식 종류 클래스를 코어 그대로 쓴다 ([p8-vv-plane-instances](../kb/dev/decision/p8-vv-plane-instances/conclusion.md)) |
| 위험 분석 산출 | 현상(ODD 조건과 `defect` 요인), 인과(`defect-rules`), 지표, 시나리오 부류의 abstract 라이브러리, 목표 거동(Runbook) | `Runbook`(`related/state`)과 `defect` 요인(`related/defect`), 인과 규칙(`related/defect-rules`)이 있다 |
| 시나리오 도메인 모델 | actor(에이전트, 유저, 서비스)와 action. OpenSCENARIO 코어 구조 위에 세운다 | **없음** (도입 7단계, [pe-scenario-is-openscenario](../kb/dev/decision/pe-scenario-is-openscenario/conclusion.md)) |
| 결함 어휘 | 세 갈래와 ODC 유형, 한정자, 트리거, 발견 단계의 조합 | **있음**(`related/defect`, 2026-09-29) |
| 역량 질문 | CQ5 작업 집합, CQ6 ODD 안팎, CQ10 결함 요인, **CQ11 무엇을 검증하는가**, CQ17 양립 후보 | [competency-questions](competency-questions.md) |

## 참조 프로파일 — 소프트웨어 개발

참조 프로파일은 코어를 개발 작업에 특수화한 결정들이고, 다른 프로파일을 만들 때 템플릿이 된다. 이 저장소는 이
프로파일의 부분집합만 쓴다. 어느 지식 종류가 채워져 있는지는 생성 뷰 `bazel build //kg:metrics`의 "plane × level"
절이 낸다. 역할은 노트 11.2절의 9역할 가운데 일부이고, 그 목록의 원본은 `kg/catalog-kg.ttl`이다. design은
developer가 겸한다(유저 결정 C4).

| 코어 항목 | 개발 프로파일의 결정 |
|---|---|
| `requirement` | EARS 문장이고, 이해관계자 관심사에서 도출한다 |
| `decision` | 설계 결정이고, 결론(concrete)과 근거, 대안(logical)의 세 단위 지식으로 이루어진 복합체다 |
| `schema` | 프로토콜 메시지와 필드를 스키마 언어로 적는다 |
| `contract` | 인터페이스 시그니처를 언어 네이티브 선언으로 적는다 |
| `artifact` | **함수.** 토큰 상한(결정 `p1-chunk-unit-is-tokens`)을 넘는 함수는 분할한다 |
| `annotation` | 코드 주석과 리뷰 코멘트이고, 코드 밖에 저장한다 |
| 앵커 해석 | 심볼 ID를 파일 안의 범위로 해석한다 |
| 판정 도구 | 컴파일러, 타입 체커, 스키마 검사기, 테스트, 린터 |
| 뷰 | tangle(코드 파일), weave(문서) |
| 결함 하위 유형 | ODC 8유형 |
| 조건 셋째 분류 단계 | 언어와 런타임, 빌드 체계, 저장소 구조, 의존성 버전 |
| 검증 환경 | 단위, 계약, mock 통합, 실제 인프라, 스테이징, 운영의 여섯 단계 |
