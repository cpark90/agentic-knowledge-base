# method — 각 단계를 어떻게 하는가

§0가 순서라면 여기는 방법이다. 구조도 v5에 따라 **코어(§1~§12,
두 KB 공통) / development(§13) / V&V(§14)** 세 층으로 적는다. 각 절차는 **입력 → 절차 →
게이트 → 산출**로 쓰고, 규칙은 [`rules.md`](rules.md), 도구는 [`tools.md`](tools.md)를
가리킨다. 절차를 바꾸면 대응 도구도 함께 본다.

# 코어 — 공통 절차

## 0. 순서와 완료 판정

전체 순서(운용 순환)는 여덟 단계다. 각 절은 그 단계를 어떻게 하는가이고, [`rules.md`](rules.md)는 결과가
유효한지의 규칙이다. 원본은 노트 Part VI·XI과 운용 지도다. 이 저장소 자신이 어디까지 왔는가의 도입 8단계는
[`roadmap.md`](roadmap.md)에 있다. 둘은 다른 축이다.

```
프로파일 구축 → ODD 작성 → 정제(저작) → 조회 → 연결 → 갱신 → 뷰 → 일반화
                                                                    │
                     (교훈이 다시 프로파일·ODD·결정으로) ←──────────┘
```

| # | 단계 | 산출 | 다음 단계의 전제가 되는 이유 | 방법 |
|---|---|---|---|---|
| 1 | **프로파일 구축** | `profile/<분야>` 모듈 — 각 plane의 실체·판정 도구·조건 어휘·결함 유형 | 어휘가 없으면 ODD의 조건을 개념에 대응시킬 수 없다 (d-0063 2단계) | [§1](#1-프로파일-구축) |
| 2 | **ODD 작성** | 조건 3분류·판정 방법·등급, 명시 제외 | ODD가 비면 스코프가 잘리지 않고 가정이 참조할 속성이 없다 — **체계 전체가 정지한다** (d-0063) | [§2](#2-odd-작성) |
| 3 | **정제(저작)** | functional → abstract → logical → concrete → executable 의 청크 | 조회·연결의 대상이 있어야 한다 | §3·§4·§5 |
| 4 | **조회** | 작업 집합 (스코프 × level 창) | 에이전트가 무엇을 보는지가 정해져야 편집의 읽기 집합이 정의된다 | [§8](#8-조회) |
| 5 | **연결** | 링크 — 편집 부산물로 구축, 복원은 예외 | 링크 없이는 무효화 범위를 계산할 수 없다 (d-0009) | [§6](#6-연결) |
| 6 | **갱신** | 가정 판정 → 무효화 전파 → 재판정 | 갱신 단절의 해소가 이 체계의 존재 이유다 (d-0007) | [§7](#7-갱신) |
| 7 | **뷰** | tangle·weave·문서·추적 매트릭스 — 저장하지 않고 질의 | 축적된 지식이 쓰이는 형태 (d-0075) | [§9](#9-뷰) |
| 8 | **일반화** | 관측 → 도메인 → 변수 → 개념. 온톨로지가 자란다 | 다음 프로젝트가 자란 어휘로 시작한다 (d-0006) | [§10](#10-일반화) |

**단계를 건너뛰지 않는다.** functional에서 곧바로 executable로 가는 것이 현재 에이전트의
기본 동작이다. 그것이 계층 단절의 원인이다 (노트 6.1절).

**정제의 산출은 개발 KB(`kb/dev/`)에, 검증 지식은 V&V KB(`kb/vv/`)에 쌓인다.** 정제와
나란히 vnv 역할이 검증 목표·시나리오·판정 기준을 저작하고 `verifies`로 개발 KB를
가리킨다. 저작·판정 분리가 KB 수준에서도 성립한다 (노트 Part VII).

### 완료 판정

각 단계는 다음으로 넘어가기 전에 판정된다. 판정은 시간이 아니라 **상태 확인**이다.

| 단계 | 완료 판정 |
|---|---|
| 프로파일 구축 | 역량 질문이 전부 질의로 답해진다 (d-0052) · `bazel test //kb/ontology:gate_test` PASS |
| ODD 작성 | 조건마다 객관적 판정 방법과 등급 A~C · 5단계 절차의 마지막(실제 조건 대조)에서 이탈 0 (d-0063) |
| 정제 | 각 전이가 근거와 `refines` 기록을 남겼다 · 게이트 PASS (d-0005) |
| 조회 | 역할별 작업 집합이 컨텍스트 예산 안에 든다 (d-0041) |
| 연결 | 링크 밀도 > 0, 복원 비율이 낮다 (d-0112) |
| 갱신 | 전수조사 없이 무효 범위가 계산된다 (d-0007) |
| 뷰 | 저장된 뷰가 없다 — 전부 질의 결과다 (d-0075) |
| 일반화 | 온톨로지 확장 건수 · 승격된 교훈이 규칙이 되었다 (d-0006 · d-0017) |

### 도입 순서

전부를 한 번에 도입하지 않는다. **앞 단계만으로 이득이 확인되지 않으면 다음 단계를
진행할 근거가 없다.** 이 저장소 자신의 진행 상태와 실측은 [`roadmap.md`](roadmap.md)에 있다.

## 1. 프로파일 구축

**아직 절차가 없다.** 코어가 무엇을 남겨 두었는지만 정해져 있다. 프로파일은 코어 클래스의
하위 클래스와 shape만 추가하고 코어를 수정하지 않는다
([`id:chunk-d0057`](../chunks/decision/d-0057-profile-extension-only-module.md)).

절차가 답해야 할 것은 분야의 무엇을 먼저 열거하는가, 역량 질문을 언제 쓰는가, 코어의 어느
클래스가 확장점인가, 완료를 무엇으로 판정하는가다. 첫째 물음의 후보는 plane별 실체·판정
도구·조건 어휘다. [`ontology.md`](ontology.md)의 두 층 구분과 참조 프로파일 표가 재료다.
첫 프로파일을 실제로 하나 만들면서 절차를 뽑는 것이 다음 산출이다 ([`roadmap.md`](roadmap.md)).

## 2. ODD 작성

새 프로젝트의 첫 산출물이다. 온톨로지는 프로젝트 간에 공유되므로 이미 있다.
**5단계를 통과하기 전에는 스코프를 파생하지 않는다** ([`id:chunk-d0063`](../chunks/decision/d-0063-odd-first-authoring-procedure.md)).

1. 프로젝트가 의존하는 조건을 **정적 요소 / 환경 조건 / 동적 요소** 3갈래로 열거한다.
2. 각 속성의 범주를 `related/condition`에서 생성된 택소노미(`taxonomy.yml`)에 대응시킨다.
   없으면 온톨로지를 먼저 확장한다. 문서는 OpenODD 형식이다
   ([`pe-odd-is-openodd`](../kb/dev/decision/pe-odd-is-openodd/conclusion.md)).
3. **값 또는 범위**와 **객관적 판정 방법**을 지정한다. "정상이다"가 아니라 "명령 X가 Y를
   반환한다"여야 한다. 등급 A~D를 매기고 **D는 ODD에 넣지 않는다**. D를 넣으면 영원히
   `unverified`인 속성이 생겨 모니터링 결과가 늘 불완전해진다.
4. 검토했으나 밖에 두는 것을 **명시 제외**에 기록한다. 서식은
   `"<대상> — reviewed YYYY-MM, 이유: <근거>"`다. 적지 않은 것과 검토 후 제외한 것을 구분하는
   것이 이 절의 존재 이유다.
5. 현재 **실제 조건이 ODD 안에 있는지 대조**한다. 명령은 `bazel run //tools:odd_check`다
   (`CHECKS.cmd`, 3.5절). 첫 모니터링에서 이탈이 나오면 틀린 쪽은 현실이 아니라 ODD다.

게이트는 `bazel test //kb/odd:gate_test`다. 산출은 `kb/odd/*-odd.yml`(OpenODD, 부록 E.4)이고,
그것에서 `*-odd.ttl`이 생성되며 그 위에서 스코프가 파생된다. 속성 범주는 `related/condition`에서
생성된 택소노미 안이어야 한다.

## 3. 청크 저작

가장 흔한 작업이다.

1. **plane과 level을 정한다.** plane 할당 기준은 **판정 방식**이고, 저장 위치나 파일 형식이
   아니다 ([rules §3](rules.md#3-plane--판정-방식으로-나뉜-종류)).
2. 해당 위치에 **파일 하나**를 만든다. 구성은 frontmatter(head) + 본문 ≤ 42줄이다
   ([rules §1](rules.md#1-chunk--자립적-최소-지식-단위)).
3. **전제가 있으면 가정을 만들고 `assumes`로 가리킨다.** 가정은 ODD 조건을 `refersTo` 해야
   한다. 가정 없는 청크는 "ODD 전체를 전제한다"는 뜻이 아니라 전제를 아직 적지 않은 것이다.
4. **통합이 필요하면** 복합체에 잇는다. 통합이 필요한 때는 함께 읽혀야 이해되거나 순서가
   뜻을 가질 때뿐이다. 그렇지 않으면 개별로 둔다 ([rules §2](rules.md#2-복합체--통합이-필요한-것만)).
5. `bazel test //...`를 실행한다.

**분할 신호**는 라벨을 하나로 쓸 수 없는 것, 본문 일부만 재사용·가정·`suspect`의 대상이 되는
것이다. **병합 신호**는 두 청크가 항상 함께 읽히는 것, 한쪽이 다른 쪽 없이 이해되지 않는 것,
합쳐도 42줄 이하인 것이다. 분할·병합은 새 IRI를 만들고 옛 IRI를 `prov:wasDerivedFrom`으로
잇는다 (d-0002 · d-0010).

## 4. 정제 전이

level은 `functional → abstract → logical → concrete → executable` 순이다. 각 정제는 **근거와
`refines` 링크를 남기고** 전이 게이트를 통과해야 한다. 전이 게이트는 어휘 검사, 후보가 비어
있지 않음, 배제 근거 존재, 판정 도구 통과다. 게이트 없이 만든 하위 청크는 고아율에 잡힌다
([`id:chunk-d0005`](../chunks/decision/d-0005-abstraction-ladder.md)).

level을 바꾸지 않는다. 전이는 기존 청크의 level 갱신이 아니라 **새 청크 + `refines`**다
(d-0071). 단계를 건너뛰면 의도와 결과만 남고 그 사이가 빈다.

## 5. 후보 관리

미확정은 언제나 **"두 항목이 연결되는가"의 미확정**이다. 값이 미확정인 것처럼 보이는 경우도
링크로 환원한다 ([`id:chunk-d0096`](../chunks/decision/d-0096-uncertainty-as-link-uncertainty.md)).

- `-space` 파일에 **변수** · **후보** · **제약**을 쓴다. 변수는 링크가 필요한 항목, 후보는
  도착점 집합, 제약은 양립 조건이다. abstract 단계는 변수까지, logical 단계는 후보와 제약까지
  채운 상태다 (d-0100).
- 가능성은 확률이 아니라 **가능 / 불가능의 집합**이다. 등급을 매기지 않고, 선호는 후보를
  기각하지 않고 순서만 정한다 (d-0097 · d-0104).
- **제약 전파는 게이트와 재검증 시점에서만** 실행한다. 편집마다 돌리지 않는다 (d-0101).
- **후보가 없으면 자동으로 풀지 않고 유저에게 넘긴다** (d-0103). 후보가 없는 상태가 모순이다.

과도한 추측이 자료구조 수준에서 막힌다. 후보가 여럿인 상태가 정상이고, 확정은 제약 전파가
나머지를 기각했을 때만 일어난다.

## 6. 연결

**링크는 산출물이 만들어지는 순간 편집 연산의 부산물로 만든다.** 이것이 구축이다. 이미
존재하는 산출물에서 관계를 되짚는 복원은 체계 도입 전 산출물·외부 유입물·구축 누락 감사에만
쓴다 ([`id:chunk-d0009`](../chunks/decision/d-0009-link-by-construction.md)).

- 탐색의 **읽기 집합**을 편집 컨텍스트에 후보 목록으로 넘기고, 편집 후 **쓰기 집합**과
  대조해 확정한다. 하네스가 읽기·쓰기를 기록하지 않으면 이 절차가 성립하지 않는다. 첫 형태는
  `bazel build //kg:workset --//kb:anchor=…`로 펼친 청크를 `bazel run //tools:handoff`가 새
  청크의 `sources`에 옮기는 것이다.
- 판정 근거는 검사 가능성 순이다. 순서는 구축 기록 > 동시 편집 이력 > 테스트 공동 커버 >
  임베딩 유사도 > 같은 세션에서 읽음이다 (d-0110). 임베딩 유사도는 후보 추림에만 쓴다.
- **임베딩 유사도를 확정 근거로 쓰지 않는다** (d-0009).

조건(`when`)·증거 기록·상태 전이 규칙은
[`p9-conditional-links`](../kb/dev/decision/p9-conditional-links/conclusion.md)·[`p9-evidence-ledger`](../kb/dev/decision/p9-evidence-ledger/conclusion.md)에
있다. 조회 알고리즘은 §8에 있다. 복원 경로는
[`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)·[`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md)에
있다.

## 7. 갱신

1. **가정을 판정한다.** 판정 유형과 판정 식이 가정과 함께 저장되어 있어야 한다 (d-0087).
   판정 유형은 그래프 질의, 파일 검사, 실행 검사, 외부 조회, 사람 확인이다.
2. 깨진 가정에 의존하는 항목을 `invalidated`로, 그 항목을 가리키는 링크의 반대편을
   `suspect`로 표시한다. 전파는 plane 단방향 규칙을 따르므로 유계다 (d-0007 · d-0088).
3. **재판정은 즉시 하지 않고 커밋·세션 종료 같은 경계에서 일괄로** 한다. 알려진 변경 패턴은
   규칙으로 자동 갱신하고, 규칙에 없는 변경만 판정으로 보낸다 (d-0106).

무효화는 삭제가 아니다. 무효화 이력은 일반화의 입력이다. 어떤 가정이 자주 깨지는가는 그
자체로 일반화 대상이다.

## 8. 조회

**읽기 응답의 기본은 라벨 목록이지 본문이 아니다** (d-0082). 순서는 스코프 → 라벨 목록 →
필요한 것만 펼치기 → 작업 집합이다. 도구는 `bazel build //kg:workset_<role>`이다. 수준 창·앵커·
예산은 `kb_workset` 인자로 준다.

- **작업 집합**(Workset)은 스코프 × 수준 창 × **앵커 이웃**으로 걸러져 에이전트에게 실제로
  보이는 청크 집합이다. 컨텍스트 통제의 단위다 (노트 0.5절,
  [`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)).
  v1의 scene·situation 어휘는 폐기되었다. 앵커 없는 요청에는 접힌 라벨 목록만 준다.
- dispatch 대상에게 전체 컨텍스트가 아니라 **스코프로 거른 작업 집합만** 넘긴다.
- **툴 표면이 할당을 따라야 한다.** 저장소만 나누고 읽기 도구가 전체를 반환하면 컨텍스트
  분리는 이름뿐이다 (d-0081).
- 컨텍스트 예산은 항목별로 분해해 통제하고 지식 본문은 잔여로 둔다 (d-0041).

조립 알고리즘은
[`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)
결정이고, 첫 형태는 `workset`([`tools.md`](tools.md))이다. 알고리즘의 순서는 앵커 → 이웃 확장 →
우선순위 → 예산 패킹이다. 예산 상한식은 Δ = m·k·42이고, 앵커 m × 이웃 k × 42줄이다.

## 9. 뷰

**모든 뷰는 질의의 결과이며 저장하지 않는다.** 저장된 뷰는 원본과 어긋나는 순간부터
거짓이 된다 ([`id:chunk-d0075`](../chunks/decision/d-0075-projection-as-query.md)).

| 뷰 | 질의 |
|---|---|
| tangle (코드 파일) | 복합체의 `artifact` 부분을 `co:index` 순으로 이어 붙인다 |
| weave (문서) | 산출물 청크와 그것을 `targets`하는 주석을 함께 뽑는다 |
| 라벨 목록 | 스코프 안 청크의 `rdfs:label`만 |
| 작업 집합 | 스코프의 plane과 ODD 조건으로 거른 청크 |
| 추적 매트릭스 | plane × plane 격자 — **빈 칸이 곧 누락이다** (d-0109) |

## 10. 일반화

관측에서 어휘로 올라간다. 정제만 있는 체계는 지식이 축적되지 않는다 (d-0006).

| 전이 | 산출 |
|---|---|
| executable → concrete | 실행 기록 |
| concrete → logical | 반복 패턴에서 도메인 추출 → `-space` 도메인 갱신 |
| logical → abstract | 도메인을 관통하는 변수 식별 |
| abstract → functional | 변수를 설명하는 개념 식별 → **온톨로지 갱신** |

마지막 전이가 특별하다. 어휘가 자라면 다음 프로젝트는 자란 어휘로 시작한다. **일반화는
자동화하지 않는다.** 후보를 제시하고 확인을 받으며, 온톨로지 갱신은 품질 검사를 통과해야
한다. **트리거는 초기에 사람 지정만 쓴다.** 반복 임계값 트리거는 관측 모수가 쌓인 뒤다
(d-0006 · d-0089). 교훈 승격이 일반화의 최소 단위다 (d-0017 · d-0127).

## 11. 검증 — V&V 층으로

v1의 "검증은 응용"(d-0130)은 v3부터 대체되었다. 검증·확인은 **두 번째 지식 베이스**이고, 절차는
§14 V&V 층에 있다 ([`p12-dev-vv-kb-exchange`](../kb/dev/decision/p12-dev-vv-kb-exchange/conclusion.md)).
코어가 제공하는 것은 시험 대상·경계(ODD)·결과 축적(실행 기록)·실패 분류(defect)의 단위다.

## 12. 영향 분석

"X를 바꾸면 무엇이 영향받는가"를 **변경 전에** 계산한다 (d-0148).

```
1. X의 IRI에서 satisfies / refines / constrains 역방향 질의 → 직접 의존 집합
2. 직접 의존 집합의 assumes 가정 중 X에 관한 것       → 무효화 후보
3. 단방향 규칙으로 하위 plane까지 반복
4. 결과: 청크 수 · plane 분포 · suspect가 될 링크 수 · 유저 승인이 필요한 결정 수
```

새 질의를 만들지 않는다. 이미 있는 역방향 질의와 단방향 규칙의 조합이다. 구조 근사는
`bazel run //tools:impact -- <타깃>`(링크 = deps, `rdeps`)이 낸다. 이 도구는 네 수치 중 셋과
직접 의존자 수를 낸다 (2026-09-11). 셋은 항목 수·plane 분포·승인 필요 결정 수다. 네 수치로
나오므로 변경의 크기가 비교 가능해진다. 유저 승인이 필요한 수가 0이 아니면 자율 진행 범위를
벗어난다.

# development — 개발 KB의 절차 (노트 7.3~7.9)

## 13. 저작 흐름과 완료

**저작 흐름 8단계**는 요구 작성(유저+design) → 형식화(`decision` abstract, `serves`) → 계약
선언(`contract` abstract) → 전개(`decision` logical `-space` / `contract` logical 사후조건 /
`schema` logical) → 확정(design+유저, 체크박스 피드백, `-space` resolved) → 스키마 확정 →
구현(developer, `artifact`) → 리뷰(`annotation`)다
([`p7-authoring-flow`](../kb/dev/decision/p7-authoring-flow/conclusion.md)). 요구마다 독립적으로
정제하고, 요구 간 순서는 `depends-on`과 ODD 시간 제약이 정한다.

| 절차 | 입력 → 산출 | 게이트 | 결정 |
|---|---|---|---|
| 정제 전이 게이트 4종 | f→a 기여 명시 / a→l 판정식·범위 / l→c 표본 근거·배제 근거 / c→e 기준 바인딩 | `gate`(미구현) | [p6-transition-gates](../kb/dev/decision/p6-transition-gates/conclusion.md) |
| 결정 확정 | `-space` → 유저 체크박스 → 후보 하나 → concrete 청크 + eliminated 항목이 대안 청크로 승격 | `space_check`·`feedback`(미구현) | [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| 계약 선언 → 구현 | 시그니처 먼저, 사후조건(CEL)이 V&V 기준의 재료 | `contract_check`(미구현) | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| 스키마 확정 | 호환성 판정 → `wasRevisionOf` 또는 새 IRI + `supersedes` | `schema_compat`(미구현) | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| 완료 판정 | 연쇄 완주 · 계약 선행 · 대안 존재 · 가정 `stable` · V&V `verifies` 유효 | `dev_metrics`(미구현) | [p7-dev-kb-completion](../kb/dev/decision/p7-dev-kb-completion/conclusion.md) |

이 저장소에서 지금 실제로 도는 것은 1(요구)과 2·4·5의 결정 부분뿐이다. 다만 `-space` 없이
결론·근거·대안을 직접 저작한다.

# V&V — V&V KB의 절차 (노트 8.19~8.27, 8.4, 12.12)

## 14. 위험 분석에서 되먹임까지

| 절차 | 요지 | 결정 |
|---|---|---|
| 위험 분석 G1~G6 | 현상 추출 → 인과 모델 → 데이터 검토 → 지표 → 시나리오 부류 → 목표 거동. 규칙성 가정 먼저. 도메인당 한 번, 초기엔 전문가 | [p8-risk-analysis-profile](../kb/dev/decision/p8-risk-analysis-profile/conclusion.md) |
| 워크플로 10단계 | 목표 파생 → 시나리오 형식화 → 논리 시나리오+기준 → 케이스 생성 → 검증기 → 환경 할당 → 실행 → 판정 → 보고 → 되먹임. **1~3은 개발 확정 전 시작** | [p8-vv-workflow](../kb/dev/decision/p8-vv-workflow/conclusion.md) |
| V&V 파생 | 요구→목표 / 결정 abstract→시나리오 abstract / 계약 사후조건→기준 / 확정 값→케이스 / 구현→검증기 | [p8-scenario-ladder-rungs](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| 시나리오 저작 | 부류(G5)에서 시작 → ODD 속성으로 변수 → 계약 사후조건으로 기준 → 배제 자극 기록. concrete는 생성기가 | [p8-scenario-authoring](../kb/dev/decision/p8-scenario-authoring/conclusion.md) |
| 케이스 생성 5규칙 | 등가분할 · 경계값(별도 집계) · t-wise · 요인 주입 · 관측 재현. 규칙·seed는 provenance에 | [p8-case-generation](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 환경 할당 | 판정 가능한 최저 단계. 요인 → 단계. 재현성 조건 | [p8-environment-assignment](../kb/dev/decision/p8-environment-assignment/conclusion.md) |
| 검증 세 방향 | 수직 완주 · 수평 실행 통과 · 기준의 질(변이 검출) | [p8-three-directions-of-verification](../kb/dev/decision/p8-three-directions-of-verification/conclusion.md) |
| 검증과 확인 | 검증은 1~5단계 검증기 / 확인은 5~6단계 실환경·유저·이탈 → `requirement` 일반화 | [p8-verification-and-validation](../kb/dev/decision/p8-verification-and-validation/conclusion.md) |
| 불일치의 귀속 | 실패 → 기호 진단 → 산출물/지식/둘 다 귀속 → 지침(귀속·조치·배제된 전략) → 조치 | [p8-mismatch-attribution](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| 보고 5종 | 검증 상태 · 커버리지 · 결함 분포 · 가정 건전성 · 독립성. 저장하지 않고 뷰, 리비전·질의 명기 | [p8-vv-reports](../kb/dev/decision/p8-vv-reports/conclusion.md) |
| 에이전트 V&V | 목표는 역할 책임, 자극은 작업 집합+요구+의도된 이탈, 기준은 shape·완주·인지 누락률·안전 정지. 3단계 시뮬레이션 프로젝트 중심 | [p8-agent-vv](../kb/dev/decision/p8-agent-vv/conclusion.md) · [p12-cognition-measurement](../kb/dev/decision/p12-cognition-measurement/conclusion.md) |
| 사후분석 | 기호 진단(불만족 핵·보간·최약 전제조건·명세 추론) → 요인 추론 → 지침 → 어휘·요구/기준·ODD 후보. 산출 없으면 실패 | [p12-symbolic-diagnosis](../kb/dev/decision/p12-symbolic-diagnosis/conclusion.md) · [p12-incident-postmortem](../kb/dev/decision/p12-incident-postmortem/conclusion.md) |
| 선제적 V&V | ODD 경계 근접 · 커버리지 공백 · 외부 지식 변화 · 증거 노화가 트리거. 산출은 전부 `origin:observed` 후보 | [p8-proactive-vv](../kb/dev/decision/p8-proactive-vv/conclusion.md) |

이 저장소는 아직 어느 절차도 실행하지 않았다. `kb/vv/`가 비어 있다 (도입 7단계).
