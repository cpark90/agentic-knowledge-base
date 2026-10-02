---
id: https://agentic-knowledge-base.dev/id/chunk/74d3682e-98df-428f-a8dd-776e8c5027e8
type: artifact
level: executable
title_ko: 함수 render_adr (tools/weave.py)
title: function render_adr in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/ed7fa3c5-2a34-4aaf-9cd1-e9f6e86d8e1f, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/ec24ef39-7e27-4fff-bba3-6fdb1829b342
---
**함수** — `render_adr(m, bodies, inputs, root)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_adr(m: Model, bodies: dict, inputs: list[str], root: Path) -> str:
    comps = m.decision_composites()
    live = [(c, r) for c, r in comps if m.status[r["conclusion"]] != "deprecated"]
    deprecated_n = len(comps) - len(live)
    decision_comps = {c for c, _ in comps}  # 손으로 쓴 복합체(composite-kg)의 부분인 옛 단일 파일 결정은 결정 복합체가 아니다
    singles_all = sorted((c for c in m.chunks if m.plane[c] == "decision" and m.comp_of.get(c) not in decision_comps), key=lambda c: m.location[c])
    singles = [c for c in singles_all if m.live(c)]
    o = head("adr", "결정 기록", "살아 있는 결정 전부 — 결정 복합체(`agt:Composite` 의 부분이 conclusion·rationale·alternatives 청크, 결론의 status ≠ deprecated)마다 "
             "결론 라벨 · 상태 · 수준 · 세 본문, 그 뒤 결정 복합체에 속하지 않는 살아 있는 `agt:DecisionChunk`(단일 파일)마다 라벨 · 상태 · 수준 · 본문. "
             "둘 다 `agt:refines`/`agt:serves` 대상 · `agt:supersedes` 연쇄 · `prov:wasDerivedFrom` · `agt:assumes` 를 낸다", m.g, inputs,
             [f"- 결정 복합체 {len(live)} (deprecated {deprecated_n} 제외) · 단일 파일 결정 {len(singles)} (v1·harness 유래 `chunks/decision/`, deprecated {len(singles_all) - len(singles)} 제외)"])
    titles_c = [m.ko(r["conclusion"]) for _, r in live]
    titles_s = [m.ko(c) for c in singles]
    # 결정은 복합체든 단일 파일이든 동격이므로 같은 깊이(h3)에 두고, 두 무리를 h2 로 묶는다 (G8 — 제목 계층은 한 단계씩)
    anchors = anchors_of(["목차", COMPOSITES_HEADING] + titles_c + [SINGLES_HEADING] + titles_s)
    a_comp, a_single = anchors[1], anchors[2 + len(live)]
    a_c, a_s = anchors[2:2 + len(live)], anchors[3 + len(live):]
    body = ["## 목차", "", f"- [{COMPOSITES_HEADING}](#{a_comp})"]
    for (c, _), title, a in zip(live, titles_c, a_c):
        body.append(f"  - [{title}](#{a}) — `{m.unit_ref(c)}`")
    body.append(f"- [{SINGLES_HEADING}](#{a_single})")
    for c, title, a in zip(singles, titles_s, a_s):
        body.append(f"  - [{title}](#{a}) — `{m.unit_ref(c)}`")
    body += ["", f"## {COMPOSITES_HEADING}", "",
             f"결론·근거·대안이 세 파일로 갈린 결정 {len(live)}건이다. 절 하나가 결정 하나이고 세 본문을 그대로 싣는다.", ""]
    for (comp, r), title in zip(live, titles_c):
        parts = [r[k] for k in ("conclusion", "rationale", "alternatives") if k in r]
        levels = " (" + " · ".join(f"{k} {m.level[r[k]]}" for k in ("rationale", "alternatives") if k in r) + ")"
        body += decision_section(m, bodies, root, "###", title, m.unit_ref(comp), parts, levels, f" · 복합체 `{kb_lib.compact_iri(str(comp))}`")
    body += [f"## {SINGLES_HEADING}", "",
             f"결론·근거·대안이 한 본문 안에 있는 옛 형식의 결정 {len(singles)}건이다. 손으로 쓴 복합체(`kg/composite-kg.ttl`)에 속한 것은 그 복합체를 적는다.", ""]
    for c, title in zip(singles, titles_s):
        comp = m.comp_of.get(c)
        comp_line = f" · 복합체 {m.ko(comp)} (`{kb_lib.compact_iri(str(comp))}`)" if comp is not None else ""
        body += decision_section(m, bodies, root, "###", title, m.unit_ref(c), [c], "", comp_line)
    return kb_lib.gendoc_assemble(o, body, inputs)
```
<!-- 인용 끝 -->
