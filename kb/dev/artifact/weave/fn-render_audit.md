---
id: https://agentic-knowledge-base.dev/id/chunk/4ed2982d-49b2-4313-856e-6b86a53fb3b0
type: artifact
level: executable
title_ko: 함수 render_audit (tools/weave.py)
title: function render_audit in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0ec64ac7-ed2b-4c44-b7d8-9e704c344f79, https://agentic-knowledge-base.dev/id/chunk/1d7270dd-9f02-4949-a1ab-2681afc73834, https://agentic-knowledge-base.dev/id/chunk/38bf7453-3138-4cc0-937e-f2cb1026219f, https://agentic-knowledge-base.dev/id/chunk/642d5db6-db19-4189-acb3-253f39bd2671, https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67, https://agentic-knowledge-base.dev/id/chunk/7cf3545d-a032-4824-826f-aca6c0876d34, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/a30e68f5-b43c-4872-9976-ebcdb40c174e, https://agentic-knowledge-base.dev/id/chunk/abdec406-8c7d-4178-9fd6-73bc42cea633, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99, https://agentic-knowledge-base.dev/id/chunk/c7c1c9ca-af8e-4435-a2cb-faaa5761faaf, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/cad35f43-9f4f-422e-b25b-61cde9208d06
---
**함수** — `render_audit(m, bodies, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_audit(m: Model, bodies: dict, inputs: list[str]) -> str:
    g = m.g
    live = {c for c in m.chunks if m.live(c)}
    vv = {c for c in live if kb_lib.kb_of(m.location[c]) == kb_lib.KB_VV}
    dev = live - vv
    by_gen = lambda c: str(next(g.objects(c, AGT.generatedBy), ""))  # noqa: E731
    obs_all = [c for c in m.chunks if m.plane[c] == "memory"]
    runs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.VV_RUN_DIR + "/") and by_gen(c) == kb_lib.RUN_GENERATOR),
                  key=lambda c: (m.at(c), m.location[c]))
    asm_obs = sorted((c for c in obs_all if m.location[c].startswith(kb_lib.DEV_MEMORY_DIR + "/") and by_gen(c) == kb_lib.ASSUME_CHECK_GENERATOR),
                     key=lambda c: (m.at(c), m.location[c]))
    latest_run, latest_asm = (runs[-1] if runs else None), (asm_obs[-1] if asm_obs else None)
    run_body = bodies.get(str(latest_run), "") if latest_run is not None else ""
    asm_body = bodies.get(str(latest_asm), "") if latest_asm is not None else ""

    pct = kb_lib.pct  # 비율 표기의 단일 정의처 (G15 — metrics 와 같은 정의)

    # 1. 리비전 — 그래프는 리비전을 담지 않는다. 실행 기록이 초기 상태(p8-reproducibility)로 담는다
    rev_m = RUN_REVISION.search(run_body)
    rev_line = (f"실행 기록의 리비전 `{rev_m.group(1)}`" + (f" ({rev_m.group(2)})" if rev_m.group(2) else "") + f" — `{Path(m.location[latest_run]).name}`"
                if rev_m else "실행 기록이 없어 리비전을 알 수 없다 — 그래프는 리비전을 담지 않는다")
    h = head("audit", "감사 보고서", "그래프 union 과 관측 청크 본문(`kb/vv/run/` 실행 기록 · `kb/dev/memory/` 가정 판정)만으로 — 검증 현황 · 최근 실행 · "
             "판정 주석 · 가정 · 추적 매트릭스(`kb_lib.TIM_CELLS`) · 검증 표시 · 링크 근거 · 자족성", g, inputs,
             [f"- 리비전: {rev_line}",
              f"- 입력의 종류: 그래프 union(head · 참조 · 시드 · 카탈로그 · 복합체 · ODD · 온톨로지) · 관측 본문 — 실행 기록 {len(runs)}건 · 가정 판정 {len(asm_obs)}건. "
              f"체계 밖 정보 0 (요구 `audit-self-sufficiency`)",
              f"- 살아 있는 청크 {len(live)} — 개발 KB {len(dev)} · V&V KB {len(vv)}"])
    body: list[str] = []

    # 절마다 함수 하나다 — 각 함수가 자기 절의 본문 조각을 내고 여기서 순서대로 잇는다. 절의 순서가 보고의 순서다.
    body += _audit_verification(m, g, dev, vv, pct)
    body += _audit_risk_goals(m, g, vv, pct)
    body += _audit_latest_run(m, runs, latest_run, run_body, by_gen)
    body += _audit_comments(m, g, live, pct, by_gen)
    body += _audit_assumptions(m, asm_obs, latest_asm, asm_body)
    body += _audit_matrix(g)
    body += _audit_verified(m, g, live)
    body += _audit_links(m, g, pct)

    # 9. 자족성 선언
    body += ["## 자족성 선언", "",
          "이 보고서의 모든 수치는 위 입력(그래프 union · 실행 기록 · 가정 판정 관측)에서 나왔다. 손으로 적은 수치는 없다. "
          "이 보고서를 다시 만드는 명령은 `bazel build //kg:audit` 이고 입력이 같으면 수치가 같다.", ""]
    return kb_lib.gendoc_assemble(h, body, inputs)
```
<!-- 인용 끝 -->
