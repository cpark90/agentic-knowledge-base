---
id: https://agentic-knowledge-base.dev/id/chunk/e6d66083-207d-45f6-8779-2b79e141111e
type: decision
level: concrete
title_ko: 작업은 셀프체크를 통과해야 끝나고 셀프체크는 게이트 전체 PASS와 원본이 바뀐 생성물의 재생성이다
title: Work ends only after the self-check, which is a passing full gate run and the regeneration of every output whose source changed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:20+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3e29e698-8ef5-4fe2-ac1b-867e596a5179
composite: {id: https://agentic-knowledge-base.dev/id/composite/3e29e698-8ef5-4fe2-ac1b-867e596a5179, title_ko: 셀프체크 — 완료 전 게이트와 재생성, title: Self-check — gates and regeneration before completion}
---
**결론** — 지식 파일이나 도구를 고친 작업은 셀프체크를 통과해야 끝난다. 셀프체크는 둘이다.

1. **게이트 전체가 PASS다.** `bazel test //...`를 돌린다. 시점은 셋이다. 작업을 완료로 보고하기 전, 유저 결정을 반영하고 `result`를 보내기 전, 커밋하기 전이다. FAIL이면 산출물을 고친다. 게이트를 약화하지 않는다(`p6-weakening-a-check-needs-user-approval`).
1. **원본을 바꾼 생성물은 생성기로 다시 만든다.** 생성물을 손으로 맞추지 않는다.

| 바꾼 원본 | 다시 만드는 명령 | 생략을 잡는 검사 |
|---|---|---|
| 청크 frontmatter의 링크 | `python3 tools/gen_build.py --root .` | `//:build_drift_test` |
| 도구 docstring·`kb_lib.SKILLS` | `python3 tools/gen_skills.py --root .` | `//:skills_drift_test` |
| 소스 파일 | `bazel run //tools:extract -- <소스>` | `//:extract_drift_test` |
| 결정의 `conventions.md`·`norm` 절 청크 | `python3 tools/gen_norms.py --root .` | `//:norms_drift_test` |
| 기계가 만든 TTL | `bazel run //tools:canonicalize -- --write <파일>` | 없음 |

- 재생성의 생략은 다음 게이트 실행에서 드리프트 테스트가 FAIL로 잡는다. 정규화만은 잡는 테스트가 없다. `canonicalize`의 `--check`를 부르는 테스트 타깃이 없기 때문이다(2026-10-04 BUILD 실측). 손으로 쓰는 TTL은 정규화 대상이 아니다.
- 셀프체크의 실행 자체를 강제하는 게이트는 없다. 셀프체크는 리뷰 규범이다. 실행 여부는 `result`와 세션 보고에 적은 PASS로 드러난다.
