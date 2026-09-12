---
id: https://agentic-knowledge-base.dev/id/chunk/828f6e56-8841-4778-94b7-fe42d706243f
type: decision
level: concrete
title_ko: 설계 공간 파일은 후보 링크와 양립 제약을 담는다
title: The -space file holds candidate links and compatibility constraints
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
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
