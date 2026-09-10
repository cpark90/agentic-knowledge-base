---
from: hci
status: open
targets: [../rules.md, ../ontology.md, ontology/entity/knowledge-item/, ontology/shapes/chunk-shapes.ttl, tools/chunk2kg.py, tools/chunk_lint.py, https://agentic-knowledge-base.dev/id/chunk-d0002, https://agentic-knowledge-base.dev/id/chunk-d0071, https://agentic-knowledge-base.dev/id/chunk-d0076, https://agentic-knowledge-base.dev/id/chunk-d0077, https://agentic-knowledge-base.dev/id/chunk-d0087]
---

# 온톨로지·ODD·kg 항목을 격자 위에 올릴 때의 plane·level 배정

유저 결정 둘이 이미 내려져 있고 문서에는 반영됐다. 남은 것은 **그 결정을 지식 산출물에
적용할 때 정해야 하는 배정**이다 — 이 항목은 그 결정 요청이다.

## 질문
"chunk는 온톨로지가 말하는 의미로만 쓴다"(2026-09-02)와 "ontology·odd·space·kg·functional
항목도 청크·구성체 형태"(2026-09-02)를 지식 산출물에 적용하려면, 온톨로지 개념·shape·ODD
조건·가정에 **plane과 level을 부여**해야 한다. 청크는 정확히 하나의 plane과 하나의 level을
갖기 때문이다. 그런데 이들은 지금까지 "축 위에 없는 기반"으로 취급되어 왔고, 어느 plane에
넣을지가 자명하지 않다 — plane은 **판정 방식**으로 나뉘는데 개념 정의의 판정은 위생 검사,
조건의 판정은 `checkMethod` 실행이라 서로 다르다.

어려운 이유가 하나 더 있다: 배정이 끝나면 **파일을 쪼개야 한다.** 지금은 한 파일에 개념이
여러 개(`plane-ontology.ttl`에 6개), ODD 한 파일에 조건 7개가 들어 있다.

## 이미 정해진 것
- chunk는 포맷이 아니라 구조 규율이고 온톨로지·ODD·kg에도 적용된다. 지식의 종류는 고유
  용어로 부른다 — [`../rules.md` §1](../rules.md#1-chunk--자립적-최소-지식-단위).
- 구성체는 통합이 필요한 것만. 개별 운영이 기본 — [`../rules.md` §2](../rules.md#2-구성체--통합이-필요한-것만).
- plane은 판정 방식으로 나뉜 종류, level은 5단 — [`../rules.md` §3·§5](../rules.md#3-plane--판정-방식으로-나뉜-종류).
- 한 청크 = 한 파일, 42줄 — 온톨로지 파일도 이미 42줄 린트를 받는다.
- 모든 지식 항목은 청크이거나 청크의 구성체다 (d-0076).

## 현재 상태
| 산출물 | 파일 | 청크 요건 충족 | 미충족 |
|---|---|---|---|
| 온톨로지 개념 53개 | 13 파일 | 42줄 · 한 파일 한 주제 | IRI로서의 항목 없음, plane·level·state 없음 |
| shape 5개 | 5 파일 | 42줄 | 같음 |
| ODD 조건 7개 | 1 파일 | — | 파일 분할 필요, plane·level 없음 |
| 가정 1개 | `base-kg.ttl` 공유 | — | `agt:Assumption`은 `KnowledgeItem` 하위가 아니다 |
| 결정 153개 | 153 파일 | **전부 충족** | — |

## 답이 가르는 것
배정이 정해지면 격자의 빈 칸이 채워지고(현재 `decision`×`concrete` 한 칸), 온톨로지·ODD
항목이 링크의 끝이 될 수 있게 된다 — 특히 "개념 정의 → 그 개념을 쓰는 항목"(`usesConcept`)
링크는 개념이 항목이어야 성립한다. 정하지 않으면 그 링크를 만들 수 없다.

## 선택지
배정안 셋. 어느 것이든 파일 분할과 `chunk2kg`의 TTL head 파싱(주석 헤더)이 따라온다.

| # | 온톨로지 개념 | shape | ODD 조건 | 가정 | 성격 |
|---|---|---|---|---|---|
| **A** | `schema` × `functional` | `schema` × `concrete` | `contract` × `concrete` | `contract` × `concrete` | 판정 방식으로 가름 — 개념 정의의 판정은 스키마 위생, 조건은 형식 검사. functional 칸이 처음 채워진다 |
| **B** | 전부 `schema` × `concrete` | 같음 | 같음 | 같음 | 단순. 그러나 "어휘의 서술적 사용 = functional"(d-0027)과 어긋난다 |
| **C** | 배정하지 않는다 | — | — | — | 기반은 격자 밖으로 유지. 유저 결정 1을 파일 수준(42줄)으로만 해석하는 안 |

**부속 결정 둘**
1. **코드 항목의 단위** — "한 청크 = 한 파일"을 코드에도 적용하면 함수 하나가 파일 하나다.
   심볼 앵커(d-0077·d-0079)를 유지하면 한 파일에 여러 항목이 된다. 어느 쪽인가?
2. **온톨로지 클래스 이름** — `agt:DecisionChunk` 등을 그대로 둘지(구조 타입의 이름이므로
   유지 권고), 종류 클래스를 하위로 따로 둘지(`agt:Decision ⊑ agt:DecisionChunk`).

## 답
(유저가 채움)
