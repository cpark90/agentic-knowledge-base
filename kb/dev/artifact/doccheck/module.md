---
id: https://agentic-knowledge-base.dev/id/chunk/b0a0581f-f939-44a3-9cb5-e4ab7398ab94
type: artifact
level: executable
title_ko: 파일 tools/doccheck.py
title: file tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d, title_ko: 파일 복합체 tools/doccheck.py, title: file composite tools/doccheck.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/782db9bf-fe98-4c49-89d5-5143bc44c0c6, https://agentic-knowledge-base.dev/id/composite/41567349-5994-4e9e-aec7-ac6603e2e6f5, https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984, https://agentic-knowledge-base.dev/id/composite/fc4042df-b620-47ee-b006-cf1ceb777197, https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3, https://agentic-knowledge-base.dev/id/composite/00affe30-5483-412c-9fa9-9df66b0b6eaf, https://agentic-knowledge-base.dev/id/composite/7ac51f50-ae24-4b21-944d-11721fe1653c]}
---
**파일** — `tools/doccheck.py` 다. 495줄 · 최상위 정의 16개 · 최상위 절 7개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""문서 현행성 게이트 — 죽은 링크·앵커·경로 (agrtls-practices-review N, 2026-09-12).

대상은 진입점 문서(README·AGENTS·STYLEGUIDE·CLAUDE·INTENT)와 docs/**/*.md, 그리고 하네스 문서
(harness/README.md · harness/agents/*.md · harness/user/README.md)다. 채널 메시지(harness/channel/**)·질문지
(harness/user/Q-*.md · harness/user/archive/**)·옛 채널 기록(legacy/)은 소멸성 소통 기록이라 대상이 아니고 링크
대상으로만 쓴다(채널 규약은 게이트 `channel`). 노트(docs/agent-knowledge-system-notes.md)는 유저 문서라 링크
대상으로만 쓴다(--target-only). 기계적으로 참·거짓이 갈리는 것만 게이트다 — 나머지는 검토 재료.

  links   마크다운 링크 [..](경로#앵커): 경로가 실재하고, #앵커는 대상 .md 파일 제목의 GitHub slug 와
          일치한다 (소문자, 공백→'-', 문자·숫자·'-'·'_' 외 제거, 같은 slug 는 -1, -2 …).
          스킴이 있는 것(http·https·mailto·urn …)은 건너뛴다. 코드 펜스·코드 스팬 안은 링크가 아니다.
  paths   백틱 안의 저장소 경로 — kb/ kg/ tools/ docs/ defs/ chunks/ space/ harness/ .claude/ 로 시작하는 것 — 가
          실재한다. 패턴·자리표시자·Bazel 라벨·생성물은 건너뛴다: `*` `<` `{` `…` `$` `//` `bazel-bin/`
          `bazel-out` `.wip` 을 포함하거나 `~` 로 시작하는 것. 생성물은 `bazel-bin/` 접두로 적는 것이
          규칙이다 — 표지가 아니라 규칙이므로 `kg/chunks-kg.ttl` 처럼 적힌 생성물은 없는 경로로 잡힌다.
          `파일:줄` 표기는 파일만 본다. 경로에는 ':' 이 없으므로 그 밖의 ':' 은 라벨로 보고 건너뛴다.
  prose   산문 문체 (STYLEGUIDE §0 단정 서술형, 유저 결정 2026-09-13) — 경어·비격식 종결(습니다·세요·해요·죠 …)이 문장 끝에
          오거나 산문에 느낌표가 있다 (kb_lib.check_prose 가 단일 정의처). 코드 펜스·코드 스팬·HTML 주석·따옴표 안과 `!=`·`![`
          는 산문이 아니다. --waivers(docs/waivers.md)에 게이트 id `prose`(축 파일)로 면제된 문서는 세지 않는다. 추측·구어는
          판정이 필요하므로 게이트가 아니라 consistency ⑦ 보고다.

  report  **보고 모드**(`--report`, 게이트가 아니다) — 문서(위치 인자, 없으면 진입점 문서 넷 `REPORT_DOCS`)가 적은
          수치를 생성물의 같은 이름 값과 쌍으로 대조해 어긋난 쌍을 센다. 위치 인자를 주면 `REPORT_DOCS` 대신 그
          목록을 대조 대상으로 쓰고, **이 모드에서만** 루트 밖 절대 경로를 허용한다(`report_doc_path` — `vv_run`
          이 케이스 자극을 워크스페이스 밖 임시 디렉토리에 두므로, 2026-10-01 vnv 요청). 이름 열넷의 원본은 V&V 기준
          `kb/vv/criteria/document-table-matches-generated.md` 의 대조 대상 목록이고, 현상은 `agt:documentLag`(P18)이다.
          짝짓기는 이름 뒤 24자 창의 수치이므로 근사다 — 이름과 값이 산문으로 떨어져 있으면 쌍이 서지 않는다.
          시점을 선언한 스냅샷 단락은 대조 밖이고, 생성물 원본이 없는 이름은 문서가 생성 명령이나 시각을 병기하면
          기준의 둘째 절로 합격이다. 생성물이 없으면(`bazel-bin` 미빌드) 그 이름을 건너뛴다고 적는다.

출력  FAIL [doccheck|prose] <파일>:<줄>: <종류> <대상> — 근거 · REPORT [doccheck] <파일>:<줄> <이름> 문서 <값> ↔ 생성물 <값>
종료  위반 → EXIT_FAIL · 입력 파일 없음/루트 밖/인자 오류 → EXIT_CONFIG · 검사 대상 0건 → EXIT_SKIP (PASS 가 아니다)
      `--report` 는 판정이 아니므로 어긋난 쌍이 있어도 0 이다.

사용  doccheck.py [--root DIR] [--waivers FILE] <문서 ...> [--target-only FILE ...]
      bazel run //tools:doccheck -- *.md docs/*.md --target-only docs/agent-knowledge-system-notes.md
      bazel run //tools:doccheck -- --report      # 문서 수치 대 생성물 수치, FAIL 아님 (진입점 문서 넷)
      bazel run //tools:doccheck -- --report /tmp/x/doc.md   # 위치 인자가 있으면 그 문서로 바꾼다, 루트 밖도 된다
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
