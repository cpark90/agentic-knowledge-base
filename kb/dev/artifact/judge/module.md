---
id: https://agentic-knowledge-base.dev/id/chunk/8f62ee13-60ea-4dac-be12-36fb38b24515
type: artifact
level: executable
title_ko: 파일 tools/judge.py
title: file tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
composite: {id: https://agentic-knowledge-base.dev/id/composite/85cd0960-2c5b-4a4c-b5be-bcf71f036c54, title_ko: 파일 복합체 tools/judge.py, title: file composite tools/judge.py, ordered: [https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add, https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436, https://agentic-knowledge-base.dev/id/composite/97e93b30-be59-4c26-b322-176b8e0f350e, https://agentic-knowledge-base.dev/id/composite/8f3b4eaf-dced-410d-98cc-6771157e17c6, https://agentic-knowledge-base.dev/id/composite/25ad6efd-997a-44a7-b5c4-dc61c13b63ed, https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc, https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83, https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac]}
---
**파일** — `tools/judge.py` 다. 717줄 · 최상위 정의 32개 · 최상위 절 8개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""판정자 — 등록된 판정 질문을 단위 지식에 물어 판정 로그와 결과 주석을 남긴다 (노트 8.14절, 결정 p8-judge-session-agreement —
질문 형·원자성·척도는 그 결정의 규칙 ⑤를 따르고, 임계는 확신도가 아니라 일치율이다 — 규칙 ③, Q-0056 Q119-a).

게이트 밖 도구다. `bazel test`는 판정을 부르지 않고 판정 로그의 형식·필수 필드만 본다(게이트 id `judge-log`).
판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다(유저 답 2026-09-30,
harness/channel/archive/legacy/handoff/judge-without-service-2026-09-30.md) — 외부 호출은 없고 응답은 `--responses`로 오프라인
입력된다. 질문·척도·임계의 원본은 프로파일 온톨로지와 shape다(`kb/ontology/profile/development/judge-*-ontology.ttl` ·
`kb/ontology/shapes/judge-question-shapes.ttl`) — 도구는 질문 문장을 상수로 갖지 않는다. 질문의 형은
noul·choice·score 셋이고 선택 집합은 255 이하다. 넘으면 독립 점수 → 명시 선택 2단계를 안내하고 거부한다.
확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(세션 판정자마다 하나) 주면
같은 (질문·입력 해시값)의 값 일치 여부를 계산해 로그의 `일치` 열에 낸다. 자동 적용은 정확도·판별력을 잰 뒤에만
켠다(`p8-judge-session-agreement` 규칙 ④) — 지금은 전부 사람 확인 큐다. `--record` 는 로그를 쓰기 전에 shape
(`kb_lib.JUDGE_LOG_SHAPES` — 판정자 둘의 답 · 일치 여부 열 · 미끼 검출 결과 · 단독 응답의 자동 적용 금지)로 검사하고
위반이 있으면 쓰지 않는다.
`--decoys <json>`(`label_sample.py --judge-sheet`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의
라벨+본문(`kb_lib.label_fingerprint`)으로 응답을 대조하고 미끼 검출률을 보고 요약에 낸다 — **대조 해시값은 항상
판정자에게 보인 라벨+본문**이지 단위 지식 파일 바이트가 아니다(2026-09-30 결함 보고, 파일 해시값으로 대조하면 세션
판정자의 응답이 전부 안 잡힌다). 파일 바이트 해시값은 로그의 `입력 해시값` 열에 그대로 남는다 — 추적용이지 대조 키가
아니다.
**쌍 모드** `--pairs <key.json>`(`label_sample.py --pair-sheet` 가 낸 정답 key — task 0262, Q-0061 Q145-a)는 링크 후보 쌍을 판정한다.
행은 쌍 하나이고 `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>`(kb_lib.pair_target)다. 응답은 쌍의 대조 해시값
(`kb_lib.pair_fingerprint`)으로 찾고 일치는 (쌍, 입력 해시값)으로 묶는다. 질문은 쌍마다 key 에 적힌 noul 질문(`overlapsHolds`·
`proposedLinkHolds`)이고 질문마다 판정 로그를 따로 낸다. `입력 해시값` 은 sha256(앵커 파일 바이트 ∥ 대상 파일 바이트)이다. 판정지를
만든 뒤 두 파일 중 하나의 라벨이나 본문이 바뀐 쌍은 낡은 판정이라 행을 내지 않는다. 미끼(음성 — 근거 없는 쌍, 양성 — 확정된 겹침)는
로그와 증거에 넣지 않고 검출률만 남긴다 — 음성 미끼에 no, 양성 미끼에 yes 가 검출이다. 결과 주석은 쌍마다 하나이고(판정자들의 값·확신도·
일치를 한 주석에) 파일 이름에 쌍 해시값 앞 8자를 싣고 `targets:` 에 두 IRI 를 적는다.
사용: bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>]
      [--record] [--into <디렉토리>] <단위 지식 파일…>
      bazel run //tools:judge -- --pairs <key.json> --responses <json> --responses <json> [--record] [--into <디렉토리>]
      python3 tools/judge.py --question labelRepresentsBody --responses r1.json --responses r2.json --decoys key.json
출력·종료: 보고는 stdout(`--out`으로 파일)이고 `--record`는 판정 로그(`kb/vv/run/judge-<UTC>.md`)와 결과
주석(`kb/vv/verdict/<슬러그>.md`)을 append-only로 쓴다. 질문 없음·형 밖·선택 집합 255 초과·응답 없음·읽을 수 없는
입력은 `FAIL [judge] …` + EXIT_CONFIG. 판정 대상(단위 지식·미끼)이 0건이면 EXIT_SKIP이다.
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
