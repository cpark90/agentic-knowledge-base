# method.md — 각 단계를 어떻게 하는가 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 102개 · 절 34 · 규약 줄 95 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/method/` 의 절 항목을 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/method/` 의 절 항목과 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 해시값은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

## 목차

- [§0. 순서와 완료 판정](#0-순서와-완료-판정)
- [§1. 프로파일 구축](#1-프로파일-구축)
- [§2. ODD 작성](#2-odd-작성)
- [§3. 단위 지식 저작](#3-단위-지식-저작)
- [§4. 정제 전이](#4-정제-전이)
- [§5. 후보 관리](#5-후보-관리)
- [§6. 연결](#6-연결)
- [§7. 갱신](#7-갱신)
- [§8. 조회](#8-조회)
- [§9. 뷰](#9-뷰)
- [§10. 일반화](#10-일반화)
- [§11. 검증 — V&V KB로](#11-검증--vv-kb로)
- [§12. 영향 분석](#12-영향-분석)
- [§13. 저작 흐름과 완료](#13-저작-흐름과-완료)
- [§14. 위험 분석에서 되먹임까지](#14-위험-분석에서-되먹임까지)
- [입력 파일](#입력-파일)

<!-- 인용 시작: 단위 지식에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

§0가 순서를 적는다면 이 문서는 방법을 적는다. 이 문서는 구조도 v5에 따라 세 부분으로 나뉘어,
§1~§12는 두 KB에 공통인 **코어**이고 §13은 **development**, §14는 **V&V**다. 각 절차는 **입력, 절차,
게이트, 산출**의 순서로 쓰고, 규칙은 [`rules.md`](rules.md)를, 도구는 [`tools.md`](tools.md)를
가리킨다. 절차를 바꾸면 대응 도구도 함께 본다.

## §0. 순서와 완료 판정

운용 순환이라 부르는 전체 순서는 여덟 단계다. 이 문서의 각 절은 그 단계를 수행하는 방법을 적고, [`rules.md`](rules.md)는
결과가 유효한지를 가르는 규칙을 적는다. 원본은 노트 Part VI·XI과 운용 지도다. 반면 이 저장소가 어디까지 왔는가를 재는 도입 8단계는
결정 [`p14-adoption-stages`](../kb/dev/decision/p14-adoption-stages/conclusion.md)에 있고, 운용 순환과는 다른 축이다. 각 단계의 통과 여부는 `bazel build //kg:metrics`가 낸다.

```
프로파일 구축 → ODD 작성 → 정제(저작) → 조회 → 연결 → 갱신 → 뷰 → 일반화
                                                                    │
                     (교훈이 다시 프로파일·ODD·결정으로) ←──────────┘
```

원본: [`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md) · [`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md) · [`p6-refinement-ladder`](../kb/dev/decision/p6-refinement-ladder/conclusion.md) · [`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md) · [`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md) · [`p6-assumption-invalidation`](../kb/dev/decision/p6-assumption-invalidation/conclusion.md) · [`p4-projection-as-query`](../kb/dev/decision/p4-projection-as-query/conclusion.md) · [`p6-ascent-generalization`](../kb/dev/decision/p6-ascent-generalization/conclusion.md).

| # | 단계 | 산출 | 다음 단계의 전제가 되는 이유 | 방법 |
|---|---|---|---|---|
| 1 | **프로파일 구축** | `profile/<분야>` 모듈이다. 각 지식 종류의 실체와 판정 도구, 조건 어휘, 결함 유형을 담는다 | 어휘가 없으면 ODD의 조건을 개념에 대응시킬 수 없다(`p3-odd-first-project-start` 2단계) | [§1](#1-프로파일-구축) |
| 2 | **ODD 작성** | 조건 3분류와 판정 방법, 등급, 명시 제외 | ODD가 비면 적용 범위가 잘리지 않고 가정이 참조할 속성이 없으므로 **체계 전체가 정지한다** | [§2](#2-odd-작성) |
| 3 | **정제(저작)** | 기능(functional)에서 추상, 논리, 구체를 거쳐 실행(executable) 수준까지 정제하는 단위 지식 | 조회와 연결의 대상이 있어야 한다 | §3, §4, §5 |
| 4 | **조회** | 적용 범위와 정제 수준 창으로 거른 작업 집합 | 에이전트가 무엇을 보는지가 정해져야 편집의 읽기 집합이 정의된다 | [§8](#8-조회) |
| 5 | **연결** | 링크 — 편집 부산물로 구축, 복원은 예외 | 링크 없이는 무효화 범위를 계산할 수 없다 | [§6](#6-연결) |
| 6 | **갱신** | 가정을 판정하고 무효화를 전파한 뒤 재검증한다 | 갱신 단절의 해소가 이 체계의 존재 이유다 | [§7](#7-갱신) |
| 7 | **뷰** | tangle과 weave, 문서, 추적 매트릭스는 저장하지 않고 질의로 만든다 | 축적된 지식이 쓰이는 형태 | [§9](#9-뷰) |
| 8 | **일반화** | 관측에서 도메인과 변수를 거쳐 개념까지 일반화하고, 그래서 온톨로지가 자란다 | 다음 프로젝트가 자란 어휘로 시작한다. | [§10](#10-일반화) |

**단계를 건너뛰지 않는다.** 현재 에이전트는 기본 동작으로 기능 수준(functional)에서 곧바로
실행 수준(executable)으로 가고, 그 건너뜀이 정제 계층 단절의 원인이다 (노트 6.1절).

**정제의 산출은 `kb/dev/`의 개발 KB에, 검증 지식은 `kb/vv/`의 V&V KB에 쌓인다.** vnv 역할은 정제와
나란히 검증 목표와 시나리오, 판정 기준을 저작하고 `verifies`로 개발 KB를 가리킨다. 따라서 저작과 판정의
분리가 KB 차원에서도 성립한다 (노트 Part VII).

### 완료 판정

각 단계는 다음 단계로 넘어가기 전에 판정되고, 그 판정은 시간이 아니라 **상태 확인**이다.

원본: [`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md) · [`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md) · [`p3-measurement-method-grades`](../kb/dev/decision/p3-measurement-method-grades/conclusion.md) · [`p6-descent-refinement`](../kb/dev/decision/p6-descent-refinement/conclusion.md) · [`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md) · [`p10-traceability-metrics`](../kb/dev/decision/p10-traceability-metrics/conclusion.md) · [`p6-assumption-invalidation`](../kb/dev/decision/p6-assumption-invalidation/conclusion.md) · [`p4-projection-as-query`](../kb/dev/decision/p4-projection-as-query/conclusion.md) · [`p6-ascent-generalization`](../kb/dev/decision/p6-ascent-generalization/conclusion.md) · [`p11-memory-promotion-rule`](../kb/dev/decision/p11-memory-promotion-rule/conclusion.md).

| 단계 | 완료 판정 |
|---|---|
| 프로파일 구축 | 역량 질문이 전부 질의로 답해지고 `bazel test //kb/ontology:gate_test`가 통과한다 |
| ODD 작성 | 조건마다 객관적 판정 방법과 등급 A~C를 갖추고, 5단계 절차의 마지막인 실제 조건 대조에서 이탈이 0이다 |
| 정제 | 각 전이가 근거와 `refines` 기록을 남겼고 게이트를 통과했다 (`p6-refinement-ladder`) |
| 조회 | 역할별 작업 집합이 컨텍스트 예산 안에 든다(`p1-context-budget-breakdown`) |
| 연결 | 링크 밀도 > 0, 복원 비율이 낮다 |
| 갱신 | 전수조사 없이 무효 범위가 계산된다 |
| 뷰 | 저장된 뷰는 없고 전부 질의 결과다 |
| 일반화 | 온톨로지 확장 건수가 집계되고 승격된 교훈이 규칙이 되었다 (`p11-lesson-promotion`). |

### 도입 순서

단계는 한 번에 모두 도입하지 않는다. **앞 단계만으로 이득이 확인되지 않으면 다음 단계를 진행할 근거가
없기** 때문이다. 이 저장소 자신의 진행 상태와 측정치는 생성 뷰 `bazel build //kg:metrics`가 낸다.

## §1. 프로파일 구축

프로파일은 코어를 특정 작업 종류에 맞게 채운 온톨로지 모듈이다(결정 `p2-skeleton-and-domain-profile`). 프로파일은 코어 클래스의
하위 클래스와 개체, 프로파일 전용 속성, shape만 더하고 코어를 수정하지 않으며, 코어를 재정의하면 boundary 게이트가 거부한다
([`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md)). 아래 절차는 첫 프로파일 `development`를
만들면서 뽑았다(2026-09-18).

1. **확장점을 코어에서 열거한다** ([`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md)). 확장점은 지식 종류 일곱의 실체와 판정 도구, 정제 수준별 assertion 형식, 조건 셋째 분류 단계, 결함 하위 유형, 상한 오버라이드, 앵커 해석기다(`p2-skeleton-and-domain-profile` 표). 이 열거가 곧 완료 판정의 분모다.

1. **확장점마다 답을 결정에서 읽는다** ([`p2-profile-answers-from-decisions`](../kb/dev/decision/p2-profile-answers-from-decisions/conclusion.md)). 결정이 없으면 유저 승인을 받아 먼저 결정을 만든다. 개발 프로파일에서 실체와 판정 도구, EARS 패턴의 원천은 결정 `p7-dev-plane-substance`이고, 앵커 해석기의 원천은 결정 `pe-anchor-is-bazel-label`이다.
1. **모듈 `kb/ontology/profile/<domain>/`에 적는다** ([`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md)). 파일 하나가 확장점 하나이며, 확장점은 실체 하위 클래스, 판정 도구 개체와 그 바인딩, 패턴 어휘다. 모듈은 `project-ontology.ttl`의 `owl:imports`에 넣고 `gen_build`로 모듈 목록을 재생성한다.
1. **바인딩한다** ([`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md)). 생성기 `chunk2kg`가 지식 종류를 실체 클래스로 타이핑하고 프로파일 필드인 요구의 `pattern`을 방출하며 데이터를 채운다(요구 33건의 EARS 패턴). 바인딩 없는 어휘는 고립 개념이다(CQ-28).
1. **역량 질문을 더한다** ([`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md)). 프로파일이 답해야 할 질문을 [`competency-questions.md`](competency-questions.md)에 등재하고 `tools/cq-queries/`에 질의를 만든다. 예로 CQ-36은 각 지식 종류의 단위 지식은 무엇이고 무엇이 판정하는가를 묻는다.
1. **완료를 판정한다** ([`p2-skeleton-and-domain-profile`](../kb/dev/decision/p2-skeleton-and-domain-profile/conclusion.md), [`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md)). 완료 조건은 게이트 통과(boundary·shape)와 새 역량 질문의 답 행 1개 이상, 코어 수정 0이다. 채우지 않은 확장점은 아래 표에 "미채움"으로 남긴다.

원본: [`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md) · [`pe-notation-and-cel`](../kb/dev/decision/pe-notation-and-cel/conclusion.md) · [`p0-condition-taxonomy-extensible`](../kb/dev/decision/p0-condition-taxonomy-extensible/conclusion.md) · [`p8-odc-defect-subtypes`](../kb/dev/decision/p8-odc-defect-subtypes/conclusion.md) · [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md) · [`pe-anchor-is-bazel-label`](../kb/dev/decision/pe-anchor-is-bazel-label/conclusion.md).

| 확장점 | 개발 프로파일 | 상태 |
|---|---|---|
| 지식 종류 실체·판정 도구 | 실체 하위 클래스 7개와 판정 도구 개체 6개, `judgedBy` | 채움(2026-09-18) |
| 정제 수준별 단언(assertion) 형식 | 요구에는 EARS 패턴 어휘, 결정에는 결론, 근거, 대안의 표지 | 일부만 정했고 `contract`와 `schema`, `artifact`는 항목이 생길 때 정한다 |
| 조건 셋째 분류 단계 | ODD 속성 7이 둘째 분류 단계에 직접 | 미채움(ODD 재배선과 함께 채운다) |
| 결함 하위 유형 | 코어 `defect` 모듈의 하위 유형 14를 그대로 쓴다 | 채움(2026-09-29, `kb/ontology/related/defect/`, 현상 22·피해 6) |
| 상한 오버라이드 | 저작 산문 1,092 토큰 · `artifact`와 `memory`의 인용 2,856 | 채움(단위는 토큰이고 값은 `BODY_TOKEN_LIMITS`에 있다, 2026-10-01) |
| 앵커 해석기 | 결정 `pe-anchor-is-bazel-label`이 정한 Bazel 라벨 | 채움 |

## §2. ODD 작성

온톨로지는 프로젝트 사이에 공유되어 이미 있으므로, ODD가 새 프로젝트의 첫 산출물이다.
**5단계를 통과하기 전에는 적용 범위를 파생하지 않는다** ([`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)).

1. 프로젝트가 의존하는 조건을 **정적 요소와 환경 조건, 동적 요소**의 세 갈래로 열거한다 ([`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)).
1. 각 속성의 범주를 `related/condition`에서 생성된 택소노미 `taxonomy.yml`에 대응시키고, 대응할 범주가 없으면 온톨로지를 먼저 확장한다 ([`pe-odd-is-openodd`](../kb/dev/decision/pe-odd-is-openodd/conclusion.md), [`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)). ODD 문서는 OpenODD 형식이다.
1. **값 또는 범위**와 **객관적 판정 방법**을 지정하고, 판정 방법은 "정상이다"가 아니라 "명령 X가 Y를 반환한다"여야 한다 ([`p3-measurement-method-grades`](../kb/dev/decision/p3-measurement-method-grades/conclusion.md), [`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)). 등급 A~D를 매기고 **D는 ODD에 넣지 않는다**. D를 넣으면 영원히 `unverified`인 속성이 생겨 모니터링 결과가 늘 불완전해진다.
1. **[지킴]** 검토했으나 밖에 두는 것은 **명시 제외**로 기록한다 ([`p3-condition-entity-from-odd-document`](../kb/dev/decision/p3-condition-entity-from-odd-document/conclusion.md), [`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)). ODD 문서의 `EXCLUSIONS_REVIEWED`에는 `concept`와 YYYY-MM 꼴의 `reviewed`, `reason`을 적고, 그래프의 `agt:excludes` 서식은 `"<대상> — reviewed YYYY-MM, 이유: <근거>"`다.
1. 현재 **실제 조건이 ODD 안에 있는지 대조**한다 ([`p3-odd-first-project-start`](../kb/dev/decision/p3-odd-first-project-start/conclusion.md)). 명령은 `bazel run //tools:odd_check`다(`CHECKS.cmd`, 3.5절). 첫 모니터링에서 이탈이 나오면 틀린 쪽은 현실이 아니라 ODD다.

ODD 작성의 게이트는 `bazel test //kb/odd:gate_test`다. 산출은 OpenODD 형식의 `kb/odd/*-odd.yml`이고, 그 YAML에서
`*-odd.ttl`이 생성되며 그 TTL 위에서 적용 범위가 파생된다(부록 E.4). 속성 범주는 `related/condition`에서
생성된 택소노미 안에 있어야 한다.

## §3. 단위 지식 저작

단위 지식 저작은 가장 흔한 작업이다.

1. **지식 종류와 정제 수준을 정한다** ([`p5-plane-by-verification`](../kb/dev/decision/p5-plane-by-verification/conclusion.md)). 지식 종류의 할당 기준은 **판정 방식**이고, 저장 위치나 파일 형식이 아니다 ([rules §3](rules.md#3-plane--판정-방식으로-나뉜-종류)).
1. 해당 위치에 **파일 하나**를 만든다 ([`p4-one-file-one-topic`](../kb/dev/decision/p4-one-file-one-topic/conclusion.md), [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md)). 파일은 frontmatter(head)와 본문으로 이루어지고, 저작 산문의 토큰 상한 1,092는 frontmatter를 뺀 본문에 건다 ([rules §1](rules.md#1-chunk--자립적-최소-지식-단위)).
1. **[지킴]** **전제가 있으면 가정을 만들고 `assumes`로 가리킨다** ([`p0-premise-as-assumption`](../kb/dev/decision/p0-premise-as-assumption/conclusion.md)). 가정은 ODD 조건 위의 명제다. 고유 전제를 아직 적지 않은 단위 지식은 기본 가정 `id:asm-chunk-conventions`를 `assumes`하고, 실제 전제가 드러나면 고유 가정을 앞에 더한다. 따라서 기본 가정만 가진 항목은 전제를 아직 적지 않은 항목이며, 리뷰가 그런 항목을 잡는다.
1. **통합이 필요하면** 복합체에 잇고, 그렇지 않으면 개별로 둔다 ([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)). 통합이 필요한 때는 함께 읽혀야 이해되거나 순서가 뜻을 가질 때뿐이다 ([rules §2](rules.md#2-복합체--통합이-필요한-것만)).
1. **지식 파일을 고치면 `bazel test //...` 를 돌린다** ([`p6-self-check-before-completion`](../kb/dev/decision/p6-self-check-before-completion/conclusion.md)). 실패하면 shape와 게이트 코드를 약화하지 않고 고친 파일을 수정한다.

**분할 신호**는 라벨을 하나로 쓸 수 없는 것, 그리고 본문 일부만 재사용이나 가정, `suspect`의 대상이
되는 것이다. **병합 신호**는 두 단위 지식이 항상 함께 읽히는 것, 한쪽이 다른 쪽 없이 이해되지 않는 것,
합쳐도 상한 이하인 것이다. 분할에서는 라벨을 잇는 조각 하나가 원 uuid를 승계하고, 나머지 조각은 새 uuid에
`specializationOf: <원 IRI>`를 적는다. 병합에서는 한 uuid를 승계하고 나머지를 폐기 상태(deprecated)로 두어
`supersedes`로 가리킨다. 링크 IRI는 뿌리 uuid로 계산되므로 조각을 가리키는 링크가 원본의 증거와 이력을 잇는다.
출처는 `prov:wasDerivedFrom`으로 적는다([`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)).

## §4. 정제 전이

정제 수준은 `functional → abstract → logical → concrete → executable` 순이다. 각 정제는 **근거와
`refines` 링크를 남기고** 전이 게이트를 통과해야 한다. 전이 게이트는 어휘 검사를 통과하는지, 후보가 비어
있지 않은지, 배제 근거가 있는지, 판정 도구를 통과하는지를 본다. 게이트 없이 만든 하위 단위 지식은 고아율에
잡힌다 ([`p6-refinement-ladder`](../kb/dev/decision/p6-refinement-ladder/conclusion.md)).

기존 단위 지식의 수준은 바꾸지 않는다. 전이는 기존 단위 지식의 수준을 갱신하는 것이 아니라 **새 단위 지식을
만들고 `refines`로 잇는 것**이다 (`p4-plane-subclass-level-property`). 단계를 건너뛰면 의도와 결과만 남고 그 사이가 빈다.

## §5. 후보 관리

미확정은 언제나 **"두 항목이 연결되는가"의 미확정**이다. 따라서 값이 미확정인 것처럼 보이는 경우도
링크로 환원한다 ([`p9-uncertainty-as-link-uncertainty`](../kb/dev/decision/p9-uncertainty-as-link-uncertainty/conclusion.md)).

- `-space` 파일에는 **변수**와 **후보**, **제약**을 쓴다 ([`p9-design-space-file`](../kb/dev/decision/p9-design-space-file/conclusion.md)). 변수는 링크가 필요한 항목이고, 후보는 도착점 집합이며, 제약은 양립 조건이다. 추상 수준에서는 변수까지, 논리 수준에서는 후보와 제약까지 채운 상태다.
- **실물 형식**은 2026-09-22의 첫 형태를 따른다 ([`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md)). 파일은 `space/<슬러그>-space.md`이고 **변수 하나가 파일 하나**다. frontmatter는 `type: agt:Space`·`level: logical`이며 지식 종류 이름을 쓰지 않는다. 본문은 산문 한두 줄과 `yaml` 펜스 하나이고, 펜스는 `variable`과 `status`, `candidates`, `constraints`, `preferences`를 담는다. `variable`은 `from`과 `kind`를, `status`는 `open` 또는 `resolved`를, `candidates`는 `to`, `state`, `when`, `evidence`, `eliminated_by`를 갖는다. 후보를 아직 열거하지 않은 공간은 `candidates`를 쓰지 않는다.
- **후보는 `deps`가 되지 않는다** ([`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md), [`pe-bazel-rules`](../kb/dev/decision/pe-bazel-rules/conclusion.md)). `space/`에는 `kb_chunk` 타깃이 없고, 나가는 것은 A-Box 그래프 `//space:design_space`와 체크박스 뷰 `//space:choices` 둘이다. 게이트 `space`가 근거 없는 배제와 확정 후보 수를 판정하며, 이 게이트가 `r-011`의 실물이고, `r-011`은 "근거 없는 할당은 자료구조 수준에서 불가능하여야 한다"이다.
- 확정의 표현에서 가능성은 **가능 / 불가능의 집합**이다 ([`p9-feasible-set-for-settlement`](../kb/dev/decision/p9-feasible-set-for-settlement/conclusion.md), [`p9-preference-partial-order`](../kb/dev/decision/p9-preference-partial-order/conclusion.md)). 선호는 후보를 기각하지 않고 순서만 정한다. 믿음 정도는 가능 집합 곁에 병기하고 판정에 들지 않는다 (`p9-possibility-as-feasible-set`, `p9-preference-partial-order`, Q90-a).
- **제약 전파는 게이트와 재검증 시점에서만** 실행하고 편집마다 돌리지 않는다 ([`p9-constraint-propagation-timing`](../kb/dev/decision/p9-constraint-propagation-timing/conclusion.md)).
- **후보가 없으면 자동으로 풀지 않고 유저에게 넘긴다** ([`p9-contradiction-handling`](../kb/dev/decision/p9-contradiction-handling/conclusion.md)). 후보가 없는 상태가 모순이다.

후보가 여럿인 상태가 정상이고 확정은 제약 전파가 나머지를 기각했을 때만 일어나므로, 과도한 추측이
자료구조 수준에서 막힌다.

## §6. 연결

**링크는 산출물이 만들어지는 순간 편집 연산의 부산물로 만든다.** 이 방식을 구축이라 한다. 반면 이미
존재하는 산출물에서 관계를 되짚는 복원은 체계 도입 전의 산출물과 외부 유입물, 구축 누락의 감사에만
쓴다 ([`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)).

- 탐색의 **읽기 집합**을 편집 컨텍스트에 후보 목록으로 넘기고, 편집 후 **쓰기 집합**과 대조해 확정한다 ([`p10-context-handoff-yields-links`](../kb/dev/decision/p10-context-handoff-yields-links/conclusion.md)). 다만 하네스의 도구가 읽기와 쓰기를 기록하지 않으면 이 절차가 성립하지 않는다. 첫 형태는 `bazel build //kg:workset --//kb:anchor=…`로 펼친 단위 지식을 `bazel run //tools:handoff`가 새 단위 지식의 `sources`에 옮기는 것이다.
- 판정 근거는 검사 가능성이 높은 것부터 쓰고, 그 순서는 구축 기록, 동시 편집 이력, 테스트 공동 커버, 임베딩 유사도, 같은 세션에서 읽음이다 ([`p10-link-judgement-evidence`](../kb/dev/decision/p10-link-judgement-evidence/conclusion.md)). 다만 임베딩 유사도는 후보 추림에만 쓴다.
- **[지킴]** **동시 편집 증거는 바뀐 파일이 20개 이하인 커밋에서만 뽑는다** ([`p10-co-edit-evidence-from-small-commits`](../kb/dev/decision/p10-co-edit-evidence-from-small-commits/conclusion.md)). 쌍은 `bazel run` 모드가 git에서 뽑아 `memory` 지식 종류의 관측으로 고정하고, 링크 후보 뷰와 증거 기록은 그 관측만 읽는다.
- **임베딩 유사도를 확정 근거로 쓰지 않는다** ([`p10-embedding-similarity-narrows-only`](../kb/dev/decision/p10-embedding-similarity-narrows-only/conclusion.md), [`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)).
- 본문에서 추출한 `cites`와 `usesConcept` 참조는 후보 링크 개체인 `candidate`이고 그 증거 종류는 구축 기록이다 ([`p10-extracted-references-are-candidates`](../kb/dev/decision/p10-extracted-references-are-candidates/conclusion.md)). 반면 확정은 링크 키에 적는 행위다.
- 복원 후보는 `bazel build //kg:link_candidates`가 낸다 ([`p10-restored-link-marking`](../kb/dev/decision/p10-restored-link-marking/conclusion.md), [`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md)). 이 명령은 본문 식별자와 테스트 공동 커버, 개념 공유로 후보를 뽑고 TIM 제약을 검사하며 앵커당 k ≤ 7개까지 낸다. 사람이 채택하면 링크 키에 적고 같은 단위 지식의 `restored` 목록에 대상을 한 번 더 적는다. 그 링크의 증거는 `proposal`이고, 복원 비율은 `metrics`와 `audit`가 센다.

조건 키 `when`과 증거 기록, 상태 전이 규칙은 결정
[`p9-conditional-links`](../kb/dev/decision/p9-conditional-links/conclusion.md)와 [`p9-evidence-ledger-with-belief`](../kb/dev/decision/p9-evidence-ledger-with-belief/conclusion.md)에
있고, 조회 알고리즘은 §8에 있다. 복원 경로는 결정
[`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)과 [`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md)에
있다.

## §7. 갱신

1. **가정을 판정한다** ([`p6-assumption-verification-methods`](../kb/dev/decision/p6-assumption-verification-methods/conclusion.md)). 판정 유형과 판정 술어가 가정과 함께 저장되어 있어야 한다. 판정 유형은 그래프 질의와 파일 검사, 실행 검사, 외부 조회, 사람 확인이다. 첫 형태는 `bazel run //tools:assume_check`이고, 이 도구에서 판정 술어는 가정이 참조하는 ODD 조건 판정의 연언이며 `--break`는 인위 파괴 실험을, `--record`는 `memory` 지식 종류인 관측의 기록을 맡는다 (2026-09-14).
1. 깨진 가정에 의존하는 항목을 `invalidated`로, 그 항목을 가리키는 링크의 반대편을 `suspect`로 표시한다 ([`p6-assumption-invalidation`](../kb/dev/decision/p6-assumption-invalidation/conclusion.md), [`p6-invalidation-propagation`](../kb/dev/decision/p6-invalidation-propagation/conclusion.md)). 전파는 지식 종류 사이의 단방향 규칙을 따르므로 유계다 (`p6-invalidation-propagation`).
1. **재검증은 즉시 하지 않고 커밋이나 세션 종료 같은 경계에서 일괄로** 한다 ([`p10-link-decay-states`](../kb/dev/decision/p10-link-decay-states/conclusion.md)). 알려진 변경 패턴은 규칙으로 자동 갱신하고, 규칙에 없는 변경만 판정으로 보낸다.

**링크 상태는 저장값이 아니라 평가 결과다**(유저 승인 2026-09-23, 링크 견고성 D). 링크의 `when`은 `in(<조건>)`과
`!`, `&&`, `||`를 쓰는 3값 논리의 ODD 조건 참조로 평가되고, 그 값이 거짓이면 확정 링크는 `suspect`로, 후보는 `invalid`로
유도된다. 유도된 상태는 그래프에 쓰지 않고 `bazel run //tools:assume_check`의 보고와 `//kg:metrics`에서만 물질화된다.
전파는 `tools/kb_lib.py`의 `SUSPECT_TRIGGERS`에 선언된 링크 종류만 도는데, 지금은 `supersedes` 하나이고 선언에 없는
종류는 돌지 않는다. 추적 매트릭스가 `suspect`로 포화되는지는 `metrics`의 포화율 한 줄이 관측한다(경고선 20%).
**본문 해시가 바뀌면 링크를 재검증하는** 경로는 `bazel run //tools:revalidate -- --base <rev>`가 닫았다. 이 도구는
바뀐 단위 지식을 양 끝으로 갖는 `agt:Link` 개체를 그래프의 같은 IRI로 낸다.

무효화는 삭제가 아니다. 무효화 이력은 일반화의 입력이고, 어떤 가정이 자주 깨지는가는 그 자체로 일반화
대상이다.

## §8. 조회

**읽기 응답의 기본은 라벨 목록이지 본문이 아니다** (`p4-label-is-the-interface`). 조회는 적용 범위를 정하고, 라벨 목록을
받고, 필요한 것만 펼쳐 작업 집합을 만드는 순서로 간다. 도구는 `bazel build //kg:workset_<role>`이다. 정제 수준의
창과 앵커는 `defs/kb.bzl`의 규칙 `kb_workset_view`의 인자로, 예산은 빌드 설정 `--//kb:budget`으로 준다.

- **작업 집합**(Workset)은 적용 범위와 정제 수준 창, **앵커 이웃**으로 걸러져 에이전트에게 실제로 보이는 지식 집합이며, 컨텍스트 통제의 단위다(노트 0.5절) ([`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)). v1의 scene·situation 어휘는 폐기되었다. 앵커 없는 요청에는 접힌 라벨 목록만 준다.
- dispatch 대상에게는 전체 컨텍스트가 아니라 **적용 범위로 거른 작업 집합만** 넘긴다 ([`p11-execution-mode-and-workset`](../kb/dev/decision/p11-execution-mode-and-workset/conclusion.md)).
- **툴 표면이 할당을 따라야 한다** ([`p5-plane-assignment-tool-surface`](../kb/dev/decision/p5-plane-assignment-tool-surface/conclusion.md)). 저장소만 나누고 읽기 도구가 전체를 반환하면 컨텍스트 분리는 이름뿐이다.
- 컨텍스트 예산은 항목별로 분해해 통제하고 지식 본문은 잔여로 둔다 ([`p1-context-budget-items`](../kb/dev/decision/p1-context-budget-items/conclusion.md)).

작업 집합의 조립 알고리즘은 결정
[`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)가 정하고,
첫 형태는 `workset`이며 [`tools.md`](tools.md)에 있다. 알고리즘은 앵커를 고르고, 이웃으로 확장하고,
우선순위를 매긴 뒤 예산 안에 패킹한다. 예산 상한식은 `Δ = m·k·1,092`이고, 앵커 수 m과 이웃 수 k, 단위 지식의
토큰 상한을 곱한 값이다. 예산은 42와 129의 곱인 5,418 토큰이다.

## §9. 뷰

**모든 뷰는 질의의 결과이며 저장하지 않는다.** 저장된 뷰는 원본과 어긋나는 순간부터
거짓이 된다 ([`p4-projection-as-query`](../kb/dev/decision/p4-projection-as-query/conclusion.md)).

원본: [`p4-projection-as-query`](../kb/dev/decision/p4-projection-as-query/conclusion.md) · [`p10-traceability-matrix`](../kb/dev/decision/p10-traceability-matrix/conclusion.md) · [`p12-documents-are-generated`](../kb/dev/decision/p12-documents-are-generated/conclusion.md) · [`p12-audit-and-onboarding-self-sufficiency`](../kb/dev/decision/p12-audit-and-onboarding-self-sufficiency/conclusion.md) · [`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md) · [`pe-generated-outputs-stay-in-bazel-out`](../kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md) · [`p12-evaluation-metrics`](../kb/dev/decision/p12-evaluation-metrics/conclusion.md) · [`p4-chunk-quality-metrics`](../kb/dev/decision/p4-chunk-quality-metrics/conclusion.md) · [`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md) · [`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md) · [`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md).

| 뷰 | 질의 |
|---|---|
| tangle, 곧 코드 파일 | 복합체의 `artifact` 부분을 `co:index` 순으로 이어 붙인다 |
| weave, 곧 문서 | 산출물과 그 항목을 `targets`로 가리키는 주석을 함께 뽑는다 |
| 라벨 목록 | 적용 범위 안 단위 지식의 `rdfs:label`만 뽑는다 |
| 작업 집합 | 적용 범위의 지식 종류와 ODD 조건으로 거른 지식이다 |
| 추적 매트릭스 | 지식 종류와 지식 종류를 맞댄 격자이며 **빈 칸이 곧 누락이다** |
| 결정 기록 문서(ADR) | 결정 기록 하나와 그 결정이 `refines`로 가리키는 요구, `supersedes` 연쇄를 모은다. 생성 명령은 `bazel build //kb/dev:adr`다(2026-09-19). |
| 요구 색인 | 요구 라벨과 EARS 패턴, 정제 결정 수, 도달 정제 수준을 싣는다. 생성 대상은 `//kb/dev:requirements`이고 `INTENT.md`의 손 목록을 대체한다 |
| 변경 이력 | `supersedes`·`prov:wasRevisionOf` 연쇄를 싣는다. 생성 대상은 `//kb/dev:changelog`다 |
| 감사 보고서 | `bazel build //kg:audit`가 검증 현황과 최근 실행, 가정, 추적 매트릭스, 검증 표시, 링크 근거를 그래프 union과 관측 본문만으로 낸다 (2026-09-19) |
| 복원 후보 | 본문 식별자와 테스트 공동 커버, 개념 공유에서 링크 후보를 뽑고 TIM 제약과 앵커당 k ≤ 7 상한을 두며, `//kg:link_candidates`가 낸다 (2026-09-19). 상한 안의 후보는 근거 순위, 공유 개념 수, 대상 IRI 순서로 정하고 라벨로 정하지 않는다 (2026-10-26, Q169-a) |
| skill | 도구 docstring과 `kb_lib.SKILLS`에서 `.claude/skills/*/SKILL.md`를 생성해 트리에 두고 드리프트 검사로 확인한다 |
| 코어 지표 | 지식 종류와 정제 수준의 교차 분포와 고아율, 세 축 대리, 링크 밀도, 크기 분포를 `bazel build //kg:metrics`로 낸다. 문서는 수치를 적지 않고 이 생성물을 인용한다(`p4-projection-as-query`) |
| 역량 질문 | CQ 질의 28개의 답을 라벨 목록으로 낸다(`//kg:cq`). 개별 질의는 `bazel run //tools:query -- <CQ>`로 낸다 |
| 정합성 보고 | `//kb:consistency`가 정확·근사 중복과 묶인 쌍의 응집 저하, 라벨 중복·형식, 용어 옛 표기를 보고한다. 판정은 사람이 한다 |
| 커뮤니티 탐지 | `//kg:communities`가 결정론적 Louvain으로 복합체 후보와 `relatedTo` 후보를 낸다. 채택·기각은 사람이 한다 |

뷰의 **형태**는 생성 전에 고정된다. 머리 블록과 본문 서식, 수치 표기의 규약은
[`STYLEGUIDE.md` §9](../STYLEGUIDE.md#9-생성-문서-bazel-binmd--생성-트리-파일)에 있고 게이트
`gendoc`이 그 규약을 강제한다. 근거 결정은
[`p12-generated-document-header`](../kb/dev/decision/p12-generated-document-header/conclusion.md)와
[`p12-generated-document-form`](../kb/dev/decision/p12-generated-document-form/conclusion.md),
[`p12-generated-documents-are-gated`](../kb/dev/decision/p12-generated-documents-are-gated/conclusion.md)다.

## §10. 일반화

정제만 있는 체계에서는 지식이 축적되지 않으므로, 일반화는 관측에서 어휘로 올라간다 (`p6-ascent-generalization`).

원본: [`p6-ascent-generalization`](../kb/dev/decision/p6-ascent-generalization/conclusion.md).

| 전이 | 산출 |
|---|---|
| 실행 수준에서 구체 수준으로 | 실행 기록 |
| 구체 수준에서 논리 수준으로 | 반복 패턴에서 도메인을 추출해 `-space` 도메인을 갱신한다 |
| 논리 수준에서 추상 수준으로 | 도메인을 관통하는 변수를 식별한다 |
| 추상 수준에서 기능 수준으로 | 변수를 설명하는 개념을 식별해 **온톨로지를 갱신한다** |

마지막 전이가 특별한 까닭은 어휘가 자라면 다음 프로젝트가 자란 어휘로 시작하기 때문이다. **일반화는
자동화하지 않는다.** 대신 후보를 제시해 확인을 받고, 온톨로지 갱신은 품질 검사를 통과해야
한다. **트리거는 초기에 사람 지정만 쓰고**, 반복 임계값 트리거는 관측 모수가 쌓인 뒤에 쓴다
(`p6-ascent-generalization`, `p6-ascent-candidate-approval`). 일반화의 최소 단위는 교훈 승격이다 (`p11-lesson-promotion`, `p11-memory-promotion-rule`).

## §11. 검증 — V&V KB로

v1의 "검증은 응용"은 v3부터 대체되었다(`p8-two-knowledge-bases`). 검증·확인은 **두 번째 지식 베이스**이고, 절차는
§14 V&V에 있다 ([`p12-dev-vv-kb-exchange`](../kb/dev/decision/p12-dev-vv-kb-exchange/conclusion.md)).
코어가 제공하는 단위는 시험 대상과 경계를 정하는 ODD, 결과를 축적하는 실행 기록, 실패를 분류하는 defect다.

2026-09-19의 첫 형태에서 사슬은 세 고리로 이루어진다. 검증 목표(`kb/vv/goal/`, requirement·functional)는 개발 요구에서
`derivesFrom`으로 파생된다. 합격 기준(`kb/vv/criteria/`, contract·logical)은 `refines`로 검증 목표를 가리키고, 그 판정
술어가 게이트다. 테스트 케이스(`kb/vv/case/`, schema·concrete)는 자극과 기대, 실행 명령을 담아 `refines`로 합격 기준을
가리키고, `verifies`로 개발 결정의 결론(concrete)을 가리킨다. 테스트 케이스가 `schema` 지식 종류인 이유는 `refines`가
contract와 schema가 decision 뒤에 오는 지식 종류의 순서를 거스르지 못하기 때문이다. 검증기(`kb/vv/verifier/`, artifact·executable)와
판정 주석(`kb/vv/verdict/`, annotation)도 2026-09-22에 실물을 얻었다. 실행기 `vv_run`이 테스트 케이스의 실행 명령 가운데
읽기 전용 검증기를 돌려 실행 기록(`kb/vv/run/`, memory·concrete, append-only, `process:vv_run`)을 남기고, 감사 보고서
`//kg:audit`가 그래프와 그 기록만으로 검증 현황을 낸다. 이로써 V&V 순환이 처음으로 닫혔다.

**테스트 케이스는 자극과 기대를 기계가 읽는 형식으로 적는다**([`p8-machine-readable-case`](../kb/dev/decision/p8-machine-readable-case/conclusion.md),
2026-09-23). 산문 옆의 `yaml` 펜스가 `files`와 `expect`를 담는다.
`files`는 이름에서 내용으로의 대응이고, `expect`는 명령마다 `exit`와 `contains`를 적는다.
검증기는 자극을 임시 디렉토리에 써서 `{{이름}}`을 실제 경로로 바꾼 뒤 실행하고 지운다. 판정은 종료 코드와 문구가 둘 다
맞아야 통과다. 종료 코드만 보면 기대한 사유로 실패했는지 모르고, 다른 이유로 실패한 검증기는 **틀린 것을 검증하기**
때문이다. 건너뛴 명령이 있는 테스트 케이스는 `pass`가 아니라 `skip`이다. 게이트의 값은 무엇을 통과시키는가가 아니라
무엇을 거부하는가에 있다.

**음성 자극은 검사하려는 규칙 하나만 어긴다**([`p8-minimal-negative-stimulus`](../kb/dev/decision/p8-minimal-negative-stimulus/conclusion.md)).
둘 이상을 어기면 종료 코드가 어느 규칙을 가리키는지 말하지 못하고 `contains` 문구만이 분기를 고정한다. 게이트 메시지는
수정 방향을 알려 주므로 개선되면서 바뀌는데, 그때 종료 코드가 받쳐 주지 않으면 고치는 사람은 새 문구를 무엇에 맞출지
모른다. 그래서 `**표본 근거**`에 그 자극이 어기는 규칙을 적고, 자극이 최소가 되지 않으면 테스트 케이스를 나눈다.
최소성은 자극을 하나씩 빼 보는 실험으로만 확인되므로 게이트가 아니라 표본 근거의 주장이다.

**검증기는 실행기의 파이썬·runfiles 문맥을 물려받지 않는다**([`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)).
실행기를 부르는 방식이 테스트 케이스의 판정을 바꾸면 재현이 아니기 때문이다. 게이트 `vv-run-env`인 `//tools:vv_run_env_test`가
그 격리를 `bazel test //...` 안에서 상시 판정한다. 이 게이트는 판정 대상을 실행기 전체가 아니라 격리의 동작으로 좁혀
중첩 bazel을 피했다.

판정자는 게이트 밖 도구이고 **세션 판정자**, 곧 외부 서비스가 아니라 새 세션을 여는 에이전트다(유저 답 2026-09-30, 결정
[`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md)). `bazel run //tools:judge -- --question <질문 id>
--responses <json> [--responses <json> …] [--decoys <json>] <청크 파일…>`은 프로파일에 등록된 판정 질문을 단위 지식에 물어 값과
확신도를 받는다. 응답은 세션 판정자가 낸 `{judge, responses: [{question, fingerprint, value, confidence}]}`를 `--responses`로
입력하고, 이 도구는 판정 로그와 결과 주석을 남긴다. 판정 로그는 `memory` 지식 종류로 `kb/vv/run/judge-<시각>.md`에
추가 전용(append-only)으로 쌓이고, 결과 주석은 `kb/vv/verdict/`에 놓인다. 게이트는 판정을 부르지 않고, 로그의 형식과 필수
필드, `일치` 열만 본다. 필수 필드는 질문 id, 값, 확신도, **판정자 식별자**, 입력 해시값, 시각이고, `일치` 열의 값은 일치,
불일치, 해당 없음이다. 질문의 형은 noul, choice, score 셋이고 선택 집합은 255 이하다.

**확신도는 자기 보고이므로 단독 응답은 자동 적용되지 않는다.** 대신 `--responses`를 둘 이상 주면 도구가 같은 질문과 입력
해시값에 대한 값의 일치 여부를 계산해 로그에 낸다. 임계는 확신도 구간이 아니라 **일치율**이고, 일치율은 판정자 둘의 일치와
`label_sample.py --decoys`의 미끼 검출로 잰다. 자동 적용은 정확도와 판별력을 잰 뒤에만 열므로, 지금은 전부 사람 확인 큐다.

판정이 필요한 질문 여섯 가운데 요약과 채움, 중복, 자리의 넷은 기계로 환원되었다. `핵심:` 항목의 지지 참조인 요약과 채움은
게이트 `summary-support`, `addition`, `empty-value`가 맡고, 중복과 자리는 `consistency.py`의 ⑩과 ⑪이 후보까지 낸다. 남는 둘인
근거와 라벨 대표성만 세션 판정자가 맡는다. 세션 판정자를 여는 쪽은 실험자(vnv)이고, 그래서 열쇠 `key.json`을 쥔 쪽이
판정자와 분리된다.

**정지 규칙** — 연속한 두 라운드에서 신규 결함 수가 줄지 않으면 다음 라운드를 열지 않고 채널로 되돌린다. 이 규칙의 목표
`verification-round-stop-rule`은 안정 상태다(유저 승인 2026-10-01). 라운드의 정의는 처음에 판정 주석의 `prov:generatedAtTime` 날짜였으나,
종료 사유를 단 명시 기록으로 바뀌었다(유저 답 Q39-c, 2026-10-04). 날짜 정의 아래의 첫 적용은 2026-10-01 orchestrator 세션이고, 그 세션에서는
신규 결함 수 2, 4, 2, 2, 2에서 규칙이 두 번 성립해 라운드를 열지 않았다.

- **[지킴]** 라운드는 `vv_run --round stop-rule|budget|complete`가 남기는 기록 `kb/vv/run/round-<UTC>.md`이고, 이 기록은 번호와 구간 안 신규 결함 수, 종료 사유를 담는다 ([`p8-verification-round-stop-rule`](../kb/dev/decision/p8-verification-round-stop-rule/conclusion.md)). 종료 사유는 `agt:RoundEndReason`의 개체 셋 중 하나다. 신규 결함 수 new(n)은 직전 기록 시각 뒤부터 기록 n 시각까지 저작된 살아 있는 판정 주석의 수이고, 다만 `process:judge` 주석은 세지 않는다. new(n) ≥ new(n−1)이면 다음 라운드를 열지 않고 채널로 되돌린다. 이 조건에서 기록 n 다음의 기록이 정지 규칙이 아닌 사유로 닫히면 `//kg:gate_test`의 verify 질의 `round-stop-rule-violated`가 위반으로 낸다. `//kg:audit`는 기록으로 구간을 자르고 기록이 없으면 날짜로 자른다(유저 답 Q39-c, 2026-10-04).

## §12. 영향 분석

`revalidate`의 `호출부` 열은 본문 해시가 바뀐 정의를 `agt:usesDefinition`인 `uses`로 가리키는 출발점의 수이고,
**코드 호출부 파손의 상한**이다(2026-09-30). 상한의 범위는 같은 모듈과 치역 경계인 `defs/kb.bzl`의 `USES_TARGETS` 안의
모듈이다. 경계 밖 모듈과 간접 호출, 상수 참조는 세지 않으므로 이 값은 저장소 전체의 호출부와 같지 않다. 또 **단위는
정의를 담은 단위 지식**이고 호출 표현식 수가 아니다. 2026-10-02의 측정에서 `pct`의 호출부는 13이었고 호출 모듈 8개
전부에 걸쳐 있었으며, 호출 표현식은 38이었고 그 가운데 직접 호출이 16, 인자로 받는 쪽이 22였다. 승인 문구의 "36 안팎"은
표현식 단위이므로 같은 자로 잰 값이 아니다. 그 측정에서 vnv 판정은 부분 성공이었고, 해소 자체는 20/20, 오탐 0이었다.
따라서 이 수치를 churn의 크기로 인용할 때는 이 경계를 함께 적는다.

"X를 바꾸면 무엇이 영향받는가"를 **변경 전에** 계산한다 (`p12-change-impact-analysis`).

```
1. X의 IRI에서 satisfies / refines / constrains 역방향 질의 → 직접 의존 집합
2. 직접 의존 집합의 assumes 가정 중 X에 관한 것       → 무효화 후보
3. 단방향 규칙으로 하위 plane까지 반복
4. 결과: 청크 수 · plane 분포 · suspect가 될 링크 수 · 유저 승인이 필요한 결정 수
```

이 계산은 새 질의를 만들지 않고, 이미 있는 역방향 질의와 단방향 규칙을 조합한다. 구조 근사는
`bazel run //tools:impact -- <타깃>`이 링크를 deps로 대응시켜 `rdeps`로 낸다. 이 도구는 네 수치 가운데 항목 수와
지식 종류 분포, 승인이 필요한 결정 수의 셋과 직접 의존자 수를 낸다 (2026-09-11). 결과가 네 수치로 나오므로 변경의
크기를 비교할 수 있다. 다만 유저 승인이 필요한 수가 0이 아니면 그 변경은 자율 진행 범위를 벗어난다.

## §13. 저작 흐름과 완료

**저작 흐름 8단계**는 아래 순서로 진행한다. 요구마다 독립적으로 정제하고, 요구 사이의 순서는
`depends-on`과 ODD 시간 제약이 정한다 ([`p7-authoring-flow`](../kb/dev/decision/p7-authoring-flow/conclusion.md)).

1. 요구 작성 단계에서는 유저와 design이 요구를 쓴다.
1. 형식화 단계에서는 `decision` 지식 종류로 정제 수준이 추상인 항목을 쓰고 `serves` 링크를 단다.
1. 계약 선언 단계에서는 `contract` 지식 종류로 추상 수준의 계약을 선언한다.
1. 전개 단계에서는 논리 수준에서 `decision`의 `-space`와 `contract`의 사후조건, `schema`를 쓴다.
1. 확정 단계에서는 design과 유저가 체크박스 피드백으로 고르고 `-space`를 `resolved`로 닫는다.
1. 스키마 확정 단계에서는 스키마를 확정한다.
1. 구현 단계에서는 developer가 `artifact` 지식 종류로 구현한다.
1. 리뷰 단계에서는 `annotation` 지식 종류로 리뷰를 남긴다.

| 절차 | 입력 → 산출 | 게이트 | 결정 |
|---|---|---|---|
| 정제 전이 게이트 4종 | 기능에서 추상으로 갈 때 기여 명시를, 추상에서 논리로 갈 때 판정 술어와 범위를, 논리에서 구체로 갈 때 표본 근거와 배제 근거를, 구체에서 실행으로 갈 때 기준 바인딩을 묻는다 | `gate`(미구현) | [`p6-transition-gates`](../kb/dev/decision/p6-transition-gates/conclusion.md) |
| 결정 확정 | `-space`에서 유저가 체크박스로 후보 하나를 고르면 구체 수준 결정이 생기고, 배제된(eliminated) 항목은 대안으로 승격한다 | `space_check`·`feedback`(미구현) | [`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| 계약 선언에서 구현으로 | 시그니처를 먼저 선언하고, CEL로 쓴 사후조건이 V&V 기준의 재료가 된다 | `contract_check`(미구현) | [`p7-contract-first`](../kb/dev/decision/p7-contract-first/conclusion.md) |
| 스키마 확정 | 호환성을 판정해 `wasRevisionOf`를 쓰거나, 새 IRI를 만들어 `supersedes`로 잇는다 | `schema_compat`(미구현) | [`p7-schema-derivation`](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| 완료 판정 | 연쇄 완주, 계약 선행, 대안 존재, 가정 `stable`, V&V `verifies` 유효 | `dev_metrics`(미구현) | [`p7-dev-kb-completion`](../kb/dev/decision/p7-dev-kb-completion/conclusion.md) |

이 저장소에서 지금 실제로 도는 것은 요구 작성인 1단계와, 2, 4, 5단계의 결정 부분뿐이다. 다만 `-space` 없이
결론과 근거, 대안을 직접 저작한다.

## §14. 위험 분석에서 되먹임까지

| 절차 | 요지 | 결정 |
|---|---|---|
| 위험 분석 G1~G6 | 현상을 추출하고, 인과 모델을 세우고, 데이터를 검토하고, 지표와 시나리오 부류를 정한 뒤 목표 거동을 정한다. 규칙성 가정을 먼저 두고, 분석은 도메인당 한 번 하며 초기에는 전문가가 맡는다 | [`p8-risk-analysis-profile`](../kb/dev/decision/p8-risk-analysis-profile/conclusion.md) |
| 워크플로 10단계 | 목표 파생, 시나리오 형식화, 논리 시나리오와 기준, 테스트 케이스 생성, 검증기, 환경 할당, 실행, 판정, 보고, 되먹임의 차례로 간다. **1~3단계는 개발 확정 전에 시작한다** | [`p8-vv-workflow`](../kb/dev/decision/p8-vv-workflow/conclusion.md) |
| V&V 파생 | 요구에서 목표를, 추상 수준 결정에서 추상 수준 시나리오를, 계약 사후조건에서 기준을, 확정 값에서 테스트 케이스를, 구현에서 검증기를 파생한다 | [`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| 시나리오 저작 | 부류(G5)에서 시작해 ODD 속성으로 변수를 정하고, 계약 사후조건으로 기준을 정한 뒤 배제 자극을 기록한다. 구체 수준 항목은 생성기가 만든다 | [`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md) |
| 테스트 케이스 생성 5규칙 | 등가분할, 경계값, t-wise, 요인 주입, 관측 재현의 다섯이고, 등가분할과 경계값은 따로 센다. 규칙과 seed는 provenance에 남긴다 | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 환경 할당 | 판정할 수 있는 가장 낮은 단계에 할당한다. 요인이 단계를 정하고, 재현성은 할당의 조건이다 | [`p8-environment-assignment`](../kb/dev/decision/p8-environment-assignment/conclusion.md) |
| 검증 세 방향 | 수직 완주, 수평 실행 통과, 기준의 질(변이 검출) | [`p8-three-directions-of-verification`](../kb/dev/decision/p8-three-directions-of-verification/conclusion.md) |
| 검증과 확인 | 검증은 1~5단계의 검증기가 하고, 확인은 5~6단계의 실환경과 유저, 이탈을 거쳐 `requirement`로 일반화한다 | [`p8-verification-and-validation`](../kb/dev/decision/p8-verification-and-validation/conclusion.md) |

위험 분석 G1의 산출은 `defect` 모듈의 요인 개체이고, 피해와 현상, 가정은 질문지의 것을 그대로 채택했다(유저 답, 2026-09-29). 현상을
더할 때는 세 갈래 아래 **잎으로만** 더하고 새 상위 개념을 만들지 않는다. 개체마다 정의와 질문지 표기 `skos:notation`, 관측
수단 `agt:observationMeans`, 출처를 적는다. 관측 수단이 아직 없으면 `미확정`을 적고 그 까닭은 정의문에 적으며, 미확정의 수가
위험 분석의 산출 후보다. 2026-10-01에 미확정은 P17과 P20의 둘이다. G2의 인과는 `agt:hasImpact`로, G3은 `agt:hasTrigger`와
`agt:discoveredAtLevel`로, G4의 지표는 `agt:severityGrade`와 `agt:exposureGrade`, `agt:detectabilityGrade`로, G5의 부류는
`agt:exposesFactor`로 적는다. 판정은 vnv가 `kb/vv/`에서 하고, T-Box 트리플은 developer가 `defect-rules`의
`impact-causation-rules.ttl`로 옮긴다. 등급은 곱하지 않는다. G6의 목표 거동은 술어가 아니라 V&V 요구와 결정의 본문으로 적는다.

| 절차 | 요지 | 결정 |
|---|---|---|
| 불일치의 귀속 | 실패하면 기호로 진단하고, 산출물이나 지식, 또는 둘 다에 귀속한 뒤, 귀속과 조치, 배제된 전략을 지침에 적고 조치한다 | [`p8-mismatch-attribution`](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| 보고 5종 | 검증 상태와 커버리지, 결함 분포, 가정 건전성, 독립성을 보고한다. 보고는 저장하지 않고 뷰로 생성하며 리비전과 질의를 명기한다 | [`p8-vv-reports`](../kb/dev/decision/p8-vv-reports/conclusion.md) |
| 에이전트 V&V | 목표는 역할 책임이고, 자극은 작업 집합과 요구, 의도된 이탈이며, 기준은 shape와 완주, 인지 누락률, 안전 정지다. 3단계 시뮬레이션 프로젝트를 중심으로 한다 | [`p8-agent-vv`](../kb/dev/decision/p8-agent-vv/conclusion.md) · [`p12-cognition-measurement`](../kb/dev/decision/p12-cognition-measurement/conclusion.md) |
| 사후분석 | 불만족 핵과 보간, 최약 전제조건, 명세 추론으로 기호 진단을 하고 요인 추론과 지침을 거쳐 어휘와 요구/기준, ODD 후보를 낸다. 산출이 없으면 실패다 | [`p12-symbolic-diagnosis`](../kb/dev/decision/p12-symbolic-diagnosis/conclusion.md) · [`p12-incident-postmortem`](../kb/dev/decision/p12-incident-postmortem/conclusion.md) |
| 선제적 V&V | ODD 경계 근접과 커버리지 공백, 외부 지식 변화, 증거 노화가 트리거이고, 산출은 전부 `origin:observed` 후보다 | [`p8-proactive-vv`](../kb/dev/decision/p8-proactive-vv/conclusion.md) |

이 저장소는 아직 어느 절차도 실행하지 않았다. `kb/vv/`가 비어 있다 (도입 7단계).

<!-- 인용 끝 -->

## 입력 파일

원본 파일 102개다. 디렉토리로 묶었고 빠진 파일은 없다.

- `kb/dev/decision/p0-condition-taxonomy-extensible/` — `conventions.md`
- `kb/dev/decision/p0-premise-as-assumption/` — `conventions.md`
- `kb/dev/decision/p0-workset-anchor-neighbourhood/` — `conventions.md`
- `kb/dev/decision/p1-chunk-unit-is-tokens/` — `conventions.md`
- `kb/dev/decision/p1-context-budget-items/` — `conventions.md`
- `kb/dev/decision/p10-co-edit-evidence-from-small-commits/` — `conventions.md`
- `kb/dev/decision/p10-context-handoff-yields-links/` — `conventions.md`
- `kb/dev/decision/p10-embedding-similarity-narrows-only/` — `conventions.md`
- `kb/dev/decision/p10-extracted-references-are-candidates/` — `conventions.md`
- `kb/dev/decision/p10-link-by-construction/` — `conventions.md`
- `kb/dev/decision/p10-link-decay-states/` — `conventions.md`
- `kb/dev/decision/p10-link-judgement-evidence/` — `conventions.md`
- `kb/dev/decision/p10-restored-link-marking/` — `conventions.md`
- `kb/dev/decision/p10-traceability-matrix/` — `conventions.md`
- `kb/dev/decision/p10-traceability-metrics/` — `conventions.md`
- `kb/dev/decision/p11-execution-mode-and-workset/` — `conventions.md`
- `kb/dev/decision/p12-audit-and-onboarding-self-sufficiency/` — `conventions.md`
- `kb/dev/decision/p12-documents-are-generated/` — `conventions.md`
- `kb/dev/decision/p12-evaluation-metrics/` — `conventions.md`
- `kb/dev/decision/p12-symbolic-diagnosis/` — `conventions.md`
- `kb/dev/decision/p2-competency-questions/` — `conventions.md`
- `kb/dev/decision/p2-profile-answers-from-decisions/` — `conventions.md`
- `kb/dev/decision/p2-skeleton-and-domain-profile/` — `conventions.md`
- `kb/dev/decision/p3-condition-entity-from-odd-document/` — `conventions.md`
- `kb/dev/decision/p3-measurement-method-grades/` — `conventions.md`
- `kb/dev/decision/p3-odd-first-project-start/` — `conventions.md`
- `kb/dev/decision/p4-community-detection-proposes-composites/` — `conventions.md`
- `kb/dev/decision/p4-one-file-one-topic/` — `conventions.md`
- `kb/dev/decision/p4-projection-as-query/` — `conventions.md`
- `kb/dev/decision/p4-redundancy-as-safety-margin/` — `conventions.md`
- `kb/dev/decision/p5-plane-assignment-tool-surface/` — `conventions.md`
- `kb/dev/decision/p5-plane-by-verification/` — `conventions.md`
- `kb/dev/decision/p6-ascent-generalization/` — `conventions.md`
- `kb/dev/decision/p6-assumption-invalidation/` — `conventions.md`
- `kb/dev/decision/p6-assumption-verification-methods/` — `conventions.md`
- `kb/dev/decision/p6-descent-refinement/` — `conventions.md`
- `kb/dev/decision/p6-refinement-ladder/` — `conventions.md`
- `kb/dev/decision/p6-self-check-before-completion/` — `conventions.md`
- `kb/dev/decision/p6-transition-gates/` — `conventions.md`
- `kb/dev/decision/p7-contract-first/` — `conventions.md`
- `kb/dev/decision/p7-dev-kb-completion/` — `conventions.md`
- `kb/dev/decision/p7-dev-plane-substance/` — `conventions.md`
- `kb/dev/decision/p7-schema-derivation/` — `conventions.md`
- `kb/dev/decision/p8-agent-vv/` — `conventions.md`
- `kb/dev/decision/p8-case-generation/` — `conventions.md`
- `kb/dev/decision/p8-environment-assignment/` — `conventions.md`
- `kb/dev/decision/p8-mismatch-attribution/` — `conventions.md`
- `kb/dev/decision/p8-odc-defect-subtypes/` — `conventions.md`
- `kb/dev/decision/p8-proactive-vv/` — `conventions.md`
- `kb/dev/decision/p8-risk-analysis-profile/` — `conventions.md`
- `kb/dev/decision/p8-scenario-authoring/` — `conventions.md`
- `kb/dev/decision/p8-scenario-ladder-rungs/` — `conventions.md`
- `kb/dev/decision/p8-three-directions-of-verification/` — `conventions.md`
- `kb/dev/decision/p8-verification-and-validation/` — `conventions.md`
- `kb/dev/decision/p8-verification-round-stop-rule/` — `conventions.md`
- `kb/dev/decision/p8-vv-reports/` — `conventions.md`
- `kb/dev/decision/p8-vv-workflow/` — `conventions.md`
- `kb/dev/decision/p9-candidate-generation-limits/` — `conventions.md`
- `kb/dev/decision/p9-candidate-storage/` — `conventions.md`
- `kb/dev/decision/p9-constraint-propagation-timing/` — `conventions.md`
- `kb/dev/decision/p9-contradiction-handling/` — `conventions.md`
- `kb/dev/decision/p9-design-space-file/` — `conventions.md`
- `kb/dev/decision/p9-feasible-set-for-settlement/` — `conventions.md`
- `kb/dev/decision/pe-anchor-is-bazel-label/` — `conventions.md`
- `kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/` — `conventions.md`
- `kb/dev/decision/pe-notation-and-cel/` — `conventions.md`
- `kb/dev/decision/pe-odd-is-openodd/` — `conventions.md`
- `kb/dev/norm/method/` — `adoption-order.md` · `authoring-flow-status.md` · `authoring-flow.md` · `candidates-closure.md` · `candidates.md` · `chunk-authoring.md` · `chunk-split-merge.md` · `completion.md` · `generalization-manual.md` · `generalization.md` · `head.md` · `impact.md` · `linking-sources.md` · `linking.md` · `odd-gate.md` · `odd.md` · `order-no-skipping.md` · `order.md` · `profile-extension-points.md` · `profile-steps.md` · `profile.md` · `refinement-transition.md` · `retrieval-assembly.md` · `retrieval.md` · `update-link-state.md` · `update.md` · `verification-cases.md` · `verification-judge.md` · `verification-stop-rule.md` · `verification.md` · `views-form.md` · `views.md` · `vv-procedures-risk.md` · `vv-procedures-status.md` · `vv-procedures.md`

