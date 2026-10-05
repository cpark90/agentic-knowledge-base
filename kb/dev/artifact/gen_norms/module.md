---
id: https://agentic-knowledge-base.dev/id/chunk/73abbe6d-7ee4-4c1d-8f71-4c1bc57951ac
type: artifact
level: executable
title_ko: 파일 tools/gen_norms.py
title: file tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T03:04:11Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/823b2096-4821-4c38-a7ea-87b9b6cba977]
composite: {id: https://agentic-knowledge-base.dev/id/composite/29a3a21d-a74b-4fc0-8764-46de4751e58a, title_ko: 파일 복합체 tools/gen_norms.py, title: file composite tools/gen_norms.py, ordered: [https://agentic-knowledge-base.dev/id/composite/aebd48bd-5503-44d2-a028-ca367564d9a2, https://agentic-knowledge-base.dev/id/composite/55330362-0aaf-42fe-bd7b-4cfec40c4e75, https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0, https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d, https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4]}
---
**파일** — `tools/gen_norms.py` 다. 566줄 · 최상위 정의 23개 · 최상위 절 5개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""규범 문서 생성기 — 절 청크(`kb/dev/norm/<문서 stem>/`)와 결정의 규약 줄(`conventions.md`)에서 규범 문서를 생성한다.

규범 문서(`STYLEGUIDE.md`·`docs/rules.md`·`docs/method.md`·`AGENTS.md`)는 방법론 층의 투영이고 원본은 청크다 (결정
p12-norm-documents-from-section-chunks, 유저 답 Q19-b·Q21-a·Q22-b). 골격은 `norm` plane 의 절 청크이고 문장은 결정의
선택 넷째 청크 `conventions.md` 의 `규약:` 줄이다 (p4-convention-slot). 생성물은 소스 트리에 두고 커밋한다 — 도구가 없어도
문서가 읽혀야 하기 때문이다(`.claude/skills` 와 같은 생성 트리 파일). //:norms_drift_test 가 생성기를 다시 돌려 바이트로 비교한다.

문서 목록의 단일 정의처는 `defs/kb.bzl` 의 `NORM_DOCS`(문서 stem → 생성 파일 경로)다. 문서 하나는 복합체 하나이고 순서는
머리 청크(composite: 선언)의 `composite.ordered` 다. 직접 부분은 9 이하이므로(4.5절, p4-composite-as-part-of) 절이 많은 문서는
절을 묶음 복합체로 나눈다 — 묶음의 첫 절 청크가 `composite: {id, title_ko, title, part_of: <문서 복합체>, ordered: […]}` 로
선언하고 묶음 안 절 청크의 `part_of` 는 묶음 IRI 다. 묶음은 제목을 내지 않고 순서만 준다 — 절의 순서는 문서 복합체의 순서를
깊이 우선으로 펼친 것이다. 머리 청크의 본문이 문서 도입문·범례이고, 절 청크마다 제목(번호는 이 도구가
머리 청크의 `numbering` 꼴로 붙인다. `numbered: false` 인 절은 번호가 없다) → 본문 → 항목을 낸다. 항목은 `items` 의 `slug#k` 가 가리키는 줄이고 결정 링크는 그 문장의
첫 문장 끝에 둔다. 문장 안 링크는 청크 기준 상대경로라 출력 위치 기준으로 다시 계산한다. 머리 블록은 생성 트리 파일의 꼴이다
(`kb_lib.gendoc_header(stamped=False)` + `gendoc_tree_notice`) — 생성 시각·지문이 없고 바이트 비교가 그 자리의 건전성 장치다.
절 청크 하나는 항목 묶음 하나(목록 하나 또는 표 하나)를 갖고 본문은 그 묶음 앞의 산문이다. 묶음의 꼴은 `form`(bullets · ordered ·
table)이고, 표는 `columns` 를 열 머리로 행마다 줄의 `a | b | …` 를 칸으로 낸다. `link_column`(columns 의 마지막)이 있으면 그 열이
결정 링크이고, 없으면 표 바로 앞에 `원본:` 한 줄이 행의 결정(주·둘째 구분 없이)을 처음 나온 순서로 낸다. 묶음 뒤의 산문과 다음 묶음은 이어짐 절
청크(`continues: true` — 제목·깊이 없음, 번호를 소비하지 않음)가 담는다.

검사: 모든 살아 있는 `규약:` 줄은 적어도 한 문서에서 쓰이고(고아 줄 FAIL) 한 문서 안에서는 한 번까지만 쓰인다(이중 소비
FAIL). 서로 다른 문서가 같은 줄을 각각 한 번씩 싣는 것은 허용한다 — 두 규범 문서에 같은 문장을 실으려고 결정에 사본 줄을 두지 않게
하기 위해서다. 강도를 요구하는 문서(머리 청크의
`strength`, 기본 required)에서 강도 없는 줄은 FAIL 이다. 없는 결정·없는 줄을 가리키는 항목, `NORM_DOCS` 와 디렉토리 집합의
불일치, 절 청크의 구조 위반(선언·순서·머리 청크의 키·첫 절의 깊이·첫 절의 이어짐)도 FAIL 이다. 표 절에서는 강도가 붙은 줄과
링크 열을 뺀 열 수와 칸 수가 다른 줄이 FAIL 이고, 표 절의 줄에는 강도 요구가 적용되지 않는다.
사용: gen_norms.py [--check] [--root .] [--doc <stem>] [--residency defs/kb.bzl] [--norm-docs <NORM_DOCS 를 담은 파일>]
출력·종료: 생성 시점 거부는 `FAIL [gen-norms] …` EXIT_FAIL, --check 의 어긋남은 `FAIL [norms-drift] …` EXIT_FAIL,
읽을 수 없는 입력은 EXIT_CONFIG. 문서가 0개여도 검사(고아 줄)는 돌고 위반이 없으면 PASS 다 — 생성기이므로 SKIP 이 아니다.
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import sys
from pathlib import Path
```
<!-- 인용 끝 -->
