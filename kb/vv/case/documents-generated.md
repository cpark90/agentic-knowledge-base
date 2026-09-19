---
id: https://agentic-knowledge-base.dev/id/chunk/cd63600d-fc05-4577-a84b-62203ac0ed74
type: schema
level: concrete
title_ko: adr·audit 뷰가 bazel-bin에 생성되고 커밋된 BUILD·skill이 두 드리프트 검사를 통과한다
title: The adr and audit views are generated under bazel-bin and the committed BUILD files and skills pass both drift checks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/c0fb71e0-f5bf-44eb-90f4-542b546bf081]
verifies: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
---
**케이스** — 문서 뷰 둘과 트리의 생성물 두 종을 자극으로 쓴다.

**자극** — `//kb/dev:adr`(살아 있는 결정 복합체 전부의 ADR)과 `//kg:audit`(감사 보고서)이다. 드리프트 검사의 대상은 `gen_build`가 만드는 BUILD 전부와 `.claude/skills/*/SKILL.md` 전부다. 음성 표본은 서술로만 둔다.

```yaml
views:    [{target: //kb/dev:adr, out: bazel-bin/kb/dev/adr.md}, {target: //kg:audit, out: bazel-bin/kg/audit.md}]
in_tree:  [{kind: BUILD, check: //:build_drift_test}, {kind: skill, check: //:skills_drift_test}]
negative: {edit: tools/vv_run.py 의 docstring 첫 문장, regenerate: false}   # 서술 표본 — [skills-drift]
```

**기대** — 두 드리프트 시험이 PASS다. 두 빌드가 성공하고 `bazel-bin/kb/dev/adr.md`·`bazel-bin/kg/audit.md`의 머리에 `- 생성 시각:`과 `- 질의:` 줄이 있다. 소스 트리에 `kb/dev/adr.md`·`kg/audit.md`가 없다. 음성 표본은 `FAIL [skills-drift] .claude/skills/vv-run/SKILL.md: …` 한 줄로 끝나고 종료 코드가 1이다.

**실행 명령** — `bazel test //:build_drift_test //:skills_drift_test && bazel build //kb/dev:adr //kg:audit`

**표본 근거** — 뷰는 본문을 쓰는 것(adr)과 관측을 쓰는 것(audit)을 하나씩 골라 `bodies` 입력의 두 용법을 덮는다. 트리 생성물은 두 종이 전부라 표본이 전수다. BUILD 쪽 음성은 기준 `generated-build-drift`가 이미 가지므로 여기서는 skill 쪽만 둔다.
