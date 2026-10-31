---
id: https://agentic-knowledge-base.dev/id/chunk/67571819-4620-4639-9e59-46e9fe4e7e29
type: decision
level: logical
title_ko: 순서와 기각을 분리해야 임의 선택이 다시 열리지 않는다
title: Separating ranking from rejection keeps arbitrary choice closed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4
---
**근거** — 선호에 기각 권한을 주면 근거 없는 수치가 후보를 지우게 되고, 캘리브레이션이 없어 등급을 채택하지 않았던 이유가 뒷문으로 돌아온다. 순서만 갖는 선호는 후보 집합을 바꾸지 않으므로 제약 전파의 결과를 오염시키지 않는다(노트 9.9절, 8.2절).

선호에 이유 문자열 `reason`을 함께 적게 하는 것은 선호 자체가 나중에 제약으로 승격될 수 있는지 판단할 재료를 남기기 위해서다.

**개정** — 유저는 믿음 정도를 선호의 동률 깨기에 넣기로 했다(유저 결정 Q-0055 Q109-b, 2026-10-24). 동률 깨기는 순서가 없는 두 후보의 순서만 정하고 후보 집합을 바꾸지 않으므로, 순서와 기각의 분리는 그대로 지켜진다. 그래서 Q90-a의 "믿음 정도는 병기만 한다"는 이 범위에서 "병기하고 동률을 깬다"로 바뀐다. 다만 믿음 정도를 언어모델의 제안보다 앞에 두는 순서는 유저에게 묻지 않았고, hci가 정해 보낸 가정이다(지시 0191). 그 가정의 이유는 믿음 정도가 재검증 가능한 증거 기록에서 계산되는 반면 언어모델의 제안은 검사 가능성 서열의 맨 아래에 있다는 것이다.
