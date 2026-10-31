---
id: https://agentic-knowledge-base.dev/id/chunk/828f6e56-8841-4778-94b7-fe42d706243f
type: decision
level: concrete
title_ko: 설계 공간 파일은 후보 링크와 양립 제약을 담는다
title: The -space file holds candidate links and compatibility constraints
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0100-design-space-file.md, id: https://agentic-knowledge-base.dev/id/chunk-d0100, title_ko: "설계 공간(-space) 파일은 후보 링크와 양립 제약을 담는다", title: "The design space file holds candidate links and compatibility constraints"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-24T19:32:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:32:48+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0100]
part_of: https://agentic-knowledge-base.dev/id/composite/77fa385a-9aa6-406f-b72f-bb966f6c42f8
composite: {id: https://agentic-knowledge-base.dev/id/composite/77fa385a-9aa6-406f-b72f-bb966f6c42f8, title_ko: 설계 공간 파일은 후보 링크와 양립 제약을 담는다, title: The -space file holds candidate links and compatibility constraints}
---
**결론** — `-space` 파일은 **후보 링크 집합과 양립 제약을 담는 파일**이다. 0.2절의 "변수 선언 + 도메인·제약"이 뜻하는 정확한 실체다.

```
space :auth-space
  variable  :auth-requirement          (functional 항목)
  candidates
    :auth-requirement refines? :oauth2
    :auth-requirement refines? :mtls
    :auth-requirement refines? :apikey
  constraints
    odd.environment.external-client → ¬(refines :apikey)
```

**단계가 채움 정도로 드러난다** — abstract 단계는 `variable`까지, logical 단계는 `candidates`와 `constraints`까지 채운 상태다. 선호는 `preferences` 블록으로 얹는다 (8.9절).

**검사** (노트 9.10절) — 게이트 `space`는 근거 없는 배제(`eliminated`인데 `eliminated_by` 없음), 확정 후보가 정확히 하나가 아닌 `resolved`, 변수와 어긋난 후보의 출발점·링크 타입, 실재하지 않는 IRI, 두 파일이 선언한 같은 변수를 거부한다. 생성 시점에는 `space2kg`가, 그래프 시점에는 `validate`의 `check_space`가 판정한다(2026-09-22, analysis·verify 계층). `space/*-space.md`는 `kb_chunk` 타깃이 아니라 A-Box 그래프 `//space:design_space`로 나간다. 위반은 저작자가 후보에 근거를 붙이거나 변수를 고쳐 해소한다.
