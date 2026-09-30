---
id: https://agentic-knowledge-base.dev/id/chunk/9b0e4980-f708-452f-b7c1-d932d6f1a6f8
type: artifact
level: executable
title_ko: 함수 main (tools/odd2kg.py)
title: function main in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
part_of: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("src")
    a = ap.parse_args()
    tax = load_yaml(a.taxonomy) or {}
    doc = load_yaml(a.src)
    if not isinstance(doc, dict) or not doc.get("MODULES"):
        print(f"FAIL [{TAG}] {a.src}: OpenODD 문서가 아니다 — 최상위 MODULES 매핑이 있어야 한다", file=sys.stderr)
        return EXIT_FAIL
    cats = set((tax.get("TAXONOMY") or {}).keys())
    errors = []
    attrs = {}  # name -> (category, decl)
    for cat, members in (doc.get("TAXONOMY") or {}).items():
        if cat not in cats:
            errors.append(f"TAXONOMY 범주 {cat!r} 가 생성된 택소노미에 없다 — 온톨로지(related/condition)를 먼저 확장하라")
            continue
        for name, decl in (members or {}).items():
            attrs[name] = (cat, decl)
    meta, checks, lits = doc.get("ATTRIBUTES") or {}, doc.get("CHECKS") or {}, doc.get("LITERALS") or {}
    conds = []
    for mod_id, mod in (doc.get("MODULES") or {}).items():
        for sec in ("INCLUDE_AND", "INCLUDE_OR", "EXCLUDE_AND", "EXCLUDE_OR"):
            for name, expr in (mod.get(sec) or {}).items():
                if name not in attrs:
                    errors.append(f"{mod_id}.{sec}: 속성 {name} 이 TAXONOMY 에 선언되지 않았다"); continue
                cat, decl = attrs[name]
                try:
                    kind, text = classify(expr, decl)
                except ValueError as e:
                    errors.append(f"{mod_id}.{sec}.{name}: {e}"); continue
                m, c = meta.get(name), checks.get(name)
                if not m or not m.get("iri") or not m.get("title") or not m.get("title_ko"):
                    errors.append(f"{name}: ATTRIBUTES(iri·title·title_ko) 가 없다"); continue
                if not c or not c.get("method") or not c.get("grade"):
                    errors.append(f"{name}: CHECKS(method·grade) 가 없다 — 판정 방법 없는 조건은 ODD에 둘 수 없다 (0.4절)"); continue
                value = text if kind != "Equal" else f"{text} — {lits[text]}" if text in lits else text
                conds.append((m["iri"], CLASS[cat], m, f"{sec} {kind}: {value}", c))
    if errors:
        print("\n".join(f"FAIL [{TAG}] {a.src}: {e}" for e in errors), file=sys.stderr)
        return EXIT_FAIL
    root = next(iter(doc["MODULES"]))
    title = doc["MODULES"][root].get("title") or {}
    mode = "restrictive" if doc.get("EXCLUDE_WHEN_UNKNOWN", True) else "permissive"
    ex = [f'"{esc(e["concept"])} — reviewed {e["reviewed"]}, 이유: {esc(e["reason"])}"' for e in doc.get("EXCLUSIONS_REVIEWED") or []]
    out = [PREAMBLE.format(src=a.src), f"id:odd-{root.replace('_', '-')} a agt:ODD ;",
           f'    rdfs:label "{esc(title.get("en", root))}"@en , "{esc(title.get("ko", root))}"@ko ;', f'    agt:mode "{mode}" ;',
           "    agt:hasCondition " + " , ".join(iri for iri, *_ in conds) + (" ;" if ex else " .")]
    if ex:
        out.append("    agt:excludes " + " , ".join(ex) + " .")
    for iri, cls, m, value, c in conds:
        out += ["", f"{iri} a {cls} ;", f'    rdfs:label "{esc(m["title"])}"@en , "{esc(m["title_ko"])}"@ko ;',
                f'    agt:conditionValue "{esc(value)}" ;', f'    agt:checkMethod "{esc(c["method"])}" ;', f'    agt:verificationGrade "{c["grade"]}" .']
    Path(a.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
