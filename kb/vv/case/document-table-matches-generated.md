---
id: https://agentic-knowledge-base.dev/id/chunk/6c117bee-b3bb-4abf-ad4a-b11e29899439
type: schema
level: concrete
title_ko: 생성물과 다른 수치 하나를 적은 임시 문서는 doccheck --report 에서 어긋남을 내고, 같은 수치를 적은 통제는 어긋난 쌍 0을 낸다
title: A temporary document carrying one number that disagrees with the generated view is reported as a mismatch by doccheck --report, and the control with the matching number reports zero mismatched pairs
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-01T23:47:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/b173e680-0135-4d83-9e0f-d8fb77d77407]
verifies: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
---
**케이스** — 기준 `document-table-matches-generated`의 (a) 이름별 값 일치 대조를 `doccheck --report`의 위치 인자로 처음 잰다. 주석 `doccheck-report-not-wrappable-as-case`가 막았던 자극(루트 밖 절대 경로)이 developer의 위치 인자 반영 뒤 선다.

**자극** — 임시 문서 둘이고 경로는 검증기가 정한다. 커밋하지 않는다. 자극은 이름 `확정 문장 커버리지` 뒤에 목표에 고정된 값(`148/148`)과 다른 수치 하나만 적어 대조 쌍 하나만 어긋나게 한다. 통제는 같은 이름에 그 값을 적은 같은 형의 문서다.

```yaml
files:
  stimulus.md: |
    확정 문장 커버리지 140/148
  control.md: |
    확정 문장 커버리지 148/148
expect:
  - exit: 0
  - exit: 0
    contains: "어긋남"
  - exit: 0
    contains: "어긋난 쌍 0"
```

**기대** — 생성물을 내는 실행은 종료 0이다. 자극을 대조한 실행은 종료 0과 문구 `어긋남`을 낸다. 통제를 대조한 실행은 종료 0과 `어긋난 쌍 0`을 낸다 — `--report`는 판정이 아니라 보고라 어긋난 쌍이 있어도 종료 코드는 늘 0이다(도구 docstring의 종료 절).

**실행 명령** — `bazel build //kg:metrics //kg:audit //kg:link_candidates; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{stimulus.md}}; python3 tools/doccheck.py --report --root . --waivers docs/waivers.md {{control.md}}`

**표본 근거** — 이 자극이 어기는 것은 이름 하나(`확정 문장 커버리지`)의 값 일치 하나뿐이다 — 문서 전체가 아니라 그 쌍만 어긋난다. 이름을 `연결 성분` 대신 쓰는 까닭은 `연결 성분`이 저작 중 흔들리는 생성물 값이라 생성물이 움직이면 통제가 깨지기 때문이다(`docs/roadmap.md` — "성분은 저작 중 흔들린다"). `확정 문장 커버리지`는 1단계 통과 조건(`p14-stage-pass-conditions`)이 고정한 목표치고 생성물 쪽 실측(`bazel-bin/kg/metrics.md`)도 `확정 문장 커버리지(절 단위) **148/148 = 100.0%**`로 그 값과 같다. 자극은 148/148을 140/148로 바꿔 대조 쌍 하나를 어긋나게 하며 통제는 148/148을 그대로 적어 그 쌍을 일치시킨다. 한계: 두 문서는 이름 하나만 담아 기준의 열넷 이름 전수를 재현하지 않는다 — 전수 대조는 진입점 문서 넷을 쓰는 실측이 기준 청크에 이미 있다.
