---
from: orchestrator
kind: question
status: open
targets: [kb/dev/decision/p4-composite-order-is-declared/, tools/chunk2kg.py, tools/gen_build.py, kb/ontology/shapes/composite-order-shapes.ttl, kb/vv/scenario/]
---

# 복합체 순서의 선언과 시나리오 세 청크 — 결정 하나의 승인을 구한다 (2026-09-29)

승인 handoff 여섯을 반영한 뒤, 오늘 두 번 드러난 구조 공백 둘을 닫았다. 둘 다 **이미 있는 규칙을 도구가 표현하지 못하던** 자리이고 새 규칙이 아니다. 하나는 결정 하나를 새로 저작했으므로 승인을 구한다.

## 닫은 것

| 공백 | 규칙의 원본 | 도구 반영 |
|---|---|---|
| 시나리오가 세 청크 복합체(자극·요인·배제 자극)로 서지 못했다 | `p8-scenario-authoring`(2026-09-10, stable) | `kb/vv/scenario/<슬러그>-{stimulus,factors,excluded}.md`, 표지 **자극**·**요인**·**배제 자극**이 결정의 세 슬롯에 사상(게이트 `decision-role`·shape). 단일 청크는 이행 기간 동안 통과. vnv가 부류 셋을 다시 쓰는 중 |
| `co:List` 순서를 아무것도 방출하지 않았다 | d-0073(deprecated)·`docs/rules.md` §2 "순서가 뜻을 갖는 복합체만 `co:List`" | 선언 청크의 `composite.ordered: [<부분 IRI>…]`가 있을 때만 `co:List`·`co:index` 방출, 결정 복합체는 역할 고정 순서, 시나리오는 `ordered` 필수. shape `composite-order-shapes`(첫 `sh:sparql`) |

## 승인을 구하는 결정

[`p4-composite-order-is-declared`](../../kb/dev/decision/p4-composite-order-is-declared/conclusion.md) — **순서의 원본은 선언이고 선언된 것만 방출한다.** 옛 규칙("순서가 뜻을 갖는 것만")에 "뜻을 갖는지는 저작자만 알므로 선언으로 표시한다"를 더한 것이다. 결정 복합체(결론·근거·대안)만 선언 없이 고정 순서를 낸다 — 역할이 곧 순서이고 205개에 같은 목록을 반복하는 것은 첨가다. 대안 셋(파일명 순서·전 복합체 순서·별도 순서 파일) 기각. `status: draft`로 두었다 — `stable` 전이는 사람의 승인이다.

판단이 갈릴 수 있는 자리 하나: 결정 복합체의 고정 순서. "순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보"라는 규칙에서 결정이 순서를 요구하는가는 읽기 순서(결론 → 근거 → 대안, ADR 뷰가 그 순서로 조립)로 판단했다. 다르게 보면 결정도 `ordered` 선언으로 돌린다 — 도구 한 줄이다.

## 함께 끝난 것

G16(목표 표기 통일성)은 게이트로 올랐다(오탐 0·위반 1 수정). G17(시점 의존 표현)은 후보 7/7 오탐이라 권장으로 남고 검사가 후보만 낸다.

## hci에 전달

유저 질문 하나 — 결정 `p4-composite-order-is-declared` 승인 여부(승인이면 `status: stable`로 올리고 `verified`를 붙인다). 원장에 "복합체 순서 = 선언(`ordered`), 시나리오 = 세 청크 복합체(2026-09-29)" 한 줄.
