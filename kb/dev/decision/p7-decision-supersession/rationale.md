---
id: https://agentic-knowledge-base.dev/id/chunk/b00eaea5-0cea-4c94-b031-37d08c50a815
type: decision
level: logical
title_ko: 삭제하면 근거가 사라지고 링크가 끊긴다
title: Deletion loses grounds and breaks links
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:09:13+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c34b1d2f-86fb-4cd1-b532-edf65e7230c7
---
**근거** (노트 7.4절, 10.11절, 4.11절) — `deprecated`는 참조는 남되 신규 참조를 금지하는 상태다(4.11절). 옛 결정을 지우면 그것을 `satisfies`하던 산출물의 링크가 댕글링이 되고, 새 결정으로 옮겨야 할지 판단할 재료가 없어진다. `supersedes`가 시간축 링크(10.2절)로 남아 있어야 "왜 바뀌었는가"가 감사(12.4절)에서 답해진다.

**개정** — 유저는 옛 결정 트리 `chunks/decision/`을 지우기로 했다(Q113-b). 파일이 없어진 IRI를 `supersedes`가 그대로 가리키면 그래프가 끝점을 단위 지식으로 추론해 shape가 거부한다. 그래서 지운 옛 결정마다 라벨 둘과 git 영구 위치만 가진 묘비를 생성 그래프에 두고, `supersedes`의 치역을 단위 지식과 묘비의 공통 상위인 지식으로 넓혔다. 묘비의 원본은 대체한 결정 결론의 `sources` 항목이고, 원문은 git 영구 위치에서 읽는다. 그래서 링크는 끊기지 않고 근거도 사라지지 않는다(Q-0061#Q146).
