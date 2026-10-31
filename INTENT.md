# intent — 이 저장소의 요구 진입 문서

이 문서는 이 저장소가 **왜 존재하고 무엇을 요구받는가**를 찾는 진입점이고, 요구 항목의 색인이다. 요구 항목 자체는
`kb/dev/requirement/`의 단위 지식이다. 그 단위 지식의 지식 종류는 `requirement`이고 정제 수준은 functional이며, 문장은 EARS 꼴로 쓴다.
이 문서는 그래프 밖에 있고, 세션을 시작할 때 `README.md`, `AGENTS.md`와 함께 읽는다.

## 궁극 목적

이 체계는 한 분야의 업체가 자기 분야의 지식을 확률적 지식 모델로 쌓고, 그 지식으로 프로젝트마다
시스템을 만들 수 있게 하려고 있다.

특정 분야에서 사업을 하는 업체는 그 분야의 지식을 에이전트가 쓸 수 있는 형태로 쌓는다. 쌓은 지식은
확률적 지식 모델, 곧 "지식을 확률 구조적으로 모델링한 결과물"이다. 추적 링크와 결정 후보는 증거에서 계산한
믿음 정도를 갖고, 질의의 답은 그 믿음 정도에서 유도한 분포로 나온다. 그리고 프로젝트마다 ODD를 정하고
이 지식을 바탕으로 시스템을 만들고 운용한다.

여기서 모델은 "학습 기반 방법에서의 주요요소인 모델"을 뜻하지 않는다(유저 2026-10-24). 지식 베이스는 어떤
모델의 학습 데이터가 아니라 그 자체가 확률적 지식 모델이다.

다만 어떤 지식을 확정할지는 믿음 정도가 정하지 않는다. 그 권한은 지식 베이스의 규칙과 게이트에 있다.

2026-10-22에 유저는 이 목적을 다음과 같이 말했다. "위키가 타뷸러 방식의 모델이라하면 딥러닝기반
방식으로 확률적인 지식의 모델링을 하는것이 목적이야." 곧 지금의 지식 베이스는 표 형식이고,
확률적 지식 모델이 목표다(Q87-b, Q89-a). 2026-10-24에 유저는 그 모델의 뜻을 다음과 같이
정했다. "확률적 지식 모델에서 모델이라는 말은 지식을 확률 구조적으로 모델링한 결과물이라는 의미에서
모델이지. 학습 기반 방법에서의 주요요소인 모델을 뜻하는 것이 아님."(Q-0063 Q153) 지식 베이스 자체를 어디까지 확률화하는지는
r-011의 개정이 정했다. 믿음 정도는 링크와 후보 곁에 함께 적고 선호가 동률일 때 순서를 가르지만, 확정과 기각,
상태 전이에는 쓰지 않는다(Q90-a, Q109-b).

이 저장소는 그 체계 자신이다. 저장소는 체계를 정의하는 온톨로지와 방법론, 도구를 담고,
자기 자신을 첫 사례로 삼아 그 체계로 관리된다.

## 두 핵심 문서

| 문서 | 자리 |
|---|---|
| [`docs/agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md) (v5) | 요구의 **근거이자 결정의 원천**이다. Part I과 산출물 정의가 요구를 낳고, Parts 0~XIII의 `[확정]`이 결정으로 재도출된다. 재도출된 결정의 수와 확정 문장의 커버리지는 생성 뷰 `bazel build //kg:metrics`의 "세 축 대리" 절이 낸다 |
| [`docs/agentic-knowledge-base-structure.md`](docs/agentic-knowledge-base-structure.md) (v5) | **운용 지도**다. 두 KB와 지식 종류, 정제 수준, 순환을 한눈에 보여 준다 |

요구는 이 두 문서를 `derives_from`으로 가리키고, 재도출된 결정이 요구를
`refines`한다. 전방 추적 커버리지인 CQ19와 후방 추적 커버리지인 CQ20의 분자는 이 연결에서 시작된다.

## 이해관계자와 관심사, 그리고 요구

요구의 IRI와 EARS 패턴, 정제하는 결정 수, 정제 도달 수준은 생성 뷰가 낸다. 생성 명령은 `bazel build //kb/dev:requirements`이고,
결과는 `bazel-bin/kb/dev/requirements.md`에 생긴다. 문서는 저장하지 않고 생성한다는 요구 `documents-are-generated`를 따르기 때문이다.
아래에는 이해관계자별 묶음만 둔다. 어느 요구가 어느 묶음에 드는지는 손으로 정했다.

| 이해관계자 | 관심사 |
|---|---|
| **업체** | 분야 지식이 프로젝트를 넘어 축적되고 재사용된다 |
| **프로젝트** | ODD 안에서 요구가 산출물로 완주하고, 조건이 깨지면 무효 범위가 계산된다 |
| **에이전트** | 200줄을 환산한 5,418토큰의 부분관측 안에서 판단할 수 있도록 관측이 재단되고 행동이 판정된다 |
| **검증자** | 만든 쪽과 판정하는 쪽이 구조적으로 분리된 채 모든 높이에 검증 대응물이 걸린다 |

### 업체 — 분야 지식의 축적과 재사용

- [`r-001`](kb/dev/requirement/) 분야 지식을 어휘로 축적한다
- [`r-002`](kb/dev/requirement/) 프로젝트를 넘는 것은 어휘·공리·코어·교훈이다
- [`r-003`](kb/dev/requirement/) 지식은 프로젝트를 넘지 않는다
- [`r-004`](kb/dev/requirement/) 반복 관측을 어휘·규칙으로 승격한다
- [`r-030`](kb/dev/requirement/r-030-export-settled-knowledge-for-models.md) 폐기(deprecated). 별도의 학습 모델을 전제로 한 요구였다(Q-0063 Q156-b)
- [`r-031`](kb/dev/requirement/r-031-check-model-output-against-settled-knowledge.md) 폐기(deprecated). 별도의 학습 모델을 전제로 한 요구였다(Q-0063 Q156-b)
- [`r-032`](kb/dev/requirement/r-032-links-and-candidates-carry-degree-of-belief.md) 링크와 결정 후보는 증거에서 계산한 믿음 정도를 가질 수 있어야 한다 (draft)

### 프로젝트 — ODD 안에서의 생산과 운용: 경계, 완주, 갱신

- [`r-005`](kb/dev/requirement/) 프로젝트의 운영 조건은 ODD 문서 하나다
- [`r-006`](kb/dev/requirement/) 모든 항목은 자기 가정을 명시한다
- [`r-007`](kb/dev/requirement/) 조건이 깨지면 전수조사 없이 무효화한다
- [`r-008`](kb/dev/requirement/) 모든 요구는 실산출물까지 내려간다
- [`r-009`](kb/dev/requirement/) 모든 산출물은 요구로 거슬러 오른다
- [`r-010`](kb/dev/requirement/) 결정은 기여하는 관심사를 명시한다
- [`r-011`](kb/dev/requirement/) 근거 없는 할당은 불가능해야 한다
- [`r-012`](kb/dev/requirement/) 변경은 링크를 재검증 대상으로 만든다

### 에이전트 — 좁은 컨텍스트에서의 판단: 관측, 통제, 일반화

- [`r-013`](kb/dev/requirement/) 라벨 목록이 본문보다 먼저다
- [`r-014`](kb/dev/requirement/) 최소 단위는 42의 배수 토큰 상한의 자립 단위 지식이다
- [`r-015`](kb/dev/requirement/) dispatch는 작업 집합만 전달한다
- [`r-016`](kb/dev/requirement/) 편집은 게이트가 판정한다
- [`r-017`](kb/dev/requirement/) 어휘 밖 지식은 거부한다
- [`r-018`](kb/dev/requirement/) 판정 방식이 다른 지식은 섞지 않는다
- [`r-019`](kb/dev/requirement/) 에이전트는 하네스의 도구로 읽기·쓰기 집합을 기록한다
- [`r-020`](kb/dev/requirement/) 세션의 경험은 승격 규칙으로 남는다

### 검증자 — 독립 판정과 완주

- [`r-021`](kb/dev/requirement/) 개발 KB와 V&V KB는 분리된다
- [`r-022`](kb/dev/requirement/) verifies의 주어는 V&V 단위 지식뿐이다
- [`r-023`](kb/dev/requirement/) 검증 대응물 없이 다음 높이로 내려가지 않는다
- [`r-024`](kb/dev/requirement/) 기준 없는 verifies는 거부한다
- [`r-025`](kb/dev/requirement/) 제품과 에이전트 둘 다 검증한다
- [`r-026`](kb/dev/requirement/) 관측은 append-only 실행 기록이다
- [`r-027`](kb/dev/requirement/r-027-generated-documents-carry-provenance.md) 생성 문서는 자기 출처와 재현 수단을 담아야 한다
- [`r-028`](kb/dev/requirement/r-028-generated-documents-share-one-form.md) 생성 문서의 서식은 하나의 규약을 따라야 한다
- [`r-029`](kb/dev/requirement/r-029-harness-self-improvement.md) 저장소의 지식이 진전하면 하네스는 스스로 개선된다

### 번호 없는 요구

아래는 파일 이름에 번호가 없는 요구다. 이 색인은 예전에 이 요구들에 r-027~r-033을 붙였다. 그러나 그 번호가 번호 붙은
r-027~r-029 파일과 겹쳤으므로, 2026-10-22 정리에서 번호를 떼고 파일 이름으로 부르기로 했다.

- [`context-budget`](kb/dev/requirement/context-budget.md) 작업 집합은 컨텍스트 예산 안에 든다
- [`deterministic-notation`](kb/dev/requirement/deterministic-notation.md) 명명과 표기는 결정론적이다
- [`explicit-versioned-inputs`](kb/dev/requirement/explicit-versioned-inputs.md) 입력은 명시되고 버전 관리된다
- [`documents-are-generated`](kb/dev/requirement/documents-are-generated.md) 문서는 저장하지 않고 생성한다
- [`verification-means-trust`](kb/dev/requirement/verification-means-trust.md) 검증 수단 자체의 신뢰도를 잰다
- [`audit-self-sufficiency`](kb/dev/requirement/audit-self-sufficiency.md) 감사는 체계의 출력만으로 성립한다
- [`reproducible-runs`](kb/dev/requirement/reproducible-runs.md) 실행은 같은 리비전과 seed에서 재현된다

## 요구를 고치려면

요구의 판정 방식은 **이해관계자 합의**다. 그래서 요구 항목의 수정과 추가는 유저 승인 사항이며,
`harness/user/`의 질문지를 거친다. 요구가 바뀌면 그 요구를 `refines`하는 결정이
전부 재검증 대상이 된다. 이 파급이 요구를 최상위에 두는 이유다.
