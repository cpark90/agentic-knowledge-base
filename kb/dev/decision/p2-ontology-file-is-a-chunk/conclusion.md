---
id: https://agentic-knowledge-base.dev/id/chunk/e461ba9e-53dd-4f09-aa99-2c06ab73f9eb
type: decision
level: concrete
title_ko: 온톨로지는 파일이 청크이고 디렉토리가 모듈이며 한 개념은 한 파일에서만 정의된다
title: In the ontology a file is a chunk and a directory is a module, and each concept is defined in exactly one file
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7, https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:14:21+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2c53f95f-200a-4ae9-8dbe-b28de0df7378
composite: {id: https://agentic-knowledge-base.dev/id/composite/2c53f95f-200a-4ae9-8dbe-b28de0df7378, title_ko: 온톨로지의 파일과 모듈 배치, title: Ontology file and module layout}
---
**결론** — 온톨로지는 파일이 청크이고 디렉토리가 모듈이며 모듈이 Bazel 패키지다. 노트 2.3절의 모듈 구조를 파일 단위로 내린 규약이다.

- **새 개념은 주제가 맞는 기존 모듈 디렉토리의 새 파일로 추가한다.** 기존 파일에 덧붙이는 것은 그 파일의 주제일 때만이다.
- **새 주제는 새 모듈 디렉토리로 추가한다.** 모듈은 `project-ontology.ttl`의 `owl:imports`와 `kb/ontology/BUILD.bazel`의 `//kb/ontology:modules`에 손으로 등록한다. 모듈의 `BUILD.bazel`은 모듈 디렉토리에서, `modules.bzl`은 `owl:imports`에서 `tools/gen_build.py`가 생성한다.
- **한 개념은 정확히 한 파일에서 정의된다.** 다른 파일에서 재정의·재선언하지 않는다. 다른 모듈의 개념은 참조만 한다. 게이트 `boundary`(`tools/validate.py`)가 이것을 판정한다.

이 결정은 `p2-ontology-module-structure`의 경계 규칙(모듈은 다른 모듈의 개념을 정의해 넣지 않는다)을 파일 단위로 좁힌다. 같은 결정의 "확장은 새 모듈 추가로만 한다"는 이 저장소에서 새 파일·새 모듈 디렉토리의 추가로 시행된다(`kb/ontology/BUILD.bazel` 주석).
