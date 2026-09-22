---
id: https://agentic-knowledge-base.dev/id/chunk/7cdb48a1-5b6d-491e-ad54-0a0e2975dd41
type: contract
level: logical
title_ko: kb/odd 의 OpenODD 원본은 파일 하나이고 그 조건 전부가 판정 방법과 등급을 가져 ODD 게이트를 통과한다
title: The OpenODD source under kb/odd is one file and all of its conditions carry a check method and a grade, passing the ODD gate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d72a3063-801a-4ec0-977c-f2f75550f5c0]
---
**합격 기준** — 기준 종류는 **산출물 품질**이다. `|{kb/odd/*.yml 중 원본}| = 1` 이고 `∀ 조건 c ∈ ODD: checkMethod(c) ≠ ∅ ∧ grade(c) ∈ {A, B, C, D}` 이며 `|conditions(ODD)| ≥ 1` 이다.

**판정식**

- 양성(문서 수): `bazel query 'labels(srcs, //kb/odd:odd)'` 의 출력이 `//kb/odd:project-odd.yml` 과 생성 택소노미 `//kb/odd:taxonomy` 둘이고 다른 `.yml` 라벨이 없다.
- 양성(조건): `bazel test //kb/odd:gate_test` 가 PASS 다. `condition-shapes.ttl` 의 `checkMethod`·`verificationGrade` 필수와 ODD 의 조건 ≥ 1 이 위반 0 이다.
- 음성(생성): `CHECKS` 항목이 없는 조건을 가진 문서는 `odd2kg` 가 생성 시점에 거부한다. 서술 표본이다.
- 음성(shape): `agt:checkMethod` 가 빠진 조건은 `FAIL [shacl]` 로 거부된다. 서술 표본이다.

**등급** — A 다. 판정은 Bazel 질의와 ODD 게이트이고 사람 판단이 없다.

판정의 원본은 `kb/odd/BUILD.bazel`, `tools/odd2kg.py` 의 `CHECKS` 검사, `kb/ontology/shapes/condition-shapes.ttl` 이다. 하위 시스템 ODD 가 상위의 부분집합이어야 한다는 규칙(3.11절)은 하위 ODD 가 없어 관측 밖이다.
