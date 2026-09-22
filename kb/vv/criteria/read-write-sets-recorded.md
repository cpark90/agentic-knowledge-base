---
id: https://agentic-knowledge-base.dev/id/chunk/01c6af30-b0a6-47c9-b574-578ca00c50c3
type: contract
level: logical
title_ko: 역할마다 읽기·쓰기 plane 이 카탈로그에 있고 쓰기 권한 밖 생성자의 청크는 writer 검사가 거부하며 읽기 집합은 sources 로 옮겨진다
title: Each role's read and write planes are in the catalog, a chunk from a producer without write permission is rejected by the writer check, and the read set is moved into sources
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/c486fdea-7d86-4618-a361-4a9415e7ff4a]
---
**합격 기준** — 기준 종류는 **불변식**이다. `∀ 역할 r: reads(r) ≠ ∅` 이고 `∀ 청크 c: role(generatedBy(c)) = r → kb(c) ∈ writesIn(r) ∧ plane(c) ∈ writes(r)`(인수 예외 포함)이며, 읽기 집합은 `sources(c) ⊇ expanded(workset)` 로 옮겨진다.

**판정식**

- 양성(카탈로그): `bazel test //kg:gate_test` 가 PASS 다. `catalog` 검사 (b) 읽기 plane ≥ 1, (c) 같은 KB 안 쓰기 plane 비공유, `writer` 검사 위반 0 이다.
- 양성(질의): `bazel build //kg:cq` 의 CQ-24 절이 역할 × reads/writes × plane 행을 낸다.
- 음성(쓰기): 쓰기 권한 없는 역할의 청크는 `FAIL [writer] <파일>: 생성자 <by> 의 역할 <역할> 는 KB <kb> 의 <Plane>Chunk 쓰기 권한이 없다 (agt:writesIn · agt:writes) — 담당 역할의 verified(인수) 또는 되돌림 (AGENTS 표 · 11.2절)` 로 끝난다. 서술 표본이다.
- 읽기: `bazel run //tools:handoff -- --workset bazel-bin/kg/workset-<역할>.md <청크>` 가 펼친 청크 IRI 를 `sources` 에 병합한다. 펼친 청크가 없으면 `handoff: 작업 집합에 펼친 청크가 없다` 로 실패한다. `bazel run` 이라 vv_run 밖이다.

**등급** — B 다. 쓰기 집합은 게이트가 판정하고 읽기 집합은 도구 실행이 필요하다.

판정의 원본은 `tools/validate.py` 의 `check_catalog`·`check_writer`, `tools/handoff.py`, `tools/cq-queries/CQ-24.rq` 다. 편집마다 자동으로 읽기 집합을 기록하는 하네스 훅은 없고 `handoff` 가 그 첫 형태다.
