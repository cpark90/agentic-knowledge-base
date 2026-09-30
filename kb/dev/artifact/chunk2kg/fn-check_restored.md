---
id: https://agentic-knowledge-base.dev/id/chunk/dae11730-e07f-47c6-becd-61b72a819b12
type: artifact
level: executable
title_ko: 함수 check_restored (tools/chunk2kg.py)
title: function check_restored in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `check_restored(path, meta)` 다. restored: 검사 → 위반 메시지 목록 (게이트 id `restored`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_restored(path: str, meta: dict) -> list:
    """restored: 검사 → 위반 메시지 목록 (게이트 id `restored`). 값은 IRI 목록이고 각 IRI 는 같은 청크의 링크 대상이어야 한다."""
    if RESTORED_KEY not in meta:
        return []
    value = meta[RESTORED_KEY]
    if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
        return [f"{path}: {RESTORED_KEY} 는 링크 대상 IRI 목록 [<IRI>, …] 이어야 한다 — 실제 {value!r}"]
    targets = link_targets(meta)
    return [f"{path}: 복원 표시 {iri} 가 링크 대상에 없다 — {RESTORED_KEY} 의 IRI 는 같은 청크의 링크 키({'·'.join(LINK_KEYS)}) 어딘가의 대상이어야 한다 "
            f"(p10-restored-link-marking)" for iri in value if iri not in targets]
```
<!-- 인용 끝 -->
