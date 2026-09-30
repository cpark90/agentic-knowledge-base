---
id: https://agentic-knowledge-base.dev/id/chunk/1c0459c2-171f-4194-9719-75449a207951
type: artifact
level: executable
title_ko: 파일 tools/labels.py
title: file tools/labels.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-labels}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f367e186-3a1a-4660-aeb4-7473d4b28b2a, title_ko: 파일 복합체 tools/labels.py, title: file composite tools/labels.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/019a25f2-901b-47ff-94e4-2449c78f7e2b, https://agentic-knowledge-base.dev/id/composite/fba87a37-4ad2-4ccb-b556-a27d4ef6b9d2]}
---
**파일** — `tools/labels.py` 다. 79줄 · 최상위 정의 2개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""라벨 목록 뷰 — 청크 파일들의 head에서 index.md를 생성한다 (노트 5.6절, 부록 E.2).

index.md는 OKF 예약 파일이며 손으로 쓰지 않는다 (유저 결정 2026-09-10 Q4). 라벨 목록이
본문보다 먼저 읽히는 것(4.4절)의 파일 형태이고, 생성물이어야 본문과 어긋나지 않는다.
절은 plane 디렉토리(h2)와 그 안의 항목 디렉토리(h3)로 갈리고, 링크는 저장소 루트 기준
경로다 — 생성물이 전 패키지를 한 파일로 합치므로 파일명 상대 링크는 성립하지 않는다 (규약 G13).

사용: labels.py --out index.md <청크 파일...>
"""
import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path
```
<!-- 인용 끝 -->
