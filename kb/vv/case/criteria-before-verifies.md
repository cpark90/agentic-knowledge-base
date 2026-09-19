---
id: https://agentic-knowledge-base.dev/id/chunk/5d821776-dc19-4202-b184-5efb11d99fcc
type: schema
level: concrete
title_ko: 커밋된 케이스 전부가 합격 기준을 refines 하여 verifies-without-criteria 질의가 행 0을 내고 감사가 같은 값을 적는다
title: Every committed case refines a pass criterion so the verifies-without-criteria query returns zero rows and the audit reports the same value
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/23979ee5-fd7a-4e14-9f91-6d3ec2794725]
verifies: [https://agentic-knowledge-base.dev/id/chunk/96966fae-587c-426f-9da7-5233844aa016]
---
**케이스** — 커밋된 V&V KB 전체를 양성 자극으로 쓴다. 음성 자극은 커밋하지 않는 서술 표본이다.

**자극** — `kb/vv/case/`의 케이스 전부다. 각 케이스는 `refines`로 `kb/vv/criteria/`의 합격 기준(`contract`·logical) 하나를, `verifies`로 `kb/dev/decision`의 결론 하나를 가리킨다. 이 케이스 자신이 그 표본이다.

```yaml
positive:  {subject: kb/vv/case/*.md, refines: kb/vv/criteria/<같은 슬러그>.md, verifies: kb/dev/decision/<id>/conclusion.md}
negative:  {subject: 케이스, refines: [], verifies: [결론]}   # 서술 표본 — head 에 넣으면 질의가 행 하나를 낸다
```

**기대** — `//kg:gate_test`가 PASS이고 `verifies-without-criteria.rq`의 결과 행이 0이다. `bazel-bin/kg/audit.md`의 검증 현황 절에 기준 없는 `verifies` **0**이 있다. 음성 표본을 head 그래프에 더하면 같은 시험이 `FAIL [verify]` 한 줄로 끝난다.

**실행 명령** — `bazel test //kg:gate_test && bazel build //kg:audit`

**표본 근거** — 양성 표본을 케이스 자신으로 두면 `refines`와 `verifies`가 한 파일에서 판정된다. 음성은 `refines`만 비워 실패 원인을 기준 부재 하나로 좁힌다. `refines` 대상이 `contract`가 아닌 경우는 같은 질의의 같은 분기라 표본을 늘리지 않는다.
