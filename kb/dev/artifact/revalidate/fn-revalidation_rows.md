---
id: https://agentic-knowledge-base.dev/id/chunk/74004d79-dc3f-461f-85e1-3e42bfe1a332
type: artifact
level: executable
title_ko: 함수 revalidation_rows (tools/revalidate.py)
title: function revalidation_rows in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/98b89c74-895c-4fc5-94d8-8db422c2b0f4, https://agentic-knowledge-base.dev/id/chunk/cf1b3c55-9f8f-446c-87d0-87ab5c66320f, https://agentic-knowledge-base.dev/id/chunk/e7c83ee2-f6d7-442d-98f1-d053996cdfd4]
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `revalidation_rows(root, cwd, universe, changed, index, incoming, composite_parts, callers)` 다. 재판정 대상 → (rows, per_chunk, label, iri_to_label).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def revalidation_rows(root: Path, cwd: str, universe: str, changed: list, index: dict, incoming: dict,
                      composite_parts: dict, callers: dict) -> tuple:
    """재판정 대상 → (rows, per_chunk, label, iri_to_label).

    대상은 다섯이다 — frontmatter 링크 양방향 · 복합체 형제 · `uses` 호출부 · `bazel rdeps` 의 하류 · 도장.
    """
    # 3. 재판정 대상 — (a) frontmatter 링크 양방향 (b) bazel rdeps
    iri_to_label = owner_labels(root)
    owners = sorted({iri_to_label[iri] for _p, kind, iri, *_ in changed if kind != "삭제" and iri in iri_to_label})
    rd = bazel_rdeps(cwd, owners, universe) if owners else {}
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
    return rows, per_chunk, label, iri_to_label
```
<!-- 인용 끝 -->
