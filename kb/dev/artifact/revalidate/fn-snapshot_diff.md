---
id: https://agentic-knowledge-base.dev/id/chunk/66bcf711-ad13-41b9-bbcb-519f83fd163f
type: artifact
level: executable
title_ko: 함수 snapshot_diff (tools/revalidate.py)
title: function snapshot_diff in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f6f22e05-67fd-4351-a17e-d9abe0817b50
---
**함수** — `snapshot_diff(base_index, base_unparsable, index, addressed)` 다. 스냅숏 둘의 차이 → (changed, head_only, base_by_iri, unread) — `base_diff` 와 같은 꼴이고 열쇠도 IRI 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def snapshot_diff(base_index: dict, base_unparsable: list, index: dict, addressed: bool) -> tuple:
    """스냅숏 둘의 차이 → (changed, head_only, base_by_iri, unread) — `base_diff` 와 같은 꼴이고 열쇠도 IRI 다.

    git 이 고른 변경 파일이 없으므로 양쪽 IRI 전부를 맞춘다. `head_only` 에는 본문 해시가 같고 링크 키나 주소가 바뀐 것만
    든다 — 바뀌지 않은 청크까지 넣으면 "head 만 바뀐 청크" 가 스냅숏 전체가 된다. `addressed` 가 거짓(파일 목록)이면 경로는
    주소가 아니라서 경로 변경을 보고하지 않는다.
    """
    base_by_iri = dict(base_index)
    unread = [u.split(":", 1)[0] for u in base_unparsable]
    changed, head_only = [], []
    for iri in sorted(set(index) | set(base_by_iri)):
        wt, base = index.get(iri), base_by_iri.get(iri)
        if wt is None:
            changed.append((base[0], "삭제", iri, None, base[1], "이 IRI 를 가리키는 링크는 깨진다"))
            continue
        path, meta = wt
        if base is None:
            changed.append((path, "신규", iri, meta, None, "base 에 이 IRI 가 없다"))
            continue
        base_path, base_meta = base
        moved = f"경로 변경(라벨 변경) `{base_path}` → `{path}`" if addressed and base_path != path else ""
        if meta["_content_hash"] != base_meta["_content_hash"]:
            changed.append((path, "본문 변경", iri, meta, base_meta,
                            " · ".join(x for x in (f"{base_meta['_content_hash']} → {meta['_content_hash']}", moved) if x)))
            continue
        keys = sorted(k for k in LINK_KEYS + ("part_of",) if (meta.get(k) or None) != (base_meta.get(k) or None))
        if keys or moved:
            head_only.append((path, keys + ([moved] if moved else [])))
    return changed, head_only, base_by_iri, unread
```
<!-- 인용 끝 -->
