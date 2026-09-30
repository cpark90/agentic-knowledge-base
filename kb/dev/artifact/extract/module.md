---
id: https://agentic-knowledge-base.dev/id/chunk/12a44438-6b75-4c5f-80b4-c717d7648b5b
type: artifact
level: executable
title_ko: 파일 tools/extract.py
title: file tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
composite: {id: https://agentic-knowledge-base.dev/id/composite/99abae51-6823-4ed8-9bfe-4255801d4681, title_ko: 파일 복합체 tools/extract.py, title: file composite tools/extract.py, ordered: [https://agentic-knowledge-base.dev/id/composite/57a845e1-da27-4d9d-b5b0-b25148ccece7, https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53, https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef, https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685, https://agentic-knowledge-base.dev/id/composite/e15e9467-610e-43bf-b882-759772f9ace0, https://agentic-knowledge-base.dev/id/composite/bdbaec34-7407-4d5e-83f8-0706026f0b98, https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0]}
---
**파일** — `tools/extract.py` 다. 672줄 · 최상위 정의 32개 · 최상위 절 7개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""코드 → 청크 추출기 — 소스 파일 하나에서 `artifact` plane 의 청크 트리를 생성한다 (p7-code-extraction-direction).

코드가 원본이고 청크는 생성물이다. 청크 파일을 손으로 고치면 드리프트 게이트(`//:extract_drift_test`)가 거부한다.
tangle(청크 → 코드)은 없다. 정체성의 원본은 소스 옆의 **등록부**(`<소스>.chunks.yml`)이고 한정 이름 → uuid 를 담는다 —
이름이 바뀌어도 uuid 가 유지되므로 개명이 청크의 삭제 + 신설로 보이지 않는다 (p10-split-keeps-work-identity).

구조는 세 층이다 (p7-code-links-on-file-composite). 파일 복합체의 선언 청크가 **파일 청크**(`module.md` — 모듈
docstring 과 import)이고 링크(`refines`·`serves`)와 검증기의 `verifies` 도착점이 거기다. 그 부분은 소스의 절
주석(`# ══ 장` · `# ── 절`)이 여는 **절 복합체**이고, 절 복합체의 부분은 절 청크와 그 절의 정의 청크다.
직접 부분은 9개를 넘을 수 없으므로(4.5절) 넘는 절은 잘라 맞추지 않고 절 주석을 요구한다 — 순서에 뜻이 없는 묶음을
만들지 않는다.

정의 청크는 선택 키 `uses: [<청크 IRI>…]` 를 갖는다 — 같은 모듈의 최상위 정의를 이름으로 쓰는 관계이고 `chunk2kg` 가
`agt:usesDefinition`(references 족의 잎)으로 방출한다. 해소는 AST 의 이름 참조뿐이며 제외는 `used_defs` 에 적혀 있다.
링크 키가 아니므로 Bazel `deps` 도 링크 개체도 되지 않는다 — 링크는 파일 복합체의 것이다. 모듈 간 호출은 이 잎이 잡지
않고, 방출은 표본 경계 `kb_lib.USES_SOURCES` 안의 소스에서만 한다 (유저 답 2026-09-30: 표본 하나에서 모듈 안 호출만
먼저 내고 링크 밀도·게이트 시간을 잰 뒤 넓힌다).

청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다(`previous_bodies`) — 소스 시각을 모든 청크에
다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지 보이지 않는다. 값의 원본은 트리이므로 `--check` 는
그대로 결정론이다.

등록부의 갱신 규칙은 넷이다. (a) 등록부에 있는 이름은 그 uuid 를 쓴다. (b) 등록부에 없는 새 이름의 본문 해시가
등록부에서 사라진 이름의 것과 같으면 **개명**이므로 `FAIL [extract]` 로 등록부 수정을 안내한다 — 정체성의 변경은
사람의 편집이다. (c) 대응이 없으면 새 uuid 를 등록부에 더한다(신설은 자동). (d) 등록부에 있는데 소스에 없으면
`FAIL [extract]` 다 — 삭제는 등록부에서 지우는 명시 행위다.

사용: bazel run //tools:extract -- tools/kb_lib.py [--root <저장소 루트>] [--check]
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리(bazel test 의 runfiles).
출력·종료: 생성 시점 거부는 `FAIL [extract] <경로>: …`, `--check` 의 어긋남은 `FAIL [extract-drift] <경로>: …` —
둘 다 EXIT_FAIL. 읽을 수 없는 입력은 EXIT_CONFIG.
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
