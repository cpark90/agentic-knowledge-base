---
id: https://agentic-knowledge-base.dev/id/chunk/a0314be9-c9ef-4b83-a8fe-da7520a85fe4
type: decision
level: logical
title_ko: 스코프와 수준 창은 볼 자격을 거를 뿐 양을 거르지 못한다
title: Scope and level window filter entitlement, not quantity
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-12T00:50:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/0e7f41dc-e010-4c71-809f-51535f17e6ce
---
**근거** (이 저장소 실측 2026-09-11; 노트 0.5절·1.1절·5.6절; LEDGER §3.2, LARGER §4.1) — 스코프 × 수준 창만으로 만든 developer 작업 집합은 라벨 목록만 573줄(수준 창 concrete로 209줄)로 예산 200줄의 세 배였고, 앵커 하나를 주자 라벨 3줄 + 본문 11줄 = 14줄이었다. 스코프는 plane 단위라 규모가 커지면 어느 plane이든 예산을 넘기므로 이것은 현재 상태의 우연이 아니라 정의의 결함이다. 두 참고 논문 모두 "대상(앵커) 식별 → 의존 방향 확장 → 우선순위 → 예산 패킹"을 검색의 기본 절차로 두며(LEDGER는 편집 지시에서 대상 노드를, LARGER는 어휘 검색 결과를 진입점으로), 이 체계의 4.8절 앵커(링크가 가리키는 청크 IRI)가 그대로 출발점이 되므로 새 개념이 아니라 기존 IRI의 두 번째 역할이다. 앵커가 없으면 접힌 라벨 목록만 주는 것은 5.6절 "본문은 요청 시"의 귀결이다. 예산 상한식은 LARGER의 Δ = m·k·L_max이고 이 체계에서 L_max = 42줄이므로, 앵커 m개 × 이웃 k개 × 42줄이 예산 200줄 안에 들도록 hops·budget으로 k를 제한한다.
