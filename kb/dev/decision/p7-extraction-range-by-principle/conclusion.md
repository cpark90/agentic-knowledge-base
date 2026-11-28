---
id: https://agentic-knowledge-base.dev/id/chunk/108a10f4-abcb-4cea-8d00-e71d462969a1
type: decision
level: logical
title_ko: 코드를 단위 지식으로 투영하는 범위는 원리가 정하고 목록은 그 실현이다
former_title_ko: ["코드를 청크로 투영하는 범위는 원리가 정하고 목록은 그 실현이다", "코드를 지식 항목으로 투영하는 범위는 원리가 정하고 목록은 그 실현이다"]
title: A principle sets the range of code projected into chunks, and the lists realise it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:57:43+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/cb7ac129-5b94-47cd-84a8-b87e7e238efe]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/70d56a11-ab22-475f-8ca6-7af9c727eb1d]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/dafd1fa0-d08a-440b-b3f8-6c3ef808c58a
composite: {id: https://agentic-knowledge-base.dev/id/composite/dafd1fa0-d08a-440b-b3f8-6c3ef808c58a, title_ko: 원리로 정하는 추출 범위, title: Extraction range set by a principle}
---
**결론** — 코드를 단위 지식으로 투영하는 범위를 원리로 정한다. `defs/kb.bzl`의 목록 셋은 그 원리의 실현이다. 새 코드 파일이 추출 대상인지는 목록을 고치기 전에 원리로 판단한다. 원리는 "규칙을 강제하거나 질의로 답하는 코드 파일은 추출하고, 빌드 배선과 시험, 하네스 운영 스크립트는 추출하지 않는다"이다(Q192-a). 추출한 파일 안에서 무엇을 항목으로 두는지는 `p7-code-extraction-direction`이 정한다.
