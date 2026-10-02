---
id: https://agentic-knowledge-base.dev/id/chunk/0deeb79a-02b2-44fa-9441-ad82b1ed51af
type: artifact
level: executable
title_ko: 함수 run (tools/revalidate.py)
title: function run in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `run(cmd, cwd, check)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run(cmd: list, cwd: str, check: bool = True) -> str:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(f"revalidate: 실패: {' '.join(cmd)}")
    return r.stdout
```
<!-- 인용 끝 -->
