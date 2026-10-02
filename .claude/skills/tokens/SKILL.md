---
name: tokens
description: 청크가 상한(저작 산문 1,092 · 인용 2,856)에 얼마나 가까운지 보거나 분할 대상을 고를 때 쓴다 — plane 별 분포·42의 배수별 초과 수·컨텍스트 예산의 환산·상위 20 청크를 고정된 어휘로 낸다.
---

# tokens — 토큰 계수기 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/rules.md` · `tools/kb_lib.py` · `tools/tokens.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

토큰 계수기 — 청크 본문의 토큰 수 분포를 고정된 공개 토크나이저로 낸다 (결정 p1-chunk-unit-is-tokens).

## 언제 쓰는가

청크가 상한(저작 산문 1,092 · 인용 2,856)에 얼마나 가까운지 보거나 분할 대상을 고를 때 쓴다 — plane 별 분포·42의 배수별 초과 수·컨텍스트 예산의 환산·상위 20 청크를 고정된 어휘로 낸다.

## 명령

```bash
bazel run //tools:tokens
bazel run //tools:tokens -- --out /tmp/tokens.md
bazel run //tools:tokens -- kb/dev/decision/<결정>/conclusion.md
```

## 원본

- 절차: [`docs/rules.md` 1. chunk — 자립적 최소 지식 단위](../../../docs/rules.md#1-chunk--자립적-최소-지식-단위)
- 도구: `tools/tokens.py` (`bazel run //tools:tokens`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:tokens -- [청크 파일…] [--out report.md] [--vocab <어휘 파일>]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
