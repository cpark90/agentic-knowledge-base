---
id: https://agentic-knowledge-base.dev/id/chunk/797958ea-3a61-41d1-9a10-d12f1c4d69b3
type: contract
level: logical
title_ko: 대안 없는 결정은 생성·로드·분석 어느 시점에서도 타깃이 되지 못하고 커밋된 결정은 전부 세 청크다
title: A decision without alternatives never becomes a target at generation, load or analysis and every committed decision has three chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/863a8842-3d1c-4406-99a9-f8d3d755e17a]
---
**합격 기준** — 기준 종류는 **산출물 품질**이다. `kb/dev/decision/<슬러그>/` 디렉토리마다 `conclusion.md`·`rationale.md`·`alternatives.md`가 있고 세 부분의 수준이 `decision`의 허용 구간 안이며 `alternatives.md`의 첫 산문 줄이 `**대안**` 표지다.

**판정식**

- 음성(분석): `bazel test //defs/tests:decision_levels_test`가 PASS다. 부분 수준 `[executable, logical, logical]`의 복합체가 `수준 허용표 위반` 문구로 실패할 때만 PASS다.
- 음성(생성): `alternatives.md`가 없는 결정 디렉토리에서 `python3 tools/gen_build.py --check --root .`가 `FAIL [gen-build] … 결론·근거·대안 세 청크가 있어야 한다`로 끝난다.
- 음성(로드): `kb_decision`에 `alternatives`를 주지 않으면 필수 속성 누락으로 로드가 실패한다.
- 음성(표지): `**대안**`으로 시작하지 않는 `alternatives.md`는 `FAIL [decision-role]`로 거부된다.
- 양성: `bazel test //:build_drift_test //kb/dev:lint_test`가 PASS다.

**등급** — B다. 생성기·청크 검사는 테스트 실행이라 비용이 있다. 분석 시점 판정만 A다.

판정의 원본은 `tools/gen_build.py`의 `scan`, `defs/kb.bzl`의 `kb_decision`, `tools/chunk_lint.py`의 `check_decision_role`이다.
