---
id: https://agentic-knowledge-base.dev/id/chunk/85034442-9338-421a-b5d6-8d90d4e16603
type: decision
level: logical
title_ko: 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보이므로 순서는 선언에서만 나온다
title: Order attached to what does not require it is false information, so order comes only from declaration
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-29T11:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c15bc5d0-4f85-4d7b-bdd2-85cca14af3ba
---
**근거** — 규칙은 이미 있었다. 옛 결정(구성체는 표준 part-of와 순서 컬렉션으로 쓴다, 2026-09-01)이 "순서가 뜻을 갖는 복합체만 `co:List`"로 정했고 `docs/rules.md`가 그것을 표로 옮겼다. 그러나 실행이 없었다 — 생성기는 `hasDirectPart`만 냈고 멤버를 IRI 순으로 정렬해 냈다. 규칙이 산문에만 있으면 언젠가 그 정렬이 순서로 읽힌다.

순서의 원본을 선언으로 두는 까닭은 둘이다. 첫째, 순서가 뜻을 갖는지는 저작자만 안다. 검증기 셋(양성 전체 → 음성 반쪽 → 오케스트레이션)은 순서가 검증 범위의 확장이지만, 요구의 관심사 묶음은 순서가 없다. 생성기는 그 차이를 알 수 없다. 둘째, 파일명·IRI 정렬은 결정적이라 재현되지만 뜻이 없다 — 그것을 `co:index`로 내면 "순서를 요구하지 않는 것에 순서를 붙인" 거짓 정보가 된다.

결정 복합체만 선언 없이 고정 순서를 내는 까닭은 역할이 곧 순서이기 때문이다. 결론 없이 근거를 읽지 않고, 대안은 결론을 전제한다. ADR 뷰(`weave`)가 이미 그 순서로 조립한다. 선언을 요구하면 205개 결정에 같은 목록을 반복해 적는 것이고, 그것은 정보가 아니라 첨가다.

`ordered`를 메타데이터로 두는 까닭은 순서가 본문의 뜻을 바꾸지 않기 때문이다. 부분의 본문 해시는 그대로이고 바뀌는 것은 묶음의 읽기 순서다 — 복원 링크 표시 `restored`와 같은 층이다.
