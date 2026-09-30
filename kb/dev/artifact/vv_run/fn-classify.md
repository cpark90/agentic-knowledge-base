---
id: https://agentic-knowledge-base.dev/id/chunk/2c7856fb-c6fb-42fb-bc34-c18e19362e57
type: artifact
level: executable
title_ko: 함수 classify (tools/vv_run.py)
title: function classify in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `classify(cmd, spec)` 다. 명령 하나의 SKIP 사유 — 실행 대상이면 None.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def classify(cmd: str, spec: dict) -> str | None:
    """명령 하나의 SKIP 사유 — 실행 대상이면 None. 자극·기대를 갖춘 케이스는 읽기 전용 검증기를 직접 부르는 음성 명령까지 실행한다."""
    if cmd.startswith(POSITIVE_PREFIXES):
        return None
    if cmd.startswith(VERIFIER_PREFIXES):
        if not spec:
            return "기계가 읽는 자극·기대가 없다 — 케이스에 `yaml` 펜스(`files`·`expect`)를 둔다 (p8-machine-readable-case)"
        return unsafe(cmd)
    if "/tmp/" in cmd:
        return "케이스가 임시 파일 경로를 적었다 — 경로는 검증기가 정한다. `files` 의 이름을 `{{이름}}` 으로 가리킨다"
    head = " ".join(cmd.split()[:2])
    return f"`{head}` — 실행 대상은 허용 목록의 읽기 전용 검증기뿐"
```
<!-- 인용 끝 -->
