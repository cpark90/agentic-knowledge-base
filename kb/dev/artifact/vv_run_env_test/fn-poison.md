---
id: https://agentic-knowledge-base.dev/id/chunk/34277117-5c2c-4fcc-9a6d-fa0bb51bac85
type: artifact
level: executable
title_ko: 함수 poison (tools/vv_run_env_test.py)
title: function poison in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/78211421-fa91-4809-8250-0a840db49298
---
**함수** — `poison(names)` 다. 부모 환경에 실행기의 bazel 파이썬 문맥을 심는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def poison(names: tuple[str, ...]) -> None:
    """부모 환경에 실행기의 bazel 파이썬 문맥을 심는다 — 실제 `bazel run` 이 하위 프로세스에 넘기던 값이다."""
    for n in names:
        os.environ[n] = "1" if n == "PYTHONSAFEPATH" else "/nonexistent/vv-run-env"
    os.environ[SENTINEL] = "keep"
```
<!-- 인용 끝 -->
