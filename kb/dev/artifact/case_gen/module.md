---
id: https://agentic-knowledge-base.dev/id/chunk/2237cfbd-7d8e-4f70-b528-bea1bfd6e8f4
type: artifact
level: executable
title_ko: 파일 tools/case_gen.py
title: file tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T12:40:09Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/5ff79a30-1dc2-45e0-be42-2d793dbcf65a]
composite: {id: https://agentic-knowledge-base.dev/id/composite/6038262a-0bc8-4f38-bb62-357c9eaeece2, title_ko: 파일 복합체 tools/case_gen.py, title: file composite tools/case_gen.py, ordered: [https://agentic-knowledge-base.dev/id/composite/1a0a0d9e-abcb-46ca-bf5b-d530a350816e, https://agentic-knowledge-base.dev/id/composite/10ce940e-ae6b-4b2e-8d0e-3bb5448ae88e, https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516, https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be, https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32, https://agentic-knowledge-base.dev/id/composite/d35350bd-7f95-4059-82b7-88108831c060, https://agentic-knowledge-base.dev/id/composite/9b61053c-0a32-44e3-83a7-5cceaaa5c57e]}
---
**파일** — `tools/case_gen.py` 다. 598줄 · 최상위 정의 28개 · 최상위 절 7개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""V&V 케이스 생성기 — 논리 시나리오의 `keep`·`cover` 에서 concrete 케이스 청크(`kb/vv/case/*.md` 꼴)를 결정론적으로 만든다.

결정 p8-case-generation: concrete 케이스는 사람이 쓰지 않는다 — `keep`+`cover` 에서 생성하고 표본 근거 없는 케이스는 거부한다.
생성 규칙은 다섯(등가분할 · 경계값 · t-wise 조합 · 요인 주입 · 관측 재현)이고 규칙·seed 는 케이스의 provenance 에 남는다.
결정 p8-scenario-authoring: `keep()` 은 자극의 자리이므로 입력은 `decision`(vv) **logical** 시나리오의 자극 청크(`<슬러그>-stimulus.md`)다.
결정 p8-machine-readable-case: 출력 케이스는 `vv_run` 이 읽는 꼴 그대로다 — 펜스 `files`·`expect`, `**실행 명령**` 한 줄.

입력 — 시나리오 자극 청크 본문의 `yaml` 펜스 하나(키 `keep`·`cover` 가 둘 다 있는 펜스. 그 밖의 펜스는 산문의 예시다):
  keep:  변수 → {odd: <ODD 속성 IRI(id:cond-…)> | outside, range: [lo, hi] (정수) | values: [값…], reject: [값…], domain: [lo, hi]}
         `range`·`values` 가 keep 이다. `reject` 는 열거 변수의 keep 밖 값, `domain` 은 범위 변수의 keep 밖까지 포함한 정의역이다.
         `odd: outside` 인 변수가 든 케이스는 `odd:outside` 를 달아 커버리지에서 빠진다 (p8-scenario-authoring 규약).
  cover: [{rule: equivalence|boundary|pairwise|factor|observed, …}]  — 항목 하나가 표본 추출 근거 하나다.
         equivalence {vars} · boundary {vars} (범위 변수만) · pairwise {vars} (열거 변수 둘 이상) ·
         factor {var, factors: {agt:<요인>: <keep 밖 값>}} · observed {run: kb/vv/run/<기록>.md, values: {변수: 값}}
  seed:  정수 — 등가분할의 대표값을 고르는 난수의 seed. 케이스의 `**표본 근거**` 에 남는다
  case:  {criteria: <기준 IRI>, verifies: [<IRI>…], derivesFrom: [<IRI>…], title_ko, title, summary, stimulus, files: {이름: 내용},
          command, accept: {prose, expect}, reject: {prose, expect}} — 문자열의 `${변수}` 를 케이스의 값으로 바꾼다.
         `derivesFrom` 은 선택이다 — 케이스의 `derivesFrom` 에 시나리오 IRI 다음으로 옮긴다(수기 케이스가 가졌던 출처 링크를 잇는다).
         생성 케이스는 `restored` 를 쓰지 않는다 — 생성기가 템플릿에서 놓는 링크는 복원이 아니라 구축이다
값을 손으로 적은 항목(`cases` 키 · 관측 재현 밖의 `values`)과 `rule` 없는 항목은 표본 근거가 없으므로 FAIL 이다.
나머지 변수는 기준값(범위 변수는 lo, 열거 변수는 values 의 첫째)에 둔다. 값이 하나라도 keep 밖이면 케이스는 `reject` 부류다.

사용: case_gen.py --out <디렉토리> [--root .] [--scenario <자극 청크>…] [--residency defs/kb.bzl] [--odd <ODD yml>]
      case_gen.py --check [--root .] [--scenario <자극 청크>…] [--cases kb/vv/case] [--all-generated]
--scenario 가 없으면 생성 모드는 `kb/vv/scenario/` 의 logical 자극 청크 중 입력 펜스가 있는 것 전부를 읽는다. --check 는 준 시나리오만 본다 —
//:case_drift_test 가 대상 목록을 명시로 준다(빈 목록이면 대상 0 이고 PASS 다. 생성기이므로 SKIP 이 아니다). `--all-generated` 는
케이스 디렉토리의 모든 케이스가 이 생성기의 것인지 본다(수기 케이스 0). 저장소에 쓰는 일은 vnv 가 `--out kb/vv/case` 로 한다.
출력·종료: 생성 시점 거부는 `FAIL [case-gen] …` EXIT_FAIL, --check 의 어긋남은 `FAIL [case-drift] …` EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import difflib
import itertools
import json
import random
import re
import sys
import uuid
from pathlib import Path

import yaml
```
<!-- 인용 끝 -->
