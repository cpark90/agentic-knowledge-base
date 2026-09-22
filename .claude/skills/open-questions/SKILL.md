---
name: open-questions
description: 무엇이 아직 미결인지 — 청크의 선택 슬롯 `미확정:` 에 든 질문과 그것을 안은 청크를 문서에 적지 않고 집계에서 인용할 때 쓴다.
---

# open_questions — 미결 집계 뷰 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/open_questions.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

미결 집계 뷰 — 청크 본문의 선택 슬롯 `미확정:` 을 모아 open.md 를 생성한다 (p4-three-empty-values, p4-slot-answers-one-question).

## 언제 쓰는가

무엇이 아직 미결인지 — 청크의 선택 슬롯 `미확정:` 에 든 질문과 그것을 안은 청크를 문서에 적지 않고 집계에서 인용할 때 쓴다.

## 명령

```bash
bazel build //kg:open && cat bazel-bin/kg/open.md
```

## 원본

- 절차: [`docs/method.md` 9. 뷰](../../../docs/method.md#9-뷰)
- 도구: `tools/open_questions.py` (`bazel run //tools:open_questions`) — 사용법은 docstring 이 원본이다

```text
open_questions.py --out open.md [--bodies <청크 .md …>] [--root .] <TTL…>   (bazel build //kg:open)
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
