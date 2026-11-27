---
id: https://agentic-knowledge-base.dev/id/chunk/77244ea8-dcdf-4646-9c5c-07e0d40cb223
type: artifact
level: executable
title_ko: 파일 tools/belief_calibration.py
title: file tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T04:11:19Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453]
composite: {id: https://agentic-knowledge-base.dev/id/composite/589ba97d-9372-4794-b33c-9b040ecccc97, title_ko: 파일 복합체 tools/belief_calibration.py, title: file composite tools/belief_calibration.py, ordered: [https://agentic-knowledge-base.dev/id/composite/53c1af98-94eb-4b8d-81cf-9914292abca6, https://agentic-knowledge-base.dev/id/composite/1edd84f8-3e8d-4183-996c-4666aefe4a4a, https://agentic-knowledge-base.dev/id/composite/7b6663a6-1c06-4819-aae0-798a36f11390, https://agentic-knowledge-base.dev/id/composite/ec53d97b-e4f9-4f6b-983a-cc20d67bb1b6]}
---
**파일** — `tools/belief_calibration.py` 다. 350줄 · 최상위 정의 12개 · 최상위 절 4개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""믿음 정도 계산 규칙의 보정 측정 — 사람 정답 라벨 표본에서 규칙마다 Brier 점수와 구간별 이항 구간을 계산해 belief-calibration.md 를 생성한다
(합격 기준 belief-calibrated-against-human-labels, 설계 공간 degree-of-belief-space 의 닫기 기준, 유저 결정 Q181-a·Q182-a).

  표본  관측 기록 `kb/vv/run/label-*.md` 의 라벨 표(`문항` · `링크 IRI` · `라벨` · `지위` 열)의 행 하나가 항목 하나다. 라벨은 1 또는 0 이고,
        지위가 '독립'으로 시작하면 독립 사람 라벨이다(Q178-b). 같은 링크 IRI 가 두 행에 나오면 설정 문제로 끝난다.
  규칙 C judge-mean  판정 로그(`kb/vv/run/judge-*.md`, generated.by `process:judge`)의 쌍 행(`대상` 이 `<출발> ↔ <도착> · <종류>`)마다
        링크 IRI 를 chunk2kg 의 규칙대로 계산한다 — `link_hash(뿌리(출발), 종류, 뿌리(도착))`, 뿌리는 head 그래프의 `prov:specializationOf`
        사슬 끝(chunk2kg.work_id)이다. 옛 결정 IRI(`…/id/chunk-dNNNN`)는 사슬에 없으므로 그대로 해시되고, 라벨 기록의 링크 IRI 도 양 끝의
        전체 IRI 로 계산했으므로(기록 본문) 같은 값이 된다. 항목의 값은 그 링크 IRI 에 결합된 판정 행의 확신도('예'의 확률) 평균이고
        run_evidence.belief_of 의 C 정의를 그대로 부른다. 같은 (판정 로그, 판정자, 극성, 확신도)는 run_evidence 처럼 한 번 센다.
        판정 증거와 달리 입력 해시값으로 낡은 판정을 거르지 않는다 — 라벨은 표본 당시 주장의 판단이고 옛 끝점 파일은 지금 없어서,
        결합 열쇠는 양 끝 IRI 와 종류로 만든 링크 IRI 하나다(Q182-a). 링크 종류 어휘로도 거르지 않는다 — 표본에는 `cites` 가 있다.
        C 는 보정 전 값이다(결정 p9-belief-by-calibrated-judge — 보정은 확신도 구간마다 표본 하한 20을 채운 뒤에 적용한다).
  규칙 A kind-rank · B beta-binomial  그래프의 `agt:DegreeOfBelief` 노드(링크의 `agt:hasDegreeOfBelief`, `agt:beliefRule`, `agt:beliefValue`)
        에서 표본의 링크 IRI 와 같은 링크의 값만 읽는다. 값이 없는 항목은 그 규칙의 표본에서 빠지고, 다른 링크(뒤이은 링크)의 값을 빌려 오지
        않는다(Q182-a). 규칙 IRI → slug 는 run_evidence.BELIEF_RULES 다.
  계산  규칙마다 값이 있는 항목 n 개로 계산한다. 값과 라벨은 분수(fractions.Fraction)로 계산해 비교에 반올림이 끼지 않는다.
        술어 1  B(R) = mean (p_i − y_i)² 이 기저율 Brier mean (ȳ − y_i)² 보다 작으면 참이고 같으면 거짓이다. ȳ 는 같은 n 항목의 참 비율이다.
        술어 2  n < 50 이면 구간은 [0, 1/3) · [1/3, 2/3) · [2/3, 1] 셋이다. 경계값 1/3 은 둘째 구간, 2/3 은 셋째 구간, 1 은 셋째 구간에 든다.
                n ≥ 50 의 구간 수는 합격 기준이 정하지 않았으므로 이 도구는 판정하지 않고 그 사실을 낸다. 표본이 있는 구간 k 마다 n_k ·
                평균 예측 p̄_k · 관측 빈도 ō_k 를 내고, 허용폭은 Binomial(n_k, p̄_k) 의 2.5% 분위수 lo 와 97.5% 분위수 hi 를 n_k 로 나눈
                [lo/n_k, hi/n_k] 다. 분위수 q 는 F(x) ≥ q 인 가장 작은 정수 x 이고(F 는 정확 이항 누적분포, 순수 파이썬 분수 계산), 구간은
                닫힌 구간이라 성공 수가 lo 이상 hi 이하이면 든다. 한 구간이라도 벗어나면 거짓이다.
        술어 3  게이트 `belief-consistency` 의 PASS 다. 이 도구는 판정하지 않고 입력으로 받지 않는다.
        n < 20 인 규칙은 '표본 부족'으로 내고 판정하지 않는다 — 값은 참고로 따로 낸다. 술어 1·2가 참인 규칙 가운데 B(R)가 가장 작은 규칙이 선택이다.
        독립 사람 라벨만으로 같은 계산을 병기하되 판정에 쓰지 않는다(Q178-b).
  판정  없음 — 뷰이고 게이트가 아니다. 설계 공간을 닫는 일은 orchestrator 가 이 생성물을 인용해 한다.

종료 코드(kb_lib): 0 생성됨 · 2 설정·입력 문제(라벨 기록 없음·라벨 표를 읽지 못함·같은 링크 IRI 의 두 행·그래프 파싱 실패)
사용: belief_calibration.py --out belief-calibration.md --records <kb/vv/run 의 .md …> --graphs <head·참조 그래프 TTL …>   (bazel build //kg:belief_calibration)
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import PROV
```
<!-- 인용 끝 -->
