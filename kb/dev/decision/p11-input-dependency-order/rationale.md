---
id: https://agentic-knowledge-base.dev/id/chunk/76db5145-4048-40cb-974f-77de5c900fdc
type: decision
level: logical
title_ko: 사슬의 위치가 불가역성과 파급 계산 순서를 결정한다
title: Position in the chain determines irreversibility and the order of impact computation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/1b1b47e5-a634-4953-bfd9-7b77bf651857
---
**근거** (노트 11.7절)

- **상위 온톨로지 선택이 사실상 불가역인 이유가 이 그림에 있다** — 사슬의 맨
  앞이므로 바뀌면 그 뒤 전부가 재정렬 대상이다.
- 스코프는 사슬의 끝이다. ODD와 카탈로그 **둘 다에서** 파생되므로(10.2절)
  어느 쪽이 바뀌어도 재파생된다.
- 언어 정책 사슬은 다른 둘과 만나지 않는다 — 표기 형식만 바꾼다. 그래서 언제
  바꿔도 비용이 국소적이다.
- 이 순서가 곧 **입력 변경의 파급 계산 순서이자 최초 인스턴스화의 진행
  순서**다. 순서를 건너뛰면 뒤의 입력이 근거 없이 정해진다.
