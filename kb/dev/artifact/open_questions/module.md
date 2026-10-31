---
id: https://agentic-knowledge-base.dev/id/chunk/f0c14e8d-c15c-4c5f-863a-3efb1b2f381a
type: artifact
level: executable
title_ko: 파일 tools/open_questions.py
title: file tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/d93492e4-f343-4736-b4a5-d04f48a3a75f, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4fe6beea-c6ab-454b-bad0-2cfede25066c, title_ko: 파일 복합체 tools/open_questions.py, title: file composite tools/open_questions.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/611551cc-ec21-4187-a12d-6a843751700f, https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0]}
---
**파일** — `tools/open_questions.py` 다. 226줄 · 최상위 정의 6개 · 최상위 절 2개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""미결 집계 뷰 — 설계 공간과 단위 지식 본문의 선택 슬롯 `미확정:` 을 모아 open.md 를 생성한다 (p4-three-empty-values, p4-slot-answers-one-question).

미결을 문서가 아니라 항목 안에 두면 집계가 생성물이 되고, 답이 왔을 때 고칠 자리가 하나다. 상세 다섯 절(질문 / 이미 정해진 것 /
현재 상태 / 답이 가르는 것 / 선택지)을 가진 미결은 설계 공간(`space/*-space.md`, `agt:Space`)이다(유저 결정 Q54-a). 이 뷰는 미결
목록의 유일한 자리다 — 손으로 관리하던 색인 문서를 대체했고(지시 0095) 그 문서는 지시 0192 로 지웠다.

  입력  head 그래프(agt:bodySlot "미확정" 인 단위 지식의 라벨·plane·level·상태·본문 위치)와 그 단위 지식의 본문,
        설계 공간 그래프(`--spaces`, //space:design_space — 공간의 제목·spaceStatus·변수·후보 링크의 상태).
        슬롯 표지는 chunk2kg 가 본문에서 찾아 넣은 값이다 — 여기서 본문을 다시 훑지 않고 그래프가 대상을 고른다.
  계산  공간마다 한 행: 제목 · status · 변수(from 라벨 · kind) · 후보 수(state 별: open · eliminated · confirmed) ·
        그 공간을 상세로 가리키는 `미확정:` 슬롯의 단위 지식. 후보 state 는 링크 상태(kb_lib.SPACE_STATE_LINK)를 거꾸로 읽는다.
        슬롯 줄 `미확정: <질문>. 상세는 `<값>`[·`<값>`]다.` 의 상세 값이 공간 IRI 이면 그 공간의 행에 붙는다.
        공간을 가리키지 않는 슬롯(상세 없음·문서 경로)은 슬롯 미결 표에 질문 한 줄로 남는다. 상세 값이 IRI 인데 공간이
        아니면 해석하지 못한 상세로 따로 낸다. 미결이 없어도 절을 낸다.
  나이  공간 행과 슬롯 미결 행에 만든 날부터 이 뷰의 생성 시각까지의 일수를 붙인다(유저 답 Q116-a). 만든 날은 그 항목의
        `generated.at`(`prov:generatedAtTime`)이다. 밀폐 빌드는 git 의 첫 커밋 날짜를 읽지 못하고 `generated.at` 은 마지막 저작
        시각이므로 이 나이는 실제 나이의 하한이다. 그 한계를 뷰 머리에 적는다.
  판정  없음 — 뷰이고 게이트가 아니다. 미결의 해소는 공간의 status·후보 state 와 단위 지식의 슬롯을 고치는 것이고 사람이 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음·본문 없음)
사용: open_questions.py --out open.md [--spaces <design-space.ttl>] [--bodies <단위 지식 .md …>] [--root .] <TTL…>   (bazel build //kg:open)
"""
import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import rdflib
from rdflib import Graph, Namespace, RDF
from rdflib.namespace import PROV

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
