---
id: https://agentic-knowledge-base.dev/id/chunk/47f637c1-3a8e-46a9-8814-2d6afdd6ef03
type: decision
level: logical
title_ko: 글이 어색했던 원인은 번역투가 아니라 문장 사이의 연결이 빠진 데 있었다
title: The prose read awkwardly because links between sentences were missing, not because of translationese
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:40:22+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/021b81f0-1ca3-4627-99cd-d603cd2eda2e
---
**근거** — 유저는 저장소의 글이 문맥상 어색해 뜻을 파악하기 어렵다고 했다(2026-10-23). 같은 날 진단한 결과, "~에 대한"이나 "~되어진" 같은 번역투는 100문장에 2~3건으로 드물었다. 대신 단위 지식 문장의 51%가 35자 이하였고, 접속어로 시작하는 문장은 1%에 못 미쳤으며, 짧은 문장이 셋 이상 이어지는 구간이 196곳이었다. 1,000자마다 가운뎃점이 9.7개, 괄호가 9.3개, 대시가 7.4개 나와 조사와 서술어의 자리를 기호가 차지했다. 따라서 원인은 문장 사이의 연결이 빠진 데 있었다. 그때의 규칙은 문장을 나누라고만 했고 이으라고는 하지 않았으므로, 규칙을 지킬수록 문장이 끊겼다.

아홉 규칙은 다음 출처에서 왔다. 국립국어원의 「2019년 중앙행정기관 공공언어 진단」은 접속 오류, 조사와 성분의 생략, 번역투, 너무 길거나 짧은 문장을 감점한다. 「행정 효율과 협업 촉진에 관한 규정」 제7조는 외국어를 뜻 전달에 필요할 때만 괄호로 함께 적게 한다. 김순영(2012, 『새국어생활』 22-1)은 "가지다", "~에 의해" 같은 번역투를 능동형과 풀어 쓰기로 고친다. Microsoft 한국어 현지화 스타일 가이드는 대시를 문장으로 풀고 흐린 대명사를 명사로 밝히게 한다. Google 개발자 문서 스타일 가이드는 끊긴 문장을 피하고 전환어를 쓰며 중요한 정보를 괄호에 넣지 않게 한다. 어느 기준도 "-다" 평서형을 문제 삼지 않으므로 단정 서술형은 그대로 둔다.

유저는 단정 서술형 결정을 둘로 나누기로 했다(유저 답 Q104-a, 2026-10-23). 종결형과 어조는 유저가 정한 것이고, 문장 구성은 조사 근거로 정한 것이어서 고칠 근거가 다르기 때문이다. 기호와 명사형 끝맺음, 가운뎃점 연쇄, 괄호 위치는 정규식으로 셀 수 있어 보고 지표로 두고, 접속어의 적절성과 지시어, 주제문은 판정이 필요해 리뷰에 맡긴다.
