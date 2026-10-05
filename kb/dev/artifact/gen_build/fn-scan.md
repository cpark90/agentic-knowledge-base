---
id: https://agentic-knowledge-base.dev/id/chunk/ad68f79e-bbb2-4a80-b6c8-518fdd88a3a2
type: artifact
level: executable
title_ko: 함수 scan (tools/gen_build.py)
title: function scan in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551, https://agentic-knowledge-base.dev/id/chunk/2d509ef2-a992-4376-8863-e6f4bd1edce1, https://agentic-knowledge-base.dev/id/chunk/7e58cd2b-ecf9-4a21-a66b-9e28aa4474e9, https://agentic-knowledge-base.dev/id/chunk/be13ce99-9dc5-4abe-8367-5558f1aa4b02]
part_of: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd
---
**함수** — `scan(root)` 다. 청크 파일 → (메타, 패키지, 타깃 이름).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def scan(root: Path):
    """청크 파일 → (메타, 패키지, 타깃 이름). IRI → 라벨 사상을 만든다."""
    items = {}  # label -> dict
    iri_to_label = {}
    for f in sorted((root / "kb/dev/requirement").glob("*.md")):
        meta, _ = parse_item(str(f))
        lab = f"//kb/dev/requirement:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "kb/dev/requirement"}
        iri_to_label[meta["id"]] = lab
    for d in sorted(p for p in (root / "kb/dev/decision").iterdir() if p.is_dir()):
        parts = {n: parse_item(str(d / f"{n}.md"))[0] for n in ("conclusion", "rationale", "alternatives") if (d / f"{n}.md").exists()}
        if set(parts) != {"conclusion", "rationale", "alternatives"}:
            raise GenBuildError(f"{d}: 결론·근거·대안 세 청크가 있어야 한다 (7.4절 대안 기록) — 있는 것: {sorted(parts)}")
        opt = d / f"{DECISION_OPTIONAL_PART}.md"
        if opt.exists():  # 규약 청크 — 세 청크 검사는 그대로이고 넷째는 선택이다 (p4-convention-slot)
            parts[DECISION_OPTIONAL_PART] = parse_item(str(opt))[0]
            if parts[DECISION_OPTIONAL_PART]["type"] != "decision":
                raise GenBuildError(f"{opt}: 규약 청크는 type: decision 이다 — 실제 {parts[DECISION_OPTIONAL_PART]['type']!r} (p4-convention-slot)")
        comp = parts["conclusion"].get("composite") or {}
        lab = f"//kb/dev/decision:{d.name}"
        items[lab] = {"kind": "decision", "parts": parts, "dir": d.name, "pkg": "kb/dev/decision", "comp_iri": comp.get("id", "")}
        for m in parts.values():
            iri_to_label[m["id"]] = lab
        if comp.get("id"):
            iri_to_label[comp["id"]] = lab
    for f in sorted((root / "chunks/decision").glob("*.md")):
        meta, _ = parse_item(str(f))
        lab = f"//chunks/decision:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "chunks/decision"}
        iri_to_label[meta["id"]] = lab
    for f in sorted((root / MEMORY_PKG).glob("*.md")):  # 관측 (memory plane, append-only) — assume_check --record 가 만든다
        meta, _ = parse_item(str(f))
        if meta["type"] != "memory":
            raise GenBuildError(f"{f}: {MEMORY_PKG} 의 청크는 type: memory 여야 한다 — 실제 {meta['type']!r} (수준 허용표 6.4절)")
        lab = f"//{MEMORY_PKG}:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": MEMORY_PKG}
        iri_to_label[meta["id"]] = lab
    for d in sorted(p for p in (root / ARTIFACT_ROOT).iterdir() if p.is_dir()) if (root / ARTIFACT_ROOT).is_dir() else []:
        pkg = f"{ARTIFACT_ROOT}/{d.name}"  # 추출된 코드 청크 — 소스 파일 하나 = 패키지 하나 (tools/extract.py 의 생성물)
        for f in sorted(d.glob("*.md")):
            meta, _ = parse_item(str(f))
            if meta["type"] != "artifact":
                raise GenBuildError(f"{f}: {ARTIFACT_ROOT}/ 의 청크는 type: artifact 여야 한다 — 실제 {meta['type']!r} "
                                    f"(추출된 코드 청크, p7-code-extraction-direction)")
            lab = f"//{pkg}:{f.stem}"
            items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": pkg}
            iri_to_label[meta["id"]] = lab
    for d in norm_pkgs(root):  # 규범 문서의 절 청크 — 문서 하나 = 패키지 하나 (p12-norm-documents-from-section-chunks)
        pkg = f"{NORM_ROOT}/{d}"
        for f in sorted((root / pkg).glob("*.md")):
            meta, _ = parse_item(str(f))
            if meta["type"] != NORM_TYPE:
                raise GenBuildError(f"{f}: {NORM_ROOT}/ 의 청크는 type: {NORM_TYPE} 이어야 한다 — 실제 {meta['type']!r} "
                                    f"(절 청크, p12-norm-documents-from-section-chunks)")
            lab = f"//{pkg}:{f.stem}"
            items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": pkg}
            iri_to_label[meta["id"]] = lab
    for sub, plane in VV_PKGS.items():  # V&V KB — 디렉토리가 plane 을 정한다. 없는 디렉토리는 빈 패키지다
        pkg = f"{VV_ROOT}/{sub}"
        for f in sorted((root / pkg).glob("*.md")):
            meta, _ = parse_item(str(f))
            if meta["type"] != plane:
                raise GenBuildError(f"{f}: {pkg} 의 청크는 type: {plane} 이어야 한다 — 실제 {meta['type']!r} (V&V KB 의 plane 실체, 결정 p8-vv-plane-instances)")
            lab = f"//{pkg}:{f.stem}"
            items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": pkg}
            iri_to_label[meta["id"]] = lab
    return group_composites(items, iri_to_label)  # 청크 전부를 본 뒤에 묶는다 — 묶음은 패키지 × composite.id 다
```
<!-- 인용 끝 -->
