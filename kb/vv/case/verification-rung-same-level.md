---
id: https://agentic-knowledge-base.dev/id/chunk/7e69ba96-e363-4ed0-bea1-2ef9602cbeae
type: schema
level: concrete
title_ko: verifies_subject_test 가 PASS 이고 감사 보고서가 요구 35 의 검증 대응물 비율과 사슬 수를 낸다
title: verifies_subject_test passes and the audit report gives the verification counterpart ratio and chain counts for the 35 requirements
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/100e3c7b-9fd4-4b43-bc2a-6068e15bbd27]
verifies: [https://agentic-knowledge-base.dev/id/chunk/525c2b08-d69e-41f1-bbcd-fbffa082a5eb]
---
**케이스** — 분석 시점 고정물 하나와 감사 뷰 하나를 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel` 의 고정물 `bad_verifies`(plane `decision` 이 `:fx_dec` 를 `verifies`)와 `//kg:audit` 이다. 2026-09-21 실측(이 케이스 반영 뒤)은 요구 35 · 검증 목표 33 · 케이스까지 이어진 목표 28 다.

```yaml
fixture:  {bad_verifies: "verifies 의 주어는"}
audit:    {covered: "35/35 = 100.0%", goals: 33, with_criteria: 33, with_case: 28}   # 목표만 있는 요구 5 — 사람 확인
negative: {case_level: concrete, target_level: logical}   # 서술 표본 — 분석 실패, 고정물 없음
```

**기대** — `verifies_subject_test` 가 PASS 다. `bazel build //kg:audit` 이 성공하고 `검증 현황` 절에 `검증 대응물이 있는 요구(…): **35/35 = 100.0%**` 와 `사슬: 검증 목표 33 · 합격 기준이 달린 목표 33 · 케이스까지 이어진 목표 28` 가 있으며 `검증 대응물 없는 요구` 목록이 없다. 수치는 사슬이 늘면 함께 는다.

**실행 명령** — `bazel test //defs/tests:verifies_subject_test && bazel build //kg:audit`

**표본 근거** — 주어 고정물은 이미 있어 그대로 쓰고, 수준 불일치 고정물은 `defs/tests` 에 없어 서술로 둔다. 감사 수치는 전수라 표본 추출이 없다. 목표만 있는 요구 5 가 "대응물은 있되 사슬이 끊긴" 경계값이다.
