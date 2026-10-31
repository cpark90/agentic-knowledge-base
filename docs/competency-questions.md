# 역량 질문 — 온톨로지의 요구사항이자 완료 판정

역량 질문은 온톨로지가 답해야 하는 질문이다. **온톨로지가 답해야 하는 질문 목록이 그 온톨로지의 요구사항이다.**
각 질문은 그래프 질의 하나로 답할 수 있어야 하고, 답할 수 없으면 필요한 개념이나 속성, 링크가 어휘에 없다는 뜻이다
([`p2-competency-questions`](../kb/dev/decision/p2-competency-questions/conclusion.md)).

답할 수 있는 질문은 질의 파일로 있다. `tools/cq-queries/`의 `CQ-NN.rq` 하나가 질문 하나이고,
`bazel run //tools:query -- CQ-NN --labels`가 그 답을 라벨 목록으로 낸다. 전체 현황은 뷰 `bazel build //kg:cq`가
낸다(2026-09-14). **이 문서는 질문과 질의 이름만 적고, 값은 `bazel build //kg:cq`로 본다.**

## 쓰는 법

1. **새 개념이나 속성을 추가할 때는 어느 질문에 기여하는지 적는다.** 어느 질문에도 기여하지 않는 개념은
   과설계이므로 만들지 않는다.
1. **답할 수 없는 질문이 다음 어휘 확장의 근거다.** 개념을 먼저 늘리고 쓸 곳을 찾지 않고, 답해야 할 질문이 있을
   때 어휘를 늘린다.
1. **질문을 답할 수 없게 만드는 변경은 검토 대상이다.** 아래 상태가 ✅에서 ❌로 내려가는 변경은 리뷰에서 걸러진다.
1. 답은 질의로 얻으므로 **저장하지 않는다**. 값은 생성 뷰 `bazel build //kg:cq`가 낸다.

질문에는 누가 언제 묻는가가 있어야 한다. 실제로 묻지 않는 질문은 요구사항이 아니다.

## 상태 표기

| 표기 | 뜻 |
|---|---|
| ✅ | 지금 질의 하나로 답한다 |
| ⚠ | 답하지만 데이터가 비어 있거나 부분만 답한다 |
| ❌ | 어휘가 없어 질의를 쓸 수 없다. 무엇이 없는지 적는다 |

---

## A. 구조와 조망

**CQ-01 ✅ 이 적용 범위 안에 무엇이 있는가 — 라벨 목록을 보여 달라.**
읽기의 기본 진입점이다. `?c a ?planeClass ; rdfs:label ?l`.

**CQ-02 ✅ 이 단위 지식은 어느 칸에 있는가 (지식 종류와 정제 수준).**
`?c a ?plane ; agt:hasLevel ?level`. 이 질의는 격자 배치와 통계의 기초다.

**CQ-03 ✅ 토큰 상한을 넘는 단위 지식이 있는가.**
`?c agt:tokenCount ?n FILTER(?n > 1092)`. 지식 종류별 상한은 `token-budget-shapes`에 있다(2026-10-01, 단위는 토큰). shape가 이미 막지만, 분포는 질의로 본다.
*값은 `bazel run //tools:query -- CQ-03`이 낸다. 분포는 `bazel run //tools:tokens`가 낸다.*

**CQ-04 ✅ 어느 복합체에도 속하지 않는 단위 지식이 있는가 (고아 후보).**
`?c a agt:Chunk FILTER NOT EXISTS { ?x agt:hasDirectPart ?c }`.
복합체는 통합이 필요한 것만 만들므로(유저 결정), 이 질의의 답이 0일 필요는 없다.

**CQ-05 ✅ 복합체의 직접 부분이 9개를 넘는가, 그리고 부분의 지식 종류나 수준이 전체와 다른가.**
`?k a agt:Composite ; agt:hasDirectPart ?p`로 집계하고 `?kl != ?pl`로 비교한다.

**CQ-06 ❌ 이 단위 지식의 라벨이 본문을 대표하는가.**
이 질문은 판정할 수 없다. 기계가 답할 수 없는 질문이어서 어휘로 풀 수 없으므로, 라벨 대표성 지표로 관측한다
([`space/evaluation-metrics-space.md`](../space/evaluation-metrics-space.md)).

## B. 경계 — ODD·가정·적용 범위

**CQ-07 ✅ 이 프로젝트는 무엇을 전제하는가 — ODD 조건과 판정 방법을 보여 달라.**
`?odd agt:hasCondition ?c . ?c agt:conditionValue ?v ; agt:checkMethod ?m ; agt:verificationGrade ?g`.

**CQ-08 ✅ 아무도 참조하지 않는 ODD 조건이 있는가 (ODD 과대의 신호).**
가정도 적용 범위도 가리키지 않는 조건이다.

**CQ-09 ✅ 전제를 적지 않은 단위 지식이 얼마나 되는가.**
`?c a agt:DecisionChunk FILTER NOT EXISTS { ?c agt:assumes ?a }`.

**CQ-10 ✅ 이 가정은 어느 조건 위에 서 있고, 판정 방법은 무엇인가.**
`?a agt:refersTo ?cond ; agt:proposition ?p`.

**CQ-11 ⚠ 이 적용 범위는 ODD의 어느 부분집합인가 — 이 역할이 볼 수 있는 조건은 무엇인가.**
`?s agt:subsetOf ?odd ; agt:includesCondition ?c`.
적용 범위 밖 의존을 묻는 질문은 어떤 지식이 적용 범위 밖의 조건에 의존하는가를 묻는다. 가정이 비어 있으면
그 답은 의미가 없다.

**CQ-12 ❌ 이 시나리오는 ODD 범위 안인가.**
`agt:Scenario`와 `odd:outside` 태그 어휘가 없다. 이 어휘는 검증 단계에서 필요해진다.

## C. 정제 계층과 후보

**CQ-13 ⚠ 이 지식은 어느 상위에서 내려왔는가 — functional까지 거슬러 달라.**
`?c agt:refines+ ?anc`. 어휘는 갖춰졌다.

**CQ-14 ⚠ 이 변수의 후보는 무엇이고 무엇이 왜 배제되었는가.**
`?l a agt:Link ; agt:linkFrom :X ; agt:linkState ?st`. 후보와 배제(`invalid`)를 상태로 구분한다.
어휘는 있으나 **배제 사유**를 담을 자리가 아직 부족하다. 근거 종류만 있고 제약 자체는 없다.

**CQ-15 ⚠ 후보가 하나로 좁혀졌는가, 그리고 후보가 0인 변수(모순)가 있는가.**
`agt:linkState "candidate"`를 집계한다.

## D. 추적성

**CQ-16 ⚠ X가 바뀌면 무엇이 영향받는가.** (영향 분석)
`?x agt:cites|agt:satisfies|agt:refines|agt:assumes ?target`를 역방향으로 따라가고, 지식 종류의 단방향 영향 규칙을 반복해 적용한다.

**CQ-17 ⚠ 이 결정을 충족하는 산출물이 있는가, 그리고 `verifies`가 없는 인터페이스는 무엇인가.**
(커버리지 — 추적 매트릭스의 빈 칸)
`?d a agt:DecisionChunk FILTER NOT EXISTS { ?x agt:satisfies ?d }`.

**CQ-18 ⚠ 이 코드는 왜 이렇게 됐는가.** (근거 추적)
`:x agt:refines+ ?anc`로 상위 수준까지 거슬러 오른다.

**CQ-19 ⚠ 지금 `suspect`나 `invalid`인 링크는 무엇인가.** (재검증 큐)
`?l a agt:Link ; agt:linkState ?s FILTER(?s IN ("suspect","invalid"))`.

**CQ-20 ✅ 이 단위 지식이 본문에서 인용하는 다른 지식은 무엇인가.**
`?a agt:cites ?b`. 인용 링크는 `tools/extract_refs.py`가 본문에서 뽑아 생성한다.

**CQ-33 ✅ 이 지식은 무엇을 대체했고 무엇에 대체되었는가 — `supersedes` 이력.**
`agt:supersedes`를 양방향으로 묻는다. 질의는 `CQ-33.rq`다.

**CQ-34 ✅ 링크가 종류별로 몇 개 있는가.**
술어별로 집계한다. 질의는 `CQ-34.rq`다.

## D-1. 신뢰 등급

**CQ-31 ✅ 이 단위 지식은 누가 만들었고 누가 검증했는가 — 사람이 검토한 단위 지식은 얼마나 되는가.**
`?c agt:generatedBy ?g`와 `?c agt:verifiedBy ?v FILTER(STRSTARTS(?v, "human:"))`. `agt:verifiedBy`는 지금 내용을 검증한 주체만 담는다.

**CQ-32 ✅ 검증한 뒤에 내용이 바뀐 단위 지식이 있는가.**
`prov:generatedAtTime >` 가장 늦은 `agt:verifiedAt`. shape가 이 경우를 FAIL로 막는다(`trust-shapes.ttl`).

## E. 갱신과 무효화

**CQ-21 ⚠ 지금 `invalidated`나 `suspect`인 단위 지식은 무엇인가.**
`?c agt:state ?s`. 어휘는 있다.

**CQ-22 ⚠ 같은 가정에 의존하는 단위 지식의 집합은 무엇인가.**
`?item agt:assumes :A`. 어휘는 있으나, 가정 데이터가 적으면 답이 의미가 없다(CQ-09).

**CQ-23 ❌ 무효로 표시된 뒤 재검토되지 않은 지식이 있는가.**
상태 전이 시각이 없다. `prov:generatedAtTime`은 생성 시각이고, 전이 이력은 남지 않는다.

## F. 역할과 가시성

**CQ-24 ✅ 이 역할은 무엇을 읽고 쓰는가, 그리고 읽을 지식 종류가 하나도 없는 역할이 있는가.**
`?r a agt:Role ; agt:reads ?p ; agt:writes ?w`.

**CQ-25 ✅ 동시에 활성화될 수 있는 에이전트 수가 ODD 한도 안인가.**
`SUM(?m) WHERE { ?r agt:maxConcurrent ?m }`를 `id:cond-concurrent-agents`와 비교한다.
**이 질의들(CQ-24와 CQ-25)이 아직 구현하지 않은 카탈로그 게이트의 자리를 채운다**
([`tools.md` §게이트 밖](tools.md#게이트-밖--규약으로-남은-것)).

## G. 일반화·교훈·결함

**CQ-26 ❌ 어떤 가정이 자주 깨지는가 / 같은 결함 요인이 몇 번 관측되었는가.**
실행 기록(`agt:Run`)과 `defect` 어휘가 없다. 이 질문의 답은 일반화 트리거의 입력이다.

**CQ-27 ❌ 이 교훈은 어디서 왔고 어느 규칙이 되었는가.**
`memory` 단위 지식과 승격 링크가 없다.

## H. 온톨로지 자기 점검

**CQ-28 ✅ 정의되었으나 한 번도 쓰이지 않은 개념이 있는가 (고립 개념).**
답에 나오는 상위 클래스와 shape는 고립의 신호가 아니다. 추론기가 없으면 상위 클래스의 인스턴스는 하위 클래스로만
나타나고, shape는 SHACL 엔진이 쓰므로 데이터에 나타나지 않기 때문이다.

**CQ-29 ✅ 한/영 라벨이나 정의가 빠진 용어가 있는가.**
`labels` 게이트가 이미 이를 강제한다.

**CQ-30 ❌ 순환 분류 계층이나 다의어, 클래스와 개체의 혼동이 있는가.**
상위 온톨로지 정렬과 추론기가 없어 검사할 수 없다
([`space/upper-ontology-alignment-space.md`](../space/upper-ontology-alignment-space.md)).

**CQ-35 ✅ 이 온톨로지 개념을 본문에서 쓰는 단위 지식은 무엇인가 (개념 검색).**
`agt:usesConcept`를 역방향으로 따라간다. 이 링크는 본문의 `agt:` 표기에서 추출한다. 질의는 `CQ-35.rq`이고, `--bind ?concept=agt:<용어>`로 개념을 묶는다.

## I. 프로파일

**CQ-36 ✅ 이 프로파일에서 각 지식 종류의 단위 지식은 무엇이고, 무엇이 그것을 판정하는가.**
`kb/ontology/profile/development/`의 실체 하위 클래스와 `agt:judgedBy` 바인딩을 묻는다. 행 하나는 지식 종류 클래스와 실체 클래스, 판정 도구의 조합이다.
질의는 `CQ-36.rq`다(2026-09-18).

**CQ-37 ✅ 살아 있는 결정 중 요구에 닿지 않는 것은 무엇인가 (기여 추적의 여집합).**
`refines`와 `serves`를 위로 따라가는 폐포(복합체 형제를 거친다)로도 살아 있는 요구에 닿지 않는 결정을 찾는다. 정의는
`tools/metrics.py`의 `reaches_req`와 같고, `deprecated`는 결정과 요구 양쪽에서 뺀다. 요구 `r-010`을 검증하는
`kb/vv/verifier/decision-names-requirement.md`가 이 질의로 판정한다. 질의는 `CQ-37.rq`이고(2026-09-21), 기대 행 수는
0이다.

**CQ-38 ✅ 서비스 층마다 단위 지식이 몇 개이고, 층을 명시하지 않은 단위 지식은 몇 개인가 — 층 할당 감사의 전체 수.**
`agt:inLayer`를 지식 종류별로 집계한다. 지식 층의 수는 층을 명시하지 않은 단위 지식 수의 **상한**이다. 명시가 없는
단위 지식에 `chunk2kg`가 기본값 `agt:knowledgeLayer`를 내므로, 지식 층을 명시한 할당과 기본값이 같은 트리플이 되기
때문이다. 질의는 `CQ-38.rq`다(2026-10-01).

## 노트 v3 CQ1~20 대응표

노트 2.7절의 역량 질문 20개와 이 문서의 CQ-01~CQ-32는 **번호도 내용도 다르다**. 노트는 어휘가 답해야 할 최소를
잡았고, 이 문서는 그 범위를 이 저장소의 완료 판정까지 넓혔다. 아래 표에서 **굵은 행은 이 문서에 없던 노트 질문**이다.

| 노트 | 질문 요지 | 이 문서 | 비고 |
|---|---|---|---|
| CQ1 | 이 코드는 어떤 결정을 충족하는가 | CQ-17 | |
| CQ2 | 결정의 가정과 그 참·거짓 | CQ-09·CQ-10 | |
| CQ3 | 배제된 대안과 이유 | CQ-14 | |
| CQ4 | 가정이 깨지면 무엇이 무효인가 | CQ-16·CQ-22 | |
| CQ5 | 이 에이전트가 지금 볼 수 있는 것 | CQ-01·CQ-11 | 작업 집합 질의 |
| CQ6 | 테스트 케이스가 ODD 안인가 밖인가 | CQ-12 | |
| CQ7 | satisfies나 verifies가 없는 지식 | CQ-17 | 추적 매트릭스 빈 칸 |
| CQ8 | 누가 언제 무엇을 근거로 | CQ-18·CQ-31 | |
| **CQ9** | **지난 프로젝트에서 같은 조건의 배제 선택** | 없음 | 프로젝트 사이의 일반화 — profile/ 이후 |
| CQ10 | 실행 기록의 결함 요인 | CQ-26 | |
| **CQ11** | **검증 지식 항목이 검증하는 logical 기준** | 없음 | V&V KB 내용이 생기면 추가한다 |
| **CQ12** | **필요하지만 적용 범위 밖인 지식** | 없음 | depends-on과 assumes 가운데 적용 범위 밖의 것 — 새로 등재해야 한다 |
| CQ13 | 같은 가정 의존 집합 | CQ-22 | |
| CQ14 | 무효화 후 미재검토 | CQ-23 | |
| CQ15 | 고립 개념 | CQ-28 | |
| **CQ16** | **결정을 담당하는 모듈 (allocates)** | 없음 | 어휘는 들어왔다(2026-09-10). 질의를 등재해야 한다 |
| CQ17 | 양립 불가 후보 중 남은 것 | CQ-15 | conflicts-with |
| CQ18 | 토큰 상한 초과가 잦은 지식 종류 | CQ-03 | 분포 관점만 더하면 된다 |
| CQ19 | executable까지 닿지 않은 요구 (정제 완주) | CQ-13 확장 | **v3의 완료 판정 축** |
| CQ20 | 요구로 거슬러 오르지 못하는 산출물 (후방 추적 귀속) | CQ-13 확장 | 〃 |

**등재해야 할 4건**(CQ9, CQ11, CQ12, CQ16)은 어휘나 데이터가 생길 때 이 문서의 해당 절로 들어온다. 그 연결은 새
개념을 추가할 때 어느 역량 질문에 기여하는지 적는 규칙(`tools/term_propose.py`의 `--cq`)이 유지한다.

---

## 커버리지 요약

| 그룹 | 질문 | ✅ | ⚠ | ❌ |
|---|---|---|---|---|
| A 구조와 조망 | 6 | 5 | — | 1(판정 불가) |
| B 경계 | 6 | 4 | 1 | 1 |
| C 정제 계층과 후보 | 3 | — | 3 | — |
| D 추적성 | 5 | 1 | 4 | — |
| D-1 신뢰 등급 | 2 | 2 | — | — |
| E 갱신과 무효화 | 3 | — | 2 | 1 |
| F 역할과 가시성 | 2 | 2 | — | — |
| G 일반화·교훈·결함 | 2 | — | — | 2 |
| H 자기 점검 | 3 | 2 | — | 1 |
| **합** | **32** | **16** | **10** | **6** |

이 표의 목적은 어휘 공백과 데이터 공백을 가르는 것이다. 2026-09-04에 `related/trace`를 추가하면서 ❌는 13건에서
6건으로 줄었다. 2026-09-07에는 신뢰 등급과 인용 추출을 더하면서 ✅가 13건에서 16건으로 늘었고, 이때 질문 2개를
추가했다. 지금 어휘가 막는 질문은 6건뿐이고, 나머지 10건은 **데이터**가 막는다.

**답하지 못하는 13건이 가리키는 어휘 공백은 넷뿐이다.**

| 공백 | 종류 | 막고 있는 질문 | 어디에 |
|---|---|---|---|
| CQ19와 CQ20 측정 | **도구화**(2026-09-10) — `bazel build //kg:metrics`의 전방 추적 커버리지와 후방 추적 커버리지 | CQ-19, CQ-20 | `tools/metrics.py` |
| ~~`related/trace`~~ | **해소**(2026-09-04, 어휘 29개) | CQ-13~20 | `kb/ontology/related/trace/` |
| ~~신뢰 등급~~ | **해소**(2026-09-07, 어휘 3개 + shape) | CQ-31·32 | `kb/ontology/related/trust/` |
| ~~인용 링크 데이터~~ | **해소**(2026-09-07, 링크 27개) | CQ-20 | `tools/extract_refs.py` |
| `satisfies`와 `refines`의 데이터 — 구축되지 않았다 | **데이터** | CQ-13, CQ-16, CQ-17, CQ-18의 답이 부분적이다 | [`method.md` §6](method.md#6-연결) · 읽기·쓰기 집합 기록 |
| `related/scene`·실행 기록·`defect` | 어휘 | CQ-12·26·27 | [`method.md` §11](method.md#11-검증--vv-kb로) |
| 상위 온톨로지 정렬·상태 전이 이력 | 어휘 | CQ-23·30 | [`space/upper-ontology-alignment-space.md`](../space/upper-ontology-alignment-space.md) |
| 라벨 대표성 판정 | 판정 불가 | CQ-06 | 지표로 관측 |

**다음 과제도 어휘가 아니라 데이터다.** `satisfies`와 `refines`는 편집의 부산물로만 생기므로, 하네스의 도구가 읽기
집합과 쓰기 집합을 기록해야 한다. 그다음 과제는 검증과 일반화의 어휘다(CQ-12, CQ-26, CQ-27).

## 실행

질의는 `bazel run //tools:query`로 돌리고, 등록한 질의 전체의 답은 `bazel build //kg:cq`가 낸다
([`tools.md` §활용 도구](tools.md#활용)). 그래프를 직접 물을 때는 다음처럼 손으로 돌린다.

```bash
python3 - <<'PY'
from rdflib import Graph
g = Graph()
for f in ['bazel-bin/kg/chunks-kg.ttl','kg/base-kg.ttl','kg/catalog-kg.ttl',
          'kg/composite-kg.ttl','bazel-bin/kb/odd/project-odd.ttl']:  # ODD TTL은 생성물 — 먼저 bazel build //kb/odd:odd
    g.parse(f)
P = 'PREFIX agt: <https://agentic-knowledge-base.dev/agt/> '
for row in g.query(P + 'SELECT ?p ?l (COUNT(?c) AS ?n) WHERE '
                       '{ ?c a ?p ; agt:hasLevel ?l } GROUP BY ?p ?l'):
    print(row)
PY
```

이 스크립트를 돌리기 전에 `bazel build //kg:chunks_kg`로 생성 그래프를 만든다.
