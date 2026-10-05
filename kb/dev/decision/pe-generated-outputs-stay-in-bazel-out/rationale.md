---
id: https://agentic-knowledge-base.dev/id/chunk/31d67fd5-de1f-4921-8b5b-2c29752428dc
type: decision
level: logical
title_ko: 뷰는 소스 밖에 두어야 이중 원본이 생기지 않고 트리에 두는 생성물은 재생성 비교가 원본과의 일치를 보장한다
title: Views kept outside the source avoid a second original, and regeneration comparison keeps committed outputs equal to their source
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/444519a5-c8d8-416b-88a5-b1bc2fd92ccc
---
**근거** — 노트 부록 E는 뷰를 build output에 대응시키고 "출력은 소스 밖"이라 적는다. 소스 트리에 같은 이름의 생성물이 있으면 원본이 둘이 되고, 손 편집이 다음 생성에서 사라진다.

예외 둘은 트리에 있어야 하는 이유가 있다. 생성 BUILD는 링크 변화를 리뷰에 드러내려고 커밋한다(`tools/gen_build.py` docstring). skill은 도구를 돌리지 않는 세션도 읽어야 하므로 커밋한다(`tools/gen_skills.py` docstring). 트리에 두는 대가로 원본과의 일치를 드리프트 테스트가 진다. 2026-09-19에 두 예외와 두 테스트가 규범 문서에 함께 들어갔다.

실측(2026-10-03)에서 규범 문서가 적지 않은 생성 트리가 하나 더 있다. 추출 청크 `kb/dev/artifact/<모듈>/`는 `tools/extract.py`의 생성물이고 `//:extract_drift_test`가 같은 방식으로 지킨다(`p7-code-extraction-direction`, 유저 승인 2026-09-30). 규범 문서의 "둘"은 그 결정보다 앞선 표기다.

미확정: 추출 청크 트리를 생성 트리 파일의 셋째 예외로 규범 문서에 올리는가.
