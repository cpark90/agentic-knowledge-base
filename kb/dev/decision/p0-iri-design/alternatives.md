---
id: https://agentic-knowledge-base.dev/id/chunk/2c1c00b0-933e-4d86-82b9-82700814091d
type: decision
level: logical
title_ko: 의미 있는 IRI와 버전을 별도 속성으로 두는 안의 기각
title: Rejecting meaningful IRIs and version as a separate property
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/eb847899-2640-4bca-955a-7f511528bc1d
---
**대안** — 경로나 라벨을 담은 의미 있는 IRI. 기각 — 읽기는 편하지만 이름이
바뀔 때마다 IRI가 바뀌고, 그때마다 참조가 끊긴다. 읽기 편의는 `rdfs:label`이
담당한다.

**대안** — 버전을 IRI가 아니라 별도 속성으로 두는 안. 기각 — 특정 버전을
가리키는 링크가 IRI 하나로 표현되지 않아, 링크의 도착점이 항상 "현재"가 된다.
