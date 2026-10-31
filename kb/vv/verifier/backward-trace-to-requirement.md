---
id: https://agentic-knowledge-base.dev/id/chunk/76be7079-4f22-4a28-91c3-ebeeaebc6812
type: artifact
level: executable
title_ko: metrics 뷰가 후방 추적 커버리지 670/673 를 내고 CQ-13 이 467 행의 functional 조상을 낸다
title: The metrics view reports a backward trace coverage of 670/673 and CQ-13 returns 467 rows of functional ancestors
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/1b595055-a384-4309-8946-800c67dd91d6]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/44a05a81-0490-4725-a114-8d42143fdc0e, https://agentic-knowledge-base.dev/id/chunk/ebf3db88-a177-4d7c-8441-992719f174d9, https://agentic-knowledge-base.dev/id/chunk/0f9685af-bae0-4224-8fbf-4f3df723e6ae]
restored: [https://agentic-knowledge-base.dev/id/chunk/44a05a81-0490-4725-a114-8d42143fdc0e, https://agentic-knowledge-base.dev/id/chunk/ebf3db88-a177-4d7c-8441-992719f174d9, https://agentic-knowledge-base.dev/id/chunk/0f9685af-bae0-4224-8fbf-4f3df723e6ae]
---
**검증기** — 생성 뷰 둘을 자극으로 쓴다.

**자극** — `//kg:metrics` 와 `//kg:cq` 다. 입력은 그래프 union(`//kg:chunks_kg`·`//kg:kg`·`//kg:references_kg`·`//kb/odd:odd`)이다. 2026-09-21 측정은 살아 있는 단위 지식 741 · 요구 68 · 비요구 673 다.

```yaml
metrics:  {line: "요구로 거슬러 오르는 비요구 청크", value: "670/673 = 99.6%", target: "100.0%"}
cq13:     {rows: 467, ancestorLevel: 기능 수준}
residue:  3                                   # 요구에 닿지 않는 살아 있는 비요구 청크 — 전부 memory 관측 (케이스 decision-names-requirement)
```

**기대** — 두 빌드가 성공한다. `bazel-bin/kg/metrics.md` 의 CQ20 절에 위 줄이 `n/d = p.p%` 꼴로 있고 `(목표 100.0%)` 가 붙어 있다. `bazel-bin/kg/cq.md` 의 CQ-13 절에 행 수와 상위 5행이 있다. 수치는 단위 지식이 바뀌면 함께 바뀐다. 판정은 뷰의 생성 성공이고 값은 인용이다.

**실행 명령** — `bazel build //kg:metrics //kg:cq`

**판정 범위** — 후방 추적은 전수 계산이라 표본 추출이 없다. 잔여 3 이 0 이 아닌 상태를 그대로 두는 것이 "오르지 못하는 산출물을 셀 수 있어야 한다" 의 표본이다. 잔여의 정체는 테스트 케이스 `decision-names-requirement` 가 지식 종류별로 대조한다.

**검증 대응물** — 이 검증기는 `tools/metrics.py`, `tools/query.py`와 질의 `CQ-13`의 항목을 `verifies` 한다. 코드 파일의 끝은 파일 복합체의 선언 항목(`module.md`)이고 질의 파일의 끝은 그 파일 항목이며, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p8-coverage-metrics`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
