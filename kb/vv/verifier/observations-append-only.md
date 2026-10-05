---
id: https://agentic-knowledge-base.dev/id/chunk/94b518f2-9c63-4023-8b6d-ef7efee81b2b
type: artifact
level: executable
title_ko: 커밋된 실행 기록 run-20260919T062548Z가 memory·concrete 청크로 lint·게이트를 통과하고 같은 이름의 재기록은 거부된다
title: The committed run record run-20260919T062548Z passes lint and gates as a memory-concrete chunk and re-recording the same name is refused
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/6bb376e1-0a34-4ab6-ba78-df2c0b030043]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 커밋된 실행 기록 하나와 그것을 다시 쓰려는 시도를 자극으로 쓴다.

**자극** — `kb/vv/run/run-20260919T062548Z.md`다. `vv_run --record`가 만든 첫 실행 기록이고 frontmatter는 `type: memory`·`level: concrete`·`generated: {by: process:vv_run}`이다. 덮어쓰기 자극은 같은 이름의 파일이 있는 상태에서 같은 초의 `--record`를 다시 부르는 것이며 산문으로만 둔다. 실행기는 시각을 파일명으로 쓰므로 같은 초 안의 두 번째 호출이 그 경로다.

```yaml
record:     {file: kb/vv/run/run-20260919T062548Z.md, plane: memory, level: concrete, generated.by: process:vv_run}
overwrite:  {same_name: true, expected_exit: 2}   # EXIT_CONFIG — 서술 표본
```

**기대** — `//kb/vv:lint_test`·`//kg:gate_test`가 PASS이고 `//kb/vv/run/...`의 분석·빌드가 성공한다. head 그래프에 그 기록이 `agt:MemoryChunk`로 오르고 감사 보고서의 최근 실행 절이 그것을 인용한다. 덮어쓰기 자극은 `FAIL [vv_run] … 이미 있다 — 실행 기록은 append-only 다 (r-026)`로 끝나고 종료 코드가 2다.

**실행 명령** — `bazel test //kb/vv:lint_test //kg:gate_test && bazel build //kb/vv/run/...`

**판정 범위** — 표본은 실행기가 실제로 만든 기록이라 손으로 쓴 형식이 섞이지 않는다. 덮어쓰기는 파일 존재 검사 하나로 판정되므로 표본 하나면 분기가 닫힌다. 이 케이스의 실행 뒤 남는 새 기록도 같은 기준의 표본이 된다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p0-run-is-an-append-only-memory-chunk` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
