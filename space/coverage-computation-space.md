---
id: https://agentic-knowledge-base.dev/id/chunk/5d13b3d5-862c-42b3-9348-cce33f3a5021
type: agt:Space
level: logical
title_ko: 커버리지의 분모를 어떻게 세는가
title: How the coverage denominator is counted
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 커버리지의 분모는 ODD다. ODD는 속성들의 값·범위 집합이고 한 속성 조합이 어느 단계에서든 한 번 검증되면 커버인데, 조합의 수는 값 범위의 곱이라 폭발한다. 분모를 전체 조합으로 세는가, 대표 조합인가, 속성별 개별 커버인가가 변수다. 요구 `r-008`(모든 요구는 실산출물까지 내려간다)에서 이 산정 규칙으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 커버리지는 세 지표로 재는 측정치이고 logical 공간 커버의 분모는 ODD 값 범위 × 변수이며 경계값 미커버는 따로 센다(`p8-coverage-metrics`). logical 공간 커버는 단계별로 합산하고 6단계 관측은 넣지 않으므로 100이 될 수 없다(`p8-environment-assignment`). 테스트베드의 환경 정의는 ODD의 부분집합이어야 한다(`p8-testbed`). 위험 케이스는 결함 요인 조합에서 위에서 아래로 구성하고 그 조합이 logical 공간의 표본 추출 근거다. 조합 공간의 빈칸이 아직 시험하지 않은 것이다(`p8-defect-factor-taxonomy`). 케이스 생성 규칙 다섯 중 하나가 t-wise이고 `cover()` 정의가 커버리지 계산의 분모다(`p8-case-generation`). 자율 진행을 허용할 커버리지 하한은 체계가 정하지 않는 입력이다.

현재 상태(2026-10-05 실측) — ODD 조건은 정적 5 · 환경 3 · 동적 1로 9개다. 7개가 단일 범주값이고 범위는 둘(동시 에이전트 수 [0 .. 5], `env_inherit` 예외 타깃 수 1 이하)이라 이 저장소의 조합 공간은 작다. V&V KB의 시나리오는 58개이고 케이스는 16개다. 케이스의 표본 근거 태그는 등가분할 10 · 요인 주입 8이고 경계값·t-wise는 0이다. logical 공간 커버를 ODD 분모로 계산하는 도구는 없다. `defect` 어휘 모듈은 있고 결함 요인을 `exposes`로 가리키는 시나리오 청크는 13개다. 위험 가중을 계산하는 도구는 없다.

답이 가르는 것 — 커버리지 수치의 의미와 자율 진행 판단의 기준이 갈린다. 분모 산정이 다르면 같은 시나리오 집합의 커버리지가 몇 배 차이 난다.

선택지 — A는 t-wise(기본 pairwise)다(`p8-coverage-denominator-t-wise`). 모든 t개 속성 조합이 최소 1회 커버된다. 분모가 계산 가능하고 조합 테스팅의 표준이다. t는 ODD 입력이다. `p8-case-generation`이 t-wise를 케이스 생성 규칙의 하나로 두었으나 분모 산정은 정하지 않아 새 후보로 둔다. B는 위험 가중이다(`p8-coverage-denominator-risk-weighted`). 결함 요인 조합에 걸린 조합만 분모에 넣는다. `defect` 어휘가 선행해야 한다. C는 프로파일 입력이다(`p8-coverage-denominator-profile-input`). 코어는 분모가 ODD라는 것만 고정하고 산정 방식은 분야마다 정한다. 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/c14eef1a-c53a-4071-84d2-5cb172ad3a0e
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/9207fbda-dd45-4fb8-8463-b8a782e1b733
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/a016fddf-fafa-47fa-bd7d-a82328f9ba81
    state: open
```
