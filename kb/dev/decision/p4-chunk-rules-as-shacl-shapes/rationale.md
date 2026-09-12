---
id: https://agentic-knowledge-base.dev/id/chunk/6f5317ee-a1fb-4990-a7e7-2ba27ea20859
type: decision
level: logical
title_ko: 산문 원칙은 셀 수 없고 shape은 게이트가 판정한다
title: Prose principles cannot be counted; shapes can be judged by the gate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/19abf7d7-e6fe-406a-be99-f9de153f4e95
---
**근거** (노트 4.4절)

- 원칙이 산문이면 준수 여부를 셀 수 없다. **검사 가능한 제약**이 되어야 게이트가
  판정하고, 판정이 에이전트 밖의 규칙으로 넘어간다.
- 다섯 원칙 중 **"접근 가능한 상세"(라벨로 대표)만 검사할 수 없다.** 이것은
  shape이 아니라 운용으로 강제한다 — 5.3절 읽기 응답이 라벨 목록을 기본으로
  쓰고, 4.13절 라벨 대표성 지표가 사후에 관측한다.
- plane별 추가 제약을 상속으로 쌓으면 공통 제약이 한 곳에만 있다.
