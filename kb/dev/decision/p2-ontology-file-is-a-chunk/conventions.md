---
id: https://agentic-knowledge-base.dev/id/chunk/05cbfeee-9625-4db8-bdc9-b79084b190da
type: decision
level: concrete
title_ko: 규범 문서 규약 — 온톨로지는 파일이 단위 지식이고 디렉토리가 모듈이며 한 개념은 한 파일에서만 정의된다
title: Normative-document conventions — In the ontology a file is a chunk and a directory is a module, and each concept is defined in exactly one file
former_title_ko: ["규범 문서 규약 — 온톨로지는 파일이 지식 항목이고 디렉토리가 모듈이며 한 개념은 한 파일에서만 정의된다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:47:22+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2c53f95f-200a-4ae9-8dbe-b28de0df7378
---
**규약** — `p2-ontology-file-is-a-chunk`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 새 개념은 **주제가 맞는 기존 모듈 디렉토리의 새 파일**로 추가하고, 새 주제는 **새 모듈 디렉토리**로 추가한다. 새 모듈은 `project-ontology.ttl`의 `owl:imports`와 `//kb/ontology:modules`에 손으로 등록한다. 반면 모듈의 `BUILD.bazel`과 `modules.bzl`은 `tools/gen_build.py`가 생성한다.
규약: [지킴] 한 개념은 정확히 한 파일에서 정의된다. 그래서 다른 파일에서 재정의하거나 재선언하지 않고 다른 모듈의 개념은 참조만 한다(boundary 게이트).
