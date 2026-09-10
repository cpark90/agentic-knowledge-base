---
id: https://agentic-knowledge-base.dev/id/chunk/55aa8967-2f34-41d4-bb94-d84f7272c7cd
type: decision
level: concrete
title_ko: level은 요구에서 산출물까지의 정제 수준다
title: Level is the refinement height from requirement to artifact
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0005]
part_of: https://agentic-knowledge-base.dev/id/composite/5ef6f4a9-343a-4f00-8e88-172521022d6b
composite: {id: https://agentic-knowledge-base.dev/id/composite/5ef6f4a9-343a-4f00-8e88-172521022d6b, title_ko: 정제 계층의 정의, title: Definition of the refinement ladder}
---
**결론** — level은 **요구에서 실산출물까지의 정제 수준**다. plane과 직교하고, 모든 지식은 다섯 단계 중 하나에 거주하며 단계마다 거주 plane과 판정 방식이 정해져 있다.

- **functional** — 요구사항. 자연어(EARS 권장), 이해관계자·관심사 명시. `requirement` **전용**. 합의로 판정. 기계가독 아님
- **abstract** — 설계·계약의 형식화. 변수는 있되 범위 없음. `decision`·`contract`. 형식 검사
- **logical** — 범위·제약·**합격 기준**. 판정식이 여기서 태어난다. `contract`·`schema`·`decision`. 제약 검사
- **concrete** — 특정 값·케이스·고정 입력. **표본 추출 근거 필수**. `schema`·`decision`·`artifact`. 근거 검사
- **executable** — 실산출물(코드·테스트·설정·모델의 head + 앵커). `artifact` **전용**. 실행으로 판정

**양 끝이 plane 전용이다.** 계층는 요구에서 시작해 산출물에서 끝나고 그 사이 세 단계가 정제다. 이 정의에서 계층는 상황의 추상화가 아니라 **요구가 산출물이 되는 사슬**이다.

**단계를 건너뛰지 않는다** — functional에서 곧바로 executable로 가는 것이 에이전트의 기본 동작이며, 그것이 문제의 원인이다.
