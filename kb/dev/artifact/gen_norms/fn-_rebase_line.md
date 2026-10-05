---
id: https://agentic-knowledge-base.dev/id/chunk/0ad37658-cf36-48b8-923d-769303f455d1
type: artifact
level: executable
title_ko: 함수 _rebase_line (tools/gen_norms.py)
title: function _rebase_line in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T17:30:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0a2c0068-9fd2-4400-9712-7f00184c9800, https://agentic-knowledge-base.dev/id/chunk/288a1409-ff72-4aa4-b505-661af74bce3e, https://agentic-knowledge-base.dev/id/chunk/61aa2e8e-5b73-49c6-91cb-987c5ffe5aeb]
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `_rebase_line(line, fix)` 다. 한 줄의 인라인 링크 대상을 `fix` 로 바꾼다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _rebase_line(line: str, fix) -> str:
    """한 줄의 인라인 링크 대상을 `fix` 로 바꾼다 — 왼쪽부터 읽으며 링크를 코드 스팬보다 먼저 시도한다.

    링크 텍스트 안의 코드 스팬(`[`x`](경로)`)은 링크의 일부라 대상을 다시 계산한다. 링크 밖에서 열린 코드 스팬은 통째로 옮긴다 —
    백틱 안에 적은 링크 꼴 예시는 링크가 아니다.
    """
    out, i = [], 0
    while i < len(line):
        ch = line[i]
        if ch in "![":
            m = MD_LINK.match(line, i)
            if m and _spans_closed(m.group(1)):
                out.append(fix(m))
                i = m.end()
                continue
        elif ch == "`":
            end = _code_span_end(line, i)
            if end >= 0:
                out.append(line[i:end])
                i = end
                continue
            end = _tick_run_end(line, i)  # 닫히지 않는 백틱 열은 글자다
            out.append(line[i:end])
            i = end
            continue
        out.append(ch)
        i += 1
    return "".join(out)
```
<!-- 인용 끝 -->
