---
id: https://agentic-knowledge-base.dev/id/chunk/870f5041-82ad-49e9-8b59-c3d2622d29e9
type: artifact
level: executable
title_ko: 질의 comment-level-not-inherited (tools/verify-queries)
title: query comment-level-not-inherited in tools/verify-queries
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-verify-queries}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**질의** — `tools/verify-queries/comment-level-not-inherited.rq` 다. 12줄이고 이 청크는 추출 생성물이다. 질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```sparql
# 안티패턴: 물려받지 않은 주석 수준 — 주석의 hasLevel 이 어느 대상의 hasLevel 과도 같지 않다
# (residency-shapes 의 의도적 공백: 주석은 구간이 아니라 대상에서 수준을 물려받는다, 6.4절 · p7-commentary-form).
# 대상이 여럿이고 수준이 다르면 **그중 하나와 같으면 통과**로 읽는다 — 상속의 출처가 대상이므로 어느 대상에서
# 물려받았는지만 물으면 되고, "가장 구체적인 대상" 으로 읽으면 수준 순서표를 질의에 세 번째로 복제해야 한다
# (순서의 정의처는 defs/kb.bzl 의 LEVELS 와 tools/chunk2kg.py 의 LEVELS 다). 결과 행 하나 = 위반 하나.
# 첫 실행(2026-09-26, 주석 7 · 대상 수준이 갈리는 주석 1): 0.
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT DISTINCT ?comment ?level WHERE {
  ?comment a agt:ReviewComment ; agt:hasLevel ?level ; agt:targets ?target .
  ?target agt:hasLevel ?any .
  FILTER NOT EXISTS { ?comment agt:targets ?t . ?t agt:hasLevel ?level }
}
```
<!-- 인용 끝 -->
