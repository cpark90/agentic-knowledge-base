---
name: workset
description: dispatch 전에 역할·수준 창·앵커로 거른 작업 집합(라벨 목록과 이웃 본문)을 컨텍스트 예산 안에서 뽑을 때 쓴다.
---

# workset — 작업 집합 뷰

> 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring과 `kb_lib.SKILLS` (`tools/gen_skills.py`). 검사: `//:skills_drift_test`

작업 집합 뷰 — 스코프 × 수준 창으로 거른 라벨 목록과 앵커 이웃을 예산 안에 담는다 (노트 0.5절, 5.6절, 11.3절).

## 언제 쓰는가

dispatch 전에 역할·수준 창·앵커로 거른 작업 집합(라벨 목록과 이웃 본문)을 컨텍스트 예산 안에서 뽑을 때 쓴다.

## 명령

```bash
bazel build //kg:workset --//kb:role=developer --//kb:anchor='<라벨|IRI>' --//kb:levels=concrete
cat bazel-bin/kg/workset-developer.md
```

## 원본

- 절차: [`docs/method.md` 8. 조회](../../../docs/method.md#8-조회)
- 도구: `tools/workset.py` (`bazel run //tools:workset`) — 사용법은 docstring 이 원본이다

```text
workset.py --role developer [--levels logical,concrete] [--anchor <IRI|라벨 부분>] [--budget 200] --out workset.md <TTL...>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
