---
id: https://agentic-knowledge-base.dev/id/chunk/3b508984-6804-4dfe-863e-59621a4e61f8
type: decision
level: logical
title_ko: 대상별 파일은 한 파일 한 주제 원칙의 shape판이고 메시지는 FAIL을 수정 안내로 만든다
title: One file per target applies the one-file-one-topic rule to shapes, and the message turns a FAIL into a repair instruction
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/715a53ec-b1a3-4a8a-92ff-31bb1806ef9b
---
**근거** — 파일 하나가 대상 하나를 담는 것은 `STYLEGUIDE.md` §0의 "한 청크는 한 파일, 한 파일은 한 주제다"가 shape에 적용된 것이다. 그 원칙의 대상에 shape가 명시돼 있다. 저장소 구축(2026-09-01) 때부터의 규약이다.

`sh:message`의 이유는 규약 원문이 적는다. 메시지가 있어야 FAIL이 곧 수정 방향 안내가 된다. 게이트 도구 규약(`STYLEGUIDE.md` §7)의 "메시지가 곧 수정 안내다"와 같은 원칙이다. 이 결정의 요구는 "편집은 게이트가 판정한다"다. 그 요구는 판정을 에이전트 밖의 규칙과 shape에 둔다.

2026-10-03 실측에서 규약은 거의 지켜진다.

- shape 파일 25개 전부가 `-shapes.ttl`로 끝난다.
- property shape 102개 가운데 95개가 `sh:message`를 갖는다.
- 나머지 7개는 `sh:or` 안의 선택지다(`defect-factor-shapes.ttl` 2, `judge-question-shapes.ttl` 5). 메시지는 그것을 감싸는 node shape에 있다.

미확정: `sh:or` 안의 선택지가 이 규약의 "모든 property shape"에 드는지 정한 기록이 없다.
