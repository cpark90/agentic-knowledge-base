---
id: https://agentic-knowledge-base.dev/id/chunk/421a713f-81f5-5b25-af24-05fe281246a8
type: schema
level: concrete
title_ko: 생성물과 다른 수치 140/148를 적은 임시 문서는 doccheck --report에서 어긋남을 내고 같은 수치를 적은 통제는 어긋난 쌍 0을 낸다
title: A temporary document carrying the number 140/148 that disagrees with the generated view is reported as a mismatch by doccheck --report, and the control reports zero mismatched pairs
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T23:35:51+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407]
verifies: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/61df20c2-e2b4-5edb-bf5f-912d06cd247c]
---
**케이스** — 기준 `document-table-matches-generated`의 이름별 값 일치 대조를 `doccheck --report`의 위치 인자로 잰다.

**자극** — 임시 문서 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 이름 `확정 문장 커버리지` 뒤에 `140/148`를 적어 대조 쌍 하나만 어긋나게 한다. 통제는 같은 이름에 목표 값을 적은 같은 형의 문서다.

```yaml
files:
  stimulus.md: "확정 문장 커버리지 140/148\n"
  control.md: "확정 문장 커버리지 148/148\n"
```

**기대** — 생성물을 내는 실행은 종료 0이다. 자극을 대조한 실행은 종료 0과 문구 `어긋남`을 낸다. 통제를 대조한 실행은 종료 0과 `어긋난 쌍 0`을 낸다. `--report`는 판정이 아니라 보고라 종료 코드는 늘 0이다.

```yaml
expect:
  - exit: 0
  - exit: 0
    contains:
      - "어긋남"
  - exit: 0
    contains:
      - "어긋난 쌍 0"
```

**실행 명령** — `bazel build //kg:metrics //kg:audit //kg:link_candidates; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{stimulus.md}}; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{control.md}}`

**표본 근거** — `sampling:factor` · seed `1` · 시나리오 `document-table-number-mismatch` · 요인 `agt:documentLag`. 값은 `cited_value=140/148`이고 판정 부류는 `reject`(keep 밖)다.
