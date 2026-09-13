# docs/ — 이 체계의 문서

**그래프 밖**이다. 검사 게이트의 통제 어휘·shape 검사 대상이 아니다. 여기 있는 것은 지식이
아니라 지식을 만드는 체계의 서술이다. 문서는 결정을 **복사하지 않고 인용한다**. 복사하면
이중 관리가 되고, 둘이 어긋나는 순간 어느 쪽이 원본인지 알 수 없어진다.

## 설계 원본

| 문서 | 다루는 것 |
|---|---|
| [`agent-knowledge-system-notes.md`](agent-knowledge-system-notes.md) | **노트 v5** — 이 체계의 설계 원본 (3,470줄, Part 0~XVII + 부록 A~E). `[확정]`은 결정으로 재도출되어 `kb/dev/decision/`에 있다 (v3 145건 + v4·v5 델타 37건 = 182건) |
| [`agentic-knowledge-base-structure.md`](agentic-knowledge-base-structure.md) | **운용 지도** — 노트를 실제 운용 관점에서 재배열한 구조도 |

본문의 `(노트 N.N절)` 인용은 전부 이 노트 **v5**의 절 번호다. 2026-09-10의 v3→v5 동기화에서
Part VII이 신설되어 옛 VII 이후가 한 칸 밀렸다.

## 목적

| 문서 | 다루는 것 |
|---|---|
| [`purpose.md`](purpose.md) | **먼저 읽는다.** 궁극 목적, 대상 지식과 순환, 두 KB, 이 저장소가 만드는 것 |
| [`../INTENT.md`](../INTENT.md) | 요구 층 진입 문서 — 이해관계자·관심사·요구 33건 인덱스 (루트) |

## 산출물

| 문서 | 다루는 것 |
|---|---|
| [`ontology.md`](ontology.md) | 코어와 분야 프로파일, 확장 규칙 — 코어 / development / V&V 세 층 |
| [`competency-questions.md`](competency-questions.md) | 온톨로지가 답해야 하는 질문과 현재 답할 수 있는 것 (노트 CQ1~20 대응표 포함) |
| [`rules.md`](rules.md) | 무엇이 유효한 구조인가 — 코어(chunk · 복합체 · plane · traceability · KG) / development / V&V |
| [`method.md`](method.md) | 운용 순서·완료 판정(§0)과 각 단계를 어떻게 하는가 — 코어 12절차 / development 저작 흐름 / V&V 위험 분석~되먹임 |
| [`tools.md`](tools.md) | **게이트 총람(원본)**, 코어 검사·활용 도구 / development / V&V 도구, Bazel 배선, 게이트 밖 규약 |

## 진행과 기록

| 문서 | 다루는 것 |
|---|---|
| [`roadmap.md`](roadmap.md) | 도입 8단계에서의 현재 위치와 다음 산출, 실측 |
| [`risks-and-tensions.md`](risks-and-tensions.md) | 체계가 실패하는 방식과 대응, 서로 당기는 힘의 균형점 |
| [`open-questions.md`](open-questions.md) | 미해결 질문 인덱스 — 노트 Part XVII 30건 + 이 저장소의 관찰 (항목 본문은 `open-questions/`) |
| [`references.md`](references.md) | 어느 구조를 어느 표준에서 가져왔는가 |
| [`glossary.md`](glossary.md) | **용어집** — 산문 한글 용어의 원본(표준 용어·영문·옛 표기·출처) |
| [`decomposition-audit.md`](decomposition-audit.md) | 노트·참조 저장소에서 지식이 어디로 갔는가와 감사의 발견 (상세 이력은 git) |

## 소통 채널

[`feedback/`](feedback/README.md)는 유저 피드백 채널이다. hci 에이전트가 담당하며, 유저와 직접
상세 소통하는 유일한 창구다. 3-lane 구조와 승인 게이트는 그 안의 `README.md`가 원본이다.
세 lane은 유저↔hci, 타 에이전트→hci, hci→조사이고, 승인 게이트의 `status: approved`는 유저만
붙인다. 유저 결정의 원문 기록은 [`feedback/purpose-statement.md`](feedback/purpose-statement.md)와
[`feedback/design-detail-review.md`](feedback/design-detail-review.md)에 있다.

## 다른 문서와의 관계

| 문서 | 위치 | 성격 |
|---|---|---|
| `README.md` | 루트 | 저장소 소개 — 세 산출물·구조·명령 |
| `AGENTS.md` | 루트 | 에이전트 하네스 — 역할·권한·소통·커밋 |
| `STYLEGUIDE.md` | 루트 | 컴포넌트별 저작 스타일 — `[지킴]`/`[권장]` |
| `INTENT.md` | 루트 | 요구 층 진입 — 궁극 목적과 요구 인덱스 |
| `docs/*.md` | 여기 | **체계 자체** — 목적·순서·어휘·규칙·방법·도구 |
