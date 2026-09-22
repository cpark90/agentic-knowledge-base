---
name: choices
description: 무엇을 아직 고르지 않았는가 — 열린 설계 변수와 그 후보를 체크박스(`[ ]` 열림 · `[-]` 배제 + 근거 · `[x]` 확정)로 확인할 때 쓴다.
---

# choices — 설계 공간의 체크박스 뷰 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/choices.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

설계 공간의 체크박스 뷰 — 열린 설계 변수와 그 후보를 choices.md 로 생성한다 (결정 p9-candidate-storage 13.5절).

## 언제 쓰는가

무엇을 아직 고르지 않았는가 — 열린 설계 변수와 그 후보를 체크박스(`[ ]` 열림 · `[-]` 배제 + 근거 · `[x]` 확정)로 확인할 때 쓴다.

## 명령

```bash
bazel build //space:choices && cat bazel-bin/space/choices.md
```

## 원본

- 절차: [`docs/method.md` 5. 후보 관리](../../../docs/method.md#5-후보-관리)
- 도구: `tools/choices.py` (`bazel run //tools:choices`) — 사용법은 docstring 이 원본이다

```text
choices.py --out choices.md <TTL…>   (bazel build //space:choices)
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
