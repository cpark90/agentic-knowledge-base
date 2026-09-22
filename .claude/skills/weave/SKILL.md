---
name: weave
description: 결정 기록·요구 색인·변경 이력·감사 보고서를 저장하지 않고 그래프와 관측에서 생성해 인용할 때 쓴다.
---

# weave — 문서 뷰 생성기 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/weave.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

문서 뷰 생성기 — 그래프와 청크 본문에서 ADR·요구 색인·변경 이력을 생성한다 (노트 4.6절 weave, method §9, p12-documents-are-generated).

## 언제 쓰는가

결정 기록·요구 색인·변경 이력·감사 보고서를 저장하지 않고 그래프와 관측에서 생성해 인용할 때 쓴다.

## 명령

```bash
bazel build //kg:audit && cat bazel-bin/kg/audit.md
bazel build //kb/dev:adr //kb/dev:requirements //kb/dev:changelog
```

## 원본

- 절차: [`docs/method.md` 9. 뷰](../../../docs/method.md#9-뷰)
- 도구: `tools/weave.py` (`bazel run //tools:weave`) — 사용법은 docstring 이 원본이다

```text
weave.py --kind adr|requirements|changelog|audit --out <파일> [--root .] <그래프 ttl …> [--bodies <청크 .md …>]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
