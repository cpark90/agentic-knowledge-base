---
id: https://agentic-knowledge-base.dev/id/chunk/77244ea8-dcdf-4646-9c5c-07e0d40cb223
type: artifact
level: executable
title_ko: 파일 tools/belief_calibration.py
title: file tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453]
---
**파일** — `tools/belief_calibration.py` 다. 495줄이고 이 단위 지식은 추출 생성물이다. 함수와 클래스, 절은 항목으로 올리지 않고 그 원문은 소스에만 있다. 링크와 가정의 자리가 이 파일 항목이다.

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
        이 평균이 보정 전 C 다. 결정 p9-belief-by-calibrated-judge 가 정한 C 의 값은 보정한 값이고, 보정은 사람 라벨 표본(C 값이 있는
        항목)이 20건 이상이면 적용한다(Q186-b). 그래서 보정 전 C 는 참고로만 내고 술어 1·2 합격과 선택의 후보에서 뺀다.
  보정한 C  Platt 보정이다. 입력은 x_i = ln(p_i / (1 − p_i))이고(p_i 는 보정 전 C), 모형 q = σ(a·x + b)의 a·b 를 라벨 y_i 의 로그 우도
        최대화로 맞춘다. p_i 는 [ε, 1 − ε]로 자르고 ε = 1e-6 이다 — 확신도는 유한 자릿수의 십진 표기여서 0 과 1 만 로짓이 무한이 되고,
        ε 은 그 밖의 값의 순서와 값을 바꾸지 않을 만큼 작으며 잘린 로짓 ±13.8 은 헤세 행렬을 부동소수점 범위 안에 둔다. 맞춤은 순수 파이썬
        (math)의 뉴턴법이고 (0, 0)에서 시작해 로그 우도가 줄면 걸음을 반으로 줄인다(최대 30번). 매개변수 변화량의 최댓값이 1e-10 미만이면
        수렴이고, 반복 상한 100번 안에 수렴하지 않거나 헤세 행렬이 특이하면 보정 불가다. 라벨이 한 값뿐이거나 한 라벨의 로짓이 모두 다른
        라벨의 로짓 이하인 분리 표본은 최대 우도 해가 무한이므로 뉴턴법 전에 보정 불가로 낸다. 보정 불가는 값을 내지 않고 판정하지 않는다.
        평가는 하나씩 빼는 교차 검증(LOO)이다 — 항목 i 의 보정값 q_i 는 i 를 뺀 n − 1 건으로 맞춘 (a, b)의 값이고, 술어 1·2 는 이 q_i 로
        판정한다. 한 번의 맞춤이라도 보정 불가이면 보정한 C 전체가 보정 불가다. 전체 n 건으로 맞춘 (a, b)는 보정 식의 기록으로만 낸다.
        q_i 는 부동소수점 값을 분수로 바꾼 값이고(Fraction(float)은 정확하다) 그 뒤의 계산은 다른 규칙과 같다.
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
        독립 사람 라벨만으로 같은 계산을 병기하되 판정에 쓰지 않는다(Q178-b). 보정한 C 는 독립 라벨이 20건 미만이면 맞추지 않고 표본
        부족으로 내며, 대신 전체 표본의 LOO 값 가운데 독립 라벨 항목만 모은 Brier 를 판정에 쓰지 않는 값으로 병기한다.
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
from math import comb, exp, isfinite, log, log1p
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import PROV
```
<!-- 인용 끝 -->
