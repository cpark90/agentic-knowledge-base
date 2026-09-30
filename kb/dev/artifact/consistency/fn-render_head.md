---
id: https://agentic-knowledge-base.dev/id/chunk/76ec82d0-58bd-48bf-9759-396619ccc984
type: artifact
level: executable
title_ko: 함수 render_head (tools/consistency.py)
title: function render_head in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9eb1877a-1bde-4cc3-a99e-4a925cccb93c
---
**함수** — `render_head(a, theta_c, items)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_head(a, theta_c, items):
    return kb_lib.gendoc_header(
        "consistency", "정합성 보고", "tools/consistency.py",
        f"살아 있는 청크의 본문 사이에서 — 정확 중복(contentHash 동일) · 라벨 중복 · 근사 중복 후보(5-shingle Jaccard ≥ {a.theta}) · "
        f"coUpdatesWith 로 묶인 쌍의 응집 저하(Jaccard < {theta_c:g}) · 결론 라벨 형식 · 용어집 옛 표기 · 단정성(추측·구어·대시 밀도) · "
        "첨가(메타 문장·채움 문구·빈 값 이상 표기) · 목록 규칙(손 번호·항목 수·중첩·항목 길이·빈 항목) · "
        "중복 확정 후보(⑩) · 자리 후보(⑪, 다른 슬롯 표지어 재등장). "
        "병합·묶기·유지 판정은 사람이 하고, ⑧·⑨ 의 통과·실패 판정은 게이트 chunk_lint 가 한다. ⑩·⑪ 은 판정자(사람 또는 "
        "세션 판정자, `tools/judge.py`)에게 넘길 후보 생성까지다",
        "bazel build //kb:consistency", a.chunks,
        f"청크 {len(items)}개 · θ = {a.theta} · θ_cohesion = {theta_c:g}",
        kb_lib.gendoc_view_notice("각 청크의 본문"), input_kind="청크 파일")
```
<!-- 인용 끝 -->
