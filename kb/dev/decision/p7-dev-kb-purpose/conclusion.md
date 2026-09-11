---
id: https://agentic-knowledge-base.dev/id/chunk/50bf2161-6921-4960-b579-060b5f19b8da
type: decision
level: concrete
title_ko: 개발 KB는 요구 명세에서 실산출물을 생산하기 위한 지식이다
title: The development KB is the knowledge for producing real artifacts from requirements
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b850e446-e631-41b6-b47c-48c334c8968e, title_ko: 개발 KB의 목적, title: Purpose of the development KB}
part_of: https://agentic-knowledge-base.dev/id/composite/b850e446-e631-41b6-b47c-48c334c8968e
---
**결론** — 개발 KB는 **요구사항 명세로부터 실질적인 산출물을 생산하기 위한 지식**이다. 담는 것은 "무엇을 만들 것인가, 왜 그렇게, 무엇을 전제로"이고, 담지 않는 것은 "만든 것이 맞는가"(V&V KB, Part VIII)다.

답하는 질문과 근거 — 무엇을 요구받았는가(`requirement`) / 어떻게 정했고 무엇을 배제했는가(`decision` 복합체) / 구성요소끼리 무엇을 약속했는가(`contract`) / 데이터가 어떤 형태로 오가는가(`schema`) / 실제로 무엇이 만들어졌는가(`artifact` 앵커) / 이 전부가 어떤 조건 위에 서 있는가(ODD + `assumes`) (노트 7.1절).
