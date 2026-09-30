---
id: https://agentic-knowledge-base.dev/id/chunk/eabed46d-9f14-4130-aebe-c2976840f5e7
type: artifact
level: executable
title_ko: 함수 main (tools/consistency.py)
title: function main in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/95c4ded8-afa7-4840-953a-949e4af4f137
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    a = parse_args()
    theta_c = a.theta_cohesion if a.theta_cohesion is not None else a.theta / 2

    def config_fail(msg: str) -> int:
        print(f"CONFIG [consistency] {msg}", file=sys.stderr)
        return EXIT_CONFIG

    try:
        apply_plane_level_state(*load_plane_level_state(a.residency))
    except (OSError, ValueError) as e:
        return config_fail(f"{a.residency}: 읽을 수 없다 — {e}")
    try:
        waivers = load_waivers(a.waivers) if a.waivers else []
    except (OSError, ValueError) as e:
        return config_fail(str(e))
    try:
        terms, has_tier = old_terms(a.glossary) if a.glossary else ([], True)
    except OSError as e:
        return config_fail(f"용어집을 읽을 수 없다 — {e}")
    try:
        items = load_items(a.chunks)
    except ValueError as e:
        return config_fail(f"청크를 파싱할 수 없다 — {e}")
    by_id = {it["id"]: it for it in items}

    def linked(x, y):
        return y["id"] in x["co"] or x["id"] in y["co"]

    def ref(it):
        return f"`{it['path']}` — {it['title_ko']}"

    exact, label_dups, near, sh = analyse_duplicates(items, a.theta)
    bound, cohesion_low = analyse_cohesion(items, by_id, sh, theta_c)
    bad_form = analyse_label_form(items)
    term_hits, term_waived = analyse_terms(items, terms, waivers)
    p = analyse_prose(items, waivers)
    total_pairs, unlinked_exact, unlinked_near, dup_candidates, placement = analyse_candidates(items, exact, near, linked)

    dup_ids = {i["id"] for g in exact for i in g} | {i["id"] for _, x, y in near for i in (x, y)}
    head = render_head(a, theta_c, items)
    lines = render_summary(items, exact, total_pairs, unlinked_exact, label_dups, near, unlinked_near,
                           cohesion_low, bound, bad_form, term_hits, term_waived, p, dup_candidates, placement, dup_ids)
    lines += render_duplicate_sections(a, exact, label_dups, near, theta_c, bound, cohesion_low, bad_form,
                                       term_hits, term_waived, has_tier, linked, ref)
    lines += render_prose_sections(p["hedge_hits"], p["colloq_hits"], p["dash_dense"], ref)
    lines += render_addition_sections(p)
    lines += render_candidate_sections(dup_candidates, placement, ref)
    Path(a.out).write_text(kb_lib.gendoc_assemble(head, lines, a.chunks, input_kind="청크 파일"), encoding="utf-8")
    return EXIT_OK
```
<!-- 인용 끝 -->
