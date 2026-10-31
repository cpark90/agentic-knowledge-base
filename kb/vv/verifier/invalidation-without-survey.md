---
id: https://agentic-knowledge-base.dev/id/chunk/ba6e8c01-3adb-48b6-9371-6a75a49af3cf
type: artifact
level: executable
title_ko: cond-build-system 을 깨면 asm-bazel-toolchain 의 직접 영향 집합 84 가 frontmatter 스캔 84 와 일치하고 CQ-22 가 assumes 링크 수만큼 행을 낸다
title: Breaking cond-build-system yields a direct impact set of 84 for asm-bazel-toolchain equal to the 84 from the frontmatter scan, and CQ-22 returns one row per assumes link
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/ebf3db88-a177-4d7c-8441-992719f174d9, https://agentic-knowledge-base.dev/id/chunk/9e4f25bd-8f21-4007-9efc-252f63211ced, https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1]
restored: [https://agentic-knowledge-base.dev/id/chunk/ebf3db88-a177-4d7c-8441-992719f174d9, https://agentic-knowledge-base.dev/id/chunk/9e4f25bd-8f21-4007-9efc-252f63211ced, https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1]
---
**검증기** — 그래프 질의 뷰 하나, 그래프 게이트 하나, 인위 파괴 실험 하나를 자극으로 쓴다.

**자극** — `//kg:cq`(CQ-22)와 `//kg:gate_test`, 그리고 `assume_check --break cond-build-system` 이다. 2026-09-21 측정은 가정 2 · `assumes` 링크 778 · 살아 있는 단위 지식 695 다.

```yaml
break:     cond-build-system                      # asm-bazel-toolchain 의 유일한 참조 조건 (등급 A)
expected:  {asm-bazel-toolchain: invalidated, asm-chunk-conventions: valid}
impact:    {graph: 84, frontmatter_scan: 84}      # 정밀도 84/84 · 재현율 84/84
cq22_rows: 778                                    # = assumes 링크 수
```

**기대** — `bazel build //kg:cq` 가 성공하고 CQ-22 절의 행 수가 `assumes` 링크 수와 같다(측정 778). `bazel test //kg:gate_test` 가 PASS 다. 실험 명령은 `asm-bazel-toolchain` 행에 `**invalidated** | 84 | 84` 를, 비교 절에 `정밀도 84/84 · 재현율 84/84 → **일치**` 를 적고 종료 코드 1 로 끝난다.

**실행 명령** — `bazel build //kg:cq && bazel test //kg:gate_test`

**판정 범위** — 조건 하나를 깨는 가장 작은 실험이 무효 범위 계산의 경계값이다. `cond-build-system` 을 고른 이유는 그것을 참조하는 가정이 하나뿐이라 영향 집합의 귀속이 유일하기 때문이다. 실험은 `bazel run` 이라 테스트 케이스의 실행 명령 밖이고 판정은 위 두 명령으로 한다.

**검증 대응물** — 이 검증기는 `tools/query.py`, 질의 `CQ-22`와 `tools/validate.py`의 항목을 `verifies` 한다. 코드 파일의 끝은 파일 복합체의 선언 항목(`module.md`)이고 질의 파일의 끝은 그 파일 항목이며, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p6-assumption-invalidation`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다. 다만 `assume_check --break` 실험은 실행 명령 밖의 서술 표본이라 실행 기록의 증거가 되지 않으므로 `tools/assume_check.py` 는 링크에서 뺀다.
