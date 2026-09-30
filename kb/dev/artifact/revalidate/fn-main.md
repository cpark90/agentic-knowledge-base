---
id: https://agentic-knowledge-base.dev/id/chunk/8737dba4-7aa0-467f-add3-14901ba38236
type: artifact
level: executable
title_ko: 함수 main (tools/revalidate.py)
title: function main in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="HEAD", help="비교할 git 리비전 (기본 HEAD)")
    ap.add_argument("--universe", default="//...", help="rdeps 의 우주")
    ap.add_argument("--out", default="")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root(워크스페이스) 기준")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    cwd = str(root)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"CONFIG [revalidate] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}", file=sys.stderr)
        return 2

    # 1. 워킹트리 청크 색인 — IRI → (경로, 라벨, meta), 들어오는 링크
    index, incoming, unparsable = {}, defaultdict(list), []
    for d in CHUNK_DIRS:
        for p in sorted((root / d).rglob("*.md")):
            rel = str(p.relative_to(root))
            try:
                meta = parse_chunk(str(p))[0]
            except ValueError as e:
                unparsable.append(f"{rel}: {e}")
                continue
            index[meta["id"]] = (rel, meta)
    for iri, (rel, meta) in index.items():
        for k, t in links_of(meta):
            incoming[t].append((k, iri))
    composite_parts = defaultdict(list)
    for iri, (rel, meta) in index.items():
        if meta.get("part_of"):
            composite_parts[meta["part_of"]].append(iri)
    # 호출부 — 대상 정의 IRI → 그것을 `uses` 로 가리키는 출발점들. 링크 키가 아니므로 links_of 와 섞지 않는다:
    # 그래야 `링크(양방향)` 열이 링크 개체의 수를 계속 뜻하고 `호출부` 열이 코드 파손의 상한을 따로 뜻한다
    callers = defaultdict(list)
    for iri, (rel, meta) in index.items():
        for t in meta.get(USES_KEY) or []:
            if t != iri:
                callers[t].append(iri)

    # 2. base 와의 차이 — 상태 M/A/D/R 인 청크 파일 + 미추적 파일
    status = {}
    for line in run(["git", "diff", "--name-status", a.base, "--", *CHUNK_DIRS], cwd).splitlines():
        parts = line.split("\t")
        st, path = parts[0][0], parts[-1]
        if path.endswith(".md"):
            status[path] = (st, parts[1] if st == "R" else path)
    for path in run(["git", "ls-files", "--others", "--exclude-standard", "--", *CHUNK_DIRS], cwd).splitlines():
        if path.endswith(".md"):
            status[path] = ("A", path)

    # 정체성은 uuid(frontmatter `id`)이고 경로는 주소다 (p10-split-keeps-work-identity · p10-function-identity-registry).
    # 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부풀고 링크가 깨진 것처럼 읽힌다.
    by_path = {rel: iri for iri, (rel, _m) in index.items()}
    base_by_iri, unread = {}, []
    for path, (st, base_path) in sorted(status.items()):
        if st == "A":
            continue
        txt = run(["git", "show", f"{a.base}:{base_path}"], cwd, check=False)
        try:
            bm = parse_text(txt, base_path) if txt else None
        except ValueError:
            unread.append(base_path)
            continue
        if bm:
            base_by_iri[bm["id"]] = (base_path, bm)
    touched = {by_path[p] for p in status if p in by_path} | set(base_by_iri)

    changed, head_only = [], []  # changed: (경로, 종류, iri, meta_wt|None, meta_base|None, 비고)
    for iri in sorted(touched):
        wt = index.get(iri)
        base = base_by_iri.get(iri)
        if wt is None:
            if base:
                changed.append((base[0], "삭제", iri, None, base[1], "이 IRI 를 가리키는 링크는 깨진다"))
            continue
        path, meta = wt
        if base is None:
            changed.append((path, "신규", iri, meta, None, "base 에 이 IRI 가 없다"))
            continue
        base_path, base_meta = base
        moved = f"경로 변경(라벨 변경) `{base_path}` → `{path}`" if base_path != path else ""
        if meta["_content_hash"] != base_meta["_content_hash"]:
            changed.append((path, "본문 변경", iri, meta, base_meta,
                            " · ".join(x for x in (f"{base_meta['_content_hash']} → {meta['_content_hash']}", moved) if x)))
        else:
            keys = sorted(k for k in LINK_KEYS + ("part_of",) if (meta.get(k) or None) != (base_meta.get(k) or None))
            head_only.append((path, keys + ([moved] if moved else [])))

    # 3. 재판정 대상 — (a) frontmatter 링크 양방향 (b) bazel rdeps
    iri_to_label = owner_labels(root)
    owners = sorted({iri_to_label[iri] for _p, kind, iri, *_ in changed if kind != "삭제" and iri in iri_to_label})
    rd = bazel_rdeps(cwd, owners, a.universe) if owners else {}
    label = lambda iri: (f"`{index[iri][0]}` — {index[iri][1].get('title_ko', '')}" if iri in index else f"<{iri}>" + (" (복합체)" if iri in composite_parts else " (없음)"))
    rows, per_chunk = [], []
    for path, kind, iri, meta, base_meta, note in changed:
        m = meta or base_meta
        out_links = links_of(m)
        in_links = [(k, s) for k, s in incoming.get(iri, []) if s != iri]
        if m.get("part_of"):
            in_links += [("part_of(형제)", s) for s in composite_parts.get(m["part_of"], []) if s != iri]
        for k, t in out_links:
            rows.append((path, k, "→", label(t), "frontmatter"))
        for k, s in in_links:
            rows.append((path, k, "←", label(s), "frontmatter"))
        called_by = sorted(callers.get(iri, ())) if kind in ("본문 변경", "삭제") else []
        for caller in called_by:  # 본문이 바뀐 정의를 이름으로 쓰는 출발점 — 코드 호출부 파손의 상한이다
            rows.append((path, USES_KEY, "←", label(caller), "frontmatter uses"))
        direct, trans = rd.get(iri_to_label.get(iri, ""), (None, None)) if kind != "삭제" else ([], [])
        for t in direct or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 직접"))
        for t in trans or []:
            rows.append((path, "deps", "←", f"`{t}`", "bazel rdeps 전이"))
        verified = bool((meta or {}).get("verified"))
        if verified:
            rows.append((path, "verified", "·", "이 청크 자신 — 검증 뒤 본문이 바뀌었다 (writer 검사 대상)", "frontmatter"))
        per_chunk.append((path, kind, m.get("title_ko", ""), len(out_links) + len(in_links), (len(direct or []), len(trans or [])),
                          len(called_by), verified, note))

    # 4. 본문 해시 변경 → 링크 재판정. 본문이 바뀐 청크를 양 끝 중 하나로 갖는 링크 개체가 suspect 로 유도된다 (노트 9.11절)
    body_changed = {iri for _path, kind, iri, _m, _b, _n in changed if kind in ("본문 변경", "변경", "신규", "삭제")}
    objs = link_objects(index, body_changed)

    rep = kb_lib.gendoc_header(
        "revalidate", f"base {a.base} 대비 재판정 대상", "tools/revalidate.py",
        f"base 리비전 `{a.base}` 와 워킹트리 사이에서 본문 해시가 바뀐 청크마다 — (a) frontmatter 링크의 상대(양방향) · "
        "(b) 복합체 형제 · (c) `bazel query rdeps` 의 하류 의존자 · (d) 그 정의를 `uses` 로 가리키는 **호출부** · "
        "(e) 그 청크를 양 끝 중 하나로 갖는 **링크 개체**(`agt:Link`)를 재판정 대상으로 (dependency-graph-design §5). 링크 개체의 상태는 저장하지 않고 여기서 물질화한다",
        f"bazel run //tools:revalidate -- --base {a.base}", [],
        f"변경 청크 {len(changed)} · 재판정 대상 {len(rows)} · 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} · "
        f"재판정 링크 개체 {len(objs)}",
        kb_lib.gendoc_view_notice("각 청크의 본문과 frontmatter 링크"),
        input_note=f"`git show {a.base}:<청크>` 와 워킹트리의 청크 파일, `bazel query` 결과 — 리비전 대비 차이라 지문을 내지 않는다",
        extra=[f"- 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} — 본문이 바뀐 정의를 `uses`(agt:usesDefinition)로 "
               "가리키는 출발점이고 **코드 호출부 파손의 상한**이다. 모듈 안 호출만 세므로 모듈 간 호출은 빠진다",
               f"- head 만 바뀐 청크 {len(head_only)} (본문 해시 동일 — 재판정 대상이 아니다)",
               f"- 본문이 바뀐 청크에 붙은 링크 개체 {len(objs)} — 유도 상태는 `{kb_lib.LINK_STATE_SUSPECT}` 다"])
    body = ["| 변경 청크 | 변경 | 라벨 | 링크(양방향) | 하류(직접/전이) | 호출부 | verified | 비고 |",
            "|---|---|---|---|---|---|---|---|"]
    for path, kind, ko, nl, (nd, nt), nc, v, note in per_chunk:
        body.append(f"| `{path}` | {kind} | {ko or kb_lib.NONE_MARK} | {nl} | {nd}/{nt} | {nc} | "
                    f"{'있음' if v else kb_lib.NONE_MARK} | {note or kb_lib.NONE_MARK} |")  # G14 — 빈 셀을 두지 않는다
    body += ["", "## 재판정 대상", "", "| 변경 청크 | 종류 | 방향 | 상대 | 출처 |", "|---|---|---|---|---|"]
    body += [f"| `{p}` | {k} | {d} | {t} | {src} |" for p, k, d, t, src in rows] or ["| " + " | ".join([kb_lib.NONE_MARK] * 3 + [f"재판정 대상 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body += ["", "## 재판정 대상 링크 개체 — 본문 해시 변경 → 링크 재판정 (노트 9.11절: 상태는 평가 결과다)", "",
             "| 링크 개체 | 종류 | 출발 | 도착 | 바뀐 끝 | 유도 상태 |", "|---|---|---|---|---|---|"]
    body += [f"| `{kb_lib.compact_iri(l)}` | `{k}` | {label(f)} | {label(t)} | {side} | {kb_lib.LINK_STATE_SUSPECT} |"
             for l, k, f, t, side in objs] \
            or ["| " + " | ".join([kb_lib.NONE_MARK] * 4 + [f"재판정 링크 개체 {kb_lib.NONE_MARK}", kb_lib.NONE_MARK]) + " |"]
    body.append("")
    if head_only:
        body += ["head 만 바뀐 청크 (링크 키 변경이 있으면 표시): " + " · ".join(f"`{p}`" + (f" [{', '.join(ks)}]" if ks else "") for p, ks in head_only[:20])
                + (f" … 외 {len(head_only) - 20}" if len(head_only) > 20 else "")]
    if unparsable or unread:
        body += ["판독 불가 파일: " + " · ".join((unparsable + [f"{u}: base 판독 불가" for u in unread])[:10])]
    text = kb_lib.gendoc_assemble(rep, body, [])
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if (rows or objs) else 0
```
<!-- 인용 끝 -->
