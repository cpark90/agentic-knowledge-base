---
id: https://agentic-knowledge-base.dev/id/chunk/2a753a77-e144-454d-9eda-42b7be3846db
type: artifact
level: executable
title_ko: 함수 judge_condition (tools/odd_check.py)
title: function judge_condition in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/bdc32d15-06d9-439b-a3b2-0d3dab05225f
---
**함수** — `judge_condition(check, root)` 다. 조건 하나의 판정 — cmd 종료 0 = in, 1 = out, 그 밖(없음·오류) = unverified.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_condition(check: dict, root: Path) -> str:
    """조건 하나의 판정 — cmd 종료 0 = in, 1 = out, 그 밖(없음·오류) = unverified."""
    cmd = check.get("cmd")
    if not cmd:
        return "unverified"
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True)
    return "in" if r.returncode == 0 else "out" if r.returncode == 1 else "unverified"
```
<!-- 인용 끝 -->
