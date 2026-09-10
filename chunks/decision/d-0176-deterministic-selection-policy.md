---
id: https://agentic-knowledge-base.dev/id/chunk-d0176
type: decision
level: concrete
title_ko: 자동 선택은 전순서 정책으로 결정한다
title: Automatic choice needs a total-order selection policy
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 후보가 여럿 남은 채로도 산출을 내야 하는 무인 경로에서는 사람의
선택을 기다리지 않고 **전순서(total order) 선택 정책**으로 하나를 고른다.
정책은 (조건 필터 → 우선 등급 → 값 비교 → 안정 식별자)의 순서로 항상
유일한 답을 낸다.

**근거** (harness-concrete docs/odr-bind-lock.md §"Selection policy")
- 선호는 후보를 기각하지 않고 순서만 정한다(d-0104). 그 순서를 사람이
  아니라 기계가 소비하려면 순서가 **전순서**여야 한다 — 부분순서로는
  동점에서 답이 갈린다.
- 그래서 마지막 tiebreak는 반드시 전순서인 키(값, 그다음 후보 식별자
  오름차순)로 둔다. 집합·해시의 순회 순서에 의존하는 선택은 같은 입력에서
  다른 답을 내므로 재현성을 깬다.
- 값 비교 규칙 자체도 고정한다 — 버전 문자열은 구분자로 쪼개 숫자 구간을
  숫자로 비교한다(`1.10.0 > 1.9.0`). 사전식 비교는 사람이 기대하는 순서와
  어긋난다.
- 정책은 지역이 전역을 덮는다: 항목별 정책 > 구성물 기본 정책 > 체계
  기본값. 그래야 한 항목만 고정하려고 전체 기본값을 바꾸지 않는다.

**대안**
- 사람 확인 대기 — 무인 재생성 경로에서는 불가. 미확정을 **표현**하는 것은
  후보 집합(d-0097·d-0098)의 일이고, 그 위에서 답을 내는 선택 정책은 별개
  층이다. 후보를 남기는 것과 자동으로 고르는 것은 충돌하지 않는다.
