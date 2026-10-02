---
id: https://agentic-knowledge-base.dev/id/chunk/1de413a3-d886-4f4a-b4d8-5899d68e6d2c
type: artifact
level: executable
title_ko: 함수 report_experiment (tools/assume_check.py)
title: function report_experiment in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5dac7240-2471-496d-a65c-f55a8a067a41
---
**함수** — `report_experiment(check, n_inv)` 다. 검증 실험의 결과와 꼬리말 — `--break` 가 없으면 빈 목록이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_experiment(check: dict | None, n_inv: int) -> list[str]:
    """검증 실험의 결과와 꼬리말 — `--break` 가 없으면 빈 목록이다."""
    body: list[str] = []
    if check:
        body += ["", "## 검증 실험 — 계산된 영향 집합 = 실제 의존 집합 (14.1 정정본 4단계 연결 조건)", "",
                f"- 계산된 직접 영향 집합(그래프 `agt:assumes`): **{check['computed']}** · 실제 의존 집합(청크 파일 frontmatter `assumes` 스캔): **{check['actual']}**",
                f"- 정밀도 {check['precision']} · 재현율 {check['recall']} → **{'일치' if check['equal'] else '불일치'}**"]
        if check["only_computed"]:
            body.append("- 그래프에만 있는 것: " + ", ".join(check["only_computed"][:10]))
        if check["only_actual"]:
            body.append("- 파일에만 있는 것: " + ", ".join(check["only_actual"][:10]))
        if check["unparsable"]:
            body.append(f"- 판독 불가 파일 {len(check['unparsable'])}건: " + " · ".join(check["unparsable"][:3]))
    if n_inv:
        body += ["", "무효 가정의 직접 영향 집합은 `invalidated`, suspect 후보는 `suspect` 표시 대상이다 — 표시는 재검증 시점에 일괄로 한다 (method §7). 삭제가 아니다."]
    return body
```
<!-- 인용 끝 -->
