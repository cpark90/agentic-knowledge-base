---
id: https://agentic-knowledge-base.dev/id/chunk/686683f8-499d-40f2-a585-9e33ef41c11a
type: decision
level: concrete
title_ko: 결정은 규범 문서에 실릴 문장을 넷째 청크 conventions.md의 규약 줄에 담는다
title: A decision holds the sentences to be carried into the normative documents as convention lines in a fourth chunk, conventions.md
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6a38d7ed-105a-44bd-9c25-400871e5e5dc
composite: {id: https://agentic-knowledge-base.dev/id/composite/6a38d7ed-105a-44bd-9c25-400871e5e5dc, title_ko: 결정의 규약 청크, title: The conventions chunk of a decision}
---
**결론** — 결정이 규범 문서에 싣는 문장은 결정 디렉토리의 선택 청크 `conventions.md`에 **`규약:`** 줄로 둔다(유저 답 Q13-a, Q22-b). 모든 결정이 이 자리 하나를 쓴다. 결론 슬롯에 `규약:`을 두는 결정은 없다.

| 항목 | 내용 |
|---|---|
| 자리 | 결정 복합체의 넷째 부분. `type: decision`, `level: concrete`, `layer: methodology`, `part_of`는 그 결정의 복합체 |
| 조건 | 결정에 규범 문서에 실릴 문장이 있을 때만 둔다 |
| 첫 줄 | 역할 태그 `**규약** — <이 결정이 규범 문서에 싣는 문장들이다 같은 한 문장>` |
| 줄 꼴 | 한 줄에 하나씩 `규약: [지킴] <문장>` 또는 `규약: [권장] <문장>`. 강도 없는 줄(표 행)도 허용하고, 강도를 요구하는 문서에서는 생성기가 거부한다 |
| 단위 | 한 줄은 문서의 항목 하나다. 하위 항목도 줄 하나씩이다. 줄은 슬롯이고 목록 항목이 아니다(목록 규칙 대상 아님) |
| 참조 | 골격이 `<결정 디렉토리>#<k>`로 줄을 가리킨다. k는 그 청크 안 `규약:` 줄의 1부터의 순번이다 |
| 링크 | 문장 안 링크는 청크 파일 기준 상대경로다. 생성기가 출력 위치 기준으로 다시 계산한다 |

- **번호를 지킨다.** 새 줄은 끝에 덧붙인다. 줄 수 상한은 없고 본문 토큰 상한 1,092만 적용한다. 넘으면 그 결정이 두 주제라는 신호다.
- **규약 줄은 그 결정의 결론이 진술하는 것의 세부만 담는다.** 세부는 서식·경로 이름·예다. 결론에 없는 새 주장은 규약 줄이 아니다. 그런 내용은 결론을 개정하거나 그 주장을 진술하는 다른 결정의 줄로 둔다. stable 결정의 개정은 유저 승인 사항이다.
- **규약 줄의 추가는 결론의 개정이 아니다.** 결론·근거·대안 본문을 바꾸지 않으므로 stable 결정에도 승인 없이 끝에 더한다. stable 결정의 기존 규약 줄을 고치는 것은 그 결정의 본문 변경이라 유저 승인 사항이다.
- 문장은 규범 문서에 그대로 실리므로 단정 서술형이고 그 문서의 표기를 따른다.
- 결정 복합체 검사(`kb_decision`·역할 태그)는 "세 청크 고정"에서 "세 청크 + 선택 `conventions.md`"로 넓어진다. 기존 세 청크 검사는 약화하지 않는다. 구현됐다(`defs/kb.bzl`의 `kb_decision` `conventions` 속성, `tools/gen_build.py`).
