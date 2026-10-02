---
id: https://agentic-knowledge-base.dev/id/chunk/d16e3817-ff8c-48b7-8c6c-cc5548540854
type: artifact
level: executable
title_ko: 파일 tools/choices.py
title: file tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/7c9d74e6-1a77-4d52-a126-644a65bfab93]
composite: {id: https://agentic-knowledge-base.dev/id/composite/020b2093-af80-4cce-8bce-86ac125c1c4a, title_ko: 파일 복합체 tools/choices.py, title: file composite tools/choices.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/454b2f0a-c75b-42fd-aad2-d24b00a2eb3b, https://agentic-knowledge-base.dev/id/composite/6c9da832-fd4f-4fba-a0f6-33561303de46]}
---
**파일** — `tools/choices.py` 다. 147줄 · 최상위 정의 4개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""설계 공간의 체크박스 뷰 — 열린 설계 변수와 그 후보를 choices.md 로 생성한다 (결정 p9-candidate-storage 13.5절).

후보는 `-space` 청크에 살고 사람에게는 체크박스로 보인다 — `[ ]` 는 열린 후보, `[-]` 는 배제된 후보와 그 근거,
`[x]` 는 확정된 후보다. `[x]` 하나만 남으면 그 변수는 resolved 다. 무엇을 아직 고르지 않았는지 한 화면에서 읽는
것이 이 뷰의 목적이고, 고르는 일은 여기서 하지 않는다 — 확정은 `-space` 청크의 `state` 를 고치고 생성기가 후보를
head 로 옮기는 것이며 그것이 한 줄 diff 로 리뷰된다.

  입력  설계 공간 그래프(`*-space.ttl`, tools/space2kg.py 의 생성물)와 head 그래프(후보·출발 항목의 라벨).
  계산  공간마다 변수(출발 항목 + 링크 타입) · 상태 · 후보의 체크 표시 · 배제 근거 · 양립 제약 · 선호를 낸다.
        체크 표시는 링크 상태에서 온다 — candidate 는 `[ ]`, invalid 는 `[-]`, confirmed 는 `[x]` 다.
  판정  없음 — 뷰이고 게이트가 아니다. 판정은 `//kg:gate_test` 의 `check_space`(게이트 id `space`)가 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음)
사용: choices.py --out choices.md <TTL…>   (bazel build //space:choices)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import Graph, RDF

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
