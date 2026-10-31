---
id: https://agentic-knowledge-base.dev/id/chunk/60271a33-e150-4e2d-a6ed-728ea04e7ce3
type: decision
level: concrete
title_ko: 두 KB는 서로 읽기만 허용하고 기준은 요구를 거쳐 고치며 저장도 분리한다
title: The two KBs allow only cross-reading, criteria change only via requirements, and storage is separated
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
layer: methodology
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}, {by: process:label-judge-20260912, at: 2026-09-12T12:40:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
part_of: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e
composite: {id: https://agentic-knowledge-base.dev/id/composite/a6634f6f-503c-4e74-8aa1-08d272e2a38e, title_ko: 독립성과 적용 범위, title: Independence and scope, former_title_ko: ["독립성과 스코프"]}
---
**결론** — 두 KB의 적용 범위 규칙.

- **설계·개발** — 개발 KB 읽기·쓰기 / V&V KB **읽기만**. 결함·커버리지·기준을 볼 수 있으나 고칠 수 없다
- **V&V** — 개발 KB 읽기만 / V&V KB 읽기·쓰기
- **감사** — 양쪽 읽기
- **orchestrator** — 개발 KB 읽기·쓰기(dispatch) / V&V KB 읽기

**기준을 고쳐야 할 때 개발 역할은 개발 KB의 요구를 고친다.** 요구가 바뀌면 V&V 역할이 검증 목표와 기준을 다시 파생한다. 기준을 직접 고치는 경로는 없다.

저장도 분리한다 — 별도 저장소 또는 별도 최상위 패키지. 링크가 V&V → 개발 방향으로만 저장되므로 **개발 KB는 V&V KB 없이 빌드되고, V&V KB는 개발 KB 없이 빌드되지 않는다.**

**게이트** (노트 8.5절) — 의존 방향(개발 → V&V 금지)은 `//kb:vv_readers` 가시성이 분석 시점에 막고 게이트 id는 `visibility`다. 개발 역할이 V&V KB에 쓴 흔적의 검사는 없다. 해소는 developer가 의존 방향을 되돌리는 것이다.

`verifies` 밖의 저작 링크(frontmatter 링크 키 `chunk2kg.LINK_KEYS`, `satisfies`·`derivesFrom`·`overlapsWith` 포함)가 `kb/dev`와 `kb/vv`를 가로지르면 `validate`의 `check_cross_kb_link`가 verify 실행 계층의 게이트 `cross-kb-link`로 거부한다(2026-10-04). 예외는 검증 목표(`kb/vv`의 functional 요구)에서 개발 요구로 가는 `derivesFrom` 하나다(`p8-scenario-ladder-rungs`). `defs/kb.bzl`의 `_check_links`는 Bazel deps(`refines`·`serves`·`supersedes`·`verifies`)만 받는데 판정에는 두 끝점의 KB·지식 종류·수준이 필요하므로 병합 그래프를 보는 `validate`가 자리다. 판정 함수 `kb_lib.cross_kb_link`는 복원 후보 생성기 `link`와 공유한다. 2026-10-04 측정에서 가로지름 46은 전부 예외였고 위반은 0이었다. 해소는 저작자가 테스트 케이스와 검증기에서 개발 항목으로 가는 링크를 `verifies`로 바꾸고 그 밖은 지우는 것이다.
