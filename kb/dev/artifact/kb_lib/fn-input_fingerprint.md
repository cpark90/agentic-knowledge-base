---
id: https://agentic-knowledge-base.dev/id/chunk/aac10f80-c526-4fab-ad8f-e93b193438f3
type: artifact
level: executable
title_ko: 함수 input_fingerprint (tools/kb_lib.py)
title: function input_fingerprint in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `input_fingerprint(paths)` 다. G4 의 입력 지문 — 정렬된 경로 순으로 내용을 이어 SHA-256, 앞 12자.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def input_fingerprint(paths) -> str:
    """G4 의 입력 지문 — 정렬된 경로 순으로 내용을 이어 SHA-256, 앞 12자. 리비전보다 정확하고 샌드박스에서도 얻는다."""
    h = hashlib.sha256()
    for p in sorted(paths, key=gendoc_input_name):
        try:
            h.update(Path(p).read_bytes())
        except OSError:
            h.update(b"\0missing\0")
    return "sha256:" + h.hexdigest()[:12]
```
<!-- 인용 끝 -->
