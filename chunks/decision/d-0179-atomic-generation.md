---
id: https://agentic-knowledge-base.dev/id/chunk-d0179
type: decision
level: concrete
title_ko: 생성은 전부 성공했을 때만 원자적으로 교체한다
title: Generation lands atomically, only on full success
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 생성은 임시 위치에 산출물 전체를 만들고 모든 게이트를 그 위에서
통과시킨 뒤, **전부 성공했을 때만** 원자적 교체로 목적지에 놓는다. 어느
단계에서든 실패하면 임시본을 버리고 목적지는 손대지 않는다.

**근거** (harness-concrete docs/odr-bind-lock.md §"Atomic emit")
- 일부 게이트는 파일을 쓴 뒤에만 판정할 수 있다 — 복사한 내용의 해시 대조가
  그렇다. 목적지에 바로 쓰면 그 실패가 **반쪽 산출물**을 남긴다.
- 반쪽 산출물은 조용한 두 번째 진실 공급원이다. 정상 결과처럼 보이지만
  어느 게이트도 통과하지 않았고, 다음 사람이 그것을 원본으로 읽는다.
  문서를 저장하지 않고 생성한다는 규율(d-0151)은 "생성 실패 = 이전 상태
  유지"가 성립해야 안전하다.
- 임시 위치는 목적지와 같은 저장 계층에 둔다 — 그래야 교체가 실제로
  원자적이다. 목적지가 이미 있으면 옛 것을 옆으로 옮긴 뒤 새 것을 놓고,
  교체 자체가 실패하면 되돌린다.
- 임시 경로가 산출물 내용에 새어서는 안 된다. 새면 임시 위치를 쓴다는
  사실만으로 실행마다 산출이 달라져 바이트 동일성(d-0178)이 깨진다.
