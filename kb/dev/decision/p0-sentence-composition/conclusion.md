---
id: https://agentic-knowledge-base.dev/id/chunk/859aeb88-b65f-422a-9549-6592005b47aa
type: decision
level: concrete
title_ko: 산문의 문장은 판정 하나에 이유와 조건을 잇고 문장 사이의 관계를 접속어로 드러낸다
title: A prose sentence carries one judgement with its reasons and conditions joined, and connectives show how sentences relate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T00:40:22+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/021b81f0-1ca3-4627-99cd-d603cd2eda2e
composite: {id: https://agentic-knowledge-base.dev/id/composite/021b81f0-1ca3-4627-99cd-d603cd2eda2e, title_ko: 산문의 문장 구성, title: Prose sentence composition}
---
**결론** — 산문의 문장은 다음 아홉 규칙으로 짠다(유저 답 Q104-a, 2026-10-23). 대상은 문서와 단위 지식의 본문, 채널 메시지, 질문지, 세션 보고다. 종결형과 어조는 결정 `p0-prose-assertive-register`가 따로 정한다.

1. 한 문장에는 판정 하나를 담고, 그 판정의 이유와 조건은 연결어미로 같은 문장에 붙인다. 짧은 단정문이 셋 이상 이어지면 합친다.
1. 문장 사이의 관계는 접속어로 드러낸다. 원인은 "그래서"나 "따라서", 대조는 "그러나"나 "반면", 제한은 "다만", 대체는 "대신"으로 잇는다.
1. 산문에는 기호(`=`, `+`, `→`, `×`)와 영어 논리어를 쓰지 않는다.
1. 문장은 명사형이 아니라 서술어로 끝낸다.
1. 셋 이상을 나열할 때는 가운뎃점 대신 "와/과"와 쉼표로 잇는다.
1. 출처 괄호는 문장 끝이나 문단 끝에 모은다. 대시는 라벨 구분자와 부제에만 쓴다.
1. 지시어가 가리킬 수 있는 대상이 둘 이상이면 명사를 되풀이하고 주어를 밝힌다.
1. 한글 표준어가 있으면 한글로 쓰고 영문은 첫 등장에만 함께 적는다. 영어 상태값은 한국어 서술어로 풀어 쓰고, 식별자 앞에는 그 종류를 가리키는 명사를 붙인다.
1. 문단은 주제문으로 시작하고, 비유는 실제 동작을 적는 문장으로 바꾼다.

명세 작성 규격 9.5절의 "및·그리고·또한으로 잇지 않는다"는 원자성이 필요한 EARS 요구 문장에만 적용한다. 규칙 3·4·5·6은 `consistency`가 보고 지표로 세고, 나머지는 리뷰가 판정한다. 둘 다 게이트가 아니다. 이미 있는 단위 지식은 새로 쓰거나 다른 이유로 고칠 때 이 규칙에 맞춘다. 일괄 재서술은 유저가 규범 문서의 결과를 읽은 뒤 다시 정한다.
