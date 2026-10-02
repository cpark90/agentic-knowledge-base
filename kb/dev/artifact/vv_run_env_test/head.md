---
id: https://agentic-knowledge-base.dev/id/chunk/585ec158-a9d6-48ce-8ecb-f52c92d2544b
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/vv_run_env_test.py)
title: module head gate in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/2fa82a3a-2e47-4bf8-8d59-2e02da4270dd]
part_of: https://agentic-knowledge-base.dev/id/composite/3c8e6ba3-aa11-4e78-b59f-c1aac562f7ce
---
**모듈 머리** — `tools/vv_run_env_test.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 종료 코드 규약의 단일 정의처
import vv_run  # noqa: E402 — 판정 대상. clean_env·run_command 는 bazel 을 부르지 않는다

GATE = kb_lib.VV_RUN_ENV_GATE
# 규약이 걷어내는 다섯. **이 목록은 이 파일이 자기 기대로 갖는다** — vv_run.BAZEL_PY_ENV 에서 읽으면 그 목록이
# 비거나 줄어도 이 검사가 통과해 아무것도 판정하지 않는다 (결정 p8-verifier-env-isolation 의 결론 문장이 원본이다)
EXPECTED_ENV = ("PYTHONSAFEPATH", "PYTHONPATH", "PYTHONHOME", "RUNFILES_DIR", "RUNFILES_MANIFEST_FILE")
SENTINEL = "VV_RUN_ENV_SENTINEL"  # 격리가 환경 전체를 비우지 않고 다섯만 걷어내는지 — PATH 가 사라지면 검증기가 돌지 않는다
CWD_PROBE = 'python3 -c "import os; print(os.getcwd())"'
```
<!-- 인용 끝 -->
