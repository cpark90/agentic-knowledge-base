---
id: https://agentic-knowledge-base.dev/id/chunk/21dfefcf-2982-4759-ab78-89ccc4d425c6
type: artifact
level: executable
title_ko: 파일 tools/tokens.py
title: file tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393]
---
**파일** — `tools/tokens.py` 다. 215줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""토큰 계수기 — 단위 지식 본문의 토큰 수 분포를 고정된 공개 토크나이저로 낸다 (결정 p1-chunk-unit-is-tokens).

크기의 단위는 줄이 아니라 토큰이다(유저 결정 2026-10-01). 상한의 숫자는 측정이 정했고 이 도구가 그 측정을
낸다 — 지식 종류별 분포, 42의 배수마다 초과 단위 지식 수와 비율, 컨텍스트 예산의 환산, 상위 20 단위 지식. 게이트가 아니라
뷰다: 상한의 강제는 `chunk_lint`(게이트 id `chunk`)와 shape(`token-budget`)의 몫이고 이 도구는 분할 대상을
고르는 자리다. 계수기는 `kb_lib.load_tokenizer`(tiktoken o200k_base, 어휘 파일 sha256 고정)이고 네트워크를
쓰지 않는다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나이므로 게이트와 이 도구가 같은 문자열을 센다.
출력은 생성 문서 규약(G1~G18)을 따르며 생성 시각을 적지 않는다 — 같은 입력에서 같은 바이트가 나와야 한다.
사용: bazel run //tools:tokens -- [단위 지식 파일…] [--out report.md] [--vocab <어휘 파일>]
출력·종료: 어휘 파일의 해시가 고정값과 다르면 `FAIL [tokens] …` EXIT_FAIL, 읽을 수 없는 입력·어휘 파일
부재는 EXIT_CONFIG, 검사 대상 0건은 SKIP 이다.
"""
from __future__ import annotations

import argparse
import os
import statistics
import sys
from pathlib import Path
```
<!-- 인용 끝 -->
