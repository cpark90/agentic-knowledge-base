---
id: https://agentic-knowledge-base.dev/id/chunk/8a37fa99-3e7e-48b5-8da8-c14ba93f5655
type: decision
level: concrete
title_ko: 개발 프로파일의 앵커 해석기는 Bazel 라벨이다
title: The development profile resolves anchors as Bazel labels
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-18T10:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
part_of: https://agentic-knowledge-base.dev/id/composite/a0067e4e-afc9-4817-ac08-3aeba8da718f
composite: {id: https://agentic-knowledge-base.dev/id/composite/a0067e4e-afc9-4817-ac08-3aeba8da718f, title_ko: 앵커 해석기 = Bazel 라벨, title: Anchor resolver = Bazel label}
---
**결론** — 개발 프로파일에서 앵커(4.8절 — 링크가 가리키는 기준점)는 **Bazel 라벨**로 해석한다. 청크 IRI는 불투명하고,
IRI ↔ 라벨 사상은 `gen_build`가 frontmatter에서 결정론적으로 만든다(`//kb/dev/decision:<슬러그>`,
`//kb/dev/requirement:<파일>`). 산문 계열의 파일 앵커는 `agt:assertionLocation`(저장소 상대 경로)이고, 코드 산출물
(`artifact` plane)의 앵커는 `//<패키지>:<타깃>`이다 — 함수 하나가 타깃 하나로 해석된다.

| 대상 | 앵커 | 해석 |
|---|---|---|
| 청크(요구·결정·관측) | IRI → `//kb/dev/<plane>:<이름>` | `gen_build` 사상표, `bazel query` |
| 산문 위치 | `agt:assertionLocation` | 저장소 상대 경로 |
| 코드(`artifact`) | Bazel 라벨 | 타깃 = 함수 하나. 의존은 `deps`, 파급은 `rdeps` |

라벨은 저장소 안에서 유일하고 파일 이동에 강하며, 링크의 구조(끊김·방향·파급)를 Bazel이 판정한다(`pe-bazel-rules`).
