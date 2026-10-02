---
id: https://agentic-knowledge-base.dev/id/chunk/0ee2e47f-3e9a-4742-8506-41a3e3aec54e
type: artifact
level: executable
title_ko: 함수 load_extracted_sources (tools/kb_lib.py)
title: function load_extracted_sources in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e7ef6bd8-9aff-42f5-bf43-505fb69d8d2e]
part_of: https://agentic-knowledge-base.dev/id/composite/581eccf7-5ec4-435b-8757-e8042fb462e3
---
**함수** — `load_extracted_sources(path, name)` 다. `defs/kb.bzl` 의 이름 목록 리터럴(`EXTRACTED_SOURCES` 방출 경계 · `USES_TARGETS` 치역 경계)을 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_extracted_sources(path: str | Path, name: str = USES_SOURCES_NAME) -> tuple[str, ...]:
    """`defs/kb.bzl` 의 이름 목록 리터럴(`EXTRACTED_SOURCES` 방출 경계 · `USES_TARGETS` 치역 경계)을 읽는다
    (M1 단일 정의처, load_residency 와 같은 해법, 2026-10-01). 값은 모듈 이름이고 접미사를 붙이지 않는 이유는
    `BUILD.bazel` 의 값과 같은 모양을 유지해서다 — 호출자가 필요한 모양(`tools/<이름>.py`·`tools/<이름>.chunks.yml`)
    으로 옮긴다. 표를 못 읽으면 ValueError — 판정 불가지 통과가 아니다(판정 불가지 통과는 조용히 비는 것과 같다).
    """
    return load_bzl_list(path, name)
```
<!-- 인용 끝 -->
