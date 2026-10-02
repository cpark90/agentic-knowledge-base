---
id: https://agentic-knowledge-base.dev/id/chunk/8dd4f994-1cfe-41c8-a207-73df40d60c1e
type: artifact
level: executable
title_ko: 함수 pip_closure_path (tools/vv_run.py)
title: function pip_closure_path in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `pip_closure_path()` 다. vv_run 자신의 `sys.path` 에서 하네스의 pip 폐포(site-packages) 항목만 모은 `PYTHONPATH` 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pip_closure_path() -> str:
    """vv_run 자신의 `sys.path` 에서 하네스의 pip 폐포(site-packages) 항목만 모은 `PYTHONPATH` 값.

    `bazel run //tools:vv_run` 로 돌면 이 과정 자신의 `sys.path` 에 자신이 선언한 서드파티 의존(`pyyaml`·`rdflib`·
    `tiktoken`)의 site-packages 경로가 이미 들어 있다 — vv_run 의 BUILD 의존에 `tiktoken` 을 더한 것(이 처리의 유일한
    배선 변경)이 그 경로를 끼운다. `PIP_CLOSURE_MARKERS` 로 그 항목만 고르고 runfiles 사본의 `tools/`(이 저장소 코드)는
    뺀다 — 검증기는 `--vocab` 인자 없이도 `KB_TOKENIZER_VOCAB` 로 같은 어휘를 찾되, 도구 모듈은 여전히 소스 트리에서
    읽는다(cwd=워크스페이스 루트가 그 몫을 한다).
    """
    return os.pathsep.join(p for p in sys.path if any(m in p for m in PIP_CLOSURE_MARKERS))
```
<!-- 인용 끝 -->
