---
id: https://agentic-knowledge-base.dev/id/chunk/b43bbf0b-8cd2-4a3c-9acb-56a1fa9e8a63
type: artifact
level: executable
title_ko: 함수 unsafe (tools/vv_run.py)
title: function unsafe in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `unsafe(cmd)` 다. 허용 목록 안이어도 실행하지 않는 사유 — 안전하면 None.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def unsafe(cmd: str) -> str | None:
    """허용 목록 안이어도 실행하지 않는 사유 — 안전하면 None. 검증기의 진입점만 허용 목록이 정하므로 인자 쪽도 본다."""
    if RECORD_FLAG.search(cmd):
        return "`--record` 는 관측을 쓴다 — 케이스의 검증기는 읽기 전용이어야 한다. 인자를 뺀다"
    m = OUT_FLAG.search(cmd)
    if m and not m.group(1).startswith("{{"):
        return "`--out` 이 저장소 안 경로에 쓴다 — 케이스의 검증기는 읽기 전용이어야 한다. 인자를 빼거나 `{{이름}}` 자극으로 가리킨다"
    if UNSAFE.search(cmd):
        return "리다이렉션·파이프·백틱 — 검증기의 출력을 파일이나 다른 명령으로 보내지 않는다"
    for inner in SUBSTITUTION.findall(cmd):
        if not inner.strip().startswith(SUBSTITUTION_HEADS):
            return f"명령 치환 `$({inner.strip()[:40]})` — 치환 안은 목록 조회(`ls`·`find`·`git rev-parse`)뿐이다"
    return None
```
<!-- 인용 끝 -->
