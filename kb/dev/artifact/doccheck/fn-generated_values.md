---
id: https://agentic-knowledge-base.dev/id/chunk/6d777811-ef05-4ecd-a3c1-78c66baba749
type: artifact
level: executable
title_ko: 함수 generated_values (tools/doccheck.py)
title: function generated_values in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/dbdeebe3-848d-4908-81dc-0c291b07bbe2]
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `generated_values(root)` 다. 이름 → [(원문, 키, 생성물)] · 읽지 못한 생성물 목록 · 그 미빌드 때문에 값을 못 얻은 이름의 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def generated_values(root: Path) -> tuple[dict, list[str], set[str]]:
    """이름 → [(원문, 키, 생성물)] · 읽지 못한 생성물 목록 · 그 미빌드 때문에 값을 못 얻은 이름의 집합."""
    text, missing = {}, []
    for key, rel in VIEW_PATHS.items():
        try:
            text[key] = (root / rel).read_text(encoding="utf-8")
        except OSError:
            missing.append(rel)
    values, skipped = {}, set()
    for label, _doc_re, sources in NUMBER_NAMES:
        found = []
        for src, pattern in sources:
            m = re.search(pattern, text.get(src, ""))
            if m:
                found.append((m.group(1), num_key(NUM_TOKEN.match(m.group(1))), src))
        values[label] = found
        if sources and not found and any(src not in text for src, _ in sources):
            skipped.add(label)
    return values, missing, skipped
```
<!-- 인용 끝 -->
