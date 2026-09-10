---
id: https://agentic-knowledge-base.dev/id/chunk/0752e39c-bf11-41ab-bde6-102c26ef58fe
type: decision
level: logical
title_ko: 역할 이름은 프로파일마다 달라도 파생 방식은 고정이고 ODD가 상한이다
title: Role names vary by profile while the derivation is fixed, and the ODD caps the catalog
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/2e3b40bb-c5f0-4355-8108-ccdf481d998a
---
**근거** (노트 11.2절)

- 카탈로그가 바뀌면 **스코프 전부가 재파생된다**(10.1절 파급). 그래서 체계는
  역할 이름이 아니라 파생 방식을 고정한다 — 역할 이름은 도메인 프로파일마다
  다르되 스코프 파생 방식은 같다.
- **카탈로그는 ODD의 동적 요소와 연결된다.** ODD가 "동시 에이전트 ≤ 4"라고
  적으면 동시에 활성화될 수 있는 역할 조합이 그 안에 있어야 하고, 위반하면
  3.5절 ODD 이탈이다 — 카탈로그가 ODD를 이기지 않는다.
- 프롬프트와 절차를 카탈로그에 넣지 않는 이유 — 그것은 판정 방법이 없는
  서술이라 shape로 검사할 수 없고, 하네스가 바뀔 때마다 입력 전체가
  재검토 대상이 된다.
