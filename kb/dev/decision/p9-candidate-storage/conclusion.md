---
id: https://agentic-knowledge-base.dev/id/chunk/7c9d74e6-1a77-4d52-a126-644a65bfab93
type: decision
level: concrete
title_ko: 후보는 -space 청크에 살고 절대 deps가 되지 않으며 확정은 head로 옮겨진다
title: Candidates live in -space chunks, never become deps, and are moved to the head on confirmation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b4561dfb-19ea-4f34-b57e-c241cae4b9da, title_ko: 후보의 저장 자리, title: Where candidates live}
part_of: https://agentic-knowledge-base.dev/id/composite/b4561dfb-19ea-4f34-b57e-c241cae4b9da
---
**결론** — 후보 링크는 확정 링크와 **다른 자리**에 저장된다. 확정은 청크 head(프런트매터 타입 키 → Bazel deps), 후보는 `-space` 청크. **후보는 절대 deps가 되지 않는다.** 확정되는 순간 생성기가 `-space`에서 head로 옮기고, 그것이 한 줄 diff로 리뷰된다 (노트 9.10절).

`-space`는 `type: agt:Space`, level logical의 OKF 청크다. **변수 하나 = 파일 하나.** 필드 — `variable`(출발 청크 + 링크 타입), `status`(open|resolved), `candidates`(각각 `to`·`state`·`eliminated_by`·`when`·`evidence` 장부), `constraints`(CEL), `preferences`. 기각된 후보는 삭제되지 않는다 — logical은 근거의 보존소다.

한 파일 안에서 후보의 재료와 확정 결과가 나란히 있다 — OKF `sources`에는 있고 `satisfies`에는 없는 항목이 "읽었지만 기각된 것"이고 그 근거는 `-space`에 있다. `chunk2kg`가 `-space`를 `agt:CandidateLink`로 올리고, 확정 링크는 `prov:wasDerivedFrom`으로 자신이 후보였던 개체를 가리킨다. 유저에게는 체크박스 파일(13.5절)로 투영된다 — `[ ]` open, `[-]` eliminated + 이유, `[x]` 확정; `[x]` 하나만 남으면 `resolved`.
