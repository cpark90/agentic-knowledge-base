---
id: https://agentic-knowledge-base.dev/id/chunk-d0159
type: decision
level: concrete
title_ko: 목록은 손으로 복제하지 않고 생성하고 대조한다
title: Generate indexes from disk and diff them in CI
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 같은 목록(색인·카탈로그·매니페스트)이 두 곳 이상에 필요하면 손으로
복제하지 않고 **디스크의 실물에서 결정론적으로 생성**하며, CI가 생성기를 검사
모드로 돌려 커밋된 산출물과 어긋나면 실패시킨다. 각 항목의 값은 실물 파일이
스스로 선언한 것을 읽고 **경로에서 추측하지 않는다**.

**근거** (harness-functional docs/federation-design.md 카탈로그 생성)
- 손으로 세 곳에 목록을 복제하던 시절 실제로 드리프트가 났다. 카탈로그에서 한
  유닛이 빠져 **union이 부분만 로드된 채 검증이 통과**했다 — 게이트는 초록인데
  검사 대상이 조용히 줄어 있었으므로, 실패 중 가장 나쁜 종류다. 게이트를
  믿으려면 게이트의 입력 범위가 먼저 보증돼야 한다.
- 생성기는 중복 자체를 없애고, 검사 모드는 "생성물이 실물과 일치하는가"를
  게이트 조건으로 만든다. 정합성을 사람의 주의력에 맡기지 않는다.
- 항목 값을 경로에서 추측하면 파일 이동이 곧 의미 변경이 된다. 실물의 선언을
  읽으면 디렉토리 배치는 사람이 읽는 조직화로만 남고 도구에는 투명해진다.

**이 저장소와의 관계** — 세 실패 모드(d-0014) 중 drift의 **생성물 판**이다.
어휘의 drift는 통제 어휘가, 생성물의 drift는 생성기와 대조 게이트가 막는다.
