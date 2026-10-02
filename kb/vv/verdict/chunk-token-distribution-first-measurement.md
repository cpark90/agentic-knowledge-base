---
id: https://agentic-knowledge-base.dev/id/chunk/ae16d211-30f9-4ae5-919c-d7ab718736d9
type: annotation
level: concrete
title_ko: 토큰 분포 첫 실측이 결정의 초과 수를 그대로 재현한다
title: The first token-distribution measurement reproduces the decision's overage counts
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T21:40:00+09:00}
---
thought (non-blocking): `bazel run //tools:tokens`의 첫 실측이 결정의 초과 수(1,092에서 저작 산문 3·코드 52, 2,856에서 코드 6)를 그대로 재현한다.

대상: https://agentic-knowledge-base.dev/id/chunk/7afd759f-26b1-4ad8-8edb-abc971dc4393

본문: `bazel run //tools:tokens -- --out <경로>`(계수기 `tiktoken 0.12.0` `o200k_base`, 청크 1,648개)로 재실측하면 저작 산문(requirement·decision 882개)의 줄당 토큰 중앙값이 27.33이고 예산 200줄의 토큰 환산은 5,467이다(결정 본문의 27.09·5,418에서 청크 수 879→882의 증가만큼 갈린다). 같은 계수기로 plane별 문턱을 다시 센 값(보고의 42의 배수 표는 42×20=840까지만 실어 1,092·2,856을 담지 못한다)은 상한 1,092 초과 저작 산문 3건(`kb/vv/case/acyclic-relation-axioms.md`·`chunk-42-lines.md`·`composite-order-shape.md`, 모두 schema plane)·코드(artifact) 52건이고, 2,856 초과 코드 6건으로 결정의 결론과 정확히 같다. 다만 2,856 초과는 코드 6건에 memory plane의 `kb/vv/run/judge-20260929T182311Z.md`(3,094토큰) 1건을 더하면 총 7건이고, 결정 결론은 코드만 세어 이 1건을 담지 않았다. 근사(3,200) 대 실측(5,467)의 비는 1.7배로 결정의 결론과 같다.

제안: `kb/vv/run/`의 memory 판정 로그는 append-only라 분할 대상이 아니므로 2,856 초과 memory 1건은 분할 계획(계획 5)이 아니라 기록으로만 남긴다.

해소: 해소 — 결정의 세 수(1,092·2,856·5,418)를 같은 계수기로 재현했고 memory의 추가 1건을 갈라 적었다.
