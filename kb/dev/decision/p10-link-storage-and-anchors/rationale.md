---
id: https://agentic-knowledge-base.dev/id/chunk/fd397d16-f882-423b-b7c7-d9cb432707d2
type: decision
level: logical
title_ko: 산출물을 열지 않고 링크를 만들고 질의할 수 있어야 한다
title: Links must be authored and queried without opening artifacts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c1ce996d-dc84-45c5-b567-a9da42421774
---
**근거** (노트 9.5·9.9절) — 이유 셋. (a) 산출물을 열지 않고 링크를 만들고 질의할 수 있다. (b) 산출물 형식마다 링크 표기를 정하지 않아도 된다. (c) 링크 모델의 저장·시각화·검사를 산출물과 독립적으로 교체할 수 있다.

앵커를 청크 ID로 고정하면 앵커 드리프트가 청크 안에 갇힌다 (4.8절) — 청크 본문이 흔들려도 ID는 같으므로 링크가 살아남고, 해석기 교체가 링크 모델에 파급되지 않는다.
