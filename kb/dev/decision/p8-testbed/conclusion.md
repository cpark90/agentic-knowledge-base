---
id: https://agentic-knowledge-base.dev/id/chunk/a9d34ef5-55e0-45eb-876e-b82e717f03d0
type: decision
level: concrete
title_ko: 테스트베드는 3~4단계 환경의 영속적 구현이고 환경 정의는 ODD의 부분집합이다
title: The testbed persists steps 3-4, and its environment is a subset of the ODD
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0139]
part_of: https://agentic-knowledge-base.dev/id/composite/8475c698-2795-4e94-8c13-85e3aa7d85eb
composite: {id: https://agentic-knowledge-base.dev/id/composite/8475c698-2795-4e94-8c13-85e3aa7d85eb, title_ko: 테스트베드, title: The testbed}
---
**결론** — 테스트베드는 **3~4단계 환경의 영속적 구현**이다. 검증 실행 결과가 미래에 재사용되려면 여섯 구성이 갖춰진다.

- **케이스 저장소** — 재현 가능한 concrete 케이스 → `-kg`의 검증 구성체
- **환경 정의** — 각 단계의 mock·인프라·seed 구성 → **ODD의 부분집합**으로 표현
- **실행기** — 검증 청크를 환경에서 실행하고 관측을 기록 → 하네스의 일부
- **관측 저장소** — 실행 기록 → `run-kg`
- **판정기** — 합격 기준 청크를 관측에 적용 → `defect-rules`
- **비교기** — 같은 검증 청크의 리비전에 따른 결과 변화 → `prov:wasRevisionOf` 연쇄 위의 질의

시뮬레이션이 ODD 밖 케이스(`odd:outside`)를 실행하는 것은 허용되되 **커버리지에 넣지 않는다.**
