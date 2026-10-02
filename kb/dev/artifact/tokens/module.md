---
id: https://agentic-knowledge-base.dev/id/chunk/21dfefcf-2982-4759-ab78-89ccc4d425c6
type: artifact
level: executable
title_ko: 파일 tools/tokens.py
title: file tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T11:12:02Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4fe35c96-c167-4a3e-b640-a888f6bcefe5, title_ko: 파일 복합체 tools/tokens.py, title: file composite tools/tokens.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/47cbe988-791e-493e-b71c-1671f649b23a, https://agentic-knowledge-base.dev/id/composite/ee6ebd51-06bf-439a-875f-bf4afa341c35, https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5]}
---
**파일** — `tools/tokens.py` 다. 207줄 · 최상위 정의 9개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""토큰 계수기 — 청크 본문의 토큰 수 분포를 고정된 공개 토크나이저로 낸다 (결정 p1-chunk-unit-is-tokens).

크기의 단위는 줄이 아니라 토큰이다(유저 결정 2026-10-01). 상한의 숫자는 실측이 정했고 이 도구가 그 실측을
낸다 — plane 별 분포, 42의 배수마다 초과 청크 수와 비율, 컨텍스트 예산의 환산, 상위 20 청크. 게이트가 아니라
뷰다: 상한의 강제는 `chunk_lint`(게이트 id `chunk`)와 shape(`token-budget`)의 몫이고 이 도구는 분할 대상을
고르는 자리다. 계수기는 `kb_lib.load_tokenizer`(tiktoken o200k_base, 어휘 파일 sha256 고정)이고 네트워크를
쓰지 않는다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나이므로 게이트와 이 도구가 같은 문자열을 센다.
출력은 생성 문서 규약(G1~G18)을 따르며 생성 시각을 적지 않는다 — 같은 입력에서 같은 바이트가 나와야 한다.
사용: bazel run //tools:tokens -- [청크 파일…] [--out report.md] [--vocab <어휘 파일>]
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
