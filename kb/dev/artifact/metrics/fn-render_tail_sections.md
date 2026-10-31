---
id: https://agentic-knowledge-base.dev/id/chunk/1559adcb-99d9-41e1-b4d1-bef792a15377
type: artifact
level: executable
title_ko: 함수 render_tail_sections (tools/metrics.py)
title: function render_tail_sections in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2]
part_of: https://agentic-knowledge-base.dev/id/composite/0c0e5dd4-eb47-4eee-b64f-647f067b7c66
---
**함수** — `render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes, default_only, gen, human, bt_excluded)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_tail_sections(g, pct, live, link_count, hist, reqs, reach, ascribed, nonreq, assumes, default_only, gen, human, bt_excluded=None):
    o = []
    o += ["", "## 링크 밀도", "", f"- 링크 {sum(link_count.values())} / 살아 있는 단위 지식 {len(live)} = **{kb_lib.num(sum(link_count.values())/max(len(live),1))}**/단위 지식",
          "- 타입별: " + " · ".join(f"`{k}` {v}" for k, v in link_count.most_common()),
          f"- 링크 개체(`agt:Link`): {sum(1 for _ in g.subjects(RDF.type, AGT.Link))} · 증거 항목: {sum(1 for _ in g.subjects(RDF.type, AGT.Evidence))}"]
    o += ["", "## 크기 분포 (본문 토큰 수가 상한에 대해 차지하는 비율, 살아 있는 단위 지식)", "",
          SIZE_HEADER, "|---|---|---|---|---|",
          "| " + " | ".join(str(hist[i]) for i in range(len(SIZE_BANDS) + 1)) + " |", "",
          f"- 상한의 9/10 초과 비율 {pct(hist[len(SIZE_BANDS)], len(live))} — 상한 근처에 몰리면 억지 분할 의심 (4.13절). "
          f"분모는 단위 지식마다 그 지식 종류의 상한이다(저작 산문 {kb_lib.MAX_BODY_TOKENS} · artifact·memory "
          f"{kb_lib.BODY_TOKEN_LIMITS['artifact']} 토큰, p1-chunk-unit-is-tokens)"]
    o += ["", "## 정제 완주 (CQ19) · 후방 추적 귀속 (CQ20)", "",
          f"- 요구 {len(reqs)}건이 `refines`/`serves` 연쇄로 닿는 가장 낮은 수준: " + " · ".join(f"{k} {v}" for k, v in reach.most_common()),
          f"- executable까지 닿은 요구: **{pct(reach.get('executable', 0), len(reqs))}** (전방 추적 커버리지, 목표 100.0%)",
          f"- 요구로 거슬러 오르는 비요구 단위 지식(관측·주석·규범 절·열린 후보 결정 제외): **{pct(ascribed, len(nonreq))}** (후방 추적 커버리지, 목표 100.0%)",
          f"- 분모에서 뺀 것: 규범 절(`norm`) {(bt_excluded or {}).get('norm', 0)}개 · 열린 공간의 후보 결정 {(bt_excluded or {}).get('candidate', 0)}개. "
          "후보 결정은 결정 완결률과 같은 함수(`metrics.decision_units`)로 가리고, 규범 절은 결정의 규약 줄을 싣는 투영이라 요구로 정제되지 않는다 "
          "(유저 답 Q116-a, `kb_lib.ASCRIPTION_EXCLUDED_PLANES`)"]
    o += ["", "## 가정 · 신뢰 등급", "",
          f"- `assumes` 링크 {assumes} · 가정 개체 {sum(1 for _ in g.subjects(RDF.type, AGT.Assumption))}",
          f"- 기본 가정만 가진 단위 지식(`assumes` 대상이 `id:asm-chunk-conventions` 하나뿐인 살아 있는 단위 지식): **{pct(default_only, len(live))}** (좁힘 진행률의 역수 — 목표 0)",
          f"- 생성자: " + " · ".join(f"`{k}` {v}" for k, v in gen.most_common()) + f" · **사람 검토(`human:`) {human}건**",
          ""]
    return o
```
<!-- 인용 끝 -->
