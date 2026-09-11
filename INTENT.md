# intent — 이 저장소의 요구 층 진입 문서

이 저장소가 **왜 존재하고 무엇을 요구받는가**의 진입점이다. 요구 항목 자체는
`kb/dev/requirement/`의 청크(`requirement` × functional, EARS)이고, 여기는 그
색인이다 — 그래프 밖이며, 세션 시작 시 `README.md`·`AGENTS.md`와 함께 읽는다.

## 궁극 목적

특정 분야에서 사업을 수행하는 업체가, 그 분야의 지식을 에이전트가 활용할 수
있는 형태로 축적하고, 프로젝트마다 그 지식 위에서 시스템을 만들고 운용한다.

이 저장소는 그 체계 자신이다 — 체계를 정의하는 온톨로지·방법론·도구를 담고,
자기 자신을 첫 사례로 그 체계로 관리한다.

## 두 핵심 문서

| 문서 | 자리 |
|---|---|
| [`docs/agent-knowledge-system-notes.md`](docs/agent-knowledge-system-notes.md) (v5, 3,470줄) | 요구의 **근거와 결정의 원천**. Part I·산출물 정의가 요구를 낳고, Parts 0~XIII의 `[확정]`이 결정으로 재도출된다 (v3 기준 145건 + v4·v5 델타 37건 + 2026-09-11 추가 3건 = 185건) |
| [`docs/agentic-knowledge-base-structure.md`](docs/agentic-knowledge-base-structure.md) (v5) | **운용 지도** — 두 KB·plane·수준·순환이 한눈에 |

요구는 이 두 문서를 `derives_from`으로 가리키고, 재도출된 결정이 요구를
`refines`한다. 전방 추적 커버리지(CQ19)·후방 추적 커버리지(CQ20)의 분자가 여기서 시작된다.

## 이해관계자와 관심사, 그리고 요구 33건

| 이해관계자 | 관심사 |
|---|---|
| **업체** | 분야 지식이 프로젝트를 넘어 축적·재사용된다 |
| **프로젝트** | ODD 안에서 요구가 산출물로 완주하고, 조건이 깨지면 무효 범위가 계산된다 |
| **에이전트** | 200줄 부분관측 안에서 판단할 수 있도록 관측이 재단되고 행동이 판정된다 |
| **검증자** | 만든 쪽과 판정하는 쪽이 구조적으로 분리된 채 모든 높이에 검증 대응물이 걸린다 |

### 업체 — 분야 지식의 축적과 재사용

- [`r-001`](kb/dev/requirement/) 분야 지식을 어휘로 축적한다 — `id:chunk/27699a04…`
- [`r-002`](kb/dev/requirement/) 프로젝트를 넘는 것은 어휘·공리·코어·교훈이다 — `id:chunk/d8e8aa97…`
- [`r-003`](kb/dev/requirement/) 청크는 프로젝트를 넘지 않는다 — `id:chunk/20148952…`
- [`r-004`](kb/dev/requirement/) 반복 관측을 어휘·규칙으로 승격한다 — `id:chunk/ae4f5c32…`

### 프로젝트 — ODD 안에서의 생산·운용 — 경계·완주·갱신

- [`r-005`](kb/dev/requirement/) 프로젝트의 운영 조건은 ODD 문서 하나다 — `id:chunk/fd0d3d18…`
- [`r-006`](kb/dev/requirement/) 모든 항목은 자기 가정을 명시한다 — `id:chunk/e5c0cbc6…`
- [`r-007`](kb/dev/requirement/) 조건이 깨지면 전수조사 없이 무효화한다 — `id:chunk/e0d0bf5c…`
- [`r-008`](kb/dev/requirement/) 모든 요구는 실산출물까지 내려간다 — `id:chunk/f4facde9…`
- [`r-009`](kb/dev/requirement/) 모든 산출물은 요구로 거슬러 오른다 — `id:chunk/f87ff3b1…`
- [`r-010`](kb/dev/requirement/) 결정은 기여하는 관심사를 명시한다 — `id:chunk/57a2dca5…`
- [`r-011`](kb/dev/requirement/) 근거 없는 할당은 불가능해야 한다 — `id:chunk/f715c53f…`
- [`r-012`](kb/dev/requirement/) 변경은 링크를 재판정 대상으로 만든다 — `id:chunk/33419d0a…`

### 에이전트 — 좁은 컨텍스트에서의 판단 — 관측·통제·일반화

- [`r-013`](kb/dev/requirement/) 라벨 목록이 본문보다 먼저다 — `id:chunk/f389ae99…`
- [`r-014`](kb/dev/requirement/) 최소 단위는 42줄 자립 청크다 — `id:chunk/166b54ec…`
- [`r-015`](kb/dev/requirement/) dispatch는 작업 집합만 전달한다 — `id:chunk/f29f5a66…`
- [`r-016`](kb/dev/requirement/) 편집은 게이트가 판정한다 — `id:chunk/f987e08c…`
- [`r-017`](kb/dev/requirement/) 어휘 밖 지식은 거부한다 — `id:chunk/0c3ad8ca…`
- [`r-018`](kb/dev/requirement/) 판정 방식이 다른 지식은 섞지 않는다 — `id:chunk/11e18898…`
- [`r-019`](kb/dev/requirement/) 하네스는 읽기·쓰기 집합을 기록한다 — `id:chunk/3b134d68…`
- [`r-020`](kb/dev/requirement/) 세션의 경험은 승격 규칙으로 남는다 — `id:chunk/875062b6…`

### 검증자 — 독립 판정과 완주

- [`r-021`](kb/dev/requirement/) 개발 KB와 V&V KB는 분리된다 — `id:chunk/42fde00d…`
- [`r-022`](kb/dev/requirement/) verifies의 주어는 V&V 청크뿐이다 — `id:chunk/2c574d24…`
- [`r-023`](kb/dev/requirement/) 검증 대응물 없이 다음 높이로 내려가지 않는다 — `id:chunk/71d2b786…`
- [`r-024`](kb/dev/requirement/) 기준 없는 verifies는 거부한다 — `id:chunk/63f17c2d…`
- [`r-025`](kb/dev/requirement/) 제품과 에이전트 둘 다 검증한다 — `id:chunk/5fa5f214…`
- [`r-026`](kb/dev/requirement/) 관측은 append-only 실행 기록이다 — `id:chunk/8117429b…`
- [`r-027`](kb/dev/requirement/context-budget.md) 작업 집합은 컨텍스트 예산 안에 든다 — `id:chunk/45f9ad28…` (v4·v5 델타 보충, 2026-09-10)
- [`r-028`](kb/dev/requirement/deterministic-notation.md) 명명과 표기는 결정론적이다 — `id:chunk/90fc2df7…` (v4·v5 델타 보충, 2026-09-10)
- [`r-029`](kb/dev/requirement/explicit-versioned-inputs.md) 입력은 명시되고 버전 관리된다 — `id:chunk/d48f87c5…` (v4·v5 델타 보충, 2026-09-10)
- [`r-030`](kb/dev/requirement/documents-are-generated.md) 문서는 저장하지 않고 생성한다 — `id:chunk/973f5595…` (v4·v5 델타 보충, 2026-09-10)
- [`r-031`](kb/dev/requirement/verification-means-trust.md) 검증 수단 자체의 신뢰도를 잰다 — `id:chunk/ee402e65…` (v4·v5 델타 보충, 2026-09-10)
- [`r-032`](kb/dev/requirement/audit-self-sufficiency.md) 감사는 체계의 출력만으로 성립한다 — `id:chunk/ba638521…` (v4·v5 델타 보충, 2026-09-10)
- [`r-033`](kb/dev/requirement/reproducible-runs.md) 실행은 같은 리비전과 seed에서 재현된다 — `id:chunk/2b1e5103…` (v4·v5 델타 보충, 2026-09-10)

## 요구를 고치려면

요구의 판정은 **이해관계자 합의**다. 항목 수정·추가는 유저 승인 사항이며
채널(`docs/feedback/`)을 경유한다. 요구가 바뀌면 그것을 `refines`하는 결정이
전부 재판정 대상이 된다 — 그것이 이 층을 최상위에 두는 이유다.
