---
id: https://agentic-knowledge-base.dev/id/chunk/8eb561b7-3127-4b38-bf4c-da672e972b3f
type: schema
level: concrete
title_ko: vnv 역할에 결정 p11-execution-mode-and-workset 을 앵커로 준 작업 집합 뷰가 이웃 본문만 펼쳐 예산 200줄 안이다
title: The vnv workset anchored on the decision p11-execution-mode-and-workset expands only the neighbour bodies and fits within the 200-line budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T01:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/7db997bc-4f86-4b0c-aa3f-e941657a94a7]
verifies: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c]
---
**케이스** — 앵커를 준 뷰·앵커 없는 통제·예산을 좁힌 음성 자극 셋을 종료 코드로 판정한다.

**자극** — `//kg:workset` 을 셋으로 빌드한다. 앵커는 결정 `p11-execution-mode-and-workset` 의 결론(`id:chunk/965f738a-db50-4729-a551-e58a90cd6320`, "dispatch에는 스코프로 거른 작업 집합만 전달한다")이다. 첫째는 앵커 + 기본 예산 200, 둘째는 앵커 없는 통제, 셋째는 같은 앵커 + 예산 10(음성 자극)이다.

```yaml
expect:
  - exit: 0
  - exit: 0
  - exit: 1
    contains: "FAIL [workset-budget]"
```

**기대** — 첫째·둘째 빌드는 종료 0이다 — 성공한 빌드 액션은 산출물 내용을 표준출력에 내지 않으므로 문구 대조는 실패하는 셋째에만 둔다. 셋째는 예산 10줄이 라벨 목록 길이보다 작아 `FAIL [workset-budget]` 로 실패한다 — 검사하는 규칙은 예산 판정 하나뿐이고 빌드의 성립·앵커 탐색은 그대로 만족한다.

**실행 명령** — `bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320; bazel build //kg:workset --//kb:role=vnv; bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320 --//kb:budget=10`

**표본 근거** — vnv 는 읽기 plane 이 셋뿐이라 스코프 거름이 가장 눈에 띄는 역할이고, 이웃이 개발 KB 결정으로만 이루어지는 까닭은 이전 판단과 같다. 예산 10은 이 앵커의 라벨 목록 길이(20줄대)보다 작게 골라 몸통을 펼치기 전에 이미 초과가 확정되게 한다 — 몸통 패킹의 근사 검사는 편입 항목마다 최대 한 줄만 초과시키므로 근접한 예산으로는 초과가 결정적이지 않다.
