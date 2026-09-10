---
id: https://agentic-knowledge-base.dev/id/chunk-d0150
type: decision
level: concrete
title_ko: 산출물 리뷰는 본문보다 먼저 맥락을 보여준다
title: Artifact review shows context before the body
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 변경된 `artifact` 청크의 리뷰어에게 산출물 본문을 읽기 전에
**"무엇을 위한 변경이고 무엇이 흔들리는가"** 를 먼저 보여준다.

**근거** (노트 10.9절) — 표시 항목과 그 출처.
- 이 청크가 충족하는 결정 = `satisfies` → `decision` 청크 라벨
- 그 결정의 가정과 현재 상태 = `assumes` + 상태
- 이 변경으로 `suspect`가 될 링크 = 8.6절 재판정 예측
- 이 청크를 검증하는 시나리오 = `verifies` 역방향
- 42줄 초과 여부, 라벨 변경 여부 = shape

- 전부 이미 있는 링크의 조회이므로 리뷰용 메타데이터를 따로 적지 않는다.
- 코드 리뷰가 대표적이나 문서·절차 리뷰도 같다 — `artifact` plane이면
  산출물의 종류를 가리지 않는다.
