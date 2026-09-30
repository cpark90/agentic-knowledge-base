---
id: https://agentic-knowledge-base.dev/id/chunk/bd4257e9-f398-4485-8765-92ca4a6348e1
type: artifact
level: executable
title_ko: 파일 tools/impact.py
title: file tools/impact.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-impact}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/05cabe0e-10b0-4e02-81b1-8f5154a94fcc]
composite: {id: https://agentic-knowledge-base.dev/id/composite/711360b7-62ed-4bfc-9088-27974668e958, title_ko: 파일 복합체 tools/impact.py, title: file composite tools/impact.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e3651d6a-824c-47cd-bd83-2db367e84196, https://agentic-knowledge-base.dev/id/composite/44b63663-ac34-40f1-92c6-a6281c93c7a6]}
---
**파일** — `tools/impact.py` 다. 70줄 · 최상위 정의 3개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""영향 분석 1단계 — 변경 전에 "X를 바꾸면 무엇이 영향받는가"를 Bazel 의존 그래프에서 계산한다 (노트 12.6절, method §12).

링크가 deps 이므로 `bazel query rdeps(//kb/..., X)` 가 직접·전이 의존 집합이다. 네 수치를 낸다 —
영향 항목 수 · plane 분포 · suspect 가 될 링크 수(직접 의존자 수) · 유저 승인이 필요한 결정 수.
의미 판정(가정·무효화 전파)은 그래프 질의의 몫이고 이것은 구조 근사다.
사용: bazel run //tools:impact -- //kb/dev/requirement:r-008-every-requirement-descends [--universe //kb/...]
"""
import argparse
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path
```
<!-- 인용 끝 -->
