---
id: https://agentic-knowledge-base.dev/id/chunk/9a417ca4-15e8-45b0-84fb-b77e5c546f79
type: decision
level: concrete
title_ko: 규범 문서 규약 — 생성 문서의 머리는 제목 한 줄과 여섯 줄의 고정 순서다
title: Normative-document conventions — The head of a generated document is one title line and six lines in fixed order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/094466b2-eced-45bf-991f-85eead474058
---
**규약** — `p12-generated-document-header`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 머리는 h1 한 줄과 여섯 줄이다. 순서는 `생성기` → `생성 시각` → `입력` → `질의` → `재현` → 성격 경고다. h1은 `# <이름> — <목적> (생성 파일)`로 끝난다.
규약: [지킴] `생성기`는 OKF 행위자 표기 `<생성기>/<버전>`을 쓴다. `생성 시각`은 ISO 8601 UTC 초 해상도다. `입력`은 파일 **목록**과 지문 `sha256:<앞 12자>`를 적는다. 개수만 적지 않는다. `재현`은 **자기 자신을** 다시 만드는 명령이다.
규약: [지킴] 드리프트 검사가 바이트 비교를 하는 생성 트리 파일(`.claude/skills/*/SKILL.md`·생성 BUILD)에는 생성 시각과 지문을 넣지 않는다. 그 자리의 건전성 장치는 결정론이다.
