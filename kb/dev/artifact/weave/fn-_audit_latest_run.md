---
id: https://agentic-knowledge-base.dev/id/chunk/38bf7453-3138-4cc0-937e-f2cb1026219f
type: artifact
level: executable
title_ko: 함수 _audit_latest_run (tools/weave.py)
title: function _audit_latest_run in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f04e6f3f-7688-4b41-a333-5dd88d484ada, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_latest_run(m, runs, latest_run, run_body, by_gen)` 다. `kb/vv/run/` 의 최신 실행 기록 요약 — 기록을 그대로 옮긴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_latest_run(m: Model, runs: list, latest_run, run_body: str, by_gen) -> list[str]:
    """`kb/vv/run/` 의 최신 실행 기록 요약 — 기록을 그대로 옮긴다 (agt:Run, append-only)."""
    body: list[str] = []
    # 3. 최근 실행 — 실행 기록을 그대로 요약한다
    body += ["## 최근 실행 — `kb/vv/run/` 의 최신 실행 기록 (agt:Run, append-only)", ""]
    if latest_run is None:
        body += ["실행 기록 없음 — `bazel run //tools:vv_run -- --record`", ""]
    else:
        rows = observation_table(run_body, kb_lib.RUN_CASE_TABLE_HEADER)
        verdicts = Counter(r[2] for r in rows if len(r) >= 3)
        body += [f"- {m.ko(latest_run)} (`{m.location[latest_run]}`, 생성 {m.at(latest_run)}, {by_gen(latest_run)}) — 실행 기록 전체 {len(runs)}건",
              "- 케이스 " + " · ".join(f"{v} **{verdicts.get(v, 0)}**" for v in kb_lib.RUN_VERDICTS) + " — SKIP 은 PASS 가 아니다", ""]
        first = run_body.split("\n", 1)[0].strip()
        if first:
            body += [f"> {first}", ""]
        if rows:
            body += [kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"] + ["| " + " | ".join(r) + " |" for r in rows] + [""]
        else:
            body += [f"- 본문에 케이스 표(헤더 `{kb_lib.RUN_CASE_TABLE_HEADER}`)가 없다", ""]
    return body
```
<!-- 인용 끝 -->
