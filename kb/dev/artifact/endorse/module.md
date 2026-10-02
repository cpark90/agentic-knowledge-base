---
id: https://agentic-knowledge-base.dev/id/chunk/5c0dd9d9-4424-4c6e-ae1d-1b8209b24286
type: artifact
level: executable
title_ko: 파일 tools/endorse.py
title: file tools/endorse.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-endorse}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-11T09:15:09Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/4ec4de00-ea81-4ed0-abf7-40beedc25e38]
composite: {id: https://agentic-knowledge-base.dev/id/composite/9a0f13d1-d6f6-48ea-9728-4e96bd777d51, title_ko: 파일 복합체 tools/endorse.py, title: file composite tools/endorse.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e7f0f4ca-74a2-4f45-9464-feb382099c39, https://agentic-knowledge-base.dev/id/composite/4a01c621-e30b-42ce-9e5d-a8a449270a57]}
---
**파일** — `tools/endorse.py` 다. 40줄 · 최상위 정의 1개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""인수 — 쓰기 권한이 있는 역할이 검토한 청크에 OKF verified 를 붙인다 (writer 검사의 해소 수단).

hci 가 만든 청크(generated.by: hci/…)는 그 plane 을 쓸 수 있는 역할(orchestrator 등)의 verified 가 있어야 게이트를
통과한다. 이 도구는 검토를 대신하지 않는다 — 검토한 역할이 자기 이름으로 돌린다.
사용: bazel run //tools:endorse -- --by orchestrator/claude-fable-5 --at 2026-09-11T10:00:00+09:00 <청크 파일...>
"""
import argparse
import os
import re
from pathlib import Path
```
<!-- 인용 끝 -->
