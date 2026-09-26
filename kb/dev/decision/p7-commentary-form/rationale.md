---
id: https://agentic-knowledge-base.dev/id/chunk/a471aa31-5149-4d07-9eab-542e19c4e259
type: decision
level: logical
title_ko: 라벨이 없으면 읽는 쪽이 행동의 크기를 매번 추측한다
title: Without a label the reader guesses how much action a comment demands
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-26T15:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/54cd62d1-0efa-4a35-b379-20d8880cc3be
---
**근거** — 주석은 두 가지를 동시에 전한다. 무엇을 보았는가와 무엇을 해야 하는가다. 후자가 형식에 없으면 읽는 쪽이 문장의 어조에서 추측하고, 추측은 사람마다 갈린다. 칭찬을 요구로 읽거나 차단 사유를 취향으로 읽는 것이 그 결과다. 라벨은 전자를, 장식은 후자를 고정한다.

닫힌 어휘를 쓰는 근거는 이 체계가 어휘 통제로 드리프트를 막는 것과 같다. 라벨이 자유 문자열이면 같은 뜻의 라벨이 여럿 생기고 집계가 불가능해진다.

`blocking` 하나만 게이트를 막는 근거는 비용이다. 모든 주석이 진행을 막으면 리뷰가 병목이 되고, 아무것도 막지 않으면 리뷰가 기록으로 끝난다. 차단의 범위를 저자가 주석마다 선언하게 하면 그 판단이 기록에 남는다.

표기를 Conventional Comments에서 가져온 근거는 `STYLEGUIDE.md` §0의 "표준어가 우선이다"이다. 리뷰 주석의 라벨 어휘는 이미 널리 쓰이는 규약이 있고, 지어낸 어휘는 근거를 스스로 대야 한다.

해소 상태를 필수로 두는 근거는 `p5-verification-tools-per-plane`이 이미 `annotation`의 판정을 "해소 상태 존재 여부만"으로 정했다는 것이다. 상태가 없으면 판정할 것이 없다.
