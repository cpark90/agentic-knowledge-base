---
id: https://agentic-knowledge-base.dev/id/chunk/58891d47-cbb3-4492-8234-f61f82de97ee
type: artifact
level: executable
title_ko: 절 run-revision (tools/weave.py)
title: section run-revision in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/c0b7f63a-353e-4fdf-9389-961b6f3e130c, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
composite: {id: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637, title_ko: 절 복합체 run-revision (tools/weave.py), title: section composite run-revision in tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/58891d47-cbb3-4492-8234-f61f82de97ee, https://agentic-knowledge-base.dev/id/chunk/f04e6f3f-7688-4b41-a333-5dd88d484ada, https://agentic-knowledge-base.dev/id/chunk/4600b6bb-eddb-4832-9854-1c587f7929d9, https://agentic-knowledge-base.dev/id/chunk/7ca2da27-a5fc-4b33-aa68-b855ee61d697], part_of: https://agentic-knowledge-base.dev/id/composite/027b8f3a-1382-4deb-a204-543e912d8e6a}
---
**절** — `tools/weave.py` 의 절 `run-revision` 다. 재료 — 관측 본문의 표와 시각을 읽는다

**정의** — `observation_table` · `as_dt` · `round_section` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 재료 — 관측 본문의 표와 시각을 읽는다 ────────────────────
RUN_REVISION = re.compile(r"리비전 `([^`]+)`(?: \(([^)]*)\))?")  # 실행 기록 본문의 리비전 표기 (vv_run.observation)
TABLE_RULE = re.compile(r":?-+:?")
```
<!-- 인용 끝 -->
