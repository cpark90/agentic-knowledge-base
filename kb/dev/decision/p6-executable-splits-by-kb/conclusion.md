---
id: https://agentic-knowledge-base.dev/id/chunk/ee51de32-a48b-4ade-a147-4953bce27364
type: decision
level: concrete
title_ko: executable의 구현과 검증은 서로 다른 KB에 산다
title: Implementation and 검증기 live in different KBs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7, https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395]
part_of: https://agentic-knowledge-base.dev/id/composite/8e8697a1-16b9-4c24-a377-340db2b6000b
composite: {id: https://agentic-knowledge-base.dev/id/composite/8e8697a1-16b9-4c24-a377-340db2b6000b, title_ko: executable 단계의 KB 분리, title: Splitting the executable level across two KBs}
---
**결론** — executable 단계는 두 KB로 갈라진다. **구현은 개발 KB의 `artifact`, verifier는 V&V KB의 `artifact`**다 (7.2절).

**`verifies` 링크의 주어가 될 수 있는 것은 V&V KB의 청크뿐이다.** 같은 저장소에 둘 때는 역할 태그로 구분하되 **스코프는 분리한다.**
