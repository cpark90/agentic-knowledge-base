---
id: https://agentic-knowledge-base.dev/id/chunk/a85b3233-35f1-42e7-8b93-7983303e3224
type: decision
level: logical
title_ko: 청크는 모든 지식이 따르는 구조 규율이고 라벨 목록이 첫 읽기라 대표하지 못하는 라벨은 잘못된 읽기가 된다
title: The chunk is a structural discipline for all knowledge, and the label list is the first read, so a label that no longer represents its body is a wrong read
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f56035ce-db13-4b21-a3a2-5f5a173f7e03
---
**근거** — 2026-09-02~04 유저 결정 원장의 7항이 청크를 포맷이 아니라 구조 규율로 정하고 온톨로지에도 적용했다. 같은 시기 유저의 구조도는 한 청크를 한 plane·한 level·한 주제·한 파일로 적었다.

노트가 두 성질을 정한다. 4.1절은 청크가 한 주제만 다루는 자립적 지식 단위라고 정한다. 그 용어 근거 가운데 구조적 글쓰기의 information block은 한 주제이고 모듈형 문서의 topic은 독립 파일이다. 4.9절은 산문 계열의 assertion을 파일 하나 = 청크 하나로 두고 IRI를 파일 경로로 해석한다.

라벨 재검토는 라벨이 인터페이스라는 결정(`p4-label-is-the-interface`)에서 나온다. 에이전트는 라벨 목록을 먼저 받고 필요한 본문만 연다. 라벨이 본문을 대표하지 못하면 청크가 잘못 나뉜 것이다. 본문 편집은 `contentHash`를 바꿔 링크를 재판정 대상으로 만들지만(노트 4.3절) 라벨은 손으로 쓴 frontmatter라 따라 바뀌지 않는다. 그래서 편집하는 쪽이 재검토한다.
