---
id: https://agentic-knowledge-base.dev/id/chunk/8af0faef-89a5-4e0d-aac7-50f4da38662c
type: artifact
level: executable
title_ko: 커밋된 테스트 케이스 전부가 합격 기준을 refines 하여 verifies-without-criteria 질의가 행 0을 내고 감사가 같은 값을 적는다
former_title_ko: ["커밋된 케이스 전부가 합격 기준을 refines 하여 verifies-without-criteria 질의가 행 0을 내고 감사가 같은 값을 적는다"]
title: Every committed case refines a pass criterion so the verifies-without-criteria query returns zero rows and the audit reports the same value
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/23979ee5-fd7a-4e14-9f91-6d3ec2794725]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-24T22:39:25+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1, https://agentic-knowledge-base.dev/id/chunk/8cdc4517-979e-4aa1-809f-b7b5adb1d219, https://agentic-knowledge-base.dev/id/chunk/202358d3-fd6f-4b1c-867d-37e5a20adf9c]
restored: [https://agentic-knowledge-base.dev/id/chunk/9e2e1287-6ee7-4e18-9c18-f2568a030de1, https://agentic-knowledge-base.dev/id/chunk/8cdc4517-979e-4aa1-809f-b7b5adb1d219, https://agentic-knowledge-base.dev/id/chunk/202358d3-fd6f-4b1c-867d-37e5a20adf9c]
---
**검증기** — 커밋된 V&V KB 전체를 양성 자극으로 쓴다. 음성 자극은 커밋하지 않는 서술 표본이다.

**자극** — `kb/vv/case/`의 테스트 케이스 전부다. 각 테스트 케이스는 `refines`로 `kb/vv/criteria/`의 합격 기준(`contract`·logical) 하나를, `verifies`로 `kb/dev/decision`의 결론 하나를 가리킨다. 이 테스트 케이스 자신이 그 표본이다.

```yaml
positive:  {subject: kb/vv/case/*.md, refines: kb/vv/criteria/<같은 슬러그>.md, verifies: kb/dev/decision/<id>/conclusion.md}
negative:  {subject: 케이스, refines: [], verifies: [결론]}   # 서술 표본 — head 에 넣으면 질의가 행 하나를 낸다
```

**기대** — `//kg:gate_test`가 PASS이고 `verifies-without-criteria.rq`의 결과 행이 0이다. `bazel-bin/kg/audit.md`의 검증 현황 절에 기준 없는 `verifies` **0**이 있다. 음성 표본을 head 그래프에 더하면 같은 시험이 `FAIL [verify]` 한 줄로 끝난다.

**실행 명령** — `bazel test //kg:gate_test && bazel build //kg:audit`

**판정 범위** — 양성 표본을 테스트 케이스 자신으로 두면 `refines`와 `verifies`가 한 파일에서 판정된다. 음성은 `refines`만 비워 실패 원인을 기준 부재 하나로 좁힌다. `refines` 대상이 `contract`가 아닌 경우는 같은 질의의 같은 분기라 표본을 늘리지 않는다.

**검증 대응물** — 이 검증기는 `tools/validate.py`, 질의 `verifies-without-criteria`와 `tools/weave.py`의 항목을 `verifies` 한다. 코드 파일의 끝은 파일 복합체의 선언 항목(`module.md`)이고 질의 파일의 끝은 그 파일 항목이며, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p8-pass-criteria`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
