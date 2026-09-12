---
id: https://agentic-knowledge-base.dev/id/chunk/09d432d9-a7cc-4e0e-bfff-8aef123d93cc
type: decision
level: logical
title_ko: 자유형 생성은 드리프트를 누적하고 형식 파일은 동일성을 비교로 판정한다
title: Free-form generation accumulates drift; a formal file makes sameness comparable
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/3b728259-9d19-4617-a431-35fccffec28c
---
**근거** (노트 6.6절) — 자유형 생성은 같은 입력에 같은 출력을 보장하지 않는다. 문장이 달라지고 달라진 문장이 다음 세션의 입력이 되어 드리프트가 누적된다. 파일 자체가 형식 언어면 산출물의 동일성이 텍스트 비교로 판정된다.

- 어휘를 온톨로지에서 가져오는 이유는 두 벌의 어휘가 생기는 것을 막기 위해서다. 언어를 따로 설계하면 키워드와 온톨로지 개념 사이에 매핑 표가 필요하고, 그 표가 드리프트의 새 자리가 된다 (r-017).
- abstract 단계에 대응시키면 정제의 나머지가 같은 파일 위의 채워 넣기가 된다 — logical은 범위·제약을, concrete는 값을 같은 표기에 더한다.
