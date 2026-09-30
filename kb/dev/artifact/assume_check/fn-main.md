---
id: https://agentic-knowledge-base.dev/id/chunk/17209da5-4e10-4e6f-9893-a2a28f5e0c41
type: artifact
level: executable
title_ko: 함수 main (tools/assume_check.py)
title: function main in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--odd", default="kb/odd/project-odd.yml", help="OpenODD 문서 (워크스페이스 상대)")
    ap.add_argument("--break", dest="broken", action="append", default=[], metavar="COND",
                    help="이 조건(id:cond-… 의 슬러그 또는 ODD 속성명)을 out 으로 가정한다 — 인위 파괴 실험. 반복 가능")
    ap.add_argument("--record", action="store_true", help=f"결과를 관측으로 {MEMORY_DIR}/obs-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    ap.add_argument("ttl", nargs="*", help=f"그래프 TTL (기본: {' '.join(DEFAULT_TTL)})")
    a = ap.parse_args()
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
    chunks = set(g.subjects(AGT.lineCount, None))
    live = {c for c in chunks if str(next(g.objects(c, AGT.status), "")) != "deprecated"}
    impact = {}
    for asm in asms:
        direct = {c for c in g.subjects(AGT.assumes, asm["iri"]) if c in live} if asm["status"] == "invalidated" else set()
        hop1, trans = propagate(g, direct, live) if direct else (set(), set())
        impact[asm["iri"]] = (direct, hop1, trans)
    broke_names = list(forced)
    broke_show = [str((attrs.get(n) or {}).get("iri", n)).replace("id:", "") for n in broke_names]  # 보고에는 조건 id 로
    check = None
    if broke_names:  # 검증 실험 — 깨진 가정 전부의 계산된 직접 영향 집합 vs frontmatter 스캔의 실제 의존 집합
        computed = set().union(*(impact[x["iri"]][0] for x in asms if x["status"] == "invalidated")) if asms else set()
        actual, unparsable = set(), []
        for x in asms:
            if x["status"] == "invalidated":
                found, bad = actual_dependents(root, str(x["iri"]))
                actual |= found
                unparsable += bad
        tp = len(computed & actual)
        check = {"computed": len(computed), "actual": len(actual), "equal": computed == actual, "unparsable": unparsable,
                 "precision": f"{tp}/{len(computed)}", "recall": f"{tp}/{len(actual)}",
                 "only_computed": sorted(local(x) for x in computed - actual), "only_actual": sorted(local(x) for x in actual - computed)}

    # 링크 상태의 물질화 — 저장하지 않고 여기서만 계산한다 (노트 9.11절)
    states = kb_lib.odd_states(cond_rows)
    when_false, when_unverified = kb_lib.suspect_by_when(g, states)
    by_trigger = kb_lib.suspect_by_trigger(g)
    sat = kb_lib.suspect_saturation(g, when_false)
    space_rows = []  # `-space` 의 양립 제약 — 링크의 when 과 같은 식 언어다 (space-ontology agt:compatibilityConstraint)
    for sp in sorted(g.subjects(AGT.spaceStatus, None), key=str):
        for c in sorted((str(x) for x in g.objects(sp, AGT.compatibilityConstraint)), key=str):
            verdict_c, left_c = kb_lib.when_eval(c, states)
            space_rows.append((local(sp), c, verdict_c, left_c))

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
    body = ["## 조건 판정 (odd_check 와 같은 판정)", "", "| 조건 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"]
    body += [f"| `{local(r['iri'])}` | {r['title_ko']} | {r['grade']} | {r['state']}{' (--break)' if r['name'] in broke_names else ''} |" for r in cond_rows]
    body += ["", "## 가정 — 판정식은 참조 조건 판정의 연언, 등급은 그 최저", "",
            "| 가정 | 판정 유형 | 판정식 | 등급 | 상태 | assumes 하는 살아 있는 청크 | 직접 영향 | suspect 후보 (1홉 / 전이) |",
            "|---|---|---|---|---|---|---|---|"]
    for x in asms:
        n_assumes = sum(1 for c in g.subjects(AGT.assumes, x["iri"]) if c in live)
        d, h1, tr = impact[x["iri"]]
        body.append(f"| `{local(x['iri'])}` {x['label']} | {x['kind']} | {x['expr']} | {x['grade']} | **{x['status']}** | {n_assumes} | {len(d)} | {len(h1)} / {len(tr)} |")
    for x in asms:
        d, h1, tr = impact[x["iri"]]
        if not d:
            continue
        body += ["", f"### 직접 영향 집합 — `{local(x['iri'])}` ({len(d)}건, suspect 후보 전이 {len(tr)}건)", ""]
        body += [f"- {label_of(g, c)} (`{local(c)}`)" for c in sorted(d, key=lambda c: label_of(g, c))[:40]]
        if len(d) > 40:
            body.append(f"- … 외 {len(d) - 40}건")
    body += ["", "## 링크 상태의 물질화 — `when` 판정과 트리거 (노트 9.11절: 상태는 저장값이 아니라 평가 결과)", "",
             f"- `when` 판정의 범위: {kb_lib.WHEN_GRAMMAR}. 그 밖의 구문은 판정하지 않고 unverified 로 남긴다 (0.4절 restrictive)",
             f"- 확정 링크 {sat['confirmed']} 중 `when` 을 가진 것 {sat['with_when']} · suspect 로 유도된 것 "
             f"**{kb_lib.pct(sat['suspect'], sat['confirmed'])}** — `when` 거짓 {sat['by_when']} · 트리거 {sat['by_trigger']} · 판정 불가 {len(when_unverified)}",
             "", "| 트리거 (링크 종류) | 전파 규칙 | 켜짐 | 근거 |", "|---|---|---|---|"]
    body += [f"| `{k}` | {rule} | {'켜짐' if on else '꺼짐'} | {basis} |" for k, rule, on, basis in kb_lib.SUSPECT_TRIGGERS]
    body += ["", "선언에 없는 링크 종류는 돌지 않는다 — 기본이 꺼짐이다. 선언의 원본은 `tools/kb_lib.py` 의 `SUSPECT_TRIGGERS` 다.", ""]
    rows = [(l, k, st, dv or kb_lib.NONE_MARK, why) for l, k, st, _v, dv, why in kb_lib.when_verdicts(g, states)]
    rows += [(l, str(next(g.objects(l, AGT.linkKind), "")).split("/")[-1], kb_lib.LINK_STATE_CONFIRMED,
              kb_lib.LINK_STATE_SUSPECT, why) for l, why in sorted(by_trigger.items(), key=lambda kv: str(kv[0]))]
    body += ["| 링크 | 종류 | 저장 상태 | 유도 상태 | 사유 |", "|---|---|---|---|---|"]
    body += [f"| `{local(l)}` | `{k or kb_lib.NONE_MARK}` | {st or kb_lib.NONE_MARK} | {dv} | {why} |" for l, k, st, dv, why in rows[:40]] \
            or [f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | `when` 을 가졌거나 트리거가 지목한 링크 {kb_lib.NONE_MARK} |"]
    if len(rows) > 40:
        body.append(f"| … | … | … | … | 외 {len(rows) - 40}건 |")
    body += ["", "| 설계 공간 | 양립 제약 | 판정 | 남긴 것 |", "|---|---|---|---|"]
    body += [f"| `{sp}` | `{c}` | {v} | {' · '.join(lft) or kb_lib.NONE_MARK} |" for sp, c, v, lft in space_rows] \
            or [f"| {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | 양립 제약 {kb_lib.NONE_MARK} |"]
    body.append("")  # 표 뒤의 빈 줄 (G 규약) — 뒤따르는 절이 없을 때도 표가 닫힌다
    if check:
        body += ["", "## 검증 실험 — 계산된 영향 집합 = 실제 의존 집합 (14.1 정정본 4단계 연결 조건)", "",
                f"- 계산된 직접 영향 집합(그래프 `agt:assumes`): **{check['computed']}** · 실제 의존 집합(청크 파일 frontmatter `assumes` 스캔): **{check['actual']}**",
                f"- 정밀도 {check['precision']} · 재현율 {check['recall']} → **{'일치' if check['equal'] else '불일치'}**"]
        if check["only_computed"]:
            body.append("- 그래프에만 있는 것: " + ", ".join(check["only_computed"][:10]))
        if check["only_actual"]:
            body.append("- 파일에만 있는 것: " + ", ".join(check["only_actual"][:10]))
        if check["unparsable"]:
            body.append(f"- 판독 불가 파일 {len(check['unparsable'])}건: " + " · ".join(check["unparsable"][:3]))
    if n_inv:
        body += ["", "무효 가정의 직접 영향 집합은 `invalidated`, suspect 후보는 `suspect` 표시 대상이다 — 표시는 재검증 시점에 일괄로 한다 (method §7). 삭제가 아니다."]
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
