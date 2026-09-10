---
id: https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395
type: requirement
level: functional
title_ko: verifies의 주어는 V&V 청크뿐이다
title: Only V&V chunks may be the subject of verifies
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 체계는 verifies 링크의 주어를 V&V KB의 청크로만 허용하여야 한다.

- **이해관계자**: 검증자 · **관심사**: 독립성
- **출처**: 노트 6.1절·7.2절 / 구조도 검증기

개발 산출물이 자기를 검증했다고 주장하는 것을 어휘 수준에서 막는다.
