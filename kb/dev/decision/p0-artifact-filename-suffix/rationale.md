---
id: https://agentic-knowledge-base.dev/id/chunk/fa97d6dc-8842-4a88-b317-d410a80cf7ce
type: decision
level: logical
title_ko: 스코프와 게이트를 파일 단위로 걸려면 성격이 파일명에 드러나야 한다
title: Per-file scopes and gates need the file kind visible in the name
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0af48edc-840f-49e8-ad8b-60dfb331854d
---
**근거** (노트 0.2절)

- 접미사만 보고 그 파일이 어휘를 담는지 개체를 담는지, 후보를 담는지 확정을
  담는지 판정할 수 있어야 스코프와 검사 게이트를 **파일 단위로** 건다.
- 어휘(`-ontology`)와 추론 규칙(`-rules`)을 가르는 이유는 둘의 갱신 주기와
  판정 방식이 다르기 때문이다. 둘 다 축 위에 있지 않다 (0.1절).
- `-space`가 두 level에 걸치는 것은 설계 공간이 미확정을 담는 파일이기
  때문이다 — 출발점만 선언된 단계와 후보·제약이 붙은 단계가 같은 형식을
  공유한다 (Part IX).
