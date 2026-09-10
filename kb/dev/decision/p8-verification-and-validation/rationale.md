---
id: https://agentic-knowledge-base.dev/id/chunk/6b6fe18d-fe67-4b27-8139-c84ef1844acd
type: decision
level: logical
title_ko: 확인이 없으면 틀린 요구를 완벽히 충족하는 시스템이 된다
title: Without validation you get a system that perfectly meets the wrong requirement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/f78cc6f9-4200-405e-8a12-7c8eb43f9c24
---
**근거** (노트 8.4절) — 확인이 없으면 틀린 요구를 완벽히 충족하는 시스템이 된다. 검증만 갖춘 체계는 모든 게이트를 통과하면서도 쓸모없는 산출물을 낼 수 있고, 그 실패는 어떤 판정식에도 걸리지 않는다.

- 둘을 `origin:` 태그로 갈라 두는 이유는 시나리오의 출처가 곧 그 결과의 목적지를 정하기 때문이다. 설계에서 파생된 시나리오의 실패는 산출물의 문제이고, 관측에서 일반화된 시나리오의 실패는 요구의 문제일 수 있다.
- 요구 변경 경로를 하나로 못 박는 이유 — 개발 역할은 기준을 고칠 수 없으므로(7.5절) "기준이 틀렸다"는 주장이 요구를 고치는 형태로만 제기된다. 경로가 하나면 변경 이력이 한 곳에 쌓이고 일반화의 기록(`prov:wasDerivedFrom`)이 끊기지 않는다.
