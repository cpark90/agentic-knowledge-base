---
id: https://agentic-knowledge-base.dev/id/chunk/12a44438-6b75-4c5f-80b4-c717d7648b5b
type: artifact
level: executable
title_ko: 파일 tools/extract.py
title: file tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
---
**파일** — `tools/extract.py` 다. 548줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""코드 → 단위 지식 추출기 — 소스 하나에서 `artifact` 지식 종류의 파일 항목을 생성한다 (p7-code-extraction-direction).

코드가 원본이고 단위 지식은 생성물이다. 단위 지식 파일을 손으로 고치면 드리프트 게이트(`//:extract_drift_test`)가 거부한다.
tangle(단위 지식 → 코드)은 없다. 정체성의 원본은 소스 옆의 **등록부**(`<소스>.chunks.yml`)이고 한정 이름 → uuid 를 담는다
(p10-function-identity-registry).

추출 범위는 파일 항목뿐이다(유저 답 Q191-a, 2026-11-28). 코드 파일 하나에서 **모듈 항목** 하나(`module.md` — 모듈
docstring 과 import 의 인용)를, 질의 파일 하나에서 **질의 항목** 하나를 낸다. 함수와 클래스, 절, 장, 모듈 머리는 항목으로
올리지 않고 그 원문은 소스에만 있다. 모듈 항목은 부분 없는 단위 지식이라 복합체를 선언하지 않는다. 링크(`refines`·`serves`)와
검증기의 `verifies` 도착점이 파일 항목이다 (p7-code-links-on-file-composite). 정의 사이의 `uses`(agt:usesDefinition)는
정의 단위 지식이 없으므로 내지 않는다.

단위 지식의 `generated.at` 은 **그 단위 지식의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 단위 지식에
다시 찍으면 실제 변경 한 건이 diff 여러 건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다. 코드 파일의 한정 이름은 `module` 하나라 (b) 는 질의 파일에만
걸린다. 추출 트리에서 이번 추출이 만들지 않는 `.md` 는 지운다(`--check` 는 그 파일을 어긋남으로 보고한다).

질의 디렉토리(`EXTRACTED_QUERY_DIRS`, 2026-10-03)는 소스가 디렉토리 `tools/<이름>` 이고 그 안의 `*.rq` 질의 파일 하나가
질의 항목 하나다 — 파일 전체가 인용 하나다. 링크(`refines`·`serves`)는 질의 항목마다 붙는다. 등록부는
`tools/<이름>.chunks.yml` 이고 키는 `query:<파일 이름 stem>` 이다. 등록부의 `refines`·`serves` 는 디렉토리의 질의 전부에
붙고, 질의 하나에만 붙는 `refines` 는 선택 키 `query_refines`(`query:<stem>: [<IRI>…]`)에 적는다 — 질의 파일 하나가 파일
항목 하나의 자리이기 때문이다. 갱신 규칙 (a)~(d) 와 도장은 파이썬 소스와 같고 `source_hash` 는 디렉토리 안 질의 파일 전부의
(이름, 바이트) 해시다(`source_digest`).

Starlark 소스(`EXTRACTED_STARLARK`, 유저 답 Q32-a, 2026-10-04)는 파이썬 소스와 같은 모양이다 — `.bzl` 은 파이썬 문법의
부분집합이므로 같은 AST 로 모듈 머리를 읽는다. 다른 것은 셋이다. 모듈 머리의 `load(...)` 가 import 자리이고, 인용 펜스의
언어가 `starlark` 이며, 생성 패키지는 `kb/dev/artifact/<이름>-bzl` 이다. 등록부의 선택 키 `wiring:` 은 **배선**(입력 집합과
인자를 잇기만 하는 최상위 정의·대입, 유저 답 Q10-a "빌드 배선은 항목이 아니다")의 이름 목록이다 — 추출기는 이름이 소스의
최상위에 실재하는지만 보고, 없는 이름이 목록에 있으면 FAIL 이다.

사용: bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check] [--residency <defs/kb.bzl>]
      bazel run //tools:extract -- tools/cq-queries   (질의 디렉토리 — EXTRACTED_QUERY_DIRS 안이어야 한다)
      bazel run //tools:extract -- defs/kb.bzl        (Starlark 소스 — EXTRACTED_STARLARK 안이어야 한다)
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      --residency 는 EXTRACTED_SOURCES 리터럴의 원본 — 없으면 <루트>/defs/kb.bzl.
출력·종료: 생성 시점 거부는 `FAIL [extract] <경로>: …`, `--check` 의 어긋남은 `FAIL [extract-drift] <경로>: …` —
둘 다 EXIT_FAIL. 읽을 수 없는 입력(EXTRACTED_SOURCES 포함)은 EXIT_CONFIG.
"""

from __future__ import annotations

import argparse
import ast
import difflib
import hashlib
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
```
<!-- 인용 끝 -->
