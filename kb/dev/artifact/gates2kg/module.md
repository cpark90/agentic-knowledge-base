---
id: https://agentic-knowledge-base.dev/id/chunk/3365f616-57b5-475b-b2a4-955e5d05881c
type: artifact
level: executable
title_ko: 파일 tools/gates2kg.py
title: file tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T16:06:51Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4f1a7107-6da2-49a5-b29b-7bc2f257f90a, title_ko: 파일 복합체 tools/gates2kg.py, title: file composite tools/gates2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5b36dc12-5981-480b-b53b-b3d740e777b7, https://agentic-knowledge-base.dev/id/composite/ff1c5437-57a6-409e-86e7-767ffd3d41ff, https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1]}
---
**파일** — `tools/gates2kg.py` 다. 139줄 · 최상위 정의 4개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""게이트 등록부(`defs/kb.bzl` 의 `GATES`) → 게이트 그래프(-kg.ttl) 생성기 (M1 단일 정의처, 2026-10-02).

게이트는 프로세스 층의 **항목**이다(결정 p0-service-is-a-three-layer-wiki) — 어느 청크의 투영으로도 환원되지
않으므로 그래프에 개체가 서야 층별 집계(CQ-38)가 셀 자리를 갖는다. 2026-10-01 실측에서 같은 목록이 넷으로
갈려 있었고(상수 26 · 코드의 태그 · 총람의 `id` 열 · 하네스 목록) 단일 정의처가 없다는 것이 그 진단이었다.

원본은 `GATES`·`TOOL_TAGS` 리터럴이고 TTL 은 생성물이다 — `kg/` 에 손으로 쓰지 않는다(`odd2kg`·`space2kg` 와
같은 자리). 개체 하나가 게이트 하나이고 IRI 는 `id:gate-<게이트 id>` 다. 도구 태그(`TOOL_TAGS`)는 게이트가
아니므로 개체를 받지 않는다.

생성 = 검사:
  - 항목마다 네 키(`tier`·`tool`·`ko`·`desc`)가 있고 `tier` 는 `GATE_TIERS` 안이다
  - 판정 도구가 파이썬 안이면 등록부 사이드카(`tools/<도구>.chunks.yml`)의 `ids: file:` 이 실재한다 —
    `agt:enforcedBy` 의 대상이 그 파일 복합체이고, 없으면 끊긴 링크를 내는 대신 여기서 거부한다
  - 파이썬 밖(`starlark`·`bazel`)인 게이트는 가리킬 코드 청크가 없어 `agt:enforcedBy` 를 갖지 않는다

사용: gates2kg.py --out gates-kg.ttl --gates defs/kb.bzl [--registry tools/<도구>.chunks.yml ...]
출력·종료: 위반은 `FAIL [gates2kg] <원본>: <메시지>` + EXIT_FAIL. 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:  # 리터럴 읽기와 종료 코드 규약의 단일 정의처는 kb_lib 다
    from tools import kb_lib
except ImportError:
    import kb_lib
```
<!-- 인용 끝 -->
