---
id: https://agentic-knowledge-base.dev/id/chunk/d572fb05-efd9-4a73-b605-f658e6ab8a52
type: artifact
level: executable
title_ko: 함수 render_summary (tools/consistency.py)
title: function render_summary in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/9eb1877a-1bde-4cc3-a99e-4a925cccb93c
---
**함수** — `render_summary(items, exact, total_pairs, unlinked_exact, label_dups, near, unlinked_near, cohesion_low, bound, bad_form, term_hits, term_waived, p, dup_candidates, placement, dup_ids)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_summary(items, exact, total_pairs, unlinked_exact, label_dups, near, unlinked_near,
                   cohesion_low, bound, bad_form, term_hits, term_waived, p, dup_candidates, placement, dup_ids):
    return ["## 요약", "",
            "| 항목 | 값 |", "|---|---|",
            f"| 정확 중복 묶음 | {len(exact)} (쌍 {total_pairs}) — coUpdatesWith 미묶음 {len(unlinked_exact)} |",
            f"| 라벨 중복 | {len(label_dups)} (용인 불가) |",
            f"| 근사 중복 후보 (Jaccard ≥ θ) | {len(near)} — 미묶음 {len(unlinked_near)} |",
            f"| 묶인 쌍 중 응집 저하 (coUpdatesWith, Jaccard < θ_cohesion) | {len(cohesion_low)} / 묶인 쌍 {len(bound)} |",
            f"| 결론 라벨 형식 위반 | {len(bad_form)} |",
            f"| 용어집 옛 표기 잔존 (tier 1) | {len(term_hits)} — 면제 {len(term_waived)}건(waivers.md) |",
            f"| 추측 표현 (⑦, 보고) | {len(p['hedge_hits'])}건 / 청크 {len({h[0]['id'] for h in p['hedge_hits']})} |",
            f"| 구어 후보 (⑦, 보고) | {len(p['colloq_hits'])}건 / 청크 {len({h[0]['id'] for h in p['colloq_hits']})} |",
            f"| 대시 밀도 > 1.0 (⑦, 문장당 \" — \") | {len(p['dash_dense'])} / {len(items)} |",
            f"| 메타 문장 (⑧, 게이트 `{ADDITION_GATE}`) | {len(p['meta_hits'])}건 / 청크 {len({h[0]['id'] for h in p['meta_hits']})}"
            f" — 면제 {len(p['meta_waived'])}건(waivers.md) |",
            f"| 채움 문구 (⑧, 게이트 `{ADDITION_GATE}`) | {len(p['filler_hits'])}건 / 청크 {len({h[0]['id'] for h in p['filler_hits']})}"
            f" — 면제 {len(p['filler_waived'])}건(waivers.md) |",
            f"| 빈 값 이상 표기 (⑧, 게이트 `{EMPTY_VALUE_GATE}`) | {len(p['empty_hits'])}건 / 청크 {len({h[0]['id'] for h in p['empty_hits']})}"
            f" — 면제 {len(p['empty_waived'])}건(waivers.md) |",
            f"| 목록 규칙 위반 (⑨, 게이트 `{LIST_RULES_GATE}`) | {len(p['list_hits'])}건 / 청크 {len({h[0]['id'] for h in p['list_hits']})}"
            f" — 면제 {len(p['list_waived'])}건(waivers.md) — " +
            (" · ".join(f"{k} {v}" for k, v in p["list_kinds"]) or kb_lib.NONE_MARK) + " |",
            f"| **중복률** (정확·근사 관련 청크 / 전체) | {kb_lib.pct(len(dup_ids), len(items))} |",
            f"| 중복 확정 후보 (⑩, 판정자 몫) | {len(dup_candidates)} |",
            f"| 자리 후보 (⑪, 판정자 몫) | {len(placement)}건 / 청크 {len({q[0]['id'] for q in placement})} |",
            ""]
```
<!-- 인용 끝 -->
