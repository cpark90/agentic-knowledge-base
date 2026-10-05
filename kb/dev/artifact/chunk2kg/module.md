---
id: https://agentic-knowledge-base.dev/id/chunk/072c3853-c694-43fd-a8b9-c834aa2e363e
type: artifact
level: executable
title_ko: 파일 tools/chunk2kg.py
title: file tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c, https://agentic-knowledge-base.dev/id/chunk/a4678d28-76ed-48df-84de-db8421a8718e]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce, title_ko: 파일 복합체 tools/chunk2kg.py, title: file composite tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24, https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da, https://agentic-knowledge-base.dev/id/composite/067a8c81-640e-4b58-8235-c18119d80f2e]}
---
**파일** — `tools/chunk2kg.py` 다. 1474줄 · 최상위 정의 44개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:tokenCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식은 YAML 부분집합이다 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}. 키마다의 설명은
그 키를 판정·방출하는 절의 주석에 있다 — 기본 키는 `청크 파싱` 절, 링크 키는 `링크의 방출과 정체성` 절,
복합체 키는 `복합체의 순서` 절이다 (규약을 강제하는 코드 옆에 둔다).

출력·종료: 위반은 `FAIL [chunk2kg] <경로>: <메시지>` (병합은 `FAIL [chunk2kg-merge]`, 특수화 사슬은 `FAIL [specialization]`) + EXIT_FAIL,
           읽을 수 없는 입력은 EXIT_CONFIG. 생성기이므로 입력 0건은 빈 그래프(SKIP 아님).
사용: chunk2kg.py --out <생성.ttl> --residency defs/kb.bzl [--vocab <어휘 파일>] <청크 파일들...>
      (--merge 는 --residency·--vocab 없이 조각을 잇기만 한다)
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import os
import re
import sys
from pathlib import Path

try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 이 도구는 rdflib 없이 돌므로(타깃마다 실행) 없으면 같은 값의 폴백
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError:
        kb_lib = None
```
<!-- 인용 끝 -->
