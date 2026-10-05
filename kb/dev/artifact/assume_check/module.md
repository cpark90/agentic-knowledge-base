---
id: https://agentic-knowledge-base.dev/id/chunk/ec773001-5697-45eb-94ad-50f56f7085aa
type: artifact
level: executable
title_ko: 파일 tools/assume_check.py
title: file tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/47ba1172-488a-4f7b-ba4b-bc63fdf39b88, https://agentic-knowledge-base.dev/id/chunk/79bcc1dd-4036-43ef-b30d-f4dff07be513, https://agentic-knowledge-base.dev/id/chunk/b36581f8-2688-46dc-9b44-3e1019a37d66]
composite: {id: https://agentic-knowledge-base.dev/id/composite/169b7deb-a7ef-4d53-9f52-ad8abd5d4c3a, title_ko: 파일 복합체 tools/assume_check.py, title: file composite tools/assume_check.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c767c9b6-7391-4c5f-b482-89293d8895ee, https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead, https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e, https://agentic-knowledge-base.dev/id/composite/5dac7240-2471-496d-a65c-f55a8a067a41]}
---
**파일** — `tools/assume_check.py` 다. 415줄 · 최상위 정의 17개 · 최상위 절 4개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""가정 판정과 전파 — 도입 4단계 "가정과 무효화"의 첫 형태 (노트 6.5절·6.9절, method §7, p6-assumption-verification-methods,
p6-assumption-invalidation).

가정(`agt:Assumption`)마다 `agt:refersTo` 한 ODD 조건을 odd_check 의 판정 함수로 판정하고 연언(AND)으로 상태를 낸다.
  valid        — 참조 조건 전부 in
  invalidated  — 하나라도 out
  unverified   — 그 밖 (판정 불가한 조건이 있다)
판정 유형은 ODD `CHECKS.cmd` 가 있으면 "실행 검사", 없으면 "사람 확인" 이고, 판정식 등급은 참조 조건 등급의 최저(A~D)다.
새 어휘는 없다 — 가정 자체의 `when` 판정식은 후속이며, 첫 형태는 참조 조건 판정의 연언으로 판정식을 파생한다.

전파 (p6-assumption-invalidation "가정이 깨지면 의존 항목이 자동으로 무효화된다", r-007 전수조사 없이):
  직접 영향 집합  = invalidated 가정을 `agt:assumes` 하는 살아 있는 청크
  suspect 후보    = 직접 영향 집합에 링크(refines·serves·supersedes·cites·coUpdatesWith·overlapsWith — 직접 트리플과 agt:Link 개체 둘 다)로
                    닿는 하류(그 항목을 가리키는 쪽, 전이) + 복합체 형제. 그래프가 원본이므로 bazel rdeps 가 아니라 head 그래프에서 센다.
검증 실험 (14.1 정정본 4단계 "연결" 조건): `--break <cond-id>` 는 그 조건을 out 으로 가정한다. 그때 계산된 직접 영향 집합을
청크 파일 frontmatter(`assumes`)를 독립적으로 스캔한 실제 의존 집합과 비교해 정밀도·재현율을 보고에 적는다.

링크 상태의 물질화 (노트 9.11절 "상태는 저장값이 아니라 평가 결과", handoff link-model-robustness-cde-2026-09-19 반영 1·2):
  when 판정   확정 링크의 `agt:when` 을 kb_lib.when_eval 로 판정한다. 판정의 범위는 **ODD 속성 참조**이고 항은 `in(<조건>)`,
              결합은 `!`·`&&`·`||`·괄호, 리터럴은 true·false 다 (kb_lib.WHEN_GRAMMAR). 비교·산술·함수 호출은 판정하지 않고
              unverified 로 남긴다. 조건 판정은 여기서 새로 하지 않고 odd_check.judge_all 의 결과를 그대로 읽는다.
  트리거      kb_lib.SUSPECT_TRIGGERS 에 켜진 종류만 전파한다 — 지금은 supersedes 하나다. 추적 매트릭스가 suspect 로 포화하는
              것을 막기 위해 좁게 선언하고, 포화율은 `bazel build //kg:metrics` 의 한 줄로 관측한다.
  저장하지 않는다  suspect 는 그래프에 적히지 않는다. 이 보고와 metrics 에서만 물질화된다.

--record 는 실행 결과를 관측(memory plane, concrete, append-only — r-026·p0-run-as-observation)으로
kb/dev/memory/obs-<UTC>.md 에 쓴다. 이미 있는 파일은 덮지 않는다. 생성 뒤 tools/gen_build.py 를 돌려 BUILD 를 갱신한다.

사용: bazel run //tools:assume_check -- [--break <cond-id>…] [--record] [--out report.md] [--odd kb/odd/project-odd.yml] [TTL…]
종료: 전부 valid 0 (EXIT_OK) · invalidated 가정 또는 `when` 이 거짓인 링크 있음 1 (EXIT_FAIL) · unverified 만 있음 3 (EXIT_SKIP) ·
      입력 문제 2 (EXIT_CONFIG)
"""
from __future__ import annotations

import argparse
import os
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, RDF, RDFS, URIRef
```
<!-- 인용 끝 -->
