---
id: https://agentic-knowledge-base.dev/id/chunk/3a35c8de-bac0-4f1e-b745-469608bc1790
type: decision
level: logical
title_ko: 본문 안에 가정과 링크를 함께 두면 청크가 문맥에 묶인다
title: Embedding assumptions and links in the body binds the chunk to its context
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/428f00f0-6790-41c0-83a8-bf8a564e848e
---
**대안**

- `[배제]` 고유 출처 어휘를 정의하는 안 — PROV-O가 구축 기록·일반화·버전을 이미
  덮으므로 새 어휘는 같은 것을 다시 쓰는 일이 된다 (4.3절).
- `[배제]` 가정과 링크를 assertion 본문 안에 두는 안 — 청크가 자기 연결을 알게
  되어 다른 복합체에서 재사용할 수 없게 된다. 가정은 6.5절, 링크는 9.5절이
  청크 IRI를 가리키는 방식으로 밖에 둔다.
