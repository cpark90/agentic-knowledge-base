---
id: https://agentic-knowledge-base.dev/id/chunk/02b29145-5996-4360-8974-d74d70cd6de4
type: artifact
level: executable
title_ko: 함수 table_cells (tools/gen_norms.py)
title: function table_cells in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `table_cells(text)` 다. 표 절의 `규약:` 줄 `a | b | c` → 칸 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def table_cells(text: str) -> list[str]:
    """표 절의 `규약:` 줄 `a | b | c` → 칸 목록. 이스케이프되지 않은 `|` 가 칸을 가른다 — `\\|` 는 칸 안의 글자다(코드 스팬 안도 같다)."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", text)]
```
<!-- 인용 끝 -->
