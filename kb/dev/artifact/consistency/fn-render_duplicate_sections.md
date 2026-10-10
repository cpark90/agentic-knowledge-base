---
id: https://agentic-knowledge-base.dev/id/chunk/e1700b86-e90d-43fa-b272-c6c66b5f43bb
type: artifact
level: executable
title_ko: 함수 render_duplicate_sections (tools/consistency.py)
title: function render_duplicate_sections in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2]
part_of: https://agentic-knowledge-base.dev/id/composite/7df89751-62ab-47e6-90b3-8fbdb19b640a
---
**함수** — `render_duplicate_sections(a, exact, label_dups, near, theta_c, bound, cohesion_low, bad_form, term_hits, term_waived, has_tier, linked, ref)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_duplicate_sections(a, exact, label_dups, near, theta_c, bound, cohesion_low, bad_form,
                              term_hits, term_waived, has_tier, linked, ref):
    lines = ["## ① 정확 중복 (contentHash 동일)", ""]
    for g in exact:
        tag = "묶임" if all(linked(x, y) for x, y in combinations(g, 2)) else "**미묶음 — 드리프트 후보**"
        lines.append(f"- {tag}: " + " / ".join(ref(i) for i in g))
    if not exact:
        lines.append("- 없음")
    lines += ["", "## ② 라벨 중복 (용인 불가)", ""]
    for (key, val), g in label_dups:
        lines.append(f"- `{key}` = \"{val}\": " + " / ".join(f"`{i['path']}`" for i in g))
    if not label_dups:
        lines.append("- 없음")
    lines += ["", f"## ③ 근사 중복 후보 (Jaccard ≥ {a.theta}) — 판정: 병합 / 묶기 / 유지", ""]
    for j, x, y in near[:50]:
        tag = "묶임" if linked(x, y) else "미묶음"
        lines.append(f"- {kb_lib.num(j)} {tag}: {ref(x)}  ↔  {ref(y)}")
    if not near:
        lines.append("- 없음")
    if len(near) > 50:
        lines.append(f"- … {len(near) - 50}건 더")
    lines += ["", f"## ④ 묶인 쌍의 응집 저하 (coUpdatesWith 쌍 {len(bound)}, Jaccard < {theta_c:g}) — 판정: suspect / 유지", ""]
    for j, x, y in cohesion_low[:50]:
        lines.append(f"- {kb_lib.num(j)} **응집 저하 — 묶었으나 본문이 갈라짐**: {ref(x)}  ↔  {ref(y)}")
    if not cohesion_low:
        lines.append("- 없음")
    if len(cohesion_low) > 50:
        lines.append(f"- … {len(cohesion_low) - 50}건 더")
    lines += ["", "## ⑤ 결론 라벨 형식 위반 (문장형이 아님)", ""]
    for it in bad_form[:50]:
        lines.append(f"- {ref(it)}")
    if not bad_form:
        lines.append("- 없음")
    if len(bad_form) > 50:
        lines.append(f"- … {len(bad_form) - 50}건 더")
    lines += ["", "## ⑥ 용어집 옛 표기 잔존 (옛 → 표준, tier 1 만)", ""]
    if a.glossary and not has_tier:
        lines.append("- info: 용어집에 `tier` 열이 없다 — 옛 표기를 전부 tier 1(기계 치환)로 본다")
    for old, std, it in term_hits[:80]:
        lines.append(f"- `{old}` → `{std}`: `{it['path']}`")
    if not term_hits:
        lines.append("- 없음")
    if len(term_hits) > 80:
        lines.append(f"- … {len(term_hits) - 80}건 더")
    if term_waived:
        lines.append(f"- 면제 {len(term_waived)}건(waivers.md, `{GATE_TERM}`) — 집계에서 뺐다:")
        lines += [f"  - `{old}` → `{std}`: `{it['path']}`" for old, std, it in term_waived[:80]]
    return lines
```
<!-- 인용 끝 -->
