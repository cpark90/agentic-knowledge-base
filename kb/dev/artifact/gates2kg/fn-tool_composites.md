---
id: https://agentic-knowledge-base.dev/id/chunk/4023eaae-fb57-4924-bb9b-beb8a2530ff2
type: artifact
level: executable
title_ko: 함수 tool_composites (tools/gates2kg.py)
title: function tool_composites in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T15:47:27Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ff1c5437-57a6-409e-86e7-767ffd3d41ff
---
**함수** — `tool_composites(registries)` 다. 등록부 사이드카들 → 도구 이름 → 파일 복합체 IRI (`ids: file:`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tool_composites(registries: list[str]) -> dict[str, str]:
    """등록부 사이드카들 → 도구 이름 → 파일 복합체 IRI (`ids: file:`).

    사이드카는 손이 원본인 등록부이고 파일 복합체가 도구 하나의 개체다 (p7-code-links-on-file-composite).
    YAML 파서를 싣지 않는다 — 필요한 것은 `ids:` 블록의 `file:` 한 줄뿐이고 이 생성기는 타깃마다 돈다.
    """
    out: dict[str, str] = {}
    for path in registries:
        p = Path(path)
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except OSError as e:
            print(f"FAIL [{TAG}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            raise SystemExit(EXIT_CONFIG)
        name = p.name[: -len(".chunks.yml")] if p.name.endswith(".chunks.yml") else p.stem
        for line in lines:
            if line.startswith("  file:"):
                out[name] = line.split(":", 1)[1].strip()
                break
    return out
```
<!-- 인용 끝 -->
