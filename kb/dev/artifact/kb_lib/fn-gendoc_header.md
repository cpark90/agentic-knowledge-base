---
id: https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074
type: artifact
level: executable
title_ko: 함수 gendoc_header (tools/kb_lib.py)
title: function gendoc_header in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_header(name, purpose, tool, query, reproduce, inputs, scale, notice, input_kind, stamped, extra, input_note)` 다. G1~G7 의 머리 블록 — 모든 생성 마크다운의 첫 블록이고 순서가 고정이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_header(name: str, purpose: str, tool: str, query: str, reproduce: str, inputs, scale: str,
                  notice: str, input_kind: str = "입력 파일", stamped: bool = True, extra=(), input_note: str = "") -> list[str]:
    """G1~G7 의 머리 블록 — 모든 생성 마크다운의 첫 블록이고 순서가 고정이다.

    Args:
      name: 문서 이름 (h1 의 앞부분, 보통 생성물 파일의 stem).
      purpose: 한 줄 목적.
      tool: 생성기 경로 (`tools/<도구>.py`).
      query: 무엇을 물어 만들었는가 (G5).
      reproduce: 자기 자신을 다시 만드는 명령 (G6). 백틱은 이 함수가 붙인다.
      inputs: 입력 파일 경로들. 목록과 지문이 여기서 나온다 (G4).
      scale: 규모 수치 (트리플 수 등).
      notice: 성격 경고 한 줄 (G7) — gendoc_view_notice · gendoc_tree_notice.
      input_kind: 입력 목록의 종류 이름 ("그래프 파일" 등).
      stamped: False 면 생성 시각과 지문을 넣지 않는다 — 재생성 바이트 비교가 건전성 장치인 생성 트리 파일이 그렇다.
      extra: 머리 블록 뒤에 붙일 추가 불릿들.
      input_note: 입력이 파일이 아닐 때(질의 결과·호스트 상태) 그 자리를 대신하는 한 줄. 주면 목록과 지문을 내지 않는다.

    Returns:
      머리 블록의 줄 목록. 마지막은 빈 줄이다.
    """
    files = [gendoc_input_name(p) for p in inputs]
    listed = " · ".join(f"`{f}`" for f in sorted(files))
    scale_part = f" · {scale}" if scale else ""
    if input_note:
        body = f"{input_note}{scale_part}"
    elif not files:
        body = f"{input_kind} {NONE_MARK}{scale_part}"
    elif len(files) <= GENDOC_INPUT_INLINE_MAX:
        fp = f" · 지문 `{input_fingerprint(inputs)}`" if stamped else ""
        body = f"{input_kind} {len(files)}개: {listed}{fp}{scale_part}"
    else:
        fp = f" · 지문 `{input_fingerprint(inputs)}`" if stamped else ""
        body = (f"{input_kind} {len(files)}개{fp}{scale_part} · 전체 목록은 "
                f"[{GENDOC_INPUTS_HEADING}](#{slug(GENDOC_INPUTS_HEADING)})")
    out = [f"# {name} — {purpose} {GENDOC_H1_SUFFIX}", "",
           f"- 생성기: `{tool}` · {GENDOC_VERSION}"]
    if stamped:
        out.append(f"- 생성 시각: {now_utc()}")
    out += [f"- 입력: {body}",
            f"- 질의: {query}",
            f"- 재현: `{reproduce}`",
            f"- {notice}"]
    return out + list(extra) + [""]
```
<!-- 인용 끝 -->
