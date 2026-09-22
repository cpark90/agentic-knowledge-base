---
id: https://agentic-knowledge-base.dev/id/chunk/550ae0b3-f359-4dcc-bf5e-529bf303f2a4
type: schema
level: concrete
title_ko: cond-build-system 을 깨면 asm-bazel-toolchain 의 직접 영향 집합 84 가 frontmatter 스캔 84 와 일치하고 CQ-22 가 assumes 링크 수만큼 행을 낸다
title: Breaking cond-build-system yields a direct impact set of 84 for asm-bazel-toolchain equal to the 84 from the frontmatter scan, and CQ-22 returns one row per assumes link
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c]
verifies: [https://agentic-knowledge-base.dev/id/chunk/b36581f8-2688-46dc-9b44-3e1019a37d66]
---
**케이스** — 그래프 질의 뷰 하나, 그래프 게이트 하나, 인위 파괴 실험 하나를 자극으로 쓴다.

**자극** — `//kg:cq`(CQ-22)와 `//kg:gate_test`, 그리고 `assume_check --break cond-build-system` 이다. 2026-09-21 실측은 가정 2 · `assumes` 링크 778 · 살아 있는 청크 695 다.

```yaml
break:     cond-build-system                      # asm-bazel-toolchain 의 유일한 참조 조건 (등급 A)
expected:  {asm-bazel-toolchain: invalidated, asm-chunk-conventions: valid}
impact:    {graph: 84, frontmatter_scan: 84}      # 정밀도 84/84 · 재현율 84/84
cq22_rows: 778                                    # = assumes 링크 수
```

**기대** — `bazel build //kg:cq` 가 성공하고 CQ-22 절의 행 수가 `assumes` 링크 수와 같다(실측 778). `bazel test //kg:gate_test` 가 PASS 다. 실험 명령은 `asm-bazel-toolchain` 행에 `**invalidated** | 84 | 84` 를, 비교 절에 `정밀도 84/84 · 재현율 84/84 → **일치**` 를 적고 종료 코드 1 로 끝난다.

**실행 명령** — `bazel build //kg:cq && bazel test //kg:gate_test`

**표본 근거** — 조건 하나를 깨는 가장 작은 실험이 무효 범위 계산의 경계값이다. `cond-build-system` 을 고른 이유는 그것을 참조하는 가정이 하나뿐이라 영향 집합의 귀속이 유일하기 때문이다. 실험은 `bazel run` 이라 케이스의 실행 명령 밖이고 판정은 위 두 명령으로 한다.
