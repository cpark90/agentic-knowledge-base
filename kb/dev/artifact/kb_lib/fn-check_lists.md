---
id: https://agentic-knowledge-base.dev/id/chunk/cd6718e1-2437-43a9-b7a2-174aced3b0e1
type: artifact
level: executable
title_ko: 함수 check_lists (tools/kb_lib.py)
title: function check_lists in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898]
part_of: https://agentic-knowledge-base.dev/id/composite/2a5c7bf9-6e66-4ad7-80de-c8a96b80bb4a
---
**함수** — `check_lists(text)` 다. 목록 규칙(4.3절) 위반 → (줄 번호, 근거).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_lists(text: str) -> list[tuple[int, str]]:
    """목록 규칙(4.3절) 위반 → (줄 번호, 근거). 보고용이다.

    보는 것은 손 번호(`2.` 이상)·항목 수·중첩 깊이·항목 길이·빈 항목이다. 같은 문법 형은 기계 판정이 되지 않아
    넣지 않는다. 길이는 **글자**로 잰다 — 항목에 이어지는 들여쓴 연속 줄을 합치고 연속 공백을 하나로 줄인 뒤
    센다. 소스 줄을 세면 손 줄바꿈(110~120자)이 그대로 위반이 되어 규칙이 저작 결함을 가리키지 못한다.
    """
    out: list[tuple[int, str]] = []
    stack: list[list] = []   # 열려 있는 목록 — [들여쓰기, 깊이, 항목 수, 첫 줄]
    item: list | None = None  # 열려 있는 항목 — [첫 줄, 내용 들여쓰기, 글자 조각들]

    def close_item():
        nonlocal item
        if item:
            n = len(" ".join(" ".join(item[2]).split()))
            if n > LIST_MAX_ITEM_CHARS:
                out.append((item[0], f"목록 항목이 {n}자다 — 항목당 {LIST_MAX_ITEM_CHARS}자 이하로 쓰고 넘으면 별도 블록으로 나눈다"))
        item = None

    def close_lists(indent: int):
        while stack and stack[-1][0] > indent:
            _, _, count, first = stack.pop()
            if count > LIST_MAX_ITEMS:
                out.append((first, f"목록 항목이 {count}개다 — {LIST_MAX_ITEMS}개 이하로 쓰고 넘으면 블록을 나눈다"))

    for ln, line in md_lines(text.split("\n")):
        m = MD_LIST_ITEM.match(line)
        if m:
            close_item()
            indent = len(m.group(1))
            close_lists(indent)
            if not stack or stack[-1][0] < indent:
                stack.append([indent, len(stack) + 1, 0, ln])
            stack[-1][2] += 1
            if stack[-1][1] > LIST_MAX_DEPTH:
                out.append((ln, f"목록 중첩이 {stack[-1][1]}단계다 — {LIST_MAX_DEPTH}단계 이하로 쓰고 넘으면 블록을 나눈다"))
            if m.group(2) and m.group(2) != "1":
                out.append((ln, f"손 번호 `{m.group(2)}.` — 순서 목록의 항목은 모두 `1.` 로 쓰고 번호는 렌더러가 매긴다"))
            if not line[m.end():].strip():
                out.append((ln, f"빈 목록 항목 — 항목이 없으면 목록을 두지 않고 `{EMPTY_REVIEWED}` 으로 적는다"))
            item = [ln, m.end(), [line[m.end():]]]
        elif not line.strip():
            close_item()
        elif item is not None and len(line) - len(line.lstrip()) >= item[1]:
            item[2].append(line.strip())
        else:
            close_item()
            close_lists(-1)
    close_item()
    close_lists(-1)
    return sorted(out)
```
<!-- 인용 끝 -->
