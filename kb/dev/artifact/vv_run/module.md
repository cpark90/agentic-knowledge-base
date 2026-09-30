---
id: https://agentic-knowledge-base.dev/id/chunk/eebf4050-9c69-46a9-9906-f194b78fd23f
type: artifact
level: executable
title_ko: 파일 tools/vv_run.py
title: file tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296, https://agentic-knowledge-base.dev/id/chunk/b8d74a2d-f94b-4fe7-8b3b-13dca638d338, https://agentic-knowledge-base.dev/id/chunk/36a0b6fa-ac60-47db-a769-b49d067f6854]
composite: {id: https://agentic-knowledge-base.dev/id/composite/5fc8dfb1-4583-4c27-8266-44c34557e4c1, title_ko: 파일 복합체 tools/vv_run.py, title: file composite tools/vv_run.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/663886da-0e72-42f0-ba6b-3dfbf495e462, https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f, https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f, https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991, https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164]}
---
**파일** — `tools/vv_run.py` 다. 577줄 · 최상위 정의 23개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""V&V executor — 케이스의 실행 명령 중 허용 목록의 양성 명령을 실행하고 결과를 실행 기록으로 남긴다 (노트 8.20절 executor,
r-026 관측은 append-only 실행 기록, p0-run-as-observation `agt:Run`, p8-vv-plane-instances memory = 실행 기록, p8-reproducibility).

케이스(`kb/vv/case/*.md`)마다 본문의 `**실행 명령**` 줄(코드 스팬 하나가 명령이다)을 읽어 명령을 `;`·`&&` 로 나눈다. **허용 목록(`bazel test`·`bazel build`·`bazel query`·
`python3 tools/gen_build.py --check`)으로 시작하는 읽기 전용 검증기만 실행한다**. 그 밖(그 밖의 `python3 …` · `bazel run …`)은 실행하지 않고
SKIP 으로 적는다. **SKIP 은 PASS 가 아니다** (docs/tools.md 실패 종류 3).

**기계가 읽는 자극·기대** (결정 p8-machine-readable-case): 케이스는 `**자극**`·`**기대**` 산문 옆에 `yaml` 펜스를 두고 키 둘을 적는다.
`files` 는 `이름: 내용` 매핑이고 검증기가 명령 앞에 임시 디렉토리로 쓰고 뒤에 지운다 — **임시 파일의 경로는 검증기가 정한다.** 케이스는 명령
안에서 그 파일을 `{{이름}}` 으로 가리키고 검증기가 실제 경로로 바꾼다. `expect` 는 명령 순서마다 `exit`(기대 종료 코드)와 `contains`(출력에서
찾을 문구)를 적는다. **판정은 둘 다 맞아야 pass** 다 — 종료 코드만 보면 "실패했는가" 는 알아도 "무엇이 거부되는가" 는 모른다. 자극과 기대를
갖춘 케이스는 저장소의 읽기 전용 검증기를 직접 부르는 음성 명령(`python3 tools/<검증기>.py`)까지 실행한다. **`bazel run //tools:<검증기>` 형태는
허용 목록 밖이다** — `bazel run` 은 runfiles 트리에서 돌아 워크스페이스 상대 경로 인자를 자극이 아닌 runfiles 의 없는 파일로 풀고, 그때 나오는
입력 단계 오류가 기대한 거부와 같은 종료 코드·문구를 내 케이스를 거짓 pass 로 만든다.
읽기 전용 검증기 목록에는 `assume_check`(가정 판정·전파, `--break <조건>` 은 호스트 상태를 읽고 ODD 판정을 가상으로
바꾸는 실험 플래그일 뿐 저장소를 쓰지 않아 안전하다)를 포함한다. 그래도 검증기 자신이 파일을 쓰는 인자
(`--record`·`{{이름}}` 자극이 아닌 저장소 안 경로의 `--out`)를 가진 호출은 허용 목록 안이어도 실행하지 않고 SKIP 한다 —
허용 목록은 명령의 진입점이 아니라 무엇을 할 수 있는가의 경계다(`unsafe()`).
**점진 도입이다** — 펜스가 없거나 규약 키가 없는 케이스는 지금처럼 양성 명령만 돌고 판정도 그대로다.
케이스 형식은 `FAIL [vv-case]` 로 거부한다 — 규약 밖 키, `expect` 항목 수 ≠ 명령 수, `files` 에 없는 `{{이름}}`, 경로를 담은 이름,
검증기를 `bazel run //tools:<검증기>` 로 부르는 명령.
면제는 `docs/waivers.md` 가 같은 게이트 id 로 선언한다(축 `파일`·`stem`).
케이스 판정: 실행한 명령이 하나라도 기대와 어긋나면 fail · **명령 전부를 실행해** 전부 기대와 맞으면 pass · 그 밖(건너뛴 명령이 있거나 실행한
명령이 없음)은 skip. 건너뛴 쪽이 "게이트가 거부한다" 를 보이는 절반이므로 절반만 실행한 케이스는 pass 가 아니다. 판정 어휘는 셋
그대로이고(kb_lib.RUN_VERDICTS) 명령 단위 실행·건너뜀·기대 대조 수를 보고와 실행 기록의 요약에 따로 적는다.
재현성 기록 (p8-reproducibility 초기 상태·환경): 리비전(`git rev-parse --short HEAD`, 워킹트리 변경 여부) · 시각(UTC) · bazel·python 버전 ·
명령마다 종료 코드·소요. 난수 seed 는 없다 — 명령은 결정적이다. 명령은 워크스페이스 루트를 cwd 로, 실행기 자신의 bazel 파이썬 문맥
(`PYTHONSAFEPATH`·`PYTHONPATH`·`RUNFILES_*`)을 뺀 환경에서 돈다 — 실행기를 어떻게 불렀는가가 판정을 바꾸면 그 판정은 재현되지 않는다.

--record 는 실행 기록을 관측(memory plane, concrete, append-only)으로 kb/vv/run/run-<UTC>.md 에 쓴다 — generated.by 는 역할이 아닌
`process:vv_run` 이라 writer 검사 밖이다(카탈로그의 executor 하위 역할을 도구가 맡는 첫 형태). 이미 있는 파일은 덮지 않는다.
생성 뒤 python3 tools/gen_build.py --root . 로 BUILD 를 갱신하고 bazel test //... 를 돌린다.
케이스가 `bazel test` 를 부르므로 `bazel run` 안에서는 중첩 실행이 된다 — odd_check 의 language_policy 와 같은 형태다. 문제가 나면
`bazel run` 밖에서 python3 tools/vv_run.py 로 돌린다.

사용: bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--out report.md] [--waivers docs/waivers.md]
      python3 tools/vv_run.py [--record] [--case <슬러그>…]
종료: fail 있음 1 (EXIT_FAIL) · 전부 pass 0 (EXIT_OK) · pass 없이 skip 만 3 (EXIT_SKIP) · 입력·케이스 형식 문제 2 (EXIT_CONFIG)
"""
from __future__ import annotations

import argparse
import difflib
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import yaml  # 케이스 본문의 `yaml` 펜스(자극·기대) — space2kg·odd2kg 와 같은 잠금
```
<!-- 인용 끝 -->
