---
id: https://agentic-knowledge-base.dev/id/chunk/5bf58955-471b-4373-9bc5-24cef0d7f893
type: artifact
level: executable
title_ko: 함수 gendoc_inputs_section (tools/kb_lib.py)
title: function gendoc_inputs_section in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_inputs_section(inputs, input_kind)` 다. G4 — 머리 블록에 접은 입력 목록의 전체.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_inputs_section(inputs, input_kind: str = "입력 파일") -> list[str]:
    """G4 — 머리 블록에 접은 입력 목록의 전체. 입력이 GENDOC_INPUT_INLINE_MAX 를 넘으면 문서 어딘가에 이 절이 있어야 한다.

    파일 하나하나를 전부 적되 디렉토리로 묶는다 — 목록이 본문을 덮지 않으면서 어느 파일이 들어갔는지 판별된다.
    """
    files = sorted({gendoc_input_name(p) for p in inputs})
    groups: dict[str, list[str]] = {}
    for f in files:
        d, _, base = f.rpartition("/")
        groups.setdefault(d + "/" if d else "./", []).append(base)
    out = [f"## {GENDOC_INPUTS_HEADING}", "",
           f"{input_kind} {len(files)}개다. 지문은 이 목록의 파일 내용을 경로 순으로 이어 낸 SHA-256 의 앞 12자다. "
           "디렉토리로 묶었고 빠진 파일은 없다.", ""]
    body = [f"- `{d}` — " + " · ".join(f"`{b}`" for b in sorted(bs)) for d, bs in sorted(groups.items())]
    return out + (body or [f"- {NONE_MARK}"]) + [""]
```
<!-- 인용 끝 -->
