---
id: https://agentic-knowledge-base.dev/id/chunk/1c0459c2-171f-4194-9719-75449a207951
type: artifact
level: executable
title_ko: 파일 tools/labels.py
title: file tools/labels.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-labels}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
---
**파일** — `tools/labels.py` 다. 79줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""라벨 목록 뷰 — 단위 지식 파일들의 head에서 index.md를 생성한다 (노트 5.6절, 부록 E.2).

index.md는 OKF 예약 파일이며 손으로 쓰지 않는다 (유저 결정 2026-09-10 Q4). 라벨 목록이
본문보다 먼저 읽히는 것(4.4절)의 파일 형태이고, 생성물이어야 본문과 어긋나지 않는다.
절은 지식 종류 디렉토리(h2)와 그 안의 항목 디렉토리(h3)로 갈리고, 링크는 저장소 루트 기준
경로다 — 생성물이 전 패키지를 한 파일로 합치므로 파일명 상대 링크는 성립하지 않는다 (규약 G13).

사용: labels.py --out index.md <단위 지식 파일...>
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path
```
<!-- 인용 끝 -->
