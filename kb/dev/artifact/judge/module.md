---
id: https://agentic-knowledge-base.dev/id/chunk/8f62ee13-60ea-4dac-be12-36fb38b24515
type: artifact
level: executable
title_ko: 파일 tools/judge.py
title: file tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
composite: {id: https://agentic-knowledge-base.dev/id/composite/85cd0960-2c5b-4a4c-b5be-bcf71f036c54, title_ko: 파일 복합체 tools/judge.py, title: file composite tools/judge.py, ordered: [https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add, https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436, https://agentic-knowledge-base.dev/id/composite/97e93b30-be59-4c26-b322-176b8e0f350e, https://agentic-knowledge-base.dev/id/composite/8f3b4eaf-dced-410d-98cc-6771157e17c6, https://agentic-knowledge-base.dev/id/composite/25ad6efd-997a-44a7-b5c4-dc61c13b63ed, https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc, https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac]}
---
**파일** — `tools/judge.py` 다. 521줄 · 최상위 정의 24개 · 최상위 절 7개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""판정자 — 등록된 판정 질문을 청크에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-session-agreement —
질문 형·척도·임계 셋 자체는 옛 결정 p8-judge-calibration-binding·p8-judge-question-form 그대로다).

게이트 밖 도구다. `bazel test`는 판정을 부르지 않고 판정 로그의 형식·필수 필드만 본다(게이트 id `judge-log`).
판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다(유저 답 2026-09-30,
harness/channel/archive/legacy/handoff/judge-without-service-2026-09-30.md) — 외부 호출은 없고 응답은 `--responses`로 오프라인
입력된다. 질문·척도·임계의 원본은 프로파일 온톨로지와 shape다(`kb/ontology/profile/development/judge-*-ontology.ttl` ·
`kb/ontology/shapes/judge-question-shapes.ttl`) — 도구는 질문 문장도 임계도 상수로 갖지 않는다. 질문의 형은
noul·choice·score 셋이고 선택 집합은 255 이하다. 넘으면 독립 점수 → 명시 선택 2단계를 안내하고 거부한다.
확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(세션 판정자마다 하나) 주면
같은 (질문·입력 지문)의 값 일치 여부를 계산해 로그의 `일치` 열에 낸다. 일치율 임계와 자동 적용은 별도 결정
(`p8-judge-session-agreement`)이 3지표 중 정확도·판별력의 재측정 뒤에 정한다 — 지금은 전부 사람 확인 큐다.
`--decoys <json>`(`label_sample.py --judge-sheet`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의
라벨+본문(`kb_lib.label_fingerprint`)으로 응답을 대조하고 미끼 검출률을 보고 요약에 낸다 — **대조 지문은 항상
판정자에게 보인 라벨+본문**이지 청크 파일 바이트가 아니다(2026-09-30 결함 보고, 파일 지문으로 대조하면 세션
판정자의 응답이 전부 안 잡힌다). 파일 바이트 지문은 로그의 `입력 지문` 열에 그대로 남는다 — 추적용이지 대조 키가
아니다.
사용: bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>]
      [--record] [--into <디렉토리>] <청크 파일…>
      python3 tools/judge.py --question labelRepresentsBody --responses r1.json --responses r2.json --decoys key.json
출력·종료: 보고는 stdout(`--out`으로 파일)이고 `--record`는 판정 로그(`kb/vv/run/judge-<UTC>.md`)와 결과
주석(`kb/vv/verdict/<슬러그>.md`)을 append-only로 쓴다. 질문 없음·형 밖·선택 집합 255 초과·응답 없음·읽을 수 없는
입력은 `FAIL [judge] …` + EXIT_CONFIG. 판정 대상(청크·미끼)이 0건이면 EXIT_SKIP이다.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph
```
<!-- 인용 끝 -->
