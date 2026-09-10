---
id: https://agentic-knowledge-base.dev/id/chunk/4bbca001-fd36-4657-a9dc-dfabb820d055
type: decision
level: logical
title_ko: 문맥 추측을 남기면 에이전트가 빈칸을 스스로 채운다
title: Context-guessing invites the agent to fill blanks on its own
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/727e4644-52bb-4880-bb4b-ba11d36469f1
---
**근거** (노트 0.0절)

- 인접 개념이 같은 단어를 쓰면 에이전트가 문맥으로 뜻을 추측해야 하고, 이는
  1.2절 "지시하지 않은 곳을 스스로 채운다"를 부르는 자리다.
- 고정된 1:1 대응이 있어야 산문에서 어휘 위반을 **기계적으로 검사**할 수
  있다. 검사 대상이 되는 대응표가 곧 온톨로지의 라벨이다 (0.6절).
- 개발 KB와 V&V KB를 이름 수준에서 갈라 두면 판정 주체가 뒤섞이는 것을
  어휘가 먼저 막는다 (Part VIII).
