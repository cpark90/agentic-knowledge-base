---
id: https://agentic-knowledge-base.dev/id/chunk/b297b7e0-4153-4802-bc7d-de6ba295e05e
type: artifact
level: executable
title_ko: 파일 tools/stamp.py
title: file tools/stamp.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-stamp}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/4ec4de00-ea81-4ed0-abf7-40beedc25e38]
composite: {id: https://agentic-knowledge-base.dev/id/composite/39d9c5d9-3e2f-4e3b-9f05-84c7476fa96b, title_ko: 파일 복합체 tools/stamp.py, title: file composite tools/stamp.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fe9a3f4c-a455-444c-b612-4f93c3897066, https://agentic-knowledge-base.dev/id/composite/9de96dc9-03ab-40b9-a90a-4481f8f9deb7]}
---
**파일** — `tools/stamp.py` 다. 119줄 · 최상위 정의 3개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""테스트 통과 도장 — 추출된 코드 청크의 `verified` 를 사람이 아니라 게이트가 찍는다 (p7-code-extraction-direction "도장").

`artifact` plane 의 `verified` 는 사람 검토가 아니라 **테스트 통과**다. 코드는 자주 바뀌므로 사람 도장을 요구하면
수정마다 `generatedAtTime ≤ verifiedAt` 게이트가 걸린다. 판정 주체를 바꾸는 것이지 검사를 약화하는 것이 아니다 —
사람 도장은 결정·요구에 남는다 (`tools/endorse.py`).

**규범: `bazel test //...` 가 종료 0 으로 끝난 뒤에만 이 도구를 돌린다.** 이 도구는 자기 안에서 `bazel test` 를
부르지 않는다 — `bazel run` 안의 중첩 Bazel 호출은 같은 출력 기반을 잠그기 때문이다. 그래서 도장은 호출자의
주장이고, 도구가 지키는 것은 **그 주장이 가리키는 내용이 실재하는가** 하나다: `--rev` 를 주지 않으면 소스 파일이
커밋되어 있어야 하고(작업 트리가 더러우면 리비전이 그 내용을 가리키지 않는다) 도장에는 그때의 소스 해시를 함께
적는다. 소스가 그 뒤에 바뀌면 추출기가 `verified` 를 **빼서** 낸다 — 수정 뒤 미검증이고 재판정이 자동이다.

도장의 자리는 등록부(`<소스>.chunks.yml`)의 `tested` 다. 생성 청크는 뷰이므로 거기에 손으로 적을 자리가 없다.
추출기가 `tested.source_hash` 가 지금 소스와 같을 때만 `verified: [{by: process:bazel-test, at: <tested.at>}]` 를
모든 생성 청크에 낸다. 리비전은 등록부와 파일 청크 본문에 남는다 — `agt:verifiedAt`·`agt:verifiedBy` 밖의 키를
head 그래프가 받지 않으므로 그래프에 리비전을 넣지 않는다.

사용: bazel run //tools:stamp -- tools/kb_lib.chunks.yml [--rev <리비전>] [--at <ISO 8601 UTC>] [--root <루트>]
      루트는 --root, 없으면 BUILD_WORKSPACE_DIRECTORY(bazel run), 없으면 현재 디렉토리.
      도장 뒤에 `bazel run //tools:extract -- <소스>` 와 `python3 tools/gen_build.py --root .` 를 돌린다.
출력·종료: 거부는 `FAIL [stamp] <경로>: <근거>` + EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
`--at` 이 지금보다 뒤이면 거부한다 — 미래 시각의 도장은 테스트 통과보다 앞선 주장이 되고, 게이트는 시계에 의존할 수 없어
(재현성) 이 판정은 쓰는 시점에만 할 수 있다.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
```
<!-- 인용 끝 -->
