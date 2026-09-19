---
id: https://agentic-knowledge-base.dev/id/chunk/0885d278-bf9d-44cc-9484-adc96e64f47f
type: schema
level: concrete
title_ko: 부분 수준이 어긋난 고정물 bad_decision_levels와 대안 파일이 빠진 결정 디렉토리가 각각 분석과 생성에서 거부된다
title: The fixture bad_decision_levels with mismatched part levels and a decision directory missing alternatives are rejected at analysis and at generation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/797958ea-3a61-41d1-9a10-d12f1c4d69b3]
verifies: [https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e]
---
**케이스** — 세 청크 규칙의 세 시점(분석·생성·표지)에 자극 하나씩을 쓴다.

**자극(분석)** — `defs/tests/BUILD.bazel`의 고정물 `bad_decision_levels`다. 세 파일이 전부 `fx_dec.md`이고 `part_levels = [executable, logical, logical]`이다.

**자극(생성)** — 임시 디렉토리 `kb/dev/decision/zz-no-alternatives/`에 `conclusion.md`·`rationale.md`만 두고 `python3 tools/gen_build.py --check --root .`를 돌린다. 실행 뒤 디렉토리를 지운다.

**자극(표지)** — `**대안**` 대신 `**결론**`으로 시작하는 `alternatives.md` 하나를 `python3 tools/chunk_lint.py --chunks <파일>`에 넣는다.

```yaml
zz-no-alternatives/: [conclusion.md, rationale.md]                # alternatives.md 없음
alternatives.md: {type: decision, body_first_line: "**결론** — …"}  # 표지 불일치
```

**기대** — 분석: `수준 허용표 위반 — plane decision 는 level executable 에 살 수 없다`로 실패하고 `decision_levels_test`가 PASS다. 생성: `FAIL [gen-build] kb/dev/decision/zz-no-alternatives: 결론·근거·대안 세 청크가 있어야 한다 (7.4절 대안 기록) — 있는 것: ['conclusion', 'rationale']`이고 종료 코드 1이다. 표지: `FAIL [decision-role] <파일>:<줄>: 본문 첫 산문 줄이 **대안** 표지로 시작해야 한다`다. 양성: `//:build_drift_test`·`//kb/dev:lint_test`가 PASS다.

**실행 명령** — `bazel test //defs/tests:decision_levels_test //:build_drift_test //kb/dev:lint_test`

**표본 근거** — 대안 없는 결정은 생성기가 타깃 자체를 만들지 않아 분석 시점 고정물로는 표현할 수 없다. 그래서 분석 표본은 수준 불일치로 대신하고, 생성·표지 표본은 커밋되지 않는 임시 입력으로 둔다.
