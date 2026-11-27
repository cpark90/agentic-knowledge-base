---
id: https://agentic-knowledge-base.dev/id/chunk/fc1144d8-e0cf-4dc0-a8f5-0d9822fb0334
type: artifact
level: executable
title_ko: 함수 load_citing (tools/weave.py)
title: function load_citing in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `load_citing(paths)` 다. 단위 지식·설계 공간 파일들 → [(저장소 상대 경로, frontmatter type, 본문)] 경로 순.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_citing(paths: list[str]) -> list[tuple[str, str, str]]:
    """단위 지식·설계 공간 파일들 → [(저장소 상대 경로, frontmatter type, 본문)] 경로 순. frontmatter 는 chunk2kg 의 파서로 읽는다."""
    out = []
    for p in paths:
        if p.endswith(".md"):
            meta, _ = parse_chunk(p)
            out.append((kb_lib.gendoc_input_name(p), str(meta.get("type", "")), kb_lib.chunk_body(Path(p).read_text(encoding="utf-8"))))
    return sorted(out)
```
<!-- 인용 끝 -->
