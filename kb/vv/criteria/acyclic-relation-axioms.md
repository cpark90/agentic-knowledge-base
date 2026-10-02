---
id: https://agentic-knowledge-base.dev/id/chunk/b2b7a878-a500-4352-976a-e7cdd6ca1d8b
type: contract
level: logical
title_ko: 세 안티패턴 질의 각각이 위반 하나만 잡고 위반을 뺀 같은 그래프는 통과한다
title: Each of the three anti-pattern queries catches exactly one violation, and the same graph without it passes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-26T00:30:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/03335ea8-fe32-45e0-9406-5e8457b81486]
---
**합격 기준** — 기준 종류는 **명세 대조**다. 그래프 `g`와 자기 참조 트리플 `t ∈ {refines, supersedes, hasDirectPart}`에 대해, `t`를 가진 `g`는 대응 질의 하나로만 `FAIL [verify]`이고, `t`를 뺀 `g`는 세 질의 모두 통과한다.

**판정식**

- 음성(refines): `python3 tools/validate.py --verify-queries tools/verify-queries ...`가 `refines-cycle.rq` 하나로 `FAIL [validate] — 1건`, 종료 코드 1이다.
- 음성(supersedes): 같은 명령이 `supersedes-cycle.rq` 하나로 `FAIL [validate] — 1건`이다.
- 음성(composite): 같은 명령이 `composite-cycle.rq` 하나로 `FAIL [validate] — 1건`이다.
- 최소성: 자기 참조 트리플만 뺀 같은 개체는 세 실험 모두 종료 코드 0이다.
- 양성: `bazel test //kg:gate_test`가 PASS다 — 커밋된 그래프에는 세 순환이 없다.

**등급** — B다. 질의는 기계 판정이나 `--verify-queries` 실행에 비용이 있다.

기준의 대상은 `tools/verify-queries/refines-cycle.rq`·`supersedes-cycle.rq`·`composite-cycle.rq`이고 판정의 원본은 `tools/validate.py`의 `check_verify`다. 공리 선언 자체(`owl:IrreflexiveProperty`·`owl:TransitiveProperty`)는 이 기준 밖이다 — pySHACL 추론이 그 위반을 내지 않으므로 선언은 문서이고 이 기준이 실제 판정을 잰다.
