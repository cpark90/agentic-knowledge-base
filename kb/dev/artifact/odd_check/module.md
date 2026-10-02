---
id: https://agentic-knowledge-base.dev/id/chunk/6f3c841f-1abc-46d4-8902-778ae97eff56
type: artifact
level: executable
title_ko: 파일 tools/odd_check.py
title: file tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/8e83391e-5fd2-499b-881c-37e6f9cb60f1, https://agentic-knowledge-base.dev/id/chunk/2df65a05-0d25-4b3c-aae9-8da6dd82218f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/860d7967-4c4a-48c3-846c-a6f932e81933, title_ko: 파일 복합체 tools/odd_check.py, title: file composite tools/odd_check.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c64a0d92-d978-4b1c-b12e-c03e8e8d1ef9, https://agentic-knowledge-base.dev/id/composite/bdc32d15-06d9-439b-a3b2-0d3dab05225f, https://agentic-knowledge-base.dev/id/composite/f0f7ba13-f15d-489f-80df-4c7ae50b0cdd]}
---
**파일** — `tools/odd_check.py` 다. 105줄 · 최상위 정의 6개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""ODD 모니터링 — 실제 조건(COD)을 ODD 문서의 CHECKS 로 판정해 이탈을 보고한다 (노트 3.5절).

CHECKS.<속성>.cmd 가 있으면 실행한다 — 종료 0 = ODD 안, 1 = 이탈, 그 밖(없음·오류) = unverified.
이탈은 결함이 아니라 신호다: 기본 대응은 작업 중단 + 유저 에스컬레이션이며, 이탈 속성에 의존하는 항목이 무효화 대상이다.
판정 함수(load_odd·judge_condition·judge_all)는 assume_check 가 재사용한다 — 가정의 판정식은 참조 조건 판정의 연언이다.
사용: bazel run //tools:odd_check -- [--odd kb/odd/project-odd.yml] [--out report.md]
"""
import argparse
import os
import subprocess
from pathlib import Path

import yaml

import sys
```
<!-- 인용 끝 -->
