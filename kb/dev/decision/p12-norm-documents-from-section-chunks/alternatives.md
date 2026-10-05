---
id: https://agentic-knowledge-base.dev/id/chunk/7090802d-edc5-4909-b2de-949738da5ecb
type: decision
level: logical
title_ko: 손 문서와 링크 게이트·기존 plane의 예외 형식·YAML 골격·본문 자리 표지·근거 열 없는 본문 표 안은 기각된다
title: Hand-written documents with a link gate, an exception form in an existing plane, a YAML skeleton, a placement marker in the body, and body tables without a source column are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:07:33+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5c148128-480b-40d0-a8ff-76bcd4884244
---
**대안** — 여섯을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 문서는 손으로 두고 결정 링크를 게이트로 검사한다(Q12-b·c 원안) | 원본이 둘로 남는다. 링크가 실재해도 링크 밖 문장의 드리프트를 막지 못한다. 유저가 Q19에서 전체 생성을 골랐다 |
| 절 청크를 `annotation` plane에 예외 형식으로 둔다(Q21-b) | 주석 형식(첫 줄 라벨·대상·본문 4문장) 검사와 충돌해 plane 하나가 형식 둘을 갖는다. 유저가 Q21에서 고르지 않았다 |
| 절 청크를 `decision` plane에 역할 태그 예외로 둔다(Q21-c) | 결론·근거·대안 검사에서 절 청크를 빼는 예외가 생긴다. 유저가 Q21에서 고르지 않았다 |
| 골격을 문서마다 YAML 파일 하나로 둔다 | 청크가 아닌 두 번째 원본 형식이 되고, 절의 순서가 그래프 밖에 남아 `chunk2kg`가 읽지 못한다 |
| 표의 자리를 본문 안 표지로 정한다(대안 B) | 본문에 산문 밖의 둘째 문법이 생긴다. `docs/method.md`처럼 한 절에 묶음이 여럿인 꼴을 풀지 못한다 |
| 근거 열이 없는 표를 절 청크 본문의 표로 둔다(대안 C) | 그 행은 `규약:` 줄이 아니라 "정확히 한 번" 검사 밖에 남고, 결정과 별개인 둘째 원본이 된다 |
