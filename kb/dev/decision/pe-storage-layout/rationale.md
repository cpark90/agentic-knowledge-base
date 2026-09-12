---
id: https://agentic-knowledge-base.dev/id/chunk/8fbc4644-38d0-4a50-8ab7-bbc01c54f53c
type: decision
level: logical
title_ko: 참조 방향이 디렉터리 경계와 일치해야 독립성이 빌드로 검사된다
title: Independence is build-checkable only if reference direction matches directory boundaries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/6d696b3f-6d63-476e-bb56-65f27d8d2ed5
---
**근거** (노트 부록 E.7, 8.5절, 5.6절) — 8.5절 "V&V → 개발 방향만"이 디렉터리 경계와 일치하면 visibility로 강제되고 독립성 게이트가 provenance 질의가 아니라 빌드 실패가 된다. `index.md`가 디렉터리마다 있는 것은 라벨 목록 우선 읽기(5.6절)의 파일 형태이며 생성물이어야 본문과 어긋나지 않는다. 온톨로지·ODD가 `kb/` 안에 있는 이유는 둘도 청크 규칙(4.1절)을 따르는 지식이기 때문이다.
