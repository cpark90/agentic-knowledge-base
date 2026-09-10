---
id: https://agentic-knowledge-base.dev/id/chunk/5b904638-6b04-463c-9c5a-d166fe96014f
type: decision
level: logical
title_ko: 검사 없는 입력은 그 위의 파생물 전체를 조용히 오염시킨다
title: An unchecked input silently contaminates everything derived from it
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/23431e57-2877-4a0f-9f25-9f8dabdfc792
---
**근거** (노트 11.6절)

- 입력이 온톨로지 어휘로 쓰이므로(10.1절) 청크와 **같은 검사 수단**을 그대로
  쓴다. 입력 전용 검사기를 따로 만들지 않는다.
- 검사 없이 들어온 입력은 그 위의 파생물 전체를 조용히 오염시킨다. 카탈로그의
  경우 **스코프 전부**가 그 오염을 물려받으므로 오염원이 가장 크다.
- read plane이 하나도 없는 역할은 작업 집합이 빈 역할이고, 재검증 시점가 0개면
  suspect 링크가 영원히 재판정되지 않는다 — 둘 다 조용히 아무 일도 일어나지
  않는 실패라 검사로만 잡힌다.
- 프로세스 규칙의 순환은 어떤 순서로도 작업이 시작되지 않는 상태다.
