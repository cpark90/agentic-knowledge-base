---
id: https://agentic-knowledge-base.dev/id/chunk-d0110
type: decision
level: concrete
title_ko: 링크 판정 근거는 검사 가능한 것부터
title: Rank link judgement evidence by checkability
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크가 성립하는지의 판정 근거는 **검사 가능성 순으로** 쓴다.

- **구축 기록**(8.3절) — 검사 가능성 가장 높음. 만든 주체가 남긴 것
- **동시 편집 이력**(같은 커밋) — 높음
- **테스트가 두 항목을 함께 커버** — 높음. `verifies`의 근거
- 임베딩 유사도 — 중간. **후보 추림에만**
- 한 세션에서 둘 다 읽음 — 낮음. 구축 기록의 약한 형태

**근거** (노트 8.8절) — 링크에는 네 한계가 있고, 각각을 이렇게 완화한다.
- **거리 부재** — 좌표계가 트리이지 거리공간이 아니다. 제약을 가진
  그래프로 한정해 다룬다.
- **판정 근거 부재** — "성립하는가"의 물리적 근거가 없다. CSP는 "성립
  가능한가"만 필요하고 이는 결정론적 검사다 (7.5절).
- **세계가 계속 변함** — 정적 스냅샷 추론이 성립하지 않는다. 2.6절 시간
  정체성과 8.6절 링크 상태로 받는다.
- **"같은 지식"의 정의** — 판단이지 사실이 아니다. 온톨로지 개념과 역할
  정보로 판단한다.
