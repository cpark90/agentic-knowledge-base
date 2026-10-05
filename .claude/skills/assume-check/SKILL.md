---
name: assume-check
description: 가정을 ODD 조건으로 판정해 깨진 가정의 직접 영향 집합과 suspect 후보를 내거나 --break 로 인위 파괴 실험을 할 때 쓴다.
---

# assume_check — 가정 판정과 전파 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/assume_check.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

가정 판정과 전파 — 도입 4단계 "가정과 무효화"의 첫 형태 (노트 6.5절·6.9절, method §7, p6-assumption-verification-methods, p6-assumption-invalidation).

## 언제 쓰는가

가정을 ODD 조건으로 판정해 깨진 가정의 직접 영향 집합과 suspect 후보를 내거나 --break 로 인위 파괴 실험을 할 때 쓴다.

## 명령

```bash
bazel run //tools:assume_check
bazel run //tools:assume_check -- --break cond-build-system
bazel run //tools:assume_check -- --record && python3 tools/gen_build.py --root .
```

## 원본

- 절차: [`docs/method.md#7-갱신`](../../../docs/method.md#7-갱신)
- 도구: `tools/assume_check.py` (`bazel run //tools:assume_check`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:assume_check -- [--break <cond-id>…] [--record] [--out report.md] [--odd kb/odd/project-odd.yml] [TTL…]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
