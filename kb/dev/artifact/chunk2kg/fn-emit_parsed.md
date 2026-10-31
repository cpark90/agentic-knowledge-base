---
id: https://agentic-knowledge-base.dev/id/chunk/321d9509-8da2-4406-9fa3-a287cafc8d55
type: artifact
level: executable
title_ko: 함수 emit_parsed (tools/chunk2kg.py)
title: function emit_parsed in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/260d24aa-5aab-4ff7-81b7-40def184e51f, https://agentic-knowledge-base.dev/id/chunk/53335074-67d7-45c8-b564-78065ea96eb8, https://agentic-knowledge-base.dev/id/chunk/8c16b743-c8b1-4799-9c5b-5b003686ac07, https://agentic-knowledge-base.dev/id/chunk/c313808a-9a95-42a4-8ca1-8ffe3e2e8e65, https://agentic-knowledge-base.dev/id/chunk/e40d0ed3-5060-4b0e-9dd9-d76acde18c0e]
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `emit_parsed(parsed, conventions, enc, errors)` 다. 읽은 단위 지식 (경로, 메타, 본문) → head 블록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_parsed(parsed: list, conventions: dict, enc, errors: list) -> list:
    """읽은 단위 지식 (경로, 메타, 본문) → head 블록. 절 항목이 줄을 싣는 결정의 IRI 를 모르면 방출하지 않고 `errors` 에 더한다."""
    blocks, graves = [], {}  # graves: 묘비 IRI → (블록, 선언한 경로) — 여러 항목이 같은 묘비를 선언하면 한 번만 낸다
    for path, meta, body in parsed:
        for t in meta.get("_tombstones") or []:
            block = emit_tombstone(t)
            if t["id"] in graves:
                if graves[t["id"]][0] != block:
                    errors.append(f"{path}: 묘비 {t['id']} 의 선언이 {graves[t['id']][1]} 와 다르다 — 같은 지운 항목의 라벨·위치는 하나다 (Q-0061#Q146)")
                continue
            graves[t["id"]] = (block, path)
            blocks.append((t["id"], block))
        missing = [sl for sl in norm_item_slugs(meta.get("_norm_items") or [], links=False) if sl not in conventions]
        if missing:
            errors.append(f"{path}: items 가 가리키는 결정 {missing} 의 복합체 IRI 를 모른다 — 생성 BUILD 의 kb_composite.conventions "
                          f"(--convention-target slug=IRI)가 넘기지 않았다. 결정 디렉토리 이름을 확인하고 tools/gen_build.py 를 다시 돌린다")
            continue
        blocks.append((meta["id"], emit_chunk(path, meta, token_count(body, enc), conventions)))
        blocks.extend(emit_links(meta))
    return blocks
```
<!-- 인용 끝 -->
