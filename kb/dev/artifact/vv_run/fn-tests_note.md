---
id: https://agentic-knowledge-base.dev/id/chunk/dda506f2-0686-4187-a9dc-b23cf1e83388
type: artifact
level: executable
title_ko: 함수 tests_note (tools/vv_run.py)
title: function tests_note in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `tests_note(commands)` 다. 케이스의 실행 명령이 돌린 테스트 수와 캐시 재사용 수 — `테스트 3 · 캐시 3`.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tests_note(commands: list[dict]) -> str:
    """케이스의 실행 명령이 돌린 테스트 수와 캐시 재사용 수 — `테스트 3 · 캐시 3`. 요약 줄이 없으면 빈 문자열."""
    ran = [c for c in commands if c["skip"] is None and c.get("tests")]
    if not ran:
        return ""
    total = sum(c["tests"][0] for c in ran)
    executed = sum(c["tests"][1] for c in ran)
    return f"테스트 {total} · 캐시 {total - executed}"
```
<!-- 인용 끝 -->
