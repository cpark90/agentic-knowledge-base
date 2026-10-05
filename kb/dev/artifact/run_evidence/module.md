---
id: https://agentic-knowledge-base.dev/id/chunk/39112a6e-ccc9-4b3f-b3f8-1d1a8b58783c
type: artifact
level: executable
title_ko: 파일 tools/run_evidence.py
title: file tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:47:19Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/d3a36010-25a1-417b-b2e7-875ccc6955ce, https://agentic-knowledge-base.dev/id/chunk/c5bb1922-eb82-4b96-a49c-a46e41c239e4]
composite: {id: https://agentic-knowledge-base.dev/id/composite/27628b6a-73ec-4466-bb12-a1a1ae970dd7, title_ko: 파일 복합체 tools/run_evidence.py, title: file composite tools/run_evidence.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/06ff52f5-9406-4ead-8685-51db4f0cb144, https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f, https://agentic-knowledge-base.dev/id/composite/e202036d-a930-4e1b-a919-03711832262b]}
---
**파일** — `tools/run_evidence.py` 다. 209줄 · 최상위 정의 3개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""실행 증거 → `satisfies` 후보의 증거 기록 (p9-evidence-ledger 결론 "실행 증거가 특별하다", p10-link-types `satisfies`).

검증기의 통과는 `verifies` 뿐 아니라 그것이 검증하는 `satisfies` 후보에도 실행(+)을, 실패는 실행(−)을 적는다 — V&V 결과가
개발 KB 후보의 증거로 흘러드는 유일한 경로이고 링크가 아니라 **증거 기록 항목**이라 방향 규칙(8.5절)을 깨지 않는다.
이 도구가 그 경로의 생성기다. 손으로 쓰는 링크가 아니라 생성물이며 출력은 `//kg:references_kg` 에 이어 붙는다.

후보의 양 끝은 개발 KB 의 코드 **파일 청크**(파일 복합체의 선언 청크, p7-code-links-on-file-composite)와 **결정 결론**이다.
증거의 원천은 둘이다.

  도장  파일 청크의 `verified` 에 `process:bazel-test`(kb_lib.STAMP_ACTOR)가 있으면 — 추출기가 `tested.source_hash` 가 지금
        소스와 같을 때만 내므로 살아 있는 도장이다 — 그 청크가 `refines` 하는 결정 결론마다 실행(+) 한 줄. 참조는 그 파일 청크다
        (도장의 시각 `agt:verifiedAt` 이 거기 있다). 도장은 통과 뒤에만 찍히므로 도장에서 (−)는 나오지 않는다.
  실행  V&V 실행 기록(`kb/vv/run/`, generated.by `process:vv_run`)의 케이스 표 한 행마다 — 그 케이스를 `refines` 하는 검증기가
        `verifies` 하는 개발 KB 파일 청크 A 와 그 케이스가 `verifies` 하는 결정 결론 D 의 쌍에 pass 는 실행(+), fail 은 실행(−)
        한 줄. 참조는 실행 기록과 케이스 둘이다. skip 은 증거가 아니다(SKIP 은 PASS 가 아니다). 건너뛴 명령이 있는데 pass 로 적힌
        옛 행도 (+)로 읽지 않는다 — 절반만 실행한 통과다.

상태는 p9-evidence-ledger 의 전이 규칙 그대로다. 실행(−)만 있으면 `invalid`(배제, 클래스 없음 — space2kg 와 같은 표현), (+)가
하나라도 있으면 `candidate`(agt:CandidateLink) — (+)와 (−)가 공존해도 자동 해소하지 않고 후보로 남긴다(충돌 = open + 유저 큐).
확정 제안은 내지 않는다 — 확정은 사람이 frontmatter `satisfies:` 에 적는 행위다. 그 쌍이 이미 확정이면 상태·클래스를 쓰지 않고
증거 항목만 그 링크에 붙인다(확정 링크도 증거 기록을 유지한다). 직접 트리플 `agt:satisfies` 는 내지 않는다 — 후보는 주장이 아니다.
링크 IRI 는 chunk2kg 와 같은 규칙(양 끝 뿌리 uuid 의 link_hash)이다.

출력·종료: 읽을 수 없는 입력은 `FAIL [run-evidence] <경로>: …` + EXIT_CONFIG. 실행 기록이 가리키는 케이스가 없으면 stderr 에
`info [run-evidence]` 로 세고 건너뛴다 — 실행 기록은 append-only 라 지난 케이스 이름이 남는다.
사용: run_evidence.py --out <생성.ttl> --residency defs/kb.bzl <청크 파일들...>   (.md 만 읽는다)
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
```
<!-- 인용 끝 -->
