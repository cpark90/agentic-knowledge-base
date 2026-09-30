---
id: https://agentic-knowledge-base.dev/id/chunk/8fab9e3c-019b-4c6d-84c8-0688df32211a
type: artifact
level: executable
title_ko: 파일 tools/vv_run_env_test.py
title: file tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/2fa82a3a-2e47-4bf8-8d59-2e02da4270dd]
composite: {id: https://agentic-knowledge-base.dev/id/composite/3c8e6ba3-aa11-4e78-b59f-c1aac562f7ce, title_ko: 파일 복합체 tools/vv_run_env_test.py, title: file composite tools/vv_run_env_test.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/585ec158-a9d6-48ce-8ecb-f52c92d2544b, https://agentic-knowledge-base.dev/id/composite/78211421-fa91-4809-8250-0a840db49298, https://agentic-knowledge-base.dev/id/composite/491eacc1-0150-4673-96c8-52951bec7409]}
---
**파일** — `tools/vv_run_env_test.py` 다. 129줄 · 최상위 정의 5개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""실행기 환경 격리 게이트 — 케이스의 명령이 실행기의 파이썬 문맥을 물려받지 않는지 `bazel test` 안에서 판정한다
(결정 p8-verifier-env-isolation, 주석 runner-env-leaks-into-case).

실행기를 어떻게 불렀는가가 케이스의 판정을 바꾸면 그 판정은 재현이 아니다. `bazel run //tools:vv_run` 의 스텁이
`PYTHONSAFEPATH=1` 을 두던 때 케이스가 부르는 검증기는 `import kb_lib` 에서 `ModuleNotFoundError` 로 죽었고
`python3 tools/vv_run.py` 는 같은 케이스를 통과시켰다. `vv_run.clean_env()` 가 그 문맥을 걷어낸다.

**이 게이트는 실행기 전체가 아니라 환경 격리만 판정한다.** 케이스가 `bazel test` 를 부르므로 실행기 전체는
테스트 타깃 안에서 돌릴 수 없다(중첩 실행). 그러나 `clean_env()` 와 `run_command()` 는 bazel 을 부르지 않는다 —
판정 대상을 격리의 동작으로 좁히면 중첩 없이 `bazel test //...` 안에 든다.

판정하는 것은 셋이다.
1. 걷어내는 변수 목록이 규약의 다섯과 정확히 같고, `clean_env()` 가 그 다섯을 **전부** 지운다.
   기대 목록은 이 파일이 자기 상수로 갖는다 — 대상 코드에서 읽으면 목록이 비어도 통과한다.
2. `PYTHONSAFEPATH=1` 을 둔 부모에서 `run_command` 로 읽기 전용 검증기를 실제 하위 프로세스로 띄워 종료 0 이다.
   격리가 없으면 `ModuleNotFoundError` 로 종료 1 이 난다.
3. 하위 프로세스의 작업 디렉토리가 실행기에 건넨 워크스페이스 루트다. 테스트 프로세스의 cwd 를 딴 곳으로 옮겨 놓고
   재므로 상속이 아니라 `cwd=root` 임이 드러난다. 실행기의 루트는 `BUILD_WORKSPACE_DIRECTORY` 다(vv_run.py main).

사용: bazel test //tools:vv_run_env_test
      python3 tools/vv_run_env_test.py [--probe chunk_lint]
종료: 위반 있음 1 (EXIT_FAIL) · 없음 0 (EXIT_OK)
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path
```
<!-- 인용 끝 -->
