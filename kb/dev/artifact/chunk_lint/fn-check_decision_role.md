---
id: https://agentic-knowledge-base.dev/id/chunk/8f6003ae-4fdf-49cc-b1d5-d299b6f34395
type: artifact
level: executable
title_ko: 함수 check_decision_role (tools/chunk_lint.py)
title: function check_decision_role in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
---
**함수** — `check_decision_role(path, text)` 다. 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_decision_role(path: Path, text: str) -> list[tuple[int, str]]:
    """결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

    type: decision 인 .md 만 대상이고 status: deprecated 는 제외한다. 본문 첫 산문 줄(빈 줄 제외 첫 줄)이 굵은 표지로 시작해야 하며,
    표지는 파일 경로가 정한다(kb_lib.decision_role_marker) — conclusion 결론 · rationale 근거 · alternatives 대안,
    V&V 시나리오 패키지의 `-stimulus`·`-factors`·`-excluded` 가 자극·요인·배제 자극, 그 밖(단일 파일 옛 결정·단일 청크
    시나리오)은 결론이다. 굵은 span 이 역할 낱말로 시작하면 한정어가 붙어도 같은 표지다(**대안 없음**·**대안 — 미확정**,
    kb_lib 주석의 첫 실행 실태).
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "decision" or fields.get("status") == "deprecated":
        return []
    expected = kb_lib.decision_role_marker(path)
    for offset, line in enumerate(body):
        if not line.strip():
            continue
        m = kb_lib.DECISION_ROLE_MARKER.match(line)
        if m and m.group(1) == expected:
            return []
        found = f'"**{m.group(1)}…**"' if m else f"{line.strip()[:40]!r}"
        return [(start + offset, f"본문 첫 산문 줄이 **{expected}** 표지로 시작해야 한다 (STYLEGUIDE §4 역할 태그) — 실제 {found}")]
    return [(start, f"본문이 비어 **{expected}** 표지가 없다 (STYLEGUIDE §4)")]
```
<!-- 인용 끝 -->
