---
id: https://agentic-knowledge-base.dev/id/chunk/33edbfb1-3ace-4b3e-975a-734e9c862566
type: decision
level: concrete
title_ko: 규범 문서 규약 — 시나리오는 부류에서 시작하는 V&V decision 복합체이고 concrete는 사람이 쓰지 않는다
title: Normative-document conventions — A scenario is a V&V decision composite that starts from a class; concrete cases are never hand-written
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/791e4e4c-db54-45f9-a03b-8922cd7cc3af
---
**규약** — `p8-scenario-authoring`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] V&V 시나리오(`kb/vv/scenario/`)의 세 청크 파일 이름은 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md`이고 역할 태그는 각각 `**자극**`·`**요인**`·`**배제 자극**`이며 선언 청크는 `-stimulus`다 (2026-09-29). 시나리오 묶음은 읽기 순서가 정해져 있으므로 `ordered`가 **필수**다 — 없으면 `gen_build`가 거부한다.
규약: 시나리오 | `decision`(vv) 복합체 — 자극·요인·배제 자극. 변수는 ODD 속성만, ODD 밖은 `odd:outside`로 커버리지 제외. 세 청크의 파일 이름은 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md`이고 역할 표지 **자극**·**요인**·**배제 자극**이 결정의 결론·근거·대안 슬롯에 사상되며 선언 청크는 `-stimulus`, `ordered`는 필수다(게이트 `decision-role`·`shacl`, 2026-09-29). 접미 판정은 `kb/vv/scenario/`에서만 걸린다 — 옛 결정에 stem이 `-factors`로 끝나는 것이 있다. 단일 청크 시나리오는 이행 기간 동안 **결론** 표지로 통과한다
규약: 시나리오 저작 | 부류(G5)에서 시작 → ODD 속성으로 변수 → 계약 사후조건으로 기준 → 배제 자극 기록. concrete는 생성기가
