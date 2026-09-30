---
id: https://agentic-knowledge-base.dev/id/chunk/b0a0581f-f939-44a3-9cb5-e4ab7398ab94
type: artifact
level: executable
title_ko: 파일 tools/doccheck.py
title: file tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d, title_ko: 파일 복합체 tools/doccheck.py, title: file composite tools/doccheck.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/782db9bf-fe98-4c49-89d5-5143bc44c0c6, https://agentic-knowledge-base.dev/id/composite/41567349-5994-4e9e-aec7-ac6603e2e6f5, https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984]}
---
**파일** — `tools/doccheck.py` 다. 204줄 · 최상위 정의 6개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""문서 현행성 게이트 — 죽은 링크·앵커·경로 (agrtls-practices-review N, 2026-09-12).

대상은 진입점 문서(README·AGENTS·STYLEGUIDE·CLAUDE·INTENT)와 docs/**/*.md 다. 채널(docs/feedback/**)은
소멸성이라 대상이 아니고(hci 스캔 몫), 노트(docs/agent-knowledge-system-notes.md)는 유저 문서라 링크
대상으로만 쓴다(--target-only). 기계적으로 참·거짓이 갈리는 것만 게이트다 — 나머지는 검토 재료.

  links   마크다운 링크 [..](경로#앵커): 경로가 실재하고, #앵커는 대상 .md 파일 제목의 GitHub slug 와
          일치한다 (소문자, 공백→'-', 문자·숫자·'-'·'_' 외 제거, 같은 slug 는 -1, -2 …).
          스킴이 있는 것(http·https·mailto·urn …)은 건너뛴다. 코드 펜스·코드 스팬 안은 링크가 아니다.
  paths   백틱 안의 저장소 경로 — kb/ kg/ tools/ docs/ defs/ chunks/ space/ .claude/ 로 시작하는 것 — 가
          실재한다. 패턴·자리표시자·Bazel 라벨·생성물은 건너뛴다: `*` `<` `{` `…` `$` `//` `bazel-bin/`
          `bazel-out` `.wip` 을 포함하거나 `~` 로 시작하는 것. 생성물은 `bazel-bin/` 접두로 적는 것이
          규칙이다 — 표지가 아니라 규칙이므로 `kg/chunks-kg.ttl` 처럼 적힌 생성물은 없는 경로로 잡힌다.
          `파일:줄` 표기는 파일만 본다. 경로에는 ':' 이 없으므로 그 밖의 ':' 은 라벨로 보고 건너뛴다.
  prose   산문 문체 (STYLEGUIDE §0 단정 서술형, 유저 결정 2026-09-13) — 경어·비격식 종결(습니다·세요·해요·죠 …)이 문장 끝에
          오거나 산문에 느낌표가 있다 (kb_lib.check_prose 가 단일 정의처). 코드 펜스·코드 스팬·HTML 주석·따옴표 안과 `!=`·`![`
          는 산문이 아니다. --waivers(docs/waivers.md)에 게이트 id `prose`(축 파일)로 면제된 문서는 세지 않는다. 추측·구어는
          판정이 필요하므로 게이트가 아니라 consistency ⑦ 보고다.

출력  FAIL [doccheck|prose] <파일>:<줄>: <종류> <대상> — 근거
종료  위반 → EXIT_FAIL · 입력 파일 없음/루트 밖/인자 오류 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)

사용  doccheck.py [--root DIR] [--waivers FILE] <문서 ...> [--target-only FILE ...]
      bazel run //tools:doccheck -- *.md docs/*.md docs/open-questions/*.md --target-only docs/agent-knowledge-system-notes.md
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      실재 판정은 루트 아래 파일계로 한다 — 테스트에서는 선언된 입력(runfiles)만 실재한다.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.parse
from pathlib import Path

try:  # 규약 상수·마크다운 헬퍼의 단일 정의처는 kb_lib (STYLEGUIDE §7)
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    try:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    except ImportError as e:  # 산문 검사·앵커 규칙의 단일 정의처라 없으면 돌릴 수 없다
        raise SystemExit(f"FAIL [doccheck] kb_lib 을 찾을 수 없다 — {e}")
```
<!-- 인용 끝 -->
