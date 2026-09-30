---
id: https://agentic-knowledge-base.dev/id/chunk/ed7fa3c5-2a34-4aaf-9cd1-e9f6e86d8e1f
type: artifact
level: executable
title_ko: 함수 decision_section (tools/weave.py)
title: function decision_section in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ec24ef39-7e27-4fff-bba3-6fdb1829b342
---
**함수** — `decision_section(m, bodies, root, level, title, ref, parts, levels_note, comp_line)` 다. 결정 하나의 절 — 복합체(세 부분)와 단일 파일(부분 하나)이 같은 형식이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_section(m: Model, bodies: dict, root: Path, level: str, title: str, ref: str, parts: list, levels_note: str, comp_line: str) -> list[str]:
    """결정 하나의 절 — 복합체(세 부분)와 단일 파일(부분 하나)이 같은 형식이다. 본문은 --bodies 에서, 없으면 --root 아래 assertionLocation 에서 읽는다."""
    con = parts[0]
    refines = sorted({t for p in parts for t in m.g.objects(p, AGT.refines)} | {t for p in parts for t in m.g.objects(p, AGT.serves)}, key=str)
    sources = sorted({t for p in parts for t in m.g.objects(p, PROV.wasDerivedFrom)}, key=str)
    assumes = sorted({t for p in parts for t in m.g.objects(p, AGT.assumes)}, key=str)
    o = [f"{level} {title}", "",
         f"- 영문: {m.en(con)} {kb_lib.GENDOC_QUOTE_LINE}",  # 라벨은 그래프에서 그대로 가져온 값이다 — 생성기가 고쳐 쓰지 않는다
         f"- 결정: `{ref}`{comp_line} · 상태 `{m.status[con]}` · 수준 {m.level[con]}{levels_note}",
         f"- 생성: {m.at(con)} ({next(m.g.objects(con, AGT.generatedBy), '')})",
         f"- 정제하는 요구: {refs(m, refines)}",
         f"- 대체한 결정: {supersedes_chain(m, parts)}",
         "- 출처: " + (" · ".join(source_ref(m, s) for s in sources) or "없음"),
         f"- 가정: {refs(m, assumes)}", ""]
    for p in parts:
        body = bodies.get(str(p))
        if body is None:
            f = root / m.location[p]
            body = kb_lib.chunk_body(f.read_text(encoding="utf-8")) if f.is_file() else f"본문 {kb_lib.NONE_MARK} — `{m.location[p]}` 가 --bodies 에도 --root 아래에도 없다"
        o += kb_lib.gendoc_quote(body)
    return o
```
<!-- 인용 끝 -->
