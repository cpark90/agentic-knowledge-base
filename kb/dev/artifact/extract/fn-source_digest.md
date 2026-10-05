---
id: https://agentic-knowledge-base.dev/id/chunk/46409669-5368-4022-9a90-fbf7d0d56eaa
type: artifact
level: executable
title_ko: 함수 source_digest (tools/extract.py)
title: function source_digest in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166
---
**함수** — `source_digest(path)` 다. 소스의 내용 해시 — 파일이면 그 바이트, 질의 디렉토리면 질의 파일 전부의 (이름, 바이트)를 이름 순으로 이은 것이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_digest(path: Path) -> str:
    """소스의 내용 해시 — 파일이면 그 바이트, 질의 디렉토리면 질의 파일 전부의 (이름, 바이트)를 이름 순으로 이은 것이다.

    등록부의 `source_hash` 와 도장(`tools/stamp.py`)의 `tested.source_hash` 가 같은 함수를 쓴다 — 둘이 갈리면 도장이
    소스를 가리키는지 판정할 수 없다. 디렉토리의 해시에 이름을 넣는 까닭은 파일 개명만으로도 소스가 바뀐 것이어서다.
    """
    if not path.is_dir():
        return hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    h = hashlib.sha256()
    for f in sorted(path.glob("*" + kb_lib.EXTRACT_QUERY_SUFFIX)):
        h.update(f.name.encode("utf-8") + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()[:16]
```
<!-- 인용 끝 -->
