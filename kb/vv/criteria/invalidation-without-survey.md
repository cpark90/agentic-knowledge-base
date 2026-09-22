---
id: https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c
type: contract
level: logical
title_ko: 가정의 의존 집합은 assumes 역질의로 나오고 인위 파괴 실험의 직접 영향 집합은 frontmatter 스캔과 정밀도·재현율 1 로 일치한다
title: An assumption's dependent set comes from one reverse assumes query, and the break experiment's direct impact set matches the frontmatter scan with precision and recall of one
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/91dbec7f-3480-49ec-a83b-0273b572afde]
---
**합격 기준** — 기준 종류는 **명세 대조**다. `impact(a) = {c | c agt:assumes a ∧ live(c)}` 이고, 조건 `k` 를 out 으로 가정했을 때 `refersTo(a) ∋ k` 인 모든 `a` 에 대해 `impact(a)` 가 파일 스캔 집합과 같다.

**판정식**

- 양성(질의): `bazel build //kg:cq` 가 성공하고 `bazel-bin/kg/cq.md` 의 CQ-22 절이 가정 × 의존 항목 행을 낸다. 행 수는 `assumes` 링크 수와 같다.
- 양성(참조): `bazel test //kg:gate_test` 가 PASS 다. `odd-ref` 위반 0 이라 모든 가정의 판정식이 파생된다.
- 실험: `bazel run //tools:assume_check -- --break cond-build-system` 이 `asm-bazel-toolchain` 을 `invalidated` 로 내고 `정밀도 N/N · 재현율 N/N → 일치` 를 적는다. 종료 코드는 1(무효 가정 있음)이다. `bazel run` 이라 vv_run 은 이 명령을 실행하지 않는다.
- 음성: `refersTo` 대상이 ODD 밖인 가정은 `odd-ref` 가 거부하므로 판정 불가 가정이 그래프에 들어오지 않는다.

**등급** — B 다. 질의·게이트는 기계 판정이고 파괴 실험은 실행 비용이 있다.

판정의 원본은 `tools/assume_check.py`(전파·`--break` 비교), `tools/cq-queries/CQ-22.rq`, `tools/validate.py` 의 `check_odd_refs` 다. 하류 suspect 전파(8단계 중 4~6)와 상태의 일괄 표시는 `revalidate` 의 몫이고 이 기준 밖이다.
