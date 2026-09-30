---
id: https://agentic-knowledge-base.dev/id/chunk/98e08ae7-f85a-4703-809f-fe20c8ac333a
type: artifact
level: executable
title_ko: 함수 git (tools/stamp.py)
title: function git in tools/stamp.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-stamp}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:27:50Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9de96dc9-03ab-40b9-a90a-4481f8f9deb7
---
**함수** — `git(root, *args)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def git(root: Path, *args: str) -> tuple[int, str]:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=30)
        return out.returncode, out.stdout.strip()
    except (OSError, subprocess.SubprocessError) as e:
        return 1, str(e)
```
<!-- 인용 끝 -->
