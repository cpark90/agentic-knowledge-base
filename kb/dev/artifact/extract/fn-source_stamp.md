---
id: https://agentic-knowledge-base.dev/id/chunk/745c745f-7657-4a5c-8c72-ce2f06a4af0e
type: artifact
level: executable
title_ko: 함수 source_stamp (tools/extract.py)
title: function source_stamp in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `source_stamp(root, src_rel)` 다. 소스 파일의 시각 — git 커밋 시각이 있으면 그것, 없으면 지금 UTC.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_stamp(root: Path, src_rel: str) -> str:
    """소스 파일의 시각 — git 커밋 시각이 있으면 그것, 없으면 지금 UTC. 소스가 바뀔 때만 갱신된다."""
    import subprocess
    try:
        out = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cI", "--", src_rel],
                             capture_output=True, text=True, timeout=20)
        if out.returncode == 0 and out.stdout.strip():
            return datetime.fromisoformat(out.stdout.strip()).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return kb_lib.now_utc()
```
<!-- 인용 끝 -->
