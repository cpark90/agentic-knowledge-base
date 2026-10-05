---
id: https://agentic-knowledge-base.dev/id/chunk/14a19009-1b05-4621-b253-ce8233be9f19
type: artifact
level: executable
title_ko: 함수 load_scenario (tools/case_gen.py)
title: function load_scenario in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a, https://agentic-knowledge-base.dev/id/chunk/d4776922-4147-4da3-a80b-caafc1acc6ac]
part_of: https://agentic-knowledge-base.dev/id/composite/10ce940e-ae6b-4b2e-8d0e-3bb5448ae88e
---
**함수** — `load_scenario(path)` 다. 자극 청크 → {path, slug, iri, at, sources, assumes, spec}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_scenario(path: Path) -> dict:
    """자극 청크 → {path, slug, iri, at, sources, assumes, spec}. logical `decision` 이 아니거나 입력 펜스가 없으면 거부한다."""
    meta, body = parse_chunk(str(path))
    if meta["type"] != "decision" or meta["level"] != "logical":
        raise CaseGenError(f"{path}: 케이스의 입력은 logical 시나리오(`decision`·`logical`)다 — 실제 {meta['type']}·{meta['level']} "
                           f"(p8-scenario-ladder-rungs: 변수 범위는 logical 높이에서 채운다)")
    fences = [f for f in vv_run.yaml_blocks(body) if all(h.search(f) for h in INPUT_HEAD)]
    if len(fences) != 1:
        raise CaseGenError(f"{path}: `keep`·`cover` 를 담은 `yaml` 펜스가 {len(fences)}개다 — 시나리오 하나에 하나다")
    try:
        spec = yaml.safe_load(fences[0])
    except yaml.YAMLError as e:
        raise CaseGenError(f"{path}: 입력 펜스를 읽을 수 없다 — {e}") from e
    raw = raw_frontmatter(path.read_text(encoding="utf-8"))
    at = re.search(r"\bat:\s*([^,}\s]+)", raw.get("generated", ""))
    if not at:
        raise CaseGenError(f"{path}: generated.at 이 없다 — 케이스의 생성 시각은 입력 시나리오의 시각이다(재생성이 바이트로 같아야 한다)")
    slug = path.stem[: -len(STIMULUS_SUFFIX)] if path.stem.endswith(STIMULUS_SUFFIX) else path.stem
    return {"path": path, "slug": slug, "iri": meta["id"], "at": at.group(1), "sources": raw.get("sources", ""),
            "assumes": raw.get("assumes", ""), "spec": spec}
```
<!-- 인용 끝 -->
