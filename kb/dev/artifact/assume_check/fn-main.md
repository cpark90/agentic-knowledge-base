---
id: https://agentic-knowledge-base.dev/id/chunk/17209da5-4e10-4e6f-9893-a2a28f5e0c41
type: artifact
level: executable
title_ko: 함수 main (tools/assume_check.py)
title: function main in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1a52fdec-22af-4925-98d0-b91f50c202b5, https://agentic-knowledge-base.dev/id/chunk/1de413a3-d886-4f4a-b4d8-5899d68e6d2c, https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/304744ba-30b6-43f2-8aee-d9532aa66c13, https://agentic-knowledge-base.dev/id/chunk/31bc1a35-7001-4936-9b80-a0bfffed1335, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/91c67aff-4114-4bf6-a319-b4aa40cbc5f1, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/a3ac2cde-76e2-4d4e-b75f-ecd7060abd39, https://agentic-knowledge-base.dev/id/chunk/a49b0fbe-30fd-4d2c-8b92-f99763bd47af, https://agentic-knowledge-base.dev/id/chunk/ae67e102-2e22-4234-8638-b2db8fa603b4, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e, https://agentic-knowledge-base.dev/id/chunk/fc00bd15-31c6-4e4b-b28e-773cbf0b1e48, https://agentic-knowledge-base.dev/id/chunk/ff4fd3d8-23db-4fee-89d7-f5c9052f5590]
part_of: https://agentic-knowledge-base.dev/id/composite/5dac7240-2471-496d-a65c-f55a8a067a41
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    a = parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    now = datetime.now(timezone.utc).replace(microsecond=0)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [assume_check] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG

    odd_path = root / a.odd
    if not odd_path.is_file():
        print(f"FAIL [assume_check] {a.odd}: ODD 문서가 없다")
        return EXIT_CONFIG
    doc = load_odd(odd_path)
    attrs = doc.get("ATTRIBUTES") or {}
    by_slug = {str(v.get("iri", "")).replace("id:", ""): k for k, v in attrs.items()}  # cond-… → 속성명
    forced, unknown = {}, []
    for b in a.broken:
        name = b if b in attrs else by_slug.get(b)
        if name:
            forced[name] = "out"
        else:
            unknown.append(b)
    if unknown:
        print(f"FAIL [assume_check] --break 대상이 ODD 에 없다: {', '.join(unknown)} — ODD 조건(id:cond-…)만 깨뜨릴 수 있다 (0.4절)")
        return EXIT_CONFIG
    g, missing = load_graph(a.ttl or DEFAULT_TTL, root)
    if missing:
        print(f"FAIL [assume_check] 그래프를 찾을 수 없다: {', '.join(missing)} — bazel run //tools:assume_check 로 돌리면 data 로 놓인다")
        return EXIT_CONFIG

    cond_rows = judge_all(doc, root, forced)
    asms = evaluate(g, cond_rows)
    chunks = set(g.subjects(AGT.tokenCount, None))
    live = {c for c in chunks if str(next(g.objects(c, AGT.status), "")) != "deprecated"}
    impact = {}
    for asm in asms:
        direct = {c for c in g.subjects(AGT.assumes, asm["iri"]) if c in live} if asm["status"] == "invalidated" else set()
        hop1, trans = propagate(g, direct, live) if direct else (set(), set())
        impact[asm["iri"]] = (direct, hop1, trans)
    broke_names = list(forced)
    broke_show = [str((attrs.get(n) or {}).get("iri", n)).replace("id:", "") for n in broke_names]  # 보고에는 조건 id 로
    check = None
    check = break_experiment(root, asms, impact) if broke_names else None
    states, when_false, when_unverified, by_trigger, sat, space_rows = materialize_states(g, cond_rows)
    # 보고
    n_inv = sum(1 for x in asms if x["status"] == "invalidated")
    n_unv = sum(1 for x in asms if x["status"] == "unverified")
    verdict = ("**무효 가정 있음**" if n_inv else "**`when` 이 거짓인 링크 있음**" if when_false
               else "판정 불가 가정 있음 (unverified)" if n_unv else "정상 — 모든 가정이 valid")
    broke_note = (f" · 인위 파괴 `--break {' '.join(broke_show)}`" if broke_names else "")
    rep = kb_lib.gendoc_header(
        "assume_check", "가정 판정과 전파", "tools/assume_check.py",
        f"ODD 조건을 판정 방법으로 실제 판정한 뒤, 가정마다 그 참조 조건 판정의 연언으로 valid·invalidated·unverified 를 정하고 "
        f"깨진 가정을 `assumes` 하는 살아 있는 청크(직접 영향)와 그 하류(suspect 후보)를 낸다 (6.9절){broke_note}",
        "bazel run //tools:assume_check", [str(odd_path)] + [str(root / f) for f in (a.ttl or DEFAULT_TTL)],
        f"가정 {len(asms)} · 살아 있는 청크 {len(live)}",
        kb_lib.gendoc_view_notice("ODD 조건 정의와 청크의 `assumes` 링크"),
        extra=[f"- 결과: {verdict} · 가정 {len(asms)} (valid {len(asms) - n_inv - n_unv} · invalidated {n_inv} · unverified {n_unv})",
               f"- 링크: 확정 {sat['confirmed']} · `when` 을 가진 것 {sat['with_when']} · suspect 로 유도된 것 "
               f"**{kb_lib.pct(sat['suspect'], sat['confirmed'])}** (`when` 거짓 {sat['by_when']} · 트리거 {sat['by_trigger']})"])
    inputs = [str(odd_path)] + [str(root / f) for f in (a.ttl or DEFAULT_TTL)]
    body = report_judgements(g, live, asms, impact, cond_rows, broke_names)
    body += report_link_states(g, states, sat, by_trigger, when_unverified, space_rows)
    body += report_experiment(check, n_inv)
    text = kb_lib.gendoc_assemble(rep, body, inputs)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")

    if a.record:
        mem = root / MEMORY_DIR
        mem.mkdir(parents=True, exist_ok=True)
        target = mem / f"obs-{now.strftime('%Y%m%dT%H%M%SZ')}.md"
        if target.exists():
            print(f"FAIL [assume_check] {target.relative_to(root)}: 이미 있다 — 관측은 append-only 다 (r-026)")
            return EXIT_CONFIG
        target.write_text(observation(now, cond_rows, asms, impact, len(live), broke_names, broke_show, check, sat), encoding="utf-8")
        print(f"관측 기록: {target.relative_to(root)} — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    return EXIT_FAIL if (n_inv or when_false) else EXIT_SKIP if (n_unv or when_unverified) else EXIT_OK
```
<!-- 인용 끝 -->
