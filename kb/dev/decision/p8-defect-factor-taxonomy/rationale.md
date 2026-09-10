---
id: https://agentic-knowledge-base.dev/id/chunk/3e497c98-a93b-4976-8d4a-1c37b0d45784
type: decision
level: logical
title_ko: 요인이 개선 대상을 지목하고 위에서 아래로 구성해야 빠진 조합이 계산된다
title: Factors point at what to fix; top-down composition makes missing combinations countable
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/941cae39-2d59-468c-bd54-9d71cf8982ba
---
**근거** (노트 8.16절) — 세 갈래가 에이전트 작업의 세 단계(읽기·조율·수행)에 대응하므로 요인이 곧 개선 대상을 지목한다. 인지 요인은 스코프와 입력을, 상호작용 요인은 협업 구조를, 실행 요인은 도구와 산출물을 가리킨다 (6.3절 "무엇이 자라는가").

- 위험 케이스를 요인에서 **위에서 아래로** 구성하면 케이스가 임의 목록이 되지 않는다. 아래에서 위로(있는 케이스를 모아) 만들면 어떤 조합이 빠졌는지 계산되지 않는다 (7.18절).
- 조합을 표본 추출 근거로 쓰면 6.8절 logical → concrete 게이트가 요구하는 근거가 요인 태그로 제출된다 — 커버리지(7.7절)와 환경 할당(7.10절)이 같은 태그를 쓴다.
