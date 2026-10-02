---
id: https://agentic-knowledge-base.dev/id/chunk/5e22443d-209f-4479-a064-9c08165f38f4
type: artifact
level: executable
title_ko: 함수 base_diff (tools/revalidate.py)
title: function base_diff in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0deeb79a-02b2-44fa-9441-ad82b1ed51af, https://agentic-knowledge-base.dev/id/chunk/1d01a493-eef5-4980-970b-5ba70be5e80e]
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `base_diff(base, cwd, index)` 다. base 리비전과 워킹트리의 차이 → (changed, head_only, base_by_iri, unread).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def base_diff(base: str, cwd: str, index: dict) -> tuple:
    """base 리비전과 워킹트리의 차이 → (changed, head_only, base_by_iri, unread).

    비교의 열쇠도 IRI 다 — 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부푼다.
    `changed` 는 (경로, 종류, iri, meta_wt|None, meta_base|None, 사유) 이고 `head_only` 는 본문 해시가 같은 것이다.
    """
    a_base = base
    # 2. base 와의 차이 — 상태 M/A/D/R 인 청크 파일 + 미추적 파일
    status = {}
    for line in run(["git", "diff", "--name-status", a_base, "--", *CHUNK_DIRS], cwd).splitlines():
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
        txt = run(["git", "show", f"{a_base}:{base_path}"], cwd, check=False)
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
    return changed, head_only, base_by_iri, unread
```
<!-- 인용 끝 -->
