---
id: https://agentic-knowledge-base.dev/id/chunk/2db0c822-35f4-4cf1-b6ab-f74e1627b428
type: artifact
level: executable
title_ko: 파일 tools/gen_skills.py
title: file tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
---
**파일** — `tools/gen_skills.py` 다. 221줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""skill 생성기 — 도구 docstring 과 kb_lib.SKILLS 에서 .claude/skills/<도구-kebab>/SKILL.md 를 생성한다 (로드맵 6단계, agrtls K).

skill 은 손으로 쓰지 않고 지식·절차에서 생성한다. 원본은 둘이다 — 각 도구 모듈의 docstring(첫 문단 = 무엇, `사용:` 줄 = 사용법)과
kb_lib.SKILLS(어떤 도구를 내는가 · 원본 절 앵커 · 언제 쓰는가 · 대표 명령). tools/BUILD.bazel 의 py_binary 목록이 도구의 실재다.
생성물은 트리에 두고 커밋한다(BUILD 와 같은 이유 — 도구가 없어도 skill 이 읽혀야 한다). //:skills_drift_test 가 생성기를 다시
돌려 트리와 비교한다 — docstring·SKILLS 를 고치고 생성을 안 돌린 경우와 손으로 쓴 skill(이중 원본)을 잡는다.
생성 본문도 단정 서술형이다 — kb_lib.check_prose 로 자기 검사한다.
사용: gen_skills.py [--check] [--root .]
출력·종료: 생성 시점 거부(도구·py_binary·docstring·절 앵커 없음, 산문 위반)는 `FAIL [gen-skills] …` EXIT_FAIL,
--check 의 어긋남·손으로 쓴 skill 은 `FAIL [skills-drift] …` EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import ast
import difflib
import re
import sys
from pathlib import Path
```
<!-- 인용 끝 -->
