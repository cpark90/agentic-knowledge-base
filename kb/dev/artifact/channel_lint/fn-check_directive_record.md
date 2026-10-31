---
id: https://agentic-knowledge-base.dev/id/chunk/b0e2a072-409f-46a0-b744-5bbc0f5eaade
type: artifact
level: executable
title_ko: 함수 check_directive_record (tools/channel_lint.py)
title: function check_directive_record in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7ea462e4-8c9b-4768-98eb-df193fcee568]
part_of: https://agentic-knowledge-base.dev/id/composite/f4e440cf-7d39-4f1b-9334-79189a47b8a2
---
**함수** — `check_directive_record(path, text)` 다. 대화 지시 기록 꼴의 네 요건 (질문지 규약의 §대화 지시 기록, Q114-a).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_directive_record(path: str, text: str) -> list[str]:
    """대화 지시 기록 꼴의 네 요건 (질문지 규약의 §대화 지시 기록, Q114-a). 꼴의 답 줄이 없으면 빈 목록이다."""
    body = body_of(text)
    base = text[:len(text) - len(body)].count("\n")  # 오류 줄 번호를 파일 기준으로 — frontmatter 의 줄 수
    lines = body.splitlines()
    marks = [i for i, ln in enumerate(lines) if DIRECTIVE_ANSWER.match(ln)]
    if not marks:
        return []
    errs = []
    first_section = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
    if not any(ln.startswith(">") for ln in lines[:first_section]):
        errs.append(f"{path}: 대화 지시 기록인데 첫 `## ` 절 앞에 원문을 옮긴 인용 블록(`>`)이 없다")
    for i in marks:
        ln = lines[i]
        m = DIRECTIVE_HEAD.match(ln)
        if not m:
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답 줄 머리가 `답: (유저의 대화 지시 원문, YYYY-MM-DD)` 가 아니다 — {ln.strip()[:60]!r}")
            continue
        try:
            datetime.date.fromisoformat(m.group(1))
        except ValueError:
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 날짜 {m.group(1)!r} 가 실재하는 날이 아니다")
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if not m.group(2).strip() and (not nxt or DIRECTIVE_READING.match(nxt) or nxt.startswith("#")):
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답에 원문이 없다 — 같은 줄이나 바로 다음 줄에 원문 또는 \"위 인용 그대로\"를 적는다")
        end = next((j for j in range(i + 1, len(lines)) if QUESTION_HEADING.match(lines[j])), len(lines))
        if not any(DIRECTIVE_READING.match(x.strip()) for x in lines[i + 1:end]):
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답 아래에 `hci의 읽기:` 가 없다 — 유저의 원문과 hci 의 해석을 섞지 않는다")
    return errs
```
<!-- 인용 끝 -->
