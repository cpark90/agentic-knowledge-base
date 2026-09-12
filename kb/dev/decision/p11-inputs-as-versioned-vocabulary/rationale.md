---
id: https://agentic-knowledge-base.dev/id/chunk/065991e2-afd8-42c4-b81a-1a166d4e6541
type: decision
level: logical
title_ko: 어휘 밖 입력은 읽히지 않고 버전 없는 입력은 재검토 범위를 못 만든다
title: Inputs outside the vocabulary cannot be read; unversioned inputs yield no review scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/81f5ea27-b01f-427d-bad5-4d35e593b94d
---
**근거** (노트 11.1절·10.5절)

- **입력이 어휘 밖에 있으면 체계가 읽을 수 없다.** 권한·실행 특성이 전부
  속성으로 표현되어야 스코프 파생과 입력 검증이 질의 하나로 환원된다.
- 어휘로 쓰면 입력 검증(10.6절)이 청크와 **같은 shape 수단**을 그대로 쓴다.
  입력만을 위한 두 번째 검사 체계를 만들지 않는다.
- 입력이 바뀌면 그 위의 파생물이 바뀐다. 언제 무엇이 바뀌었는지 남아야
  파생물의 재검토 범위가 계산된다 — ODD를 버전 관리하는 이유와 같다.
- 예시의 `agt:maxConcurrent`처럼 ODD 동적 요소와 대조해야 하는 값도 속성이
  되므로, 카탈로그와 ODD의 충돌이 기계적으로 검사된다(10.2절).
