---
id: https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b
type: contract
level: logical
title_ko: 본문 43줄 이상은 청크 검사와 shape 둘 다에서 거부되고 커밋된 청크는 전부 42줄 이하다
title: A body of 43 lines or more is rejected by both the chunk lint and the shape and every committed chunk is within 42
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/14414342-1e2f-4f00-a100-8c18642d0ebd]
---
**합격 기준** — 기준 종류는 **임계**다. 모든 청크에 대해 `본문 줄 수 ≤ 42`가 성립한다. 본문 줄 수는 frontmatter와 앞뒤 빈 줄을 뺀 나머지이고 `agt:lineCount`와 같은 값이다.

**판정식**

- 음성(검사기): 본문 43줄인 `.md`를 `python3 tools/chunk_lint.py --chunks <파일>`에 넣으면 `FAIL [chunk] <파일>: 본문 43줄 > 42줄`로 끝나고 종료 코드가 1이다.
- 음성(shape): 같은 파일의 head 조각에서 `agt:lineCount 43`이 `agt:ChunkShape`의 `sh:maxInclusive 42`에 걸려 `//kg:gate_test`가 FAIL이다.
- 양성: `bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test`가 PASS다. 청크 타깃의 빌드 검증 액션 `KbChunkLint`도 같은 검사를 돈다.
- 임계값의 두 정의처 `MAX_BODY_LINES`와 `sh:maxInclusive`가 같은 값 42다.

**등급** — B다. 판정은 기계가 하되 청크 검사와 shape 검증의 실행 비용이 있다.

기준의 대상은 `chunks/`·`kb/dev`·`kb/vv`의 모든 `.md` 청크이고 판정의 원본은 `tools/chunk_lint.py`와 `kb/ontology/shapes/chunk-shapes.ttl`이다.
