---
name: metrics
description: 고아율·CQ19·CQ20 커버리지·도입 단계 통과 조건 같은 수치를 문서에 적지 않고 생성물에서 인용할 때 쓴다.
---

# metrics — 코어 지표 뷰 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/metrics.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

코어 지표 뷰 — 그래프에서 metrics.md를 생성한다 (노트 4.13절, 10.14절, 12.3절, 14.1절).

## 언제 쓰는가

고아율·CQ19·CQ20 커버리지·도입 단계 통과 조건 같은 수치를 문서에 적지 않고 생성물에서 인용할 때 쓴다.

## 명령

```bash
bazel build //kg:metrics && cat bazel-bin/kg/metrics.md
```

## 원본

- 절차: [`docs/method.md` 완료 판정](../../../docs/method.md#완료-판정)
- 도구: `tools/metrics.py` (`bazel run //tools:metrics`) — 사용법은 docstring 이 원본이다

```text
metrics.py --out metrics.md --residency defs/kb.bzl <TTL...>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
