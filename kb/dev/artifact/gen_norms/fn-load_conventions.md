---
id: https://agentic-knowledge-base.dev/id/chunk/412335c9-3334-4503-8547-23227e453d66
type: artifact
level: executable
title_ko: 함수 load_conventions (tools/gen_norms.py)
title: function load_conventions in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41, https://agentic-knowledge-base.dev/id/chunk/eb4346c1-beed-427d-8e9d-767bc87f2e0b]
part_of: https://agentic-knowledge-base.dev/id/composite/55330362-0aaf-42fe-bd7b-4cfec40c4e75
---
**함수** — `load_conventions(root)` 다. 결정 slug → {path, lines: [(강도 또는 None, 문장)…], live}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_conventions(root: Path) -> dict[str, dict]:
    """결정 slug → {path, lines: [(강도 또는 None, 문장)…], live}. 규약 청크가 없는 결정은 `path` 가 None 이다.

    줄 순번 k 는 `lines` 의 1부터의 색인이다. 펜스 안의 `규약:` 은 예시이지 줄이 아니다. deprecated 규약 청크는 살아 있지
    않다 — 그 줄은 고아가 아니고 가리켜도 안 된다.
    """
    out: dict[str, dict] = {}
    base = root / DECISION_ROOT
    for d in sorted(p for p in base.iterdir() if p.is_dir()) if base.is_dir() else []:
        entry = {"path": None, "lines": [], "live": False, "linkable": (d / CONCLUSION_FILE).is_file()}
        f = d / CONVENTIONS_FILE
        if f.is_file():
            meta, body = parse_chunk(str(f))
            if meta["type"] != "decision":
                raise GenNormsError(f"{rel(root, f)}: 규약 청크는 type: decision 이다 — 실제 {meta['type']!r} (p4-convention-slot)")
            fence = None
            for line in body.splitlines():
                m = BODY_FENCE.match(line)
                if fence:
                    if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                        fence = None
                    continue
                if m:
                    fence = m.group(1)
                    continue
                cm = CONVENTION_LINE.match(line)
                if not cm:
                    continue
                sm = STRENGTH.match(cm.group(1))
                entry["lines"].append((sm.group(1), sm.group(2)) if sm else (None, cm.group(1)))
            entry.update(path=rel(root, f), live=meta["status"] != "deprecated")
        out[d.name] = entry
    return out
```
<!-- 인용 끝 -->
