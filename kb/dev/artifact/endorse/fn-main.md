---
id: https://agentic-knowledge-base.dev/id/chunk/3d2b2b8c-6a17-43ac-bcbd-a2af891dfeb3
type: artifact
level: executable
title_ko: 함수 main (tools/endorse.py)
title: function main in tools/endorse.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-endorse}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-11T09:15:09Z}
part_of: https://agentic-knowledge-base.dev/id/composite/4a01c621-e30b-42ce-9e5d-a8a449270a57
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", required=True, help="<역할>/<모델> — 카탈로그에 있는, 그 plane 을 쓰는 역할")
    ap.add_argument("--at", required=True, help="ISO 8601")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    for f in a.files:
        p = root / f
        t = p.read_text(encoding="utf-8")
        entry = f"{{by: {a.by}, at: {a.at}}}"
        m = re.search(r"^verified: \[(.*)\]$", t, re.M)
        if m:
            if a.by in m.group(1):
                continue
            t = t.replace(m.group(0), f"verified: [{m.group(1)}, {entry}]")
        else:
            t = re.sub(r"^(generated: .*)$", r"\1\nverified: [" + entry + "]", t, count=1, flags=re.M)
        p.write_text(t, encoding="utf-8")
        print(f"{f}: verified by {a.by}")
    return 0
```
<!-- 인용 끝 -->
