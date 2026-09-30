#!/usr/bin/env python3
"""음성 시험 고정물 — 최상위 구역이 11개(모듈 머리 + 절 10)인 소스. 파일 복합체의 직접 부분 상한 9를 넘긴다.

`tools/extract.py` 의 `Builder.build` 가 `FAIL [extract]` 로 거부해야 한다 (4.5절, p7-code-links-on-file-composite).
장 주석(`# ══ 장`)으로 절을 묶는 것이 고치는 방법이고, 9개씩 자르는 것은 하지 않는다.
"""


# ── 하나 ────────────────────
def one() -> int:
    return 1


# ── 둘 ────────────────────
def two() -> int:
    return 2


# ── 셋 ────────────────────
def three() -> int:
    return 3


# ── 넷 ────────────────────
def four() -> int:
    return 4


# ── 다섯 ────────────────────
def five() -> int:
    return 5


# ── 여섯 ────────────────────
def six() -> int:
    return 6


# ── 일곱 ────────────────────
def seven() -> int:
    return 7


# ── 여덟 ────────────────────
def eight() -> int:
    return 8


# ── 아홉 ────────────────────
def nine() -> int:
    return 9


# ── 열 ────────────────────
def ten() -> int:
    return 10
