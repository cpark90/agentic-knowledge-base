---
id: https://agentic-knowledge-base.dev/id/chunk/082fbbdd-904c-4476-b773-8ebe8a85418e
type: artifact
level: executable
title_ko: 함수 rebase_links (tools/gen_norms.py)
title: function rebase_links in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:27:34Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0ad37658-cf36-48b8-923d-769303f455d1]
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `rebase_links(text, src, out)` 다. 청크(`src`, 루트 상대) 기준 상대 링크 → 출력(`out`) 기준.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def rebase_links(text: str, src: str, out: str) -> str:
    """청크(`src`, 루트 상대) 기준 상대 링크 → 출력(`out`) 기준. 링크 밖의 코드 스팬·펜스 안, 절대 URL, 문서 안 앵커는 그대로다."""
    src_dir, out_dir = os.path.dirname(src), os.path.dirname(out) or "."

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if URL_SCHEME.match(target) or target.startswith(("#", "/")):
            return m.group(0)
        path, sep, anchor = target.partition("#")
        new = os.path.relpath(os.path.normpath(os.path.join(src_dir, path)), out_dir).replace(os.sep, "/")
        return m.group(1) + new + sep + anchor + m.group(3)

    # 펜스 밖은 문단 단위로 읽는다 — 코드 스팬은 문단 안에서 줄을 넘을 수 있으므로(CommonMark 6.1) 줄 단위로 읽으면 다음 줄에서
    # 닫히는 백틱이 뒤의 링크 텍스트 안 백틱과 짝지어져 링크가 다시 계산되지 않는다
    lines, para, fence = [], [], None

    def flush() -> None:
        if para:
            lines.extend(_rebase_line("\n".join(para), fix).split("\n"))
            para.clear()

    for line in text.split("\n"):
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            lines.append(line)
            continue
        if m:
            flush()
            fence = m.group(1)
            lines.append(line)
            continue
        if not line.strip():
            flush()
            lines.append(line)
            continue
        para.append(line)
    flush()
    return "\n".join(lines)
```
<!-- 인용 끝 -->
