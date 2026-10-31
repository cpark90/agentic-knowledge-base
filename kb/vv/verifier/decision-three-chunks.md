---
id: https://agentic-knowledge-base.dev/id/chunk/c6534f23-4a9a-436c-be8b-29d47d4a1c2a
type: artifact
level: executable
title_ko: 부분 수준이 어긋난 고정물 bad_decision_levels와 대안 파일이 빠진 결정 디렉토리가 각각 분석과 생성에서 거부된다
title: The fixture bad_decision_levels with mismatched part levels and a decision directory missing alternatives are rejected at analysis and at generation
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/797958ea-3a61-41d1-9a10-d12f1c4d69b3]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc, https://agentic-knowledge-base.dev/id/chunk/d54dd037-5b16-4649-922d-f7c9b7b5c510, https://agentic-knowledge-base.dev/id/chunk/3b9822e1-5e35-4f9e-8c26-429350db7faa]
restored: [https://agentic-knowledge-base.dev/id/chunk/5e66ed6e-bc41-4da5-b863-a928f146a7bc, https://agentic-knowledge-base.dev/id/chunk/d54dd037-5b16-4649-922d-f7c9b7b5c510, https://agentic-knowledge-base.dev/id/chunk/3b9822e1-5e35-4f9e-8c26-429350db7faa]
---
**검증기** — 세 단위 지식 규칙의 세 시점(분석·생성·표지)에 자극 하나씩을 쓴다.

**자극(분석)** — `defs/tests/BUILD.bazel`의 고정물 `bad_decision_levels`다. 세 파일이 전부 `fx_dec.md`이고 `part_levels = [executable, logical, logical]`이다.

**자극(생성)** — 임시 디렉토리 `kb/dev/decision/zz-no-alternatives/`에 `conclusion.md`·`rationale.md`만 두고 `python3 tools/gen_build.py --check --root .`를 돌린다. 실행 뒤 디렉토리를 지운다.

**자극(표지)** — `**대안**` 대신 `**결론**`으로 시작하는 `alternatives.md` 하나를 `python3 tools/chunk_lint.py --chunks <파일>`에 넣는다.

```yaml
zz-no-alternatives/: [conclusion.md, rationale.md]                # alternatives.md 없음
alternatives.md: {type: decision, body_first_line: "**결론** — …"}  # 표지 불일치
```

**기대** — 분석: `수준 허용표 위반 — plane decision 는 level executable 에 살 수 없다`로 실패하고 `decision_levels_test`가 PASS다. 생성: `FAIL [gen-build] kb/dev/decision/zz-no-alternatives: 결론·근거·대안 세 청크가 있어야 한다 (7.4절 대안 기록) — 있는 것: ['conclusion', 'rationale']`이고 종료 코드 1이다. 표지: `FAIL [decision-role] <파일>:<줄>: 본문 첫 산문 줄이 **대안** 표지로 시작해야 한다`다. 양성: `//:build_drift_test`·`//kb/dev:lint_test`가 PASS다.

**실행 명령** — `bazel test //defs/tests:decision_levels_test //:build_drift_test //kb/dev:lint_test`

**판정 범위** — 대안 없는 결정은 생성기가 타깃 자체를 만들지 않아 분석 시점 고정물로는 표현할 수 없다. 그래서 분석 표본은 수준 불일치로 대신하고, 생성·표지 표본은 커밋되지 않는 임시 입력으로 둔다.

**검증 대응물** — 이 검증기는 `defs/kb.bzl`, `tools/gen_build.py`와 `tools/chunk_lint.py`의 항목을 `verifies` 한다. 끝은 파일 복합체의 선언 항목(`module.md`)이고, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p7-alternatives-mandatory`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
