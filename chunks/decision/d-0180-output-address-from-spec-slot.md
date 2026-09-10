---
id: https://agentic-knowledge-base.dev/id/chunk-d0180
type: decision
level: concrete
title_ko: 산출물의 주소는 구현이 아니라 명세의 슬롯에서 얻는다
title: An artifact's address comes from the spec slot, not the implementation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 생성된 산출물의 이름과 위치는 **명세 쪽 슬롯**에서 파생하고,
그 슬롯을 실현한 구현에서 파생하지 않는다. 구현을 다른 후보로 바꿔도
산출물의 주소는 그대로이므로 그것을 참조하던 쪽이 깨지지 않는다.

**근거** (harness-concrete docs/odr-bind-lock.md §"Stable emitted filenames")
- 이것이 "기술이 바뀌어도 같은 것"이라는 주장의 조작적 정의다 — 같은
  슬롯을 다른 구현이 실현하는 것이 교체이고, 이름이 따라 바뀌면 그것은
  교체가 아니라 다른 산출물의 등장이다.
- 구현 파일의 이름을 그대로 물려받으면 후보 교체가 곧 이름 변경이 된다.
  명세는 그대로인데 사용자가 깨지므로, 교체의 무해성(같은 명세·다른
  바인딩·같은 판정 결과)이 이름 층에서 무너진다.
- 앵커를 내용이 아니라 지속 식별자에 두는 규칙(d-0077)의 산출물 쪽
  대응이다. 명세의 슬롯 식별자가 산출물의 앵커 노릇을 한다.
- 후보 개념 자체가 없는 퇴화 경우(구현이 하나뿐이고 슬롯을 세우지 않은
  경우)에만 참조의 원래 이름을 그대로 쓴다.
