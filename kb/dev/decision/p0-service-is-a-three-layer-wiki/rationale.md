---
id: https://agentic-knowledge-base.dev/id/chunk/1c6140ac-741b-4d1f-8ba1-025d02020e91
type: decision
level: logical
title_ko: 서비스의 정의가 없으면 통일의 기준이 없고 층은 plane과 직교해야 결정이 두 역할을 가질 수 있다
title: Without a service definition there is no unification criterion, and layers must be orthogonal to planes so a decision can hold either role
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-03T18:13:57+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-03T19:53:33+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c4b958be-e5e4-43b6-b23f-989f628cb07f
---
**근거** — 유저의 지적은 둘이다: 세부가 기획과 다르고, 전체가 하나의 서비스로 통일되지 않고 산발적이다. 산발의 실측은 도구 37·그래프 로더 11·뷰 매크로마다 선언·skill 20 대 도구 37·손 문서 15·로드맵의 "첫 형태" 19곳이다. 무엇을 기준으로 다듬을지는 서비스의 정의가 정한다 — 정의가 "에이전트 하네스 제품"이면 통일 축은 실행 표면이고, "지식 베이스 자체"면 지식 층이다. 유저가 셋(지식·방법론·프로세스)을 한 위키로 정의했으므로 그 셋이 층이고 통일 축은 "모든 것이 한 층의 항목이거나 투영인가"다.

층을 plane의 상위 분류가 아니라 직교 속성으로 두는 까닭은 같은 plane의 항목이 다른 역할을 갖기 때문이다. 결정 plane에 분야의 결정(지식)과 저작 규칙의 결정(방법론)이 함께 있고, 요구 plane에도 같다. plane을 층 아래로 넣으면 그 둘을 가를 수 없다. 기본값을 지식으로 두는 까닭은 항목 대부분이 그것이고 표시 누락이 산발로 세어지지 않게 하려는 것이다 — 방법론·프로세스는 명시한다.

규범 문서를 투영으로 두는 까닭은 `p12-documents-are-generated`다. 손 문서 15 가운데 수치를 저장한 자리가 열에 하나 낡아 있었다(현상 P18 실측). 원본이 청크이고 문서가 생성되면 그 어긋남이 없다. 노트를 동결하는 까닭은 기획 원본의 정정이 의도 대 노트의 어긋남이 확인된 자리에서만 일어나야 하기 때문이다 — 42줄/토큰이 그 첫 사례다.

편입이 제거보다 앞서는 까닭은 유저 지시다. 산발은 잘못 만들어진 것이 아니라 층의 형식을 얻지 못한 것이다.

뷰·skill을 투영으로 두는 근거는 유저 답 Q9-a(2026-10-03)다. 뷰 13 가운데 열둘은 생성기 함수가 이미 `layer: process` 코드 청크이고(orchestrator 실측 2026-10-03), skill은 도구 docstring 청크와 `kb_lib` 절 청크에서 생성된다. 내용이 원본 청크에서 결정론적으로 나오므로 층을 원본만 가져야 같은 것을 두 번 세지 않는다. 빌드 배선을 항목에서 빼는 근거는 유저 답 Q10-a(2026-10-03)다. 손 BUILD와 `defs/*.bzl`의 배선은 무엇을 어떤 입력으로 돌리는지의 정의이고, 그 의미는 게이트 개체와 도구 청크가 이미 담는다.
