---
id: https://agentic-knowledge-base.dev/id/chunk/d54dd037-5b16-4649-922d-f7c9b7b5c510
type: artifact
level: executable
title_ko: 파일 tools/gen_build.py
title: file tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/047c5c56-2b6c-4f8b-993e-32f3a35fd1d6, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c, https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e]
composite: {id: https://agentic-knowledge-base.dev/id/composite/9bb41e68-1b5c-4d4c-aee0-32a2899bedf9, title_ko: 파일 복합체 tools/gen_build.py, title: file composite tools/gen_build.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fa831b18-16bd-4c86-8fa9-8ac3d941c6f2, https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd, https://agentic-knowledge-base.dev/id/composite/569c6e75-e264-4981-bf0b-bba156b541c8, https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa, https://agentic-knowledge-base.dev/id/composite/e563bac1-7552-474e-a036-f6ced4999bc4]}
---
**파일** — `tools/gen_build.py` 다. 467줄 · 최상위 정의 17개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""BUILD 생성기 — frontmatter·owl:imports 에서 패키지별 BUILD.bazel 을 생성한다 (bazel-dependency-review 2단계).

원본은 그래프(frontmatter 링크, owl:imports)이고 BUILD 는 커밋되는 뷰다. 링크 변화가 PR diff 에 보이도록
커밋하며, //:build_drift_test 가 생성기를 다시 돌려 커밋본과 비교한다 — frontmatter 를 고치고 BUILD 를 안 돌린
경우를 잡는다. 사용: gen_build.py [--check] [--root .] [--residency defs/kb.bzl]
출력·종료: 생성 시점 거부(세 청크 없는 결정 디렉토리·끊긴 링크·`_check_bundle` 의 패키지 밖 부분·중복 선언·이질·상한·
`composite.ordered` 와 부분 집합의 불일치)는 `FAIL [gen-build] <경로>: …`, frontmatter 위반은
chunk2kg 의 규칙이므로 `FAIL [chunk2kg] …`, --check 의 어긋남은 `FAIL [build-drift] <BUILD>: …` — 모두 EXIT_FAIL.
읽을 수 없는 입력은 EXIT_CONFIG.
"""
import argparse
import difflib
import re
import sys
from pathlib import Path
```
<!-- 인용 끝 -->
