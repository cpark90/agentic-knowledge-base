---
id: https://agentic-knowledge-base.dev/id/chunk/0785017b-530e-497b-9dfd-caaeb0f145f2
type: decision
level: logical
title_ko: 마지막 조건이 두 KB 연동의 실체다
title: The last condition is what coupling of the two KBs actually means
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c831629d-706d-4d61-90e5-f4d848758731
---
**근거** (노트 7.9절, 8.1절, 8.3절) — 개발 KB는 자기 완결을 판정하지 못하고 V&V KB의 상태를 읽어야 한다. 이것이 "연동의 이유는 완주"(8.1절)의 구체적 형태다 — 검증 대응물(`verifies`)가 없으면 같은 높이의 개발 청크는 다음 높이로 내려갈 수 없고, 따라서 완료 판정도 V&V 대응물의 존재와 상태를 조건으로 갖는다. 1~4는 개발 KB 안에서 질의로 판정되고(CQ19·CQ20, 대안 shape, 계약 선행 verify), 5만 밖을 읽는다.
