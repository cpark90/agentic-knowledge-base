---
id: https://agentic-knowledge-base.dev/id/chunk/d2c6d26d-171a-421d-93af-57b68ab462fc
type: artifact
level: executable
title_ko: 함수 main (tools/handoff.py)
title: function main in tools/handoff.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-handoff}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-11T09:15:09Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/0b8984a8-4b3a-4b30-9c38-041302b18093
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workset", required=True)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    read_set = re.findall(r"<!-- iri: (\S+) -->", Path(a.workset).read_text(encoding="utf-8"))
    if not read_set:
        raise SystemExit("handoff: 작업 집합에 펼친 청크가 없다 — 앵커를 주고 다시 만들어라")
    for f in a.files:
        text = Path(f).read_text(encoding="utf-8")
        m = re.search(r"^sources: \[(.*)\]$", text, re.M)
        existing = re.findall(r"resource: (\S+?)[,}]", m.group(1)) if m else []
        merged = existing + [r for r in read_set if r not in existing]
        line = "sources: [" + ", ".join("{resource: " + r + "}" for r in merged) + "]"
        text = text.replace(m.group(0), line) if m else text.replace("\ngenerated:", "\n" + line + "\ngenerated:", 1)
        Path(f).write_text(text, encoding="utf-8")
        print(f"{f}: sources {len(existing)} → {len(merged)}")
    return 0
```
<!-- 인용 끝 -->
