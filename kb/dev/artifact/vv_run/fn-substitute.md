---
id: https://agentic-knowledge-base.dev/id/chunk/4f74f6b4-a466-4f0e-95c2-4f22a919fbd0
type: artifact
level: executable
title_ko: 함수 substitute (tools/vv_run.py)
title: function substitute in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `substitute(cmd, subs)` 다. 명령의 `{{이름}}` 을 실제 경로로 바꾼다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def substitute(cmd: str, subs: dict[str, str]) -> str:
    """명령의 `{{이름}}` 을 실제 경로로 바꾼다. 이름이 `files` 에 있음은 형식 검사(check_case)가 이미 보장한다."""
    return PLACEHOLDER.sub(lambda m: subs.get(m.group(1), m.group(0)), cmd)
```
<!-- 인용 끝 -->
