---
id: https://agentic-knowledge-base.dev/id/chunk/f0c14e8d-c15c-4c5f-863a-3efb1b2f381a
type: artifact
level: executable
title_ko: 파일 tools/open_questions.py
title: file tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/d93492e4-f343-4736-b4a5-d04f48a3a75f, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4fe6beea-c6ab-454b-bad0-2cfede25066c, title_ko: 파일 복합체 tools/open_questions.py, title: file composite tools/open_questions.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/611551cc-ec21-4187-a12d-6a843751700f, https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0]}
---
**파일** — `tools/open_questions.py` 다. 134줄 · 최상위 정의 3개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""미결 집계 뷰 — 청크 본문의 선택 슬롯 `미확정:` 을 모아 open.md 를 생성한다 (p4-three-empty-values, p4-slot-answers-one-question).

미결을 문서가 아니라 항목 안에 두면 집계가 생성물이 되고, 답이 왔을 때 고칠 자리가 하나다. 이 뷰는 그 집계만
맡는다 — 미결의 상세(다섯 절)는 42줄 청크에 들어가지 않아 `docs/open-questions.md` 색인과 그 아래 문서로 남고,
뷰는 그것을 대체하지 않는다.

  입력  head 그래프(agt:bodySlot "미확정" 인 청크의 라벨·plane·level·상태·본문 위치)와 그 청크의 본문.
        슬롯 표지는 chunk2kg 가 본문에서 찾아 넣은 값이다 — 여기서 본문을 다시 훑지 않고 그래프가 대상을 고른다.
  계산  본문에서 `미확정: <질문 한 문장>. 상세는 `<문서>`다.` 줄을 뽑아 질문과 상세 문서 경로로 가른다.
        상세 경로가 없으면 `없음` 이다. 미결이 없어도 절을 낸다.
  판정  없음 — 뷰이고 게이트가 아니다. 미결의 해소는 답이 온 뒤 청크의 슬롯을 고치는 것이고 사람이 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(그래프를 읽을 수 없음·본문 없음)
사용: open_questions.py --out open.md [--bodies <청크 .md …>] [--root .] <TTL…>   (bazel build //kg:open)
"""
import argparse
import re
import sys
from pathlib import Path

import rdflib
from rdflib import Graph, Namespace, RDF

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
```
<!-- 인용 끝 -->
