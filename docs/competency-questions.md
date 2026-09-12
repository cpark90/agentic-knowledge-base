# 역량 질문 — 온톨로지의 요구사항이자 완료 판정

**온톨로지가 답해야 하는 질문 목록이 그 온톨로지의 요구사항이다.** 각 질문은 그래프 질의
하나로 답할 수 있어야 하고, 답할 수 없으면 필요한 개념·속성·링크가 어휘에 없다는 뜻이다
([`id:chunk-d0052`](../chunks/decision/d-0052-competency-questions.md)).

## 쓰는 법

1. **새 개념·속성을 추가할 때 어느 질문에 기여하는지 적는다.** 어느 질문에도 기여하지
   않으면 과설계다 — 만들지 않는다.
2. **답할 수 없는 질문이 다음 어휘 확장의 근거다.** 개념을 먼저 늘리고 쓸 곳을 찾는 것이
   아니라, 답해야 할 질문이 어휘를 부른다.
3. **질문을 답할 수 없게 만드는 변경은 검토 대상이다** — 아래 상태가 ✅에서 ❌로 내려가는
   변경은 리뷰에 걸린다.
4. 답은 질의이므로 **저장하지 않는다**. 아래 실측값은 2026-09-04의 질의 결과이며, `query`
   도구가 생기면 이 표의 값은 생성물이 된다.

질문은 "누가 언제 묻는가"가 있어야 한다 — 실제로 묻지 않는 질문은 요구사항이 아니다.

## 상태 표기

| 표기 | 뜻 |
|---|---|
| ✅ | 지금 질의 하나로 답한다 (실측값 포함) |
| ⚠ | 답하지만 데이터가 비어 있거나 부분만 답한다 |
| ❌ | 어휘가 없어 질의를 쓸 수 없다 — 무엇이 없는지 적는다 |

---

## A. 구조와 조망

**CQ-01 ✅ 이 스코프 안에 무엇이 있는가 — 라벨 목록을 보여 달라.**
읽기의 기본 진입점. `?c a ?planeClass ; rdfs:label ?l`.
*실측: `decision`×`concrete` 153건. 다른 칸은 비어 있다.*

**CQ-02 ✅ 이 항목은 어느 칸에 있는가 (plane × level).**
`?c a ?plane ; agt:hasLevel ?level`. 격자 배치와 통계의 기초.
*실측: `DecisionChunk`×`concrete` 153 · `Composite`×`concrete` 38.*

**CQ-03 ✅ 42줄을 넘는 항목이 있는가.**
`?c agt:lineCount ?n FILTER(?n > 42)`. shape이 이미 막지만 분포는 질의로 본다.
*실측: 0건. 최빈 15줄·최대 22줄.*

**CQ-04 ✅ 어느 항목도 복합체에 속하지 않는가 (고아 후보).**
`?c a agt:Chunk FILTER NOT EXISTS { ?x agt:hasDirectPart ?c }`.
*실측: 0건. 단 복합체는 통합이 필요한 것만 만들므로(유저 결정) 이 값이 0이어야 하는 것은
아니다 — 링크가 생기면 "복합체에도 링크에도 걸리지 않은 것"으로 정의가 바뀐다.*

**CQ-05 ✅ 복합체의 직접 부분이 9개를 넘는가 / 부분의 plane·level이 전체와 다른가.**
`?k a agt:Composite ; agt:hasDirectPart ?p` 집계와 `?kl != ?pl` 비교.
*실측: 최대 8개, 이질 0건. 동질성은 shape이 아직 강제하지 않는다 — 이 질의가 대리 검사다.*

**CQ-06 ❌ 이 항목의 라벨이 본문을 대표하는가.**
판정 불가 — 기계가 답할 수 없는 질문이라 어휘로 풀 수 없다. 지표(라벨 대표성)로 관측한다
([`open-questions/evaluation-metrics.md`](open-questions/evaluation-metrics.md)).

## B. 경계 — ODD·가정·스코프

**CQ-07 ✅ 이 프로젝트는 무엇을 전제하는가 — ODD 조건과 판정 방법을 보여 달라.**
`?odd agt:hasCondition ?c . ?c agt:conditionValue ?v ; agt:checkMethod ?m ; agt:verificationGrade ?g`.
*실측: 조건 7(정적 4·환경 2·동적 1), 등급 A 5·B 2, 판정 방법 누락 0.*

**CQ-08 ✅ 아무도 참조하지 않는 ODD 조건이 있는가 (ODD 과대의 신호).**
가정도 스코프도 가리키지 않는 조건.
*실측: 1건 — `id:cond-network`. 조건 참조율 6/7.*

**CQ-09 ✅ 전제를 적지 않은 항목이 얼마나 되는가.**
`?c a agt:DecisionChunk FILTER NOT EXISTS { ?c agt:assumes ?a }`.
*실측: **152/153**. 가정이 사실상 안 쓰이고 있다 — 무효화 전파의 입력이 비어 있다는 뜻.*

**CQ-10 ✅ 이 가정은 어느 조건 위에 서 있는가 / 판정 방법은 무엇인가.**
`?a agt:refersTo ?cond ; agt:proposition ?p`.
*실측: 가정 1개(`id:asm-bazel-toolchain` → `cond-build-system`). 판정 유형·판정 식 속성은
아직 어휘에 없다 — d-0087이 요구하는 다섯 유형이 미구현.*

**CQ-11 ⚠ 이 스코프는 ODD의 어느 부분집합인가 — 이 역할이 볼 수 있는 조건은 무엇인가.**
`?s agt:subsetOf ?odd ; agt:includesCondition ?c`.
*실측: 스코프 5개 전부 `subsetOf` 보유, 참조 조건 6/7. 다만 "스코프 밖 의존"(어떤 항목이
스코프 밖 조건에 의존하는가)은 가정이 비어 있어 답이 무의미하다.*

**CQ-12 ❌ 이 시나리오는 ODD 범위 안인가.**
`agt:Scenario`와 `odd:outside` 태그 어휘가 없다. 검증 단계에서 필요해진다.

## C. 계층과 후보

**CQ-13 ⚠ 이 항목은 어느 상위에서 내려왔는가 — functional까지 거슬러 달라.**
`?c agt:refines+ ?anc`. 어휘는 갖춰졌으나 현재 항목이 전부 `concrete`라 답이 비어 있다.
*실측: 연쇄 0건. `functional`·`abstract`·`logical`·`executable` 개체가 한 번도 쓰이지 않았다.*

**CQ-14 ⚠ 이 변수의 후보는 무엇이고 무엇이 왜 배제되었는가.**
`?l a agt:Link ; agt:linkFrom :X ; agt:linkState ?st` — 후보와 배제(`invalid`)를 상태로 구분한다.
어휘는 있으나 **배제 사유**를 담을 자리가 아직 얇다(근거 종류만 있고 제약 자체는 없다).
*실측: 링크 개체 0건.*

**CQ-15 ⚠ 후보가 하나로 좁혀졌는가 / 후보가 0인 변수가 있는가(모순).**
`agt:linkState "candidate"` 집계. *실측: 후보 링크 0건 — 아직 아무것도 생성되지 않았다.*

## D. 추적성

**CQ-16 ⚠ X가 바뀌면 무엇이 영향받는가.** (영향 분석)
`?x agt:cites|agt:satisfies|agt:refines|agt:assumes ?target` 역방향 + plane 단방향 규칙 반복.
*실측: 인용 링크 27개로 **첫 답이 나온다** — 예: d-0002가 바뀌면 그것을 인용하는 항목이
영향 후보다. `satisfies`·`refines`는 여전히 0이라 답이 부분이다.*

**CQ-17 ⚠ 이 결정을 충족하는 산출물이 있는가 / `verifies`가 없는 인터페이스는 무엇인가.**
(커버리지 — 추적 매트릭스의 빈 칸)
`?d a agt:DecisionChunk FILTER NOT EXISTS { ?x agt:satisfies ?d }`.
*실측: **153/153** — 모든 결정이 매트릭스의 빈 칸이다.*

**CQ-18 ⚠ 이 코드는 왜 이렇게 됐는가.** (근거 추적)
`:x agt:refines+ ?anc` 로 상위 수준까지 거슬러 오른다. *실측: 연쇄 0건.*

**CQ-19 ⚠ 지금 `suspect`·`invalid`인 링크는 무엇인가.** (재판정 큐)
`?l a agt:Link ; agt:linkState ?s FILTER(?s IN ("suspect","invalid"))`.
*실측: 0건 — 링크 개체 자체가 없다.*

**CQ-20 ✅ 이 항목이 본문에서 인용하는 다른 항목은 무엇인가.**
`?a agt:cites ?b`. `tools/extract_refs.py`가 본문에서 뽑아 생성한다.
*실측: **항목 20개가 27개의 인용 링크**를 만들고 22개 항목이 인용받는다. 링크가 0이 아닌
첫 지표이며, 인용 대상이 실재하지 않으면 생성이 실패한다(참조 무결성).*

## D-1. 신뢰 등급

**CQ-31 ✅ 이 항목은 누가 만들었고 누가 검증했는가 — 사람이 검토한 항목은 얼마나 되는가.**
`?c agt:generatedBy ?g` · `?c agt:verifiedBy ?v FILTER(STRSTARTS(?v, "human:"))`.
*실측: 153개 전부 `claude/fable-5` 생성, **사람 검토 0건**. 유저 승인이 그래프에 기록된 적이
없다는 사실이 처음으로 질의로 드러난다.*

**CQ-32 ✅ 검증한 뒤에 내용이 바뀐 항목이 있는가.**
`prov:generatedAtTime > agt:verifiedAt` — shape이 이것을 FAIL로 막는다(`trust-shapes.ttl`).
*실측: 0건(검증 항목 자체가 없다). 음성 시험으로 게이트가 실제로 거부함을 확인했다.*

## E. 갱신과 무효화

**CQ-21 ⚠ 지금 `invalidated`·`suspect`인 항목은 무엇인가.**
`?c agt:state ?s`. 어휘는 있다.
*실측: 전부 `valid`(153). 상태 전이가 한 번도 일어나지 않았다 — 가정과 링크가 없어서다.*

**CQ-22 ⚠ 같은 가정에 의존하는 항목 집합은 무엇인가.**
`?item agt:assumes :A`. 어휘는 있으나 데이터가 1건뿐이라 답이 무의미하다(CQ-09).

**CQ-23 ❌ 무효로 표시된 뒤 재검토되지 않은 항목이 있는가.**
상태 전이 시각이 없다. `prov:generatedAtTime`은 생성 시각이고 전이 이력은 남지 않는다.

## F. 역할과 가시성

**CQ-24 ✅ 이 역할은 무엇을 읽고 쓰는가 / 읽을 plane이 하나도 없는 역할이 있는가.**
`?r a agt:Role ; agt:reads ?p ; agt:writes ?w`.
*실측: orchestrator 5 · developer 3 · vnv 2 · inspection 6 · hci 6. read plane 0인 역할 없음.
write는 orchestrator=decision · developer=artifact · vnv=annotation로 비겹침.*

**CQ-25 ✅ 동시에 활성화될 수 있는 에이전트 수가 ODD 한도 안인가.**
`SUM(?m) WHERE { ?r agt:maxConcurrent ?m }` vs `id:cond-concurrent-agents`.
*실측: 합 5, 한도 ≤ 5 — 경계에 걸쳐 있다. 역할을 하나라도 늘리면 이탈이다.*
**이 세 질의(CQ-24·25)가 곧 미구현 카탈로그 게이트다** —
[`tools.md` §게이트 밖](tools.md#게이트-밖--규약으로-남은-것).

## G. 일반화·교훈·결함

**CQ-26 ❌ 어떤 가정이 자주 깨지는가 / 같은 결함 요인이 몇 번 관측되었는가.**
실행 기록(`agt:Run`)과 `defect` 어휘가 없다. 일반화 트리거의 입력이다.

**CQ-27 ❌ 이 교훈은 어디서 왔고 어느 규칙이 되었는가.**
`memory` 항목과 승격 링크가 없다.

## H. 온톨로지 자기 점검

**CQ-28 ✅ 정의되었으나 한 번도 쓰이지 않은 개념이 있는가 (고립 개념).**
*실측: 정의된 `agt:` 용어 59개 중 데이터에서 쓰인 것 44개, 미사용 15개 —
`Chunk`·`KnowledgeItem`·`Condition`·`Level`·`ExecutionMode`(상위 클래스, 추론기 없이는
인스턴스가 하위 클래스로만 나타남), shape 5개(SHACL 엔진이 쓰므로 데이터에 안 나타남),
그리고 **`functional`·`abstract`·`logical`·`executable`** — 이 넷은 진짜 미사용이며 계층이
concrete 한 칸만 쓰고 있다는 증거다.*

**CQ-29 ✅ 한/영 라벨이나 정의가 빠진 용어가 있는가.**
`labels` 게이트가 이미 강제한다. *실측: 0건.*

**CQ-30 ❌ 순환 계층·다의어·클래스와 개체 혼동이 있는가.**
상위 온톨로지 정렬과 추론기가 없어 검사할 수 없다
([`open-questions/upper-ontology-alignment.md`](open-questions/upper-ontology-alignment.md)).

## 노트 v3 CQ1~20 대응표

노트 2.7절의 역량 질문 20개와 이 문서의 CQ-01~32는 **번호도 내용도 다르다** —
노트는 어휘가 답해야 할 최소를, 여기는 이 저장소의 완료 판정까지 넓혀 잡았다.
대응은 아래와 같고, **굵은 행이 이 문서에 없던 노트 질문**이다.

| 노트 | 질문 요지 | 이 문서 | 비고 |
|---|---|---|---|
| CQ1 | 이 코드는 어떤 결정을 충족하는가 | CQ-17 | |
| CQ2 | 결정의 가정과 그 참·거짓 | CQ-09·CQ-10 | |
| CQ3 | 배제된 대안과 이유 | CQ-14 | |
| CQ4 | 가정이 깨지면 무엇이 무효인가 | CQ-16·CQ-22 | |
| CQ5 | 이 에이전트가 지금 볼 수 있는 것 | CQ-01·CQ-11 | 작업 집합 질의 |
| CQ6 | 케이스가 ODD 안인가 밖인가 | CQ-12 | |
| CQ7 | satisfies·verifies 없는 항목 | CQ-17 | 추적 매트릭스 빈 칸 |
| CQ8 | 누가 언제 무엇을 근거로 | CQ-18·CQ-31 | |
| **CQ9** | **지난 프로젝트에서 같은 조건의 배제 선택** | 없음 | 프로젝트 간 일반화 — profile/ 이후 |
| CQ10 | 실행 기록의 결함 요인 | CQ-26 | |
| **CQ11** | **검증 청크가 검증하는 logical 기준** | 없음 | V&V KB 내용이 생기면 추가 |
| **CQ12** | **필요하지만 스코프 밖인 청크** | 없음 | depends-on·assumes 중 스코프 밖 — 신규 등재 필요 |
| CQ13 | 같은 가정 의존 집합 | CQ-22 | |
| CQ14 | 무효화 후 미재검토 | CQ-23 | |
| CQ15 | 고립 개념 | CQ-28 | |
| **CQ16** | **결정을 담당하는 모듈 (allocates)** | 없음 | 어휘는 들어옴(2026-09-10) — 질의 등재 필요 |
| CQ17 | 양립 불가 후보 중 남은 것 | CQ-15 | conflicts-with |
| CQ18 | 42줄 초과가 잦은 plane | CQ-03 | 분포 관점만 추가 필요 |
| CQ19 | executable까지 닿지 않은 요구 (정제 완주) | CQ-13 확장 | **v3의 완료 판정 축** |
| CQ20 | 요구로 거슬러 오르지 못하는 산출물 (후방 추적 귀속) | CQ-13 확장 | 〃 |

**등재 필요 4건**(CQ9·11·12·16)은 어휘·데이터가 생기는 시점에 이 문서의 해당
절로 들어온다 — 새 개념을 추가할 때 어느 역량 질문에 기여하는지 적는 규칙
(`tools/term_propose.py`의 `--cq`)이 그 연결을 유지한다.

---

## 커버리지 요약

| 그룹 | 질문 | ✅ | ⚠ | ❌ |
|---|---|---|---|---|
| A 구조와 조망 | 6 | 5 | — | 1(판정 불가) |
| B 경계 | 6 | 4 | 1 | 1 |
| C 계층과 후보 | 3 | — | 3 | — |
| D 추적성 | 5 | 1 | 4 | — |
| D-1 신뢰 등급 | 2 | 2 | — | — |
| E 갱신과 무효화 | 3 | — | 2 | 1 |
| F 역할과 가시성 | 2 | 2 | — | — |
| G 일반화·교훈·결함 | 2 | — | — | 2 |
| H 자기 점검 | 3 | 2 | — | 1 |
| **합** | **32** | **16** | **10** | **6** |

**추이**: 2026-09-04 `related/trace` 추가로 ❌ 13 → 6. 2026-09-07 신뢰 등급과 인용 추출로
✅ 13 → 16(질문 2개 추가). 어휘가 막는 것은 6건뿐이고 나머지 10건은 **데이터**가 막는다 —
어휘 공백과 데이터 공백을 가르는 것이 이 표의 목적이다.

**답하지 못하는 13건이 가리키는 어휘 공백은 넷뿐이다.**

| 공백 | 종류 | 막고 있는 질문 | 어디에 |
|---|---|---|---|
| CQ19·CQ20 측정 | **도구화**(2026-09-10) — `bazel build //kg:metrics`의 전방 추적 커버리지·후방 추적 커버리지 | CQ-19·20 | `tools/metrics.py` |
| ~~`related/trace`~~ | **해소**(2026-09-04, 어휘 29개) | CQ-13~20 | `kb/ontology/related/trace/` |
| ~~신뢰 등급~~ | **해소**(2026-09-07, 어휘 3개 + shape) | CQ-31·32 | `kb/ontology/related/trust/` |
| ~~인용 링크 데이터~~ | **해소**(2026-09-07, 링크 27개) | CQ-20 | `tools/extract_refs.py` |
| `satisfies`·`refines` 데이터 — 구축이 안 됨 | **데이터** | CQ-13·16·17·18의 답이 부분 | [`method.md` §6](method.md#6-연결) · 읽기·쓰기 집합 기록 |
| `related/scene`·실행 기록·`defect` | 어휘 | CQ-12·26·27 | [`method.md` §11](method.md#11-검증--vv-층으로) |
| 상위 온톨로지 정렬·상태 전이 이력 | 어휘 | CQ-23·30 | [`open-questions/`](open-questions/) |
| 라벨 대표성 판정 | 판정 불가 | CQ-06 | 지표로 관측 |

**다음도 어휘가 아니라 데이터다** — `satisfies`·`refines`는 편집의 부산물로만 생기므로
하네스가 읽기·쓰기 집합을 기록해야 한다. 그다음이 검증·일반화 어휘(CQ-12·26·27).
`roadmap.md`의 "다음 산출"이 이 순서를 따른다.

## 실행

지금은 손으로 돌린다. `query` 도구가 생기면 이 목록이 그 도구의 입력이 되고, 상태 표가
생성물이 된다 ([`tools.md` §활용 도구](tools.md#활용-첫-형태-5)).

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

`bazel build //kg:chunks_kg` 를 먼저 돌려 생성 그래프를 만든다.
