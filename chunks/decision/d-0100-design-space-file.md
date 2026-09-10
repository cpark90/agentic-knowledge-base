---
id: https://agentic-knowledge-base.dev/id/chunk-d0100
type: decision
level: concrete
title_ko: 설계 공간(-space) 파일은 후보 링크와 양립 제약을 담는다
title: The design space file holds candidate links and compatibility constraints
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — `-space` 파일은 **후보 링크 집합과 양립 제약을 담는 파일**이다.
`variable`(링크가 필요한 항목) 선언, `candidates`(후보 링크),
`constraints`(양립 조건)로 구성한다. 0.2절 "변수 선언 + 도메인·제약"이
뜻하는 것이 이것이다.

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

**근거** (노트 7.4절)
- 사다리 단계가 파일의 채움 정도로 드러난다 — **abstract 단계는
  `variable`까지, logical 단계는 `candidates`와 `constraints`까지** 채운
  상태다.
- 후보와 제약이 한 파일에 있으므로 제약 전파(7.3절)가 이 파일 위에서
  국소적으로 동작한다.
