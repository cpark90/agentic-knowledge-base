---
id: https://agentic-knowledge-base.dev/id/chunk/eca585ee-464a-4c02-a09c-f68a54900ecb
type: artifact
level: executable
title_ko: 함수 check_names (tools/channel_lint.py)
title: function check_names in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898, https://agentic-knowledge-base.dev/id/chunk/0d94f5a5-2678-4f1b-9143-2847818c4669]
part_of: https://agentic-knowledge-base.dev/id/composite/30c94888-c0b3-4616-8c73-db2b38068fb2
---
**함수** — `check_names(it, names, former)` 다. 식별자 옆 한글 이름 — `created` 가 NAMES_SINCE 이상인 항목에서, KB 항목으로 풀리는 백틱 토큰의 줄에 그 한글 이름이 있는가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_names(it: dict, names: dict, former: bool = True) -> list[str]:
    """식별자 옆 한글 이름 — `created` 가 NAMES_SINCE 이상인 항목에서, KB 항목으로 풀리는 백틱 토큰의 줄에 그 한글 이름이 있는가.

    former 가 참이면(게이트 — 이미 보낸 기록) 옛 이름도 받는다. 발신 전 검사는 거짓을 넘겨 현재 이름만 받는다.
    """
    since = datetime.datetime.fromisoformat(NAMES_SINCE)
    path, value = it["path"], it["meta"].get("created", "")
    when = created_at(value, since.tzinfo)
    if when is None:
        return [f"{path}: created {value!r} 를 시각으로 읽을 수 없다 — 이름 검사의 시행 시각({NAMES_SINCE})과 비교하지 못한다"] if value else []
    if when < since:
        return []
    errs = []
    for ln, line in md_lines(it["text"].split("\n")):
        seen = set()
        for m in MD_CODE_SPAN.finditer(line):
            tok = m.group(2).strip()
            if tok in seen or tok not in names:
                continue
            seen.add(tok)
            kind, ko, old = names[tok]
            if any(n in line for n in ko) or (former and any(n in line for n in old)):
                continue
            want = " 또는 ".join(f'"{n}"' for n in ko)
            why = "옛 이름만 있다 — 새 메시지는 현재 이름을 적는다" if any(n in line for n in old) else "한글 이름이 없다"
            errs.append(f"{path}:{ln}: 식별자 `{tok}`({kind}) 옆에 {why} — 같은 줄에 한글 이름을 그대로 적는다: {want}")
    return errs
```
<!-- 인용 끝 -->
