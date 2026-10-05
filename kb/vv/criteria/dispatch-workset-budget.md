---
id: https://agentic-knowledge-base.dev/id/chunk/7db997bc-4f86-4b0c-aa3f-e941657a94a7
type: contract
level: logical
title_ko: 앵커를 준 역할별 작업 집합 뷰는 스코프 plane 밖 청크를 담지 않고 5,418토큰 예산 안이다
title: An anchored per-role workset view holds no chunk outside the scope planes and fits within the 5,418-token budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-05T12:48:58+09:00}
verified: [{by: vnv/claude-sonnet-5-5, at: 2026-10-05T12:49:06+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/7a0e2c24-70d8-4d00-ae0f-d083b8ec87a8]
---
**합격 기준** — 기준 종류는 **불변식**이다. `workset(role, window, anchor) = {c ∈ live | plane(c) ∈ reads(role) ∪ writes(role) ∧ level(c) ∈ window}` 에서 앵커 1홉 이웃만 본문을 펼치고 `tokens(view) ≤ budget` 이다.

**판정식**

- 양성(예산): `bazel build //kg:workset --//kb:role=vnv --//kb:anchor=<IRI 또는 라벨 부분>` 이 성공하고 `bazel-bin/kg/workset-vnv.md` 의 머리 `예산 판정` 줄이 `→ 예산 안` 으로 끝난다.
- 양성(스코프): 같은 생성물의 라벨 목록 첫 줄이 `scope: vnv` 와 조건 목록·수준 창을 적고, 목록의 plane 이 카탈로그의 `agt:reads`·`agt:writes` 안이다.
- 양성(준수율): `bazel build //kg:metrics` 의 `2단계 대리` 절에 역할별 `n/d = p.p%` 가 있다.
- 음성(앵커): 작업 집합 안에 없는 앵커는 `workset: 앵커 '<값>' 를 작업 집합 안에서 찾지 못했다` 로 생성이 실패한다. 서술 표본이다.
- 음성(예산): 앵커 없는 전체 목록은 `예산 초과` 로 판정된다. 케이스 `labels-before-bodies` 가 그 표본이다.

**등급** — A 다. 판정은 생성 뷰의 머리 줄이고 사람 판단이 없다.

판정의 원본은 `tools/workset.py` 의 `verdict` 계산과 `defs/kb.bzl` 의 `kb_workset_view`(빌드 설정 `//kb:role`·`anchor`·`levels`·`hops`·`budget`)다. 앵커가 있으면 예산 초과를 `FAIL [workset-budget]` 과 종료 1로 거부하고(결정 `p1-workset-budget-fails-only-with-anchor`) 앵커가 없으면 판정만 적고 종료 0이다.
