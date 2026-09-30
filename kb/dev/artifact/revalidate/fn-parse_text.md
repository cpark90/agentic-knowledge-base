---
id: https://agentic-knowledge-base.dev/id/chunk/1d01a493-eef5-4980-970b-5ba70be5e80e
type: artifact
level: executable
title_ko: 함수 parse_text (tools/revalidate.py)
title: function parse_text in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `parse_text(text, name)` 다. base 리비전의 파일 내용을 parse_chunk 로 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_text(text: str, name: str):
    """base 리비전의 파일 내용을 parse_chunk 로 읽는다 — 해시 계산이 head 그래프와 같게."""
    with tempfile.NamedTemporaryFile("w", suffix=".md", prefix=Path(name).stem + "-", delete=False, encoding="utf-8") as t:
        t.write(text)
        tmp = t.name
    try:
        return parse_chunk(tmp)[0]
    finally:
        os.unlink(tmp)
```
<!-- 인용 끝 -->
