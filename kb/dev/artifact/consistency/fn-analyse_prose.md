---
id: https://agentic-knowledge-base.dev/id/chunk/962a8c5e-a14a-48b2-a819-7740f980902b
type: artifact
level: executable
title_ko: 함수 analyse_prose (tools/consistency.py)
title: function analyse_prose in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/6c400590-b47a-4724-88dc-6d918284ffac, https://agentic-knowledge-base.dev/id/chunk/764328d8-e7e9-4fdf-9e87-e04f59d61a65, https://agentic-knowledge-base.dev/id/chunk/cd6718e1-2437-43a9-b7a2-174aced3b0e1]
part_of: https://agentic-knowledge-base.dev/id/composite/02bb9c9f-7720-4f02-ae31-b3eee5ba6865
---
**함수** — `analyse_prose(items, waivers)` 다. ⑦ 단정성 — 게이트 prose 가 거부하지 않는 나머지(추측·구어·대시 밀도)를 보고한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_prose(items, waivers):
    """⑦ 단정성 — 게이트 prose 가 거부하지 않는 나머지(추측·구어·대시 밀도)를 보고한다. 판정은 사람 몫이다.

    대시 밀도 = 산문 조각 안의 " — " 수 / max(1, 문장 수). 문장 = PROSE_SENTENCE_END(마침표 종결, 또는 마침표 없는 종결 "다" +
    | ) 닫는 따옴표 줄끝). "다." 만 세면 209/621, 종결 "다" 기반은 130 — 명사형 종결·인용 괄호를 놓쳐 대안 양식이 전부
    걸렸다(대리의 결함). 마침표 종결까지 세면 28 — 그 상위는 라벨 대시("- 라벨 — 설명", "| 셀 | `id` — 설명")의 불릿·표
    청크라 라벨 대시를 뺀다(PROSE_LABEL_DASH) → 1. 문장 없이 절 대시만 있는 청크는 여전히 잡힌다.
    ⑧ 첨가 · ⑨ 목록 — 같은 본문을 한 번만 읽어 ⑦ 과 함께 센다. 셋 다 보고이고 판정은 사람 몫이다.
    """
    hedge_hits, colloq_hits, dash_dense = [], [], []
    meta_hits, filler_hits, empty_hits, list_hits = [], [], [], []
    meta_waived, filler_waived, empty_waived, list_waived = [], [], [], []
    for it in items:
        text = Path(it["path"]).read_text(encoding="utf-8")
        _, hedges, colloquial = check_prose(it["path"], text)
        hedge_hits += [(it, ln, expr) for ln, expr in hedges]
        colloq_hits += [(it, ln, expr) for ln, expr in colloquial]
        m_hits, f_hits, e_hits = check_addition(text)
        # 면제(waivers.md, 축 파일)는 집계에서 빼되 목록에 남긴다 — ⑥ 이 선례다
        for gate, hits, out, out_w in ((ADDITION_GATE, m_hits, meta_hits, meta_waived),
                                       (ADDITION_GATE, f_hits, filler_hits, filler_waived),
                                       (EMPTY_VALUE_GATE, e_hits, empty_hits, empty_waived)):
            dst = out_w if waived(waivers, gate, it["path"], "파일") else out
            dst.extend((it, ln, expr, quote) for ln, expr, quote in hits)
        lw = waived(waivers, LIST_RULES_GATE, it["path"], "파일")
        (list_waived if lw else list_hits).extend((it, ln, why) for ln, why in check_lists(text))
        segs = [seg for _, seg in prose_segments(text)]
        dashes = sum(seg.count(" — ") - len(PROSE_LABEL_DASH.findall(seg)) for seg in segs)  # 라벨 대시는 절 연결이 아니다
        sentences = sum(len(PROSE_SENTENCE_END.findall(seg)) for seg in segs)
        density = dashes / max(sentences, 1)
        if density > 1.0:
            dash_dense.append((density, dashes, sentences, it))
    dash_dense.sort(key=lambda t: (-t[0], t[3]["path"]))
    return {"hedge_hits": hedge_hits, "colloq_hits": colloq_hits, "dash_dense": dash_dense,
            "meta_hits": meta_hits, "filler_hits": filler_hits, "empty_hits": empty_hits, "list_hits": list_hits,
            "meta_waived": meta_waived, "filler_waived": filler_waived, "empty_waived": empty_waived,
            "list_waived": list_waived, "list_kinds": list_rule_counts(list_hits)}
```
<!-- 인용 끝 -->
