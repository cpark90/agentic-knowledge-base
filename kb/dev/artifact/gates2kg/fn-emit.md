---
id: https://agentic-knowledge-base.dev/id/chunk/5626d1aa-8b86-4c12-ab4c-ec1e76b25bb5
type: artifact
level: executable
title_ko: 함수 emit (tools/gates2kg.py)
title: function emit in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T16:06:51Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f15f1ad5-6a97-49e0-a1b6-d7cc84dd3b8e]
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
---
**함수** — `emit(gates, tiers, layer, tools, outside, where)` 다. 게이트 등록부 → TTL.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit(gates: dict, tiers: tuple, layer: str, tools: dict[str, str], outside: tuple, where: str) -> str:
    """게이트 등록부 → TTL. 키·계층의 위반과 판정 도구의 부재는 생성 시점에 거부한다."""
    errors = []
    blocks = []
    for gate_id in sorted(gates):
        spec = gates[gate_id]
        missing = [k for k in ("tier", "tool", "ko", "desc") if not spec.get(k)]
        if missing:
            errors.append(f"{where}: 게이트 {gate_id!r} 에 {', '.join(missing)} 가 없다")
            continue
        if spec["tier"] not in tiers:
            errors.append(f"{where}: 게이트 {gate_id!r} 의 계층 {spec['tier']!r} 이 어휘 밖이다 — {list(tiers)} 중 하나다")
            continue
        props = [
            "a agt:Gate",
            f'rdfs:label "{escape(gate_id)}"@en , "{escape(spec["ko"])}"@ko',
            f'skos:definition "{escape(spec["desc"])}"@ko',
            f"agt:inLayer {LAYER_INDIVIDUAL % layer}",
            f"agt:gateTier {TIER_INDIVIDUAL % spec['tier']}",
        ]
        if spec["tool"] not in outside:
            iri = tools.get(spec["tool"])
            if not iri:
                errors.append(f"{where}: 게이트 {gate_id!r} 의 판정 도구 {spec['tool']!r} 의 파일 복합체를 찾을 수 없다 — "
                              f"tools/{spec['tool']}.chunks.yml 의 `ids: file:` 가 agt:enforcedBy 의 대상이다")
                continue
            props.append(f"agt:enforcedBy <{iri}>")
        head = f"id:{kb_lib.GATE_ID_PREFIX}{gate_id} {props[0]}"
        blocks.append(" ;\n    ".join([head] + props[1:]) + " .")
    if errors:
        print("\n".join(f"FAIL [{TAG}] {e}" for e in errors), file=sys.stderr)
        raise SystemExit(EXIT_FAIL)
    return HEADER + "\n" + "\n\n".join(blocks) + "\n"
```
<!-- 인용 끝 -->
