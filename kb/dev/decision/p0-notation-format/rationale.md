---
id: https://agentic-knowledge-base.dev/id/chunk/14188a01-8332-4451-a538-8a857aa490dd
type: decision
level: logical
title_ko: 별도 용어집은 어긋나고 어긋난 시점을 알 방법이 없다
title: A separate glossary drifts and the drift is undetectable
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/fc68c83c-8feb-47ce-8dea-30f24d2ee645
---
**근거** (노트 0.6절)

- 케밥과 PascalCase를 갈라 쓰면 문장에 나온 이름이 개체를 가리키는지 개념을
  가리키는지가 **표기만으로** 판정된다.
- 용어집을 별도 파일로 두면 온톨로지와 어긋나고 어긋난 시점을 알 방법이 없다.
  라벨에 두면 어휘의 갱신이 곧 용어집의 갱신이다.
- 1:1 대응을 고정해야 한글 산문과 영어 식별자 사이의 번역이 결정론적이 되고,
  동음 충돌 회피(0.0절)가 두 언어 모두에서 성립한다.
- 동의어 금지는 산문에 대한 규칙이고, 어휘 수준의 강제는 SKOS 라벨
  등록으로 한다 (0.8절).
