---
id: https://agentic-knowledge-base.dev/id/chunk/cdda88c0-dd6f-4d38-8636-427ba3977c40
type: schema
level: concrete
title_ko: 시드의 가정 둘(asm-bazel-toolchain·asm-chunk-conventions)이 ODD 조건을 가리키고 살아 있는 청크 전부가 그 위에 선다
title: The two seeded assumptions asm-bazel-toolchain and asm-chunk-conventions refer to ODD conditions and every living chunk stands on them
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5680c0bc-347b-47f1-a8ad-5b4ef768702f]
verifies: [https://agentic-knowledge-base.dev/id/chunk/98142727-d920-46fc-a3e2-22e7d9a57b65]
---
**케이스** — 시드 그래프의 가정 둘과 그것을 `assumes` 하는 커밋된 청크 전체를 자극으로 쓴다.

**자극** — `kg/base-kg.ttl`의 `id:asm-bazel-toolchain`(`agt:refersTo id:cond-build-system`)과 `id:asm-chunk-conventions`(`agt:refersTo id:cond-repo-layout, id:cond-language-policy`)다. 이 케이스를 포함한 `kb/dev`·`kb/vv`의 모든 청크가 둘 중 하나 이상을 `assumes` 한다. 음성 표본은 서술로만 둔다.

```yaml
asm-bazel-toolchain:    {refersTo: [cond-build-system]}                      # ODD 조건 — 판정 방법·등급 있음
asm-chunk-conventions:  {refersTo: [cond-repo-layout, cond-language-policy]}  # 기본 가정 — 항목별 좁힘이 대체한다
negative:               {assumes: id:asm-missing}                            # 서술 표본 — [dangling] 한 줄
```

**기대** — `//kg:gate_test`·`//kb/odd:gate_test`가 PASS다. `bazel-bin/kg/cq.md`의 CQ-09 행 수가 0이다. 음성 표본은 `FAIL [dangling] … agt:assumes 대상이 없다` 한 줄로 끝나고 종료 코드가 1이다.

**실행 명령** — `bazel test //kg:gate_test //kb/odd:gate_test && bazel build //kg:cq`

**표본 근거** — 가정 둘은 저장소의 모든 청크가 공유하는 전제라 양성 표본이 전수다. 음성은 IRI 하나만 틀리게 하여 실패 원인을 참조 무결성 하나로 좁힌다. `refersTo` 쪽 음성은 ODD 참조 검사의 같은 분기라 표본을 늘리지 않는다.
