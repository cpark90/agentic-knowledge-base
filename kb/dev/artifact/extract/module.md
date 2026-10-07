---
id: https://agentic-knowledge-base.dev/id/chunk/12a44438-6b75-4c5f-80b4-c717d7648b5b
type: artifact
level: executable
title_ko: 파일 tools/extract.py
title: file tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
composite: {id: https://agentic-knowledge-base.dev/id/composite/99abae51-6823-4ed8-9bfe-4255801d4681, title_ko: 파일 복합체 tools/extract.py, title: file composite tools/extract.py, ordered: [https://agentic-knowledge-base.dev/id/composite/57a845e1-da27-4d9d-b5b0-b25148ccece7, https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53, https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef, https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685, https://agentic-knowledge-base.dev/id/composite/30b84220-a222-44db-9ae1-0486db2a18ec, https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0, https://agentic-knowledge-base.dev/id/composite/bdbaec34-7407-4d5e-83f8-0706026f0b98, https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166, https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0]}
---
**파일** — `tools/extract.py` 다. 994줄 · 최상위 정의 42개 · 최상위 절 9개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""코드 → 청크 추출기 — 소스 파일 하나에서 `artifact` plane 의 청크 트리를 생성한다 (p7-code-extraction-direction).

코드가 원본이고 청크는 생성물이다. 청크 파일을 손으로 고치면 드리프트 게이트(`//:extract_drift_test`)가 거부한다.
tangle(청크 → 코드)은 없다. 정체성의 원본은 소스 옆의 **등록부**(`<소스>.chunks.yml`)이고 한정 이름 → uuid 를 담는다 —
이름이 바뀌어도 uuid 가 유지되므로 개명이 청크의 삭제 + 신설로 보이지 않는다 (p10-split-keeps-work-identity).

구조는 파일 → 절 → 함수의 세 단이다 (p7-code-links-on-file-composite). 파일 복합체의 선언 청크가 **파일 청크**(`module.md` — 모듈
docstring 과 import)이고 링크(`refines`·`serves`)와 검증기의 `verifies` 도착점이 거기다. 그 부분은 소스의 절
주석(`# ══ 장` · `# ── 절`)이 여는 **절 복합체**이고, 절 복합체의 부분은 절 청크와 그 절의 정의 청크다.
직접 부분은 9개를 넘을 수 없으므로(4.5절) 넘는 절은 잘라 맞추지 않고 절 주석을 요구한다 — 순서에 뜻이 없는 묶음을
만들지 않는다.

정의 청크는 선택 키 `uses: [<청크 IRI>…]` 를 갖는다 — 최상위 정의를 이름으로 쓰는 관계이고 `chunk2kg` 가
`agt:usesDefinition`(references 족의 잎)으로 방출한다. 해소는 AST 의 이름 참조뿐이며 제외는 `used_defs` 와
`used_foreign_defs` 에 적혀 있다. 링크 키가 아니므로 Bazel `deps` 도 링크 개체도 되지 않는다 — 링크는 파일 복합체의
것이다. 경계는 둘이고 둘 다 `--residency`(기본 `<루트>/defs/kb.bzl`) 의 리터럴이 단일 정의처다(M1). **방출 경계**
`EXTRACTED_SOURCES` 안의 소스에서만 내고(2026-10-01 — 표본 하나에서 먼저 내고 링크 밀도·게이트 시간을 잰 뒤 37 파일
전부로 넓혔다, 유저 답 1), **치역 경계** `USES_TARGETS` 안의 모듈만 모듈 밖 대상으로 삼는다(2026-10-01, 유저 답 1 —
표본 쌍 `kb_lib` 하나부터). 치역 경계 밖의 모듈을 가리키는 호출은 내지 않는다 — 넓히는 일은 그 리터럴에 이름을
더하는 것이다.

청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 청크에
다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다.

질의 디렉토리(`EXTRACTED_QUERY_DIRS`, 2026-10-03)는 다른 모양이다. 소스가 디렉토리 `tools/<이름>` 이고 그 안의
`*.rq` 질의 파일 하나가 청크 하나다 — 질의는 함수로 나뉘지 않으므로 파일 전체가 인용 하나이고 복합체를 세우지 않는다.
링크(`refines`·`serves`)는 청크마다 붙는다 — 질의 파일이 곧 링크의 자리다. 등록부는 `tools/<이름>.chunks.yml` 이고
키는 `query:<파일 이름 stem>` 이다. 등록부의 `refines`·`serves` 는 디렉토리의 질의 전부에 붙고, 질의 하나에만 붙는 `refines` 는
선택 키 `query_refines`(`query:<stem>: [<IRI>…]`)에 적는다 — 질의 파일 하나가 파일 복합체 하나의 자리이기 때문이다.
갱신 규칙 (a)~(d) 와 도장은 파이썬 소스와 같고 `source_hash` 는 디렉토리 안 질의 파일 전부의 (이름, 바이트) 해시다
(`source_digest`).

Starlark 소스(`EXTRACTED_STARLARK`, 유저 답 Q32-a, 2026-10-04)는 파이썬 소스와 같은 모양이다 — `.bzl` 은 파이썬 문법의
부분집합이므로 같은 AST 로 읽고, 최상위 정의 = 정의 청크 · 절 주석 = 절 복합체 · 최상위 리터럴 = 절 청크의 선언이다.
다른 것은 셋이다. 모듈 머리의 `load(...)` 가 import 자리이고, 인용 펜스의 언어가 `starlark` 이며, 생성 패키지는
`kb/dev/artifact/<이름>-bzl` 이다. 등록부의 선택 키 `wiring:` 은 **배선**(입력 집합과 인자를 잇기만 하는 최상위 정의·대입,
유저 답 Q10-a "빌드 배선은 항목이 아니다")의 이름 목록이고 추출기는 그 정의를 청크로 내지 않는다 — 소스에 없는 이름이
목록에 있으면 FAIL 이고, 배선만 남는 절은 절 청크를 세우지 않는다. 파일 청크 본문이 뺀 이름을 적는다.

사용: bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check] [--residency <defs/kb.bzl>]
      bazel run //tools:extract -- tools/cq-queries   (질의 디렉토리 — EXTRACTED_QUERY_DIRS 안이어야 한다)
      bazel run //tools:extract -- defs/kb.bzl        (Starlark 소스 — EXTRACTED_STARLARK 안이어야 한다)
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
      --residency 는 EXTRACTED_SOURCES 리터럴의 원본 — 없으면 <루트>/defs/kb.bzl.
출력·종료: 생성 시점 거부는 `FAIL [extract] <경로>: …`, `--check` 의 어긋남은 `FAIL [extract-drift] <경로>: …` —
둘 다 EXIT_FAIL. 읽을 수 없는 입력(EXTRACTED_SOURCES 포함)은 EXIT_CONFIG.
"""

from __future__ import annotations

import argparse
import ast
import difflib
import hashlib
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
```
<!-- 인용 끝 -->
