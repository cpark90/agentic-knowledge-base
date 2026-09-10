---
id: https://agentic-knowledge-base.dev/id/chunk/0df66b13-e01e-4119-a581-050ba505a7ec
type: decision
level: logical
title_ko: 형식 검사가 없으면 형식 이탈이 유효한 지식으로 저장된다
title: Without format checks, off-format output is stored as valid knowledge
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/194f050d-929c-4c2c-a42e-887beed7b690
---
**근거** (노트 6.7절) — 에이전트의 출력은 사람의 검토로 걸러지지 않는다(1.1절). 형식 검사가 없으면 형식 이탈이 그대로 저장되고 다음 세션은 그것을 유효한 지식으로 읽는다.

- 세 무효 출력 유형은 서로 다른 실패다. 중간 산출물 반환은 작업 미완료, 형식 오류는 표기 실수, 형식 이탈은 지시 무시다 — 유형별로 통과율을 세야 모델 문제와 프롬프트 문제가 갈린다.
- 모델 교체 시 통과율을 먼저 재는 이유는 게이트의 강도가 모델의 구조화 출력 능력에 의존하기 때문이다. 통과율이 떨어진 채 운영하면 게이트가 병목이 되어 우회 압력이 생긴다.
- T-Box 품질 검사와 A-Box 게이트를 나누는 이유 — 어휘의 결함과 인스턴스의 결함은 고치는 주체와 시점이 다르다.
