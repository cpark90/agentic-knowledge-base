---
id: https://agentic-knowledge-base.dev/id/chunk/e2533f18-359f-4bbb-920f-fdda1df12126
type: decision
level: logical
title_ko: ODD가 틀리면 그 위의 모든 것이 틀린다
title: If the ODD is wrong, everything above it is wrong
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d53cfcf9-c765-4bfe-b787-a420967a6f35
---
**근거** (노트 3.6절) — ODD 위에 스코프·가정·기준·케이스가 서 있으므로 ODD가 잘못되면 그 전부가 잘못된다. 그래서 편집 통제 수준을 2.4절 T-Box와 같게 둔다.

순서를 온톨로지 → ODD → 파생물로 고정하는 이유는 어휘 밖 속성이 ODD에 들어오는 것을 막기 위해서다. 그것을 허용하면 ODD가 새 어휘의 생성지가 되어 2.5절 용어 제안 워크플로를 우회한다.

변경 유형을 셋으로 닫으면 파급 규칙을 유형별로 미리 정할 수 있다. 축소만 무효화를 낳고 정밀화는 파급이 없다는 것이 재검토 비용을 예측 가능하게 만든다.
