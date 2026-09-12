---
id: https://agentic-knowledge-base.dev/id/chunk/36a0b6fa-ac60-47db-a769-b49d067f6854
type: decision
level: concrete
title_ko: 재현성은 검증 청크의 속성이 아니라 환경 할당의 조건이다
title: Reproducibility is a condition of environment assignment, not a chunk attribute
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d, https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0137]
part_of: https://agentic-knowledge-base.dev/id/composite/c71e12a1-2a31-43f5-af40-c670d767f559
composite: {id: https://agentic-knowledge-base.dev/id/composite/c71e12a1-2a31-43f5-af40-c670d767f559, title_ko: 검증의 재현성, title: Reproducibility of verification}
---
**결론** — 1~4단계 검증 청크는 **재현 가능해야 한다.** concrete 케이스가 재현 가능하려면 다음이 기록된다.

- **초기 상태** — 지식 베이스의 리비전 + ODD 버전 + 환경 구성
- **자극 열** — 순서 있는 입력, 시각 포함
- **난수 seed** — 합성 데이터·자동 응답의 seed
- **환경 버전** — 실행 단계, mock 버전, 인프라 버전
- **에이전트 버전**(에이전트 검증 시) — 모델, 하네스, 스코프 버전

**재현이 안 되는 검증은 5~6단계로 강등된다.** 재현성은 검증 청크의 속성이 아니라 **환경 할당의 조건**이다.

실행 기록에서 일반화할 때(6.3절 일반화) 재현 가능한 형태로 만들 수 없는 관측은 `origin:observed` 태그를 유지한 채 6단계 관측으로 남긴다 — 억지로 concrete 케이스로 만들지 않는다.
