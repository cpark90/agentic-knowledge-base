---
id: https://agentic-knowledge-base.dev/id/chunk/4b6ece88-9936-435d-b114-96c75670880e
type: artifact
level: executable
title_ko: 함수 clean_env (tools/vv_run.py)
title: function clean_env in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `clean_env()` 다. 실행기 자신의 bazel 파이썬 문맥을 뺀 환경 — 케이스의 검증기는 워크스페이스 셸에서 부른 것과 같아야 한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def clean_env() -> dict[str, str]:
    """실행기 자신의 bazel 파이썬 문맥을 뺀 환경 — 케이스의 검증기는 워크스페이스 셸에서 부른 것과 같아야 한다.

    `bazel run //tools:vv_run` 의 스텁은 `PYTHONSAFEPATH=1` 을 두고, 그러면 하위 프로세스의 `python3 tools/validate.py` 가
    스크립트 디렉토리를 sys.path 에 얹지 못해 `import kb_lib` 에서 죽는다 — 자극에 닿기 전이다. runfiles 쪽 변수도 뺀다.
    실행기를 어떻게 불렀는가가 케이스의 판정을 바꾸면 그 판정은 재현되지 않는다 (p8-reproducibility).
    """
    return {k: v for k, v in os.environ.items() if k not in BAZEL_PY_ENV}
```
<!-- 인용 끝 -->
