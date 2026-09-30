---
id: https://agentic-knowledge-base.dev/id/chunk/b2c2e02d-e0ff-47a5-ae59-c97c4f96b895
type: artifact
level: executable
title_ko: 함수 check_blocking_comment (tools/chunk_lint.py)
title: function check_blocking_comment in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
---
**함수** — `check_blocking_comment(text)` 다. 해소되지 않은 `issue (blocking)` 주석 (게이트 id `blocking-comment`) → [(줄 번호, 이유)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_blocking_comment(text: str) -> list[tuple[int, str]]:
    """해소되지 않은 `issue (blocking)` 주석 (게이트 id `blocking-comment`) → [(줄 번호, 이유)].

    결정 p7-commentary-form 이 정한 **유일한 게이트 효과**다. `issue (blocking)` 이면서 `해소: 열림` 인 주석만 막고
    나머지 라벨·장식·해소 상태는 기록이라 막지 않는다. 판정은 해소 상태의 존재만 보고 이유의 내용을 보지 않는다
    (p5-verification-tools-per-plane). 첫 줄 꼴과 닫힌 어휘 자체는 shape(review-comment-body-shapes.ttl)가 본다.
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "annotation" or fields.get("status") not in kb_lib.LIVE_STATES:
        return []
    form = comment_form(body)
    if (form.get("label"), form.get("decoration")) != kb_lib.COMMENT_BLOCKING or form.get("resolution") != kb_lib.COMMENT_OPEN:
        return []
    ln = start + next((i for i, l in enumerate(body) if l.strip()), 0)
    on = " · ".join(form.get("targets") or []) or kb_lib.EMPTY_UNDECIDED
    return [(ln, f'해소되지 않은 `{form["label"]} ({form["decoration"]})` 주석이다 — 대상 {on}, 요지 "{form.get("gist", "")}". '
                 f'대상을 고친 뒤 `해소: {kb_lib.COMMENT_RESOLUTIONS[1]} — <이유>` 로, 받지 않기로 했으면 '
                 f'`해소: {kb_lib.COMMENT_RESOLUTIONS[2]} — <이유>` 로 바꾼다 (p7-commentary-form)')]
```
<!-- 인용 끝 -->
