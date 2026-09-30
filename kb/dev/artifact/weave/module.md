---
id: https://agentic-knowledge-base.dev/id/chunk/202358d3-fd6f-4b1c-867d-37e5a20adf9c
type: artifact
level: executable
title_ko: 파일 tools/weave.py
title: file tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/c0b7f63a-353e-4fdf-9389-961b6f3e130c, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/50eac9df-d01a-488f-8254-02ba61b00bf0, title_ko: 파일 복합체 tools/weave.py, title: file composite tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/b69488a2-ddf2-4c5d-b093-be38c4f5a853, https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574, https://agentic-knowledge-base.dev/id/composite/ec24ef39-7e27-4fff-bba3-6fdb1829b342, https://agentic-knowledge-base.dev/id/composite/8330a4d7-2140-46ed-b107-9196a6c03aa2, https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637]}
---
**파일** — `tools/weave.py` 다. 579줄 · 최상위 정의 14개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""문서 뷰 생성기 — 그래프와 청크 본문에서 ADR·요구 색인·변경 이력을 생성한다 (노트 4.6절 weave, method §9, p12-documents-are-generated).

문서는 저장하지 않고 질의로 생성한다. 생성물 머리에 생성 시각(UTC)과 쓴 질의를 적는다 — 사본이 원본으로 오인되지 않게
(p12-documents-are-generated). 생성물은 bazel-bin 에만 있다 (kb_weave 매크로: //kb/dev:adr · :requirements · :changelog).
  adr           살아 있는 결정 전부 — 결정 복합체마다 한 절(제목 = 결론 라벨, 상태, 수준, 결론·근거·대안 본문을 청크 파일에서 frontmatter 를
                뺀 그대로), 그 뒤 "단일 파일 결정" 절에 결정 복합체에 속하지 않는 살아 있는 결정(chunks/decision/, v1·harness 유래)을 같은
                형식으로. 둘 다 refines 하는 요구 라벨, supersedes 연쇄(대체한 옛 결정 라벨), sources, 가정 라벨을 낸다. 목차가 먼저다
  requirements  요구 색인 표 — 라벨 ko·en, EARS 패턴(agt:pattern), refines/serves 하는 살아 있는 결정 수, 정제 도달 최저 수준
                (metrics 의 CQ19 와 같은 정의: refines/serves 하류의 가장 낮은 level), IRI. INTENT.md 의 손 목록을 대체하는 뷰다
  changelog     supersedes 쌍(새 → 옛)을 새 결정의 generated.at 순으로, prov:wasRevisionOf 가 있으면 함께
  audit         감사 보고서 (로드맵 8단계 "복원과 감사", 요구 audit-self-sufficiency) — 입력은 그래프 union 과 관측 청크 본문(kb/vv/run/ 의
                실행 기록 · kb/dev/memory/ 의 가정 판정)뿐이다. 체계 밖 정보 0. 절: 리비전·입력 / 검증 현황(요구의 검증 대응물 · verifies 대상
                결정 · 사슬 수 · 기준 없는 verifies) / 최근 실행(케이스별 pass·fail·skip 그대로) / 판정 주석(주석 수 · 라벨 분포 · 해소 열림 ·
                그중 게이트를 막는 issue (blocking); p7-commentary-form) / 가정(최신 assume_check 관측) / 추적 매트릭스
                (kb_lib.TIM_CELLS — metrics 와 같은 정의) / 검증 표시(verified 주체 종류 · 검증 뒤 수정) / 링크 근거(증거 종류 · 복원 비율) /
                자족성 선언. bodies 에 //kb/vv:bodies·//kb/dev:bodies 를 준다 (//kg:audit)
그래프는 query·metrics 와 같은 union 을 kb_lib.load_union 으로 올린다. 본문은 --bodies 의 청크 파일에서 frontmatter id 로 찾는다.
사용: weave.py --kind adr|requirements|changelog|audit --out <파일> [--root .] <그래프 ttl …> [--bodies <청크 .md …>]
종료: 0 생성됨 · 2 입력 문제(kind 밖·그래프 파일 없음·본문 파싱 불가) — 뷰라 판정 실패(1)는 없다. 결정 0건은 빈 절이지 실패가 아니다
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef
```
<!-- 인용 끝 -->
