---
id: https://agentic-knowledge-base.dev/id/chunk/8f6003ae-4fdf-49cc-b1d5-d299b6f34395
type: artifact
level: executable
title_ko: 함수 check_decision_role (tools/chunk_lint.py)
title: function check_decision_role in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a5547d6c-a232-4c09-83b0-81eb591e8bc6, https://agentic-knowledge-base.dev/id/chunk/b61b3d07-041e-43c2-bb5d-cf3239db7602]
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
---
**함수** — `check_decision_role(path, text)` 다. 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_decision_role(path: Path, text: str) -> list[tuple[int, str]]:
    """결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role`) → [(줄 번호, 이유)].

    type: decision 인 .md 만 대상이고 status: deprecated 는 제외한다. 본문 첫 산문 줄(빈 줄 제외 첫 줄)이 굵은 표지로 시작해야 하며,
    표지는 파일 경로가 정한다(kb_lib.decision_role_marker) — conclusion 결론 · rationale 근거 · alternatives 대안,
    V&V 시나리오 패키지의 `-stimulus`·`-factors`·`-excluded` 가 자극·요인·배제 자극이다. 그 밖의 파일명은 역할 이름 밖이라
    표지를 정할 수 없고 그 자체로 위반이다(단일 파일 꼴 폐지, 유저 답 Q-0061 Q147-a). 줄 머리의 굵은 span 이 표지인가는 방출과 같은 `kb_lib.body_slot_mark` 가 판정한다 — 한정어는 괄호·대시·
    `없음` 꼴, 12자 이하, 마침표 없음일 때만 같은 표지다(**대안 없음**·**대안 — 미확정**, p4-slot-marker-by-position).
    """
    fields, body, start = split_frontmatter(text)
    if fields.get("type") != "decision" or fields.get("status") == "deprecated":
        return []
    expected = kb_lib.decision_role_marker(path)
    if not expected:
        return [(1, f"결정 파일 이름 {Path(path).name!r} 이 역할 이름 밖이다 — conclusion·rationale·alternatives·conventions, "
                    f"V&V 시나리오는 <슬러그>-stimulus·-factors·-excluded 중 하나여야 한다 (STYLEGUIDE §4)")]
    for offset, line in enumerate(body):
        if not line.strip():
            continue
        head = line.lstrip()  # 자리 조건은 줄 머리 — 표지·한정어 판정은 방출과 같은 kb_lib.body_slot_mark 하나다
        span = kb_lib.BODY_SLOT_SPAN.match(head)
        mark = kb_lib.body_slot_mark(head, span) if span else ""
        if mark == expected:
            return []
        found = f'"**{mark}…**"' if mark else f"{line.strip()[:40]!r}"
        return [(start + offset, f"본문 첫 산문 줄이 **{expected}** 표지로 시작해야 한다 (STYLEGUIDE §4 역할 태그) — 실제 {found}")]
    return [(start, f"본문이 비어 **{expected}** 표지가 없다 (STYLEGUIDE §4)")]
```
<!-- 인용 끝 -->
