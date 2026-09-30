---
id: https://agentic-knowledge-base.dev/id/chunk/58891d47-cbb3-4492-8234-f61f82de97ee
type: artifact
level: executable
title_ko: 절 run-revision (tools/weave.py)
title: section run-revision in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/c0b7f63a-353e-4fdf-9389-961b6f3e130c, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
composite: {id: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637, title_ko: 절 복합체 run-revision (tools/weave.py), title: section composite run-revision in tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/58891d47-cbb3-4492-8234-f61f82de97ee, https://agentic-knowledge-base.dev/id/chunk/f04e6f3f-7688-4b41-a333-5dd88d484ada, https://agentic-knowledge-base.dev/id/chunk/4600b6bb-eddb-4832-9854-1c587f7929d9, https://agentic-knowledge-base.dev/id/chunk/4ed2982d-49b2-4313-856e-6b86a53fb3b0, https://agentic-knowledge-base.dev/id/chunk/4575d9a3-a280-4905-a59f-154e4dac2ae0], part_of: https://agentic-knowledge-base.dev/id/composite/50eac9df-d01a-488f-8254-02ba61b00bf0}
---
**절** — `tools/weave.py` 의 절 `run-revision` 다. audit — 감사 보고서 (로드맵 8단계, audit-self-sufficiency: 체계 밖 정보 없이 생성)

**정의** — `observation_table` · `as_dt` · `render_audit` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── audit — 감사 보고서 (로드맵 8단계, audit-self-sufficiency: 체계 밖 정보 없이 생성) ──────────────────────────────────────
RUN_REVISION = re.compile(r"리비전 `([^`]+)`(?: \(([^)]*)\))?")  # 실행 기록 본문의 리비전 표기 (vv_run.observation)
TABLE_RULE = re.compile(r":?-+:?")










if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- 인용 끝 -->
