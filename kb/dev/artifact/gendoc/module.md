---
id: https://agentic-knowledge-base.dev/id/chunk/0a421535-c9ff-40ab-a04f-cd96deb799a9
type: artifact
level: executable
title_ko: 파일 tools/gendoc.py
title: file tools/gendoc.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gendoc}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/160ca62a-0dd2-4b06-a5e5-21bb1fc54fbe, https://agentic-knowledge-base.dev/id/chunk/61906023-e4bb-46b1-a6db-4bf4635b631b, https://agentic-knowledge-base.dev/id/chunk/2314093a-f5e3-4fc0-96a0-6c5d35db03ee]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f2a94f2c-1866-41da-848c-d018a7dfc647, title_ko: 파일 복합체 tools/gendoc.py, title: file composite tools/gendoc.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c0b686cd-daa8-4f89-8cb1-9e142f072f04, https://agentic-knowledge-base.dev/id/composite/b6587551-3784-48fb-ae97-e98493afa24b]}
---
**파일** — `tools/gendoc.py` 다. 101줄 · 최상위 정의 1개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""생성 문서 게이트 — 에이전트가 만드는 마크다운의 가독성·건전성 규약 G1~G18 (유저 지시 2026-09-21).

규약의 단일 정의처는 `tools/kb_lib.py` 다 (STYLEGUIDE §7). 이 도구는 그 `check_gendoc` 을 파일들에 돌린다.
생성기가 같은 모듈의 `gendoc_header` 로 머리 블록을 내므로, 출력 형태는 생성 전에 고정되고 파싱·형식 복구가 필요 없다.

  머리 블록  G1 h1 한 줄이 첫 줄이고 `(생성 파일)` 로 끝난다 · G2 생성기와 규약 버전 · G3 생성 시각(ISO 8601 UTC 초) ·
             G4 입력 파일 목록과 내용 지문(SHA-256 앞 12자)과 규모 수치 · G5 질의 · G6 자기 자신을 다시 만드는 명령 ·
             G7 성격 경고 한 줄. 순서가 고정이다.
  본문 서식  G8 제목 계층은 한 단계씩 (MD001) · G9 h1 은 문서당 하나 (MD025) · G10 표의 헤더·열 수·앞뒤 빈 줄
             (MD055·MD056·MD058) · G11 펜스에 언어 (MD040) · G12 본문 120줄 초과면 목차 절 (ISO/IEC/IEEE 26514:2022 9.10.5) ·
             G13 링크의 경로·앵커가 생성물이 놓이는 위치 기준으로 실재 · G14 빈 값은 `없음` 하나.
  건전성     G15 비율은 `n/d = p.p%` — 분모 없는 백분율을 쓰지 않는다 · G16 목표 표기 `(목표 <값>)` 의 통일성(2026-09-29
             게이트화 — "붙여야 하는가"는 사람 판단으로 남는다) · G18 산문은 단정 서술형 (STYLEGUIDE §0).
             G17 시점 의존 표현은 권장이고 게이트가 아니다 — 후보만 `kb_lib.check_gendoc` 의 둘째 반환값으로 낸다
             (2026-09-29 오탐률 실측, 후보 전부가 오탐).

생성 트리 파일(`.claude/skills/*/SKILL.md`)은 `--deterministic` 대상이다 — 생성 시각과 지문을 넣으면 드리프트
바이트 비교가 매번 깨지므로 그 둘을 빼고, 결정론이 그 자리의 건전성 장치라는 사실을 성격 경고 줄에 적는다.

출력  FAIL [gendoc] <파일>:<줄>: <근거>
종료  위반 → EXIT_FAIL · 입력 파일 없음·루트 밖 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)

사용  gendoc.py [--root DIR] <생성 문서 ...>
      bazel test //:gendoc_test
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:  # 규약의 단일 정의처는 kb_lib (STYLEGUIDE §7)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError as e:
        raise SystemExit(f"FAIL [gendoc] kb_lib 을 찾을 수 없다 — {e}")
```
<!-- 인용 끝 -->
