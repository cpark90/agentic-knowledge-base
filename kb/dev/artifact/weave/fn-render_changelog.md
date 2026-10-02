---
id: https://agentic-knowledge-base.dev/id/chunk/18d615ae-85a5-4737-825a-7674dc3b3ce9
type: artifact
level: executable
title_ko: 함수 render_changelog (tools/weave.py)
title: function render_changelog in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/8330a4d7-2140-46ed-b107-9196a6c03aa2
---
**함수** — `render_changelog(m, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_changelog(m: Model, inputs: list[str]) -> str:
    pairs = []
    for new, old in m.g.subject_objects(AGT.supersedes):
        at = m.at(new)
        try:
            key = datetime.fromisoformat(at)
        except ValueError:
            key = datetime.max
        if key.tzinfo is None:  # 시간대 없는 값은 UTC 로 본다 — 정렬 키의 비교 가능성만 위한 것
            key = key.replace(tzinfo=timezone.utc)
        pairs.append((key, m.ko(new), new, old, at))
    pairs.sort(key=lambda p: (p[0], p[1], str(p[2]), str(p[3])))
    revisions = sorted(m.g.subject_objects(PROV.wasRevisionOf), key=lambda so: (str(so[0]), str(so[1])))
    o = head("changelog", "변경 이력", "`agt:supersedes` 쌍(새 → 옛)을 새 결정의 `prov:generatedAtTime` 순으로 · `prov:wasRevisionOf` 쌍 전부", m.g, inputs,
             [f"- supersedes {len(pairs)}쌍 · wasRevisionOf {len(revisions)}쌍"])
    body = ["## supersedes — 새 결정이 옛 결정을 대체한 순서", "",
          "| 시각 (새 결정 generated.at) | 새 결정 | 자리 | 옛 결정 | 옛 상태 |", "|---|---|---|---|---|"]
    for _, label, new, old, at in pairs:
        body.append(f"| {at} | {label} | `{m.unit_ref(m.decision_unit(new))}` | {m.ko(old)} (`{kb_lib.compact_iri(str(old))}`) | `{m.status.get(old, '?')}` |")
    body += ["", "## wasRevisionOf — 같은 정체성의 개정", ""]
    if revisions:
        body += ["| 개정 | 이전 |", "|---|---|"] + [f"| {m.ko(s)} (`{kb_lib.compact_iri(str(s))}`) | {m.ko(t)} (`{kb_lib.compact_iri(str(t))}`) |" for s, t in revisions] + [""]
    else:
        body += [f"{kb_lib.NONE_MARK} — 개정은 아직 `supersedes`(새 IRI)로만 기록됐다", ""]
    return kb_lib.gendoc_assemble(o, body, inputs)
```
<!-- 인용 끝 -->
