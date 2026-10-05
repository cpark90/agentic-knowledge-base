---
id: https://agentic-knowledge-base.dev/id/chunk/1deba644-0689-40f1-b1a0-cf5f3153603d
type: decision
level: concrete
title_ko: 규범 문서 규약 — 생성 문서의 본문 서식은 마크다운 표준 규칙과 빈 값 한 표기를 따른다
title: Normative-document conventions — The body of a generated document follows standard Markdown rules and one empty-value form
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6364f6e3-f553-4178-946c-36246fed08a9
---
**규약** — `p12-generated-document-form`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 제목 계층은 한 단계씩 내려가고 h1은 문서당 하나다. 표는 헤더 행을 갖고 모든 행의 열 수가 같고 앞뒤에 빈 줄이 있다. 펜스에 언어를 명시한다.
규약: [지킴] 본문이 120줄을 넘으면 목차 절을 둔다. 앵커는 `doccheck`의 `slug`로 만든다.
규약: [지킴] 링크는 **생성물이 놓이는 위치 기준으로** 실재해야 한다. 생성물은 소스 트리와 다른 곳에 놓이므로 소스 기준 상대경로가 성립하지 않는다.
규약: [지킴] 빈 값은 `없음` 하나로 적는다. 표 셀을 비우거나 대시로 두지 않는다. 절은 비어도 제목을 남긴다.
규약: [지킴] 비율은 `n/d = p.p%` 꼴이고 소수 한 자리다. 분모 없는 백분율을 쓰지 않는다. 0 분모는 `없음`이다. 자릿수 상수는 `kb_lib`에 하나만 둔다.
규약: [지킴] 산문은 §0의 단정 서술형이다.
규약: [지킴] 청크 본문·라벨을 그대로 옮겨 싣는 **인용 구역**은 표시로 감싼다. 그 안에서는 표·펜스·빈 값·수치·산문의 다섯을 판정하지 않는다. 생성기는 원문을 고쳐 쓰지 않고, 원본은 이미 자기 게이트를 통과했다. 제목 계층·h1·목차·링크는 구역 안에도 적용한다.
규약: [지킴] 제목 줄과 링크 텍스트는 수치 표기 판정 밖이다. 이름에 든 백분율은 측정이 아니다.
규약: [권장] 목표가 정의된 수치에는 `(목표 <값>)`을 붙인다. **[지킴]** 붙였다면 표기는 한 꼴이다 — 통일성은 게이트 `gendoc`(G16)이 강제한다(2026-09-29 실측: 위반 1·오탐 0). "목표를 붙여야 하는가"는 게이트 밖 사람 판단이다.
