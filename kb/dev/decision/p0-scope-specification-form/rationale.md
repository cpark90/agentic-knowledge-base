---
id: https://agentic-knowledge-base.dev/id/chunk/ce657f56-0814-4797-9568-5338f42fc40b
type: decision
level: logical
title_ko: mode가 없으면 적히지 않은 것의 뜻이 추측에 맡겨진다
title: Without a mode, the meaning of what is unwritten is left to guesswork
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/780d333f-1d35-4e81-83cf-58355a1d3d41
---
**근거** (노트 0.4절)

- mode를 명시해야 **적히지 않은 것의 의미**가 결정된다. mode 없이
  include/exclude만 있으면 목록에 없는 조건을 허용으로 볼지 금지로 볼지가
  에이전트의 추측에 맡겨진다 (1.2절).
- write의 기본이 `restrictive`인 것은 쓰기의 실수가 읽기의 실수보다 되돌리기
  비싸기 때문이다. 읽기는 하네스가 컨텍스트 예산과 함께 정한다.
- **conditional이 프로세스 규칙의 기계적 강제 수단이다.** 예시 문장은 10.1절
  "구현 전 상세 설계"를 문서 규칙이 아니라 게이트 검사로 만든다 — 편집의
  허용 여부를 게이트가 판정한다는 요구가 여기서 실현된다.
