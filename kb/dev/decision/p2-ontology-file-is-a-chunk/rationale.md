---
id: https://agentic-knowledge-base.dev/id/chunk/93c4f43d-2c89-494c-aad8-c33b0f8bfcbb
type: decision
level: logical
title_ko: 정의처가 하나여야 어휘가 갈라지지 않고 모듈을 한 파일로 합치면 청크 상한을 넘는다
title: A single place of definition keeps the vocabulary from diverging, and merging a module into one file exceeds the chunk limit
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2c53f95f-200a-4ae9-8dbe-b28de0df7378
---
**근거** — 저장소 구축(2026-09-01) 때 정한 원칙 "한 청크는 한 파일"이 온톨로지에도 적용된다. `STYLEGUIDE.md` §0은 지식·온톨로지·shape 전부를 그 원칙의 대상으로 적는다. 디렉토리를 모듈로, 모듈을 Bazel 패키지로 두면 모듈 사이의 `owl:imports`가 빌드의 deps와 같은 꼴이 된다. `kb/ontology/BUILD.bazel`의 최상위 모듈은 `owl:imports`에서 생성한 목록을 deps로 받는다.

정의처를 파일 하나로 두는 까닭은 어휘의 갈라짐(anti-drift)을 막는 것이다. `STYLEGUIDE.md` §0의 강인성 표는 anti-drift의 게이트로 `validate.py`의 vocab·labels·boundary를 적는다. boundary는 "한 agt: 용어는 정확히 한 모듈 파일에서만 정의된다"를 판정하고 그 출처를 노트 2.3절 경계 규칙으로 적는다.

모듈 하나를 파일 하나로 두면 청크 상한을 지키지 못한다. 2026-10-03 실측(o200k_base 근사, `@prefix`·주석·빈 줄 제외)에서 모듈 14 가운데 7이 한 파일로 합치면 1,092 토큰을 넘는다. 가장 큰 `related/defect`는 파일 17개, 약 9,980 토큰이다.

미확정: 기존 모듈 디렉토리에 새 파일을 더하는 것이 노트 2.3절의 "기존 모듈을 수정하지 않는다"에 어긋나지 않는다고 판정한 기록이 없다. 시행 중인 읽기는 `kb/ontology/BUILD.bazel` 주석의 "확장은 새 파일·새 모듈 디렉토리 추가로만 한다"다.
