---
id: https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd
type: decision
level: concrete
title_ko: 코드는 원본이고 함수 청크는 추출된 생성물이며 드리프트 게이트가 둘의 일치를 강제한다
title: Code is the source, function chunks are extracted artefacts, and a drift gate enforces their agreement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-10-05T00:30:10+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T00:30:20+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/cfdffdf2-c863-4f22-bdfc-2d58e26550be
composite: {id: https://agentic-knowledge-base.dev/id/composite/cfdffdf2-c863-4f22-bdfc-2d58e26550be, title_ko: 코드의 추출 방향, title: The extraction direction for code}
---
**결론** — 코드를 청크로 올리되 **생성 방향은 추출**이다(유저 답 2026-09-30 "권고대로"). `tools/*.py`가 원본이고 함수 청크(`artifact` plane, `executable` 수준)는 추출기 `extract`의 생성물이다. 청크 파일을 손으로 고치면 드리프트 게이트 `extract_drift`가 거부한다. tangle(청크 → 파일)은 없다.

| 항목 | 정함 |
|---|---|
| 원본 | 소스 파일. 출처 개체 `id:src-<경로>`가 `sources`에 선다 |
| 생성물 | 함수 하나 = 청크 하나(본문은 소스를 코드 펜스로 인용 — 생성기는 원문을 고쳐 쓰지 않는다) + 파일 청크(모듈 docstring·상수·import) |
| 도장 | `artifact`의 `verified`는 사람이 아니라 **테스트 통과**(`process:bazel-test` + 리비전)다 — 수정마다 재판정이 자동이다 |
| 예산 | `artifact`의 토큰 상한은 **프로파일 파라미터**다. 1,092토큰이 인위적 분할을 부르면 그 plane만 값을 따로 둔다 |
| 범위 | 전부 올리는 것이 목표다. 표본 `tools/kb_lib.py` 하나로 churn(재판정 건수·게이트 시간·`revalidate` 후보)을 한 주기 잰 뒤 34 파일로 넓힌다 |

추출은 코드 편집을 그대로 둔다 — 잦은 변경에 가장 강인한 형태다. 링크·가정을 손으로 달 자리가 생성물에 없다는 대가는 파일 복합체가 진다(`p7-code-links-on-file-composite`).
