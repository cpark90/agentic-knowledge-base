---
id: https://agentic-knowledge-base.dev/id/chunk/61df20c2-e2b4-5edb-bf5f-912d06cd247c
type: decision
level: logical
title_ko: 논리 시나리오 자극 — 생성물과 다른 수치 하나를 적은 문서의 대조
title: Logical scenario stimulus — comparing a document that carries one number differing from the generated view
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:35:51+09:00}
overlapsWith: [https://agentic-knowledge-base.dev/id/chunk/15d8c8e5-5bd9-44ba-ae32-7580a70fc20c, https://agentic-knowledge-base.dev/id/chunk/c4972f95-7e4e-43f6-b1fa-45426d0ca688]
restored: [https://agentic-knowledge-base.dev/id/chunk/15d8c8e5-5bd9-44ba-ae32-7580a70fc20c, https://agentic-knowledge-base.dev/id/chunk/c4972f95-7e4e-43f6-b1fa-45426d0ca688]
refines: [https://agentic-knowledge-base.dev/id/chunk/31b9d3b9-577d-486a-8792-1146783508ae]
part_of: https://agentic-knowledge-base.dev/id/composite/b828c5d9-fb96-5bda-ae36-9ffa25d272c2
composite: {id: https://agentic-knowledge-base.dev/id/composite/b828c5d9-fb96-5bda-ae36-9ffa25d272c2, title_ko: 생성물과 다른 수치 하나를 적은 문서의 대조, title: Comparing a document that carries one number differing from the generated view, ordered: [https://agentic-knowledge-base.dev/id/chunk/61df20c2-e2b4-5edb-bf5f-912d06cd247c, https://agentic-knowledge-base.dev/id/chunk/1db975d8-8401-5176-88de-210d99fe67b9, https://agentic-knowledge-base.dev/id/chunk/44e8f650-ce19-505a-86b0-505b34dfaa01]}
---
**자극** — abstract 자극(생성물의 수치가 바뀌고 문서의 표가 그대로인 편집)을 값으로 좁힌다. actor는 문서를 저작하는 에이전트이고 action은 이름 `확정 문장 커버리지` 뒤에 생성물과 다른 값을 적은 임시 문서를 `doccheck --report`로 대조하는 것이다. 순서는 생성물 빌드 → 자극 대조 → 통제 대조다. `keep()`은 목표에 고정된 값 `148/148`이다. 변수는 문서에 적은 값 `cited_value` 하나이고 ODD 속성 `id:cond-build-system`(빌드 체계 — 생성물은 `bazel-out`에만 있다)에 매인다.

```yaml
keep:
  cited_value: {odd: "id:cond-build-system", values: ["148/148"], reject: ["140/148"]}
cover:
  - {rule: factor, var: cited_value, factors: {"agt:documentLag": "140/148"}}
seed: 1
case:
  criteria: https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407
  verifies: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
  title_ko: "생성물과 다른 수치 ${cited_value}를 적은 임시 문서는 doccheck --report에서 어긋남을 내고 같은 수치를 적은 통제는 어긋난 쌍 0을 낸다"
  title: "A temporary document carrying the number ${cited_value} that disagrees with the generated view is reported as a mismatch by doccheck --report, and the control reports zero mismatched pairs"
  summary: "기준 `document-table-matches-generated`의 이름별 값 일치 대조를 `doccheck --report`의 위치 인자로 잰다."
  stimulus: "임시 문서 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 이름 `확정 문장 커버리지` 뒤에 `${cited_value}`를 적어 대조 쌍 하나만 어긋나게 한다. 통제는 같은 이름에 목표 값을 적은 같은 형의 문서다."
  files:
    stimulus.md: "확정 문장 커버리지 ${cited_value}\n"
    control.md: "확정 문장 커버리지 148/148\n"
  command: "bazel build //kg:metrics //kg:audit //kg:link_candidates; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{stimulus.md}}; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{control.md}}"
  reject:
    prose: "생성물을 내는 실행은 종료 0이다. 자극을 대조한 실행은 종료 0과 문구 `어긋남`을 낸다. 통제를 대조한 실행은 종료 0과 `어긋난 쌍 0`을 낸다. `--report`는 판정이 아니라 보고라 종료 코드는 늘 0이다."
    expect:
      - {exit: 0}
      - {exit: 0, contains: ["어긋남"]}
      - {exit: 0, contains: ["어긋난 쌍 0"]}
```
