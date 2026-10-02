---
name: impact
description: 청크·결정을 고치기 전에 영향 항목 수·plane 분포·suspect 가 될 링크 수·승인이 필요한 결정 수를 계산할 때 쓴다.
---

# impact — 영향 분석 1단계 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/impact.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

영향 분석 1단계 — 변경 전에 "X를 바꾸면 무엇이 영향받는가"를 Bazel 의존 그래프에서 계산한다 (노트 12.6절, method §12).

## 언제 쓰는가

청크·결정을 고치기 전에 영향 항목 수·plane 분포·suspect 가 될 링크 수·승인이 필요한 결정 수를 계산할 때 쓴다.

## 명령

```bash
bazel run //tools:impact -- //kb/dev/requirement:<타깃>
bazel run //tools:impact -- //kb/dev/decision:<결정> --universe //kb/...
```

## 원본

- 절차: [`docs/method.md` 12. 영향 분석](../../../docs/method.md#12-영향-분석)
- 도구: `tools/impact.py` (`bazel run //tools:impact`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:impact -- //kb/dev/requirement:r-008-every-requirement-descends [--universe //kb/...]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
