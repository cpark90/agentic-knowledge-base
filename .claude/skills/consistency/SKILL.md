---
name: consistency
description: 커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도) 후보를 보고로 확인할 때 쓴다.
---

# consistency — 정합성 보고 뷰

> 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring과 `kb_lib.SKILLS` (`tools/gen_skills.py`). 검사: `//:skills_drift_test`

정합성 보고 뷰 — 중복·라벨 형식·용어 위반을 청크 파일에서 보고한다 (p4-redundancy-as-safety-margin).

## 언제 쓰는가

커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도) 후보를 보고로 확인할 때 쓴다.

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
