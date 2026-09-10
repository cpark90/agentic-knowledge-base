---
id: https://agentic-knowledge-base.dev/id/chunk/d2ecafaf-cb13-4b9f-a337-11b9c454427a
type: decision
level: logical
title_ko: 유형이 자동 판정의 범위와 무효화 전파의 주기를 가른다
title: The kind determines what can be judged automatically and how often
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/674dc862-8a79-40df-a50e-9643d9caca63
---
**근거** (노트 6.9절) — 유형을 열거하는 목적은 판정의 자동화 가능 범위를 드러내는 것이다. 앞의 셋은 하네스가 스스로 돌릴 수 있고, 외부 조회는 접근 권한이 필요하며, 사람 확인은 유저 채널을 거친다 — 무효화 전파(6.10절)를 돌리는 주기가 유형마다 다르다.

- 판정 식을 assertion 안에 적게 하면 "가정은 적혀 있으나 확인할 방법이 없다"는 상태가 `unverified`로 명시된다. 판정 불가를 숨기지 않고 상태로 드러내는 것이 6.5절 세 상태의 취지다.
- 3.9절 등급과 짝을 이루므로, ODD에 넣을 수 없는 등급의 판정 방법은 가정의 판정 방법으로도 약하다.
