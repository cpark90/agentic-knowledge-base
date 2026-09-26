---
id: https://agentic-knowledge-base.dev/id/chunk/fa3d84ac-38c1-4e08-8638-107fe30915e0
type: schema
level: concrete
title_ko: when 이 거짓인 확정 링크 하나가 assume_check 에서 suspect 로 유도되고 종료 코드 1 이며 when 만 뺀 같은 자극은 종료 0 이다
title: A single confirmed link with a false when is derived to suspect by assume_check with exit code 1, and the same stimulus without the when clause exits 0
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-26T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c]
verifies: [https://agentic-knowledge-base.dev/id/chunk/2921c7a6-95a6-49b2-83d1-4b90bfd44c1a]
---
**케이스** — `when` 이 거짓인 확정 링크 하나를 자극으로 쓴다. `assume_check` 가 `READ_ONLY_VERIFIERS` 열에 든 뒤 처음으로 이 경로를 케이스로 잰다.

**자극** — 임시 파일 하나다. 이름은 `vv-when-cycle.ttl` 이고 경로는 검증기가 정한다. 커밋하지 않는다. 확정 링크(`agt:ConfirmedLink`) 하나가 `agt:when: "in(cond-build-system)"` 과 지지 증거 `runResult` 를 갖는다. 가정·의존 청크는 없다.

```yaml
files:
  vv-when-cycle.ttl: |
    @prefix agt: <https://agentic-knowledge-base.dev/agt/> .
    @prefix id:  <https://agentic-knowledge-base.dev/id/> .
    id:link-vv-when-sample a agt:Link , agt:ConfirmedLink ;
        agt:linkFrom id:chunk-vv-when-sample-from ; agt:linkTo id:chunk-vv-when-sample-to ;
        agt:linkKind agt:refines ; agt:linkState "confirmed" ; agt:when "in(cond-build-system)" ;
        agt:hasEvidence id:evidence-vv-when-sample .
    id:evidence-vv-when-sample a agt:Evidence ; agt:evidenceKind agt:runResult ;
        agt:evidenceRef "vv-when-cycle probe" ; agt:polarity "+" .
expect:
  - exit: 1
    contains: ["`when` 이 거짓인 링크 있음", "confirmed | suspect", "거짓 — `in(cond-build-system)`"]
  - exit: 0
```

**기대** — `--break cond-build-system` 을 준 실행은 종료 1, "`when` 이 거짓인 링크 있음"과 링크 행 `confirmed → suspect`·사유 `when 거짓 — in(cond-build-system)` 을 낸다. `--break` 없는 같은 자극은 종료 0 이다.

**실행 명령** — `python3 tools/assume_check.py --break cond-build-system {{vv-when-cycle.ttl}}; python3 tools/assume_check.py {{vv-when-cycle.ttl}}`

**표본 근거** — 이 자극이 어기는 규칙은 `when` 판정 하나다(`p8-minimal-negative-stimulus`). 링크 외에 가정·의존 청크가 없어 무효 가정 경로와 섞이지 않는다. 최소성은 두 번째 명령이 통제다 — 같은 자극에서 `--break` 만 뺀 실행이 종료 0 임을 같은 케이스 안에서 보인다(2026-09-26 재현). 한계: `--break` 는 그래프·ODD 뿐 아니라 **호스트의 실제 판정도 읽는다** — `cond-build-system` 이 이미 out 인 호스트에서는 두 번째 명령도 종료 1 일 수 있다. 이 케이스는 그 조건이 in 인 호스트(2026-09-26 실측)를 전제하고, 이 한계를 숨기지 않는다.
