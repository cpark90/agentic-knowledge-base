---
id: https://agentic-knowledge-base.dev/id/chunk/3abf45b4-eb13-4c63-80e4-83848c227928
type: artifact
level: executable
title_ko: 함수 render_requirements (tools/weave.py)
title: function render_requirements in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/8330a4d7-2140-46ed-b107-9196a6c03aa2
---
**함수** — `render_requirements(m, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_requirements(m: Model, inputs: list[str]) -> str:
    reqs = sorted((c for c in m.chunks if m.plane[c] == "requirement" and m.live(c)), key=lambda c: m.location[c])
    down = defaultdict(set)  # metrics.py CQ19 와 같은 정의 — refines/serves 를 거꾸로 내려간다
    for pred in (AGT.refines, AGT.serves):
        for s, t in m.g.subject_objects(pred):
            down[t].add(s)

    def deepest(r) -> str:
        seen, stack, best = set(), [r], -1
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            if x in m.level and m.level[x] in LEVELS:
                best = max(best, LEVELS.index(m.level[x]))
            stack.extend(down.get(x, ()))
        return LEVELS[best] if best >= 0 else "none"

    def refining_decisions(r) -> int:
        units = set()
        for s in down.get(r, ()):
            if m.plane.get(s) == "decision":
                unit = m.decision_unit(s)
                roles = m.decision_roles(unit) if unit not in m.chunks else {}
                alive = m.status[roles["conclusion"]] != "deprecated" if roles else m.live(s)
                if alive:
                    units.add(unit)
        return len(units)

    rows, patterns, reach = [], Counter(), Counter()
    for r in reqs:
        pat = next(m.g.objects(r, AGT.pattern), None)
        pat_s = PATTERN_VALUE.get(pat, str(pat).split("/")[-1]) if pat is not None else kb_lib.NONE_MARK
        d, n = deepest(r), refining_decisions(r)
        patterns[pat_s] += 1
        reach[d] += 1
        rows.append(f"| `{Path(m.location[r]).stem}` | {m.ko(r)} | {m.en(r)} | {pat_s} | {n} | {d} | `{kb_lib.compact_iri(str(r))}` |")
    o = head("requirements", "요구 색인", "살아 있는 `agt:RequirementChunk` 마다 라벨 ko·en · `agt:pattern` · 이 요구를 `agt:refines`/`agt:serves` 하는 살아 있는 결정 단위 수 "
             "· `refines`/`serves` 하류의 가장 낮은 level (metrics CQ19 와 같은 정의) · IRI", m.g, inputs,
             [f"- 요구 {len(reqs)} · EARS 패턴: " + (" · ".join(f"{k} {v}" for k, v in patterns.most_common()) or "없음")
              + " · 도달 수준: " + " · ".join(f"{k} {v}" for k, v in sorted(reach.items(), key=lambda kv: LEVELS.index(kv[0]) if kv[0] in LEVELS else 99))
              + f" · 정제 결정 없는 요구 {sum(1 for row in rows if '| 0 |' in row)}"])
    body = ["| 파일 | 요구 | title | EARS | 정제 결정 | 도달 수준 | IRI |", "|---|---|---|---|---|---|---|"] + rows + [""]
    return kb_lib.gendoc_assemble(o, body, inputs)
```
<!-- 인용 끝 -->
