---
from: hci
status: approved
targets: [docs/feedback/label-representativeness-sheet.md]
---

# 라벨 대표성 실험 — 정답지

**예측을 다 적기 전에는 열지 않는다.** 먼저 보면 실험이 무효가 된다 — 본문을 알고 나면 라벨이
대표하는지를 판단할 수 없기 때문이다(순응 편향).

기록지([`label-representativeness-sheet.md`](label-representativeness-sheet.md))의 번호와 여기 번호가 같다.
각 행의 "본문 요지"는 그 청크 본문의 **첫 문단 240자**다 — 전문이 필요하면 파일 경로로 연다.
예측과 대조해 적합 / 부분 / 부적합을 기록지에 적는다.

| # | 파일 | 본문 요지 (첫 문단, 240자) |
|---|---|---|
| 1 | `kb/dev/decision/p8-vv-plane-instances/alternatives.md` | **대안** — 시나리오·기준·verifier를 위해 새 plane을 만드는 안. 기각 — V&V KB는 코어의 두 번째 인스턴스다. 일곱 plane의 판정 방식은 같고 실체만 다르며, 시나리오는 `decision`, 기준은 `contract`에 정확히 맞는다 (8.2절). |
| 2 | `kb/dev/decision/p3-odd-maintenance/alternatives.md` | **대안** — **온톨로지에 없는 속성을 ODD에 바로 적는 안.** 배제 — ODD가 어휘 생성지가 되어 통제 어휘(0.0절)와 용어 제안 워크플로(2.5절)를 우회하고, 같은 개념이 프로젝트마다 다른 이름으로 굳는다. |
| 3 | `kb/dev/decision/p6-assumption-verification-methods/conclusion.md` | **결론** — 6.5절 "기계적으로 판정 가능한 형태"의 유형은 다섯이며 3.9절 판정 방법 등급과 짝을 이룬다. |
| 4 | `kb/dev/decision/p5-plane-by-verification/conclusion.md` | **결론** — 종류가 다른 지식을 하나의 컨텍스트에 섞지 않는다. 각 지식이 **"맞다"고 판정되는 메커니즘이 근본적으로 다르기** 때문이다. plane은 온톨로지 `entity/` 모듈의 최상위 분류에 대응하며, 일곱이다. |
| 5 | `kb/dev/decision/p8-risk-analysis-profile/conclusion.md` | **결론** — V&V KB의 프로파일(2.11절)은 **위험 분석**으로 만든다. 도메인의 열린 세계를 유한한 산출물로 구조화하는 절차이며, 프로젝트에 앞서 도메인당 한 번 수행하고 프로젝트마다 재사용한다 (노트 8.21절). |
| 6 | `kb/dev/decision/p10-standard-trace-queries/rationale.md` | **근거** (노트 9.7·9.13절) — 이 넷은 링크 모델의 역량 질문(2.7절)이다. 링크 타입과 카디널리티는 이 질의들이 답을 낼 수 있도록 고른 것이고, 답이 안 나오는 질의가 생기면 TIM에 빈 곳이 있다는 신호다. |
| 7 | `kb/dev/decision/p10-traceability-metrics/conclusion.md` | **결론** — 추적성은 다섯 지표로 관측하고, 각 지표에는 무엇을 경고하는지가 함께 정의된다. |
| 8 | `kb/dev/requirement/r-001-accumulate-domain-knowledge.md` | **요구** — 체계는 분야 지식을 에이전트가 활용할 수 있는 형태 — 공통 어휘(온톨로지)와 그 위의 항목 — 로 축적하여야 한다. |
| 9 | `kb/dev/decision/p9-constraint-sources-and-kinds/rationale.md` | **근거** (노트 9.3절) — 셋은 수명과 파급이 다르다. 공리를 고치면 온톨로지 전체의 링크가 재검토 대상이 되고, 제약을 완화하면 그 설계 공간의 후보 집합만 늘며, 가정이 깨지면 `assumes`를 타고 그 가정에 선 항목만 무효화된다 (6.5절). |
| 10 | `kb/dev/decision/p9-same-level-relations/rationale.md` | **근거** (노트 9.11절, 4.5절, 6.11절) — 어느 청크들이 한 복합체인가는 사람이 임의로 정하는 것이 아니라 후보 중 확정된 것이므로 후보·조건·증거 기록의 형식이 그대로 맞고, 4.5절의 7±2 상한이 후보 수 상한으로 재해석된다. 일반화가 증거 기록을 읽는 이유는 "같은 조건에서 K회 기각"이 곧 배제 반복(6.11절)이고, 그것을 공리화하는 것이 최약 전제조건(12.12절)의 일이기 때문이다 — 청크가 아니 |
| 11 | `kb/dev/decision/p4-composite-as-part-of/rationale.md` | **근거** (노트 4.5절) |
| 12 | `kb/dev/decision/p2-ontology-module-structure/conclusion.md` | **결론** — 온톨로지는 단일 파일이 아니라 **모듈로 나누고 최상위에서 import하여 합친다.** `project-ontology`는 import만 하는 얇은 최상위다. |
| 13 | `kb/dev/decision/p7-decision-spans-three-levels/rationale.md` | **근거** (노트 7.2절, 6.2절, 9.10절) — abstract는 변수의 선언이 온톨로지 어휘만 쓰는가로, logical은 후보에 범위·제약·배제 근거가 있는가로, concrete는 표본 근거와 배제 근거가 있는가로 판정된다 (6.8절 게이트). 판정이 다른 것을 한 청크에 두면 한 수준의 실패가 다른 수준을 `draft`로 끌어내린다. `refines`로 잇기 때문에 전방 추적 커버리지(7.1절)이 결정 안에서도 계 |
| 14 | `kb/dev/decision/p0-state-units-revision-workset/alternatives.md` | **대안** — **v1의 scene·situation·scenario 3분리는 폐기되었다.** 관측자 관점의 유무로 세 시간열 개체를 두던 안(scene = 시점 스냅샷, situation = 스코프로 거른 부분, scenario = scene의 시간열 + 행동 + 트리거)은 v3에서 쓰지 않는다. |
| 15 | `kb/dev/requirement/r-024-criteria-before-verifies.md` | **요구** — verifies 링크가 합격 기준 없이 저작되면, 체계는 그것을 거부하여야 한다. |
| 16 | `kb/dev/decision/p6-invalidation-propagation/alternatives.md` | **대안** — 무효화를 상위 plane으로도 전파하는 안. 기각 — 단방향 규칙이 없으면 전파가 순환한다. 6단계의 정지 조건(하위 plane으로만 반복)이 유계성을 만든다 (6.10절, 5.2절). |
| 17 | `kb/dev/decision/p3-odd-required-sections/conclusion.md` | **결론** — 파일명은 `project-odd`, 표기는 0.4절 명세 형식(mode / include / exclude / conditional)이다. 다음 절을 갖는다. |
| 18 | `kb/dev/decision/p8-three-directions-of-verification/rationale.md` | **근거** (노트 8.6절) — 세 번째가 빠지면 "통과했다"는 말이 공허하다. **아무것도 거르지 않는 기준도 통과하기 때문이다.** 에이전트는 통과하는 기준을 쓰는 쪽으로 치우치므로(1.2절), 기준의 질을 별도 방향으로 세우지 않으면 커버리지 수치만 오른다. |
| 19 | `kb/dev/requirement/audit-self-sufficiency.md` | **요구** — 체계는 감사 보고서와 온보딩이 체계 밖 정보(구두 설명, 별도 문서) 없이 생성되도록 하여야 한다. |
| 20 | `kb/dev/decision/p7-decision-supersession/conclusion.md` | **결론** — 결정의 대체는 `supersedes`다. 새 결정이 옛 결정을 가리키고, 옛 결정의 `satisfies` 링크가 전부 `suspect`가 된다 (10.11절). 옛 결정은 삭제되지 않고 `deprecated`로 남는다 (노트 7.4절). |
| 21 | `kb/dev/requirement/r-019-record-read-write-sets.md` | **요구** — 에이전트의 편집이 일어나면, 하네스는 읽기 집합과 쓰기 집합을 기록하여 링크를 편집의 부산물로 구축하여야 한다. |
| 22 | `kb/dev/decision/p2-tbox-abox-separation/conclusion.md` | **결론** — 온톨로지(개념 정의)와 지식그래프(개체)를 **다른 파일에 둔다.** 0.2절 접미사가 이를 강제한다. |
| 23 | `kb/dev/decision/p8-environment-assignment/rationale.md` | **근거** (노트 8.10절) — 요인 분류가 할당을 결정하므로 할당이 취향이 아니라 근거를 갖는다 (r-011). "이 검증은 통합 환경이 필요하다"는 주장은 그 검증이 겨냥하는 요인으로 증명된다. |
| 24 | `kb/dev/requirement/r-007-invalidate-without-survey.md` | **요구** — ODD 조건이 깨지면, 체계는 그 조건을 가정하는 모든 항목을 전수조사 없이 자동으로 무효화 표시하여야 한다. |
| 25 | `kb/dev/decision/p1-three-breaks-common-vocabulary/conclusion.md` | **결론** — 부분관측 행위자 여럿이 한 프로젝트를 만들면 세 곳에서 끊어진다: **정제**(의도→산출물), **일반화**(시행착오→개념), **갱신**(변경→상위 지식 반영). 세 단절의 공통 원인은 **공통 어휘의 부재**이므로, 이 체계는 어휘(Part II)에서 시작해 세 단절을 각각 정제 계층(Part VI)의 정제·일반화·무효화로 잇는다. |
| 26 | `kb/dev/decision/p7-dev-plane-substance/conclusion.md` | **결론** — 개발 프로파일(부록 D)에서 일곱 plane의 실체. 6.4절 수준 허용표를 개발 관점에서 다시 읽은 것이다 (노트 7.2절). |
| 27 | `kb/dev/decision/p5-verification-tools-per-plane/alternatives.md` | **대안** — 판정 도구가 없는 plane의 청크도 게이트를 통과시키는 안. 기각 — plane은 판정 방식으로 정의되므로 판정 도구가 없으면 그 plane의 청크는 검사될 수 없다 (5.4절). |
| 28 | `kb/dev/decision/p8-verification-and-validation/alternatives.md` | **대안** — 검증만 두고 평가(요구 자체가 맞는가)를 생략하는 안. 기각 — 틀린 요구를 완벽히 충족하는 시스템이 된다 (8.4절). |
| 29 | `kb/dev/decision/p7-dev-plane-substance/rationale.md` | **근거** (노트 7.2절, 5.1절, 6.4절) — plane은 판정 방식으로 정의되고(5.1절) 프로파일은 코어를 확장만 한다(2.11절). 그래서 개발 프로파일이 정하는 것은 새 plane이 아니라 각 plane의 **실체**(무엇이 그 plane의 청크인가), **단위**(42줄에 무엇 하나가 들어가는가), **판정 도구**(5.4절 — 도구 없는 plane은 게이트를 통과할 수 없다)다. 거주 수준은 6.4절 수준  |
| 30 | `kb/dev/decision/p8-odc-defect-subtypes/alternatives.md` | **대안** — 결함 하위 유형을 ODC 여덟 유형만으로 두는 안. 기각 — 인지·상호작용 갈래에는 ODC에 없는 에이전트 고유 유형(오독·누락·낡음·오인·채널)이 필요하다 (8.17절). |
