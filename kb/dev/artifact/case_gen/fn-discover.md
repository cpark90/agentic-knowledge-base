---
id: https://agentic-knowledge-base.dev/id/chunk/006ec0fb-bfe1-4695-9abf-423664b5532d
type: artifact
level: executable
title_ko: 함수 discover (tools/case_gen.py)
title: function discover in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/10ce940e-ae6b-4b2e-8d0e-3bb5448ae88e
---
**함수** — `discover(root)` 다. `kb/vv/scenario/` 의 logical 자극 청크 중 입력 펜스가 있는 것 — 생성 모드에서 --scenario 가 없을 때의 대상이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def discover(root: Path) -> list[Path]:
    """`kb/vv/scenario/` 의 logical 자극 청크 중 입력 펜스가 있는 것 — 생성 모드에서 --scenario 가 없을 때의 대상이다."""
    out = []
    for p in sorted((root / SCENARIO_DIR).glob("*.md")):
        meta, body = parse_chunk(str(p))
        if meta["type"] == "decision" and meta["level"] == "logical" and any(
                all(h.search(f) for h in INPUT_HEAD) for f in vv_run.yaml_blocks(body)):
            out.append(p)
    return out
```
<!-- 인용 끝 -->
