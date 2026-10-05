---
id: https://agentic-knowledge-base.dev/id/chunk/47277b95-1097-5aba-8c95-fbb7d526e0cd
type: schema
level: concrete
title_ko: when이 거짓인 확정 링크 하나가 cond-build-system을 깬 assume_check에서 suspect로 유도되고 종료 코드 1이며 깨지 않은 같은 자극은 종료 0이다
title: A single confirmed link whose when is false is derived to suspect by assume_check with cond-build-system broken, and the same stimulus without the break exits 0
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:case_gen, at: 2026-10-04T21:22:42+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/762f6674-5a5a-4284-bd2d-6374ba22596c]
verifies: [https://agentic-knowledge-base.dev/id/chunk/2921c7a6-95a6-49b2-83d1-4b90bfd44c1a]
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/94abc6b4-5443-51c2-9871-2ea56efb8a0a]
---
**케이스** — `when`이 거짓인 확정 링크 하나를 자극으로 쓴다.

**자극** — 임시 파일 하나다. 이름은 `vv-when-cycle.ttl`이고 경로는 검증기가 정한다. 커밋하지 않는다. 확정 링크 하나가 `in(cond-build-system)`인 `when`과 지지 증거를 갖는다. 가정·의존 청크는 없다.

```yaml
files:
  vv-when-cycle.ttl: "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n@prefix id:  <https://agentic-knowledge-base.dev/id/> .\nid:link-vv-when-sample a agt:Link , agt:ConfirmedLink ;\n    agt:linkFrom id:chunk-vv-when-sample-from ; agt:linkTo id:chunk-vv-when-sample-to ;\n    agt:linkKind agt:refines ; agt:linkState \"confirmed\" ; agt:when \"in(cond-build-system)\" ;\n    agt:hasEvidence id:evidence-vv-when-sample .\nid:evidence-vv-when-sample a agt:Evidence ; agt:evidenceKind agt:runResult ;\n    agt:evidenceRef \"vv-when-cycle probe\" ; agt:polarity \"+\" .\n"
```

**기대** — `--break cond-build-system`을 준 실행은 종료 1과 `when`이 거짓인 링크, 링크 행 `confirmed → suspect`, 사유를 낸다. `--break` 없는 같은 자극은 종료 0이다.

```yaml
expect:
  - exit: 1
    contains:
      - "`when` 이 거짓인 링크 있음"
      - "confirmed | suspect"
      - "거짓 — `in(cond-build-system)`"
  - exit: 0
```

**실행 명령** — `python3 tools/assume_check.py --break cond-build-system {{vv-when-cycle.ttl}}; python3 tools/assume_check.py {{vv-when-cycle.ttl}}`

**표본 근거** — `sampling:factor` · seed `1` · 시나리오 `when-false-suspect` · 요인 `agt:brokenAssumption`. 값은 `broken=cond-build-system`이고 판정 부류는 `reject`(keep 밖)다.
