---
id: https://agentic-knowledge-base.dev/id/chunk/a1596cb9-42a6-467b-b07f-049b266e6c5b
type: decision
level: logical
title_ko: 읽기 응답은 라벨·상태·핵심 링크만이고 본문은 요청 시다
title: A read response carries labels, states and key links only; bodies on request
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/3ebc2598-b846-412e-b76e-4ebb13ce90a4
---
**근거** (노트 5.3절, 5.6절)

- 5.6절이 응답의 실제 형태를 못 박는다 — 스코프와 작업 집합 크기(몇 개 중 몇
  개를 보였는지), plane 디렉토리별 (read)/(write) 표시, 청크마다 `[ID] 라벨 ·
  상태 · 핵심 링크` 한 줄, `suspect`면 그 이유 한 줄, 나머지는 접어서 `... 3
  more (expand?)`.

```
scope: developer-scope   workset: 7 chunks (4 shown, 3 collapsed)
design/  (read)
  [d-17] OAuth2 채택                       stable
  [d-18] 토큰 저장소는 Redis                suspect  ← 가정 a2 unverified
source/  (write)
  [s-203] verify_token                     stable   satisfies d-17
  ... 3 more (expand?)
```

- **라벨·상태·핵심 링크만**으로 조망이 서고 본문이 선택이 되어야 200줄 예산
  안에서 4~5개 청크가 조망된다(4.1절).
- plane별 응답이 다른 것은 각 plane에서 "무엇이 바뀌었나"의 단위가 다르기
  때문이다 — 스키마는 필드, 계약은 시그니처, 산출물은 심볼이다.
