---
id: https://agentic-knowledge-base.dev/id/chunk/2a84b29d-2217-4f0a-80af-ef04b3cb55cb
type: artifact
level: executable
title_ko: 함수 q (tools/impact.py)
title: function q in tools/impact.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-impact}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/44b63663-ac34-40f1-92c6-a6281c93c7a6
---
**함수** — `q(expr, cwd)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def q(expr: str, cwd: str) -> list[str]:
    r = subprocess.run(["bazel", "query", expr, "--noshow_progress", "--output=label"], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr); raise SystemExit(f"impact: bazel query 실패: {expr}")
    return [l for l in r.stdout.split("\n") if l.startswith("//")]
```
<!-- 인용 끝 -->
