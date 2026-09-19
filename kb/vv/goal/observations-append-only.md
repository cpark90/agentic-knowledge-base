---
id: https://agentic-knowledge-base.dev/id/chunk/63187a4f-7908-4cad-8128-60b70edb99bd
type: requirement
level: functional
pattern: ubiquitous
title_ko: 검증 실행의 관측은 concrete 실행 기록으로 append-only 저장되어야 한다
title: Observations of a verification run must be stored as append-only concrete run records
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d]
---
**검증 목표** — 관측된 실행이 `agt:Run`이며 concrete 전용·append-only라는 결정이 실행기와 게이트로 강제된다는 것이 보여져야 한다. 실행 기록은 memory plane의 청크로 저장되고 고쳐지지 않는다.

- **이해관계자**: 검증 역할 · 감사 역할 · **관심사**: 관측

**무엇을 관측하면 성립하는가**

- `vv_run --record`가 `kb/vv/run/run-<UTC>.md`를 새 파일로만 만들고, 같은 이름이 있으면 `FAIL [vv_run] … 이미 있다 — 실행 기록은 append-only 다 (r-026)`로 거부한다.
- 실행 기록은 `type: memory`·`level: concrete`이고 `memory`의 허용 구간은 `concrete` 하나뿐이라 다른 수준은 분석 시점에 실패한다.
- 커밋된 실행 기록 전부가 청크 검사와 게이트를 통과하고 head 그래프에 오른다. 감사 보고서의 최근 실행 절이 그것을 인용한다.

판정의 원본은 `tools/vv_run.py`의 `main`(덮어쓰기 거부)과 `defs/kb.bzl`의 `RESIDENCY["memory"]`다.
