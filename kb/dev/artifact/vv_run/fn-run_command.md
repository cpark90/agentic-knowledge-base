---
id: https://agentic-knowledge-base.dev/id/chunk/72467e81-75de-4b48-92ac-2d429de91d8e
type: artifact
level: executable
title_ko: 함수 run_command (tools/vv_run.py)
title: function run_command in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `run_command(cmd, root)` 다. 셸로 실행 — 워크스페이스 루트에서.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run_command(cmd: str, root: Path) -> dict:
    """셸로 실행 — 워크스페이스 루트에서. 종료 코드·소요·출력 꼬리를 남긴다."""
    t0 = time.monotonic()
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, env=clean_env())
    out = r.stdout + r.stderr
    tail = "\n".join(out.strip().splitlines()[-6:])
    m = EXECUTED.search(out)
    tests = (int(m.group(2)), int(m.group(1))) if m else None  # (전체, 실행) — 없으면 요약 줄이 없는 실패
    return {"rc": r.returncode, "secs": time.monotonic() - t0, "tail": tail, "out": out, "tests": tests}
```
<!-- 인용 끝 -->
