---
name: consistency
description: 커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도)·첨가(메타 문장·채움·빈 값 이상 표기)·목록 규칙 후보를 보고로 확인할 때 쓴다.
---

# consistency — 정합성 보고 뷰 (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/consistency.py` · `tools/kb_lib.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 청크 파일에서 보고한다 (p4-redundancy-as-safety-margin).

## 언제 쓰는가

커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도)·첨가(메타 문장·채움·빈 값 이상 표기)·목록 규칙 후보를 보고로 확인할 때 쓴다.

## 명령

```bash
bazel build //kb:consistency && cat bazel-bin/kb/consistency.md
```

## 원본

- 절차: [`docs/method.md` 9. 뷰](../../../docs/method.md#9-뷰)
- 도구: `tools/consistency.py` (`bazel run //tools:consistency`) — 사용법은 docstring 이 원본이다

```text
consistency.py --out consistency.md [--theta 0.5] [--theta-cohesion θ/2] [--glossary docs/glossary.md] [--waivers docs/waivers.md] <청크 .md …>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
