---
id: https://agentic-knowledge-base.dev/id/chunk/cb7ac129-5b94-47cd-84a8-b87e7e238efe
type: requirement
level: functional
pattern: event-driven
title_ko: 저장소의 지식이 진전하면 하네스는 스스로 개선된다
title: When the repository's knowledge advances, the harness improves itself
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-05T20:25:34+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T20:25:36+09:00}]
---
**요구** — 저장소의 지식이 진전하면(결정·관측·어휘가 늘거나 바뀌면), 하네스(도구·게이트·뷰·skill)는 그 진전을 반영해 스스로 개선되어야 한다 — 사람이 하네스를 따로 고치는 것이 아니라 지식에서 하네스가 생성·갱신된다.

- **이해관계자**: 유저 · **관심사**: 통일과 되먹임
- **출처**: 유저 지시 2026-09-23(하네스는 저장소의 지식 진전을 반영해 스스로 개선해야 한다), 통일 기획 0단계(2026-10-01)

판정의 자리는 되먹임 사슬이다 — 관측 → 일반화 → 승격 → 게이트·도구 갱신. 지금 실물은 `term_propose`(승격 큐, 관측에서 어휘로 승격한 사례 1건)·`gen_skills`(도구 → skill 생성)·추출(코드 → 청크)·규범 문서 생성(결정의 규약 줄과 절 청크 → `STYLEGUIDE.md`·`docs/rules.md`·`docs/method.md`·`AGENTS.md`)·게이트 `rung-before-descent`(하강마다 검증 대응물 강제)다. 역방향(지식 → 도구 코드)은 없다. 이 요구는 통일 기획 5단계에서 검증 사슬(목표 `harness-follows-knowledge` → 기준 → 검증기)이 선 뒤 유저 승인으로 `stable`이 됐다(Q53-a).

미확정: 하네스의 어느 부분이 지식에서 생성되는가의 경계 — 2단계 편입(도구 → 절차 청크, 게이트 → 규칙 청크)이 그 답의 첫 형태다.
