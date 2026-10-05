---
id: https://agentic-knowledge-base.dev/id/chunk/b18ba980-389e-4fda-b1e5-852db74c491e
type: artifact
level: executable
title_ko: 파일 tools/label_sample.py
title: file tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4, https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
composite: {id: https://agentic-knowledge-base.dev/id/composite/06cd565d-e749-42fe-88da-1a56fd71a2a5, title_ko: 파일 복합체 tools/label_sample.py, title: file composite tools/label_sample.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/0642de89-2ca0-4a05-b091-a2adf00d4e0e, https://agentic-knowledge-base.dev/id/composite/f8d4f7c1-457b-4464-a913-96c62e1fcb28, https://agentic-knowledge-base.dev/id/composite/fff3d0e5-ad0f-4eb4-b8c9-e9ae7d1ce791]}
---
**파일** — `tools/label_sample.py` 다. 195줄 · 최상위 정의 5개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""라벨 대표성 실험 표본 — 층화 표본 + 미끼 (harness/user/archive/legacy/label-representativeness-protocol.md, 4.13절).

판정자(다른 세션의 에이전트)는 **라벨만** 보고 본문을 예측한 뒤, 본문을 보고 척도(질문
`agt:labelRepresentsBody`의 상황 문장 — 프로파일이 원본, 단일 정의처는 `kb_lib.judge_load_profile`)와
확신도(0~1)를 매긴다. 미끼는 라벨을 다른 청크의 본문에 바꿔 붙인 음성 표본이다 — 판정자가
라벨을 읽지 않고 본문에 순응하면 미끼를 못 잡는다(판별력, 8.14절). seed 고정으로 재현된다.

산출 (같은 seed 면 같은 결과):
  <out>/sheet.md — 실험자 기록물. 항목 번호·라벨(ko/en)만. 본문·출처·미끼 여부 없음
  <out>/key.json — 실험자만 본다. 번호 → 파일·본문·층·미끼 여부(미끼면 본문의 실제 출처)·`tools/judge.py --decoys`의 입력
  <judge-sheet>/labels.md·bodies.md (선택, `--judge-sheet <dir>`) — 세션 판정자에게 **주는 것**. 생성 머리·입력
    파일 절·경로·seed 를 싣지 않는다(저장소 위치·답의 단서를 주지 않는다) — 게이트 대상 생성 문서가 아니라
    실험 자극이므로 `<dir>`은 **워크스페이스 밖**이어야 하고 안이면 거부한다(2026-09-30 vnv 결함 보고 ④).
    labels.md는 번호·라벨(ko/en)·**대조 지문**(`kb_lib.label_fingerprint` — 응답에 그대로 적어 돌려준다),
    bodies.md는 번호·본문이다(라벨 공개 → 예측 → 이 파일로 본문 공개의 순서).

사용: label_sample.py --out <dir> [--judge-sheet <워크스페이스 밖 dir>] [--seed 20260911]
      [--sizes req=10,conc=20,rat=15,alt=15] [--decoys 10] [--profile kb/ontology/profile/development] <청크 .md …>
"""
import argparse
import json
import os
import random
import sys
from pathlib import Path
```
<!-- 인용 끝 -->
