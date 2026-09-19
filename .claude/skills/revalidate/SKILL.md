---
name: revalidate
description: 청크 본문을 고친 뒤 base 리비전 대비 재판정 대상(링크 상대·복합체 형제·하류 의존자)을 표로 낼 때 쓴다.
---

# revalidate — 재검증 후보

> 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring과 `kb_lib.SKILLS` (`tools/gen_skills.py`). 검사: `//:skills_drift_test`

재검증 후보 — 본문 해시가 바뀐 청크의 링크와 하류 의존자를 재판정 대상으로 보고한다 (dependency-graph-design §5, method §7).

## 언제 쓰는가

청크 본문을 고친 뒤 base 리비전 대비 재판정 대상(링크 상대·복합체 형제·하류 의존자)을 표로 낼 때 쓴다.

## 명령

```bash
bazel run //tools:revalidate -- --base HEAD
bazel run //tools:revalidate -- --base <rev> --out /tmp/revalidate.md
```

## 원본

- 절차: [`docs/method.md` 7. 갱신](../../../docs/method.md#7-갱신)
- 도구: `tools/revalidate.py` (`bazel run //tools:revalidate`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:revalidate -- [--base HEAD] [--universe '//...'] [--out report.md]
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--이-문서가-원본이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
