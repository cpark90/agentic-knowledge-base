---
id: https://agentic-knowledge-base.dev/id/chunk/e40d0ed3-5060-4b0e-9dd9-d76acde18c0e
type: artifact
level: executable
title_ko: 함수 emit_links (tools/chunk2kg.py)
title: function emit_links in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
---
**함수** — `emit_links(meta)` 다. frontmatter 링크 하나 = agt:Link 개체 하나 + 증거 하나 (9.11절, 10.10절).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_links(meta: dict) -> list:
    """frontmatter 링크 하나 = agt:Link 개체 하나 + 증거 하나 (9.11절, 10.10절).

    링크는 청크를 저작할 때 편집 연산의 부산물로 생겼으므로(10.3절 구축) 증거 종류는 구축 기록이고,
    참조는 그 청크 자신(생성 기록 generatedBy·generatedAtTime 을 지닌다). restored: 에 적힌 대상의 링크는 복원 링크라 증거가 한 줄 더
    붙는다 — 후보의 출처 proposal(도구·에이전트가 제안하고 사람이 frontmatter 에 적어 확정, p10-restored-link-marking). 확정 기록
    constructionRecord 는 복원 링크에도 남는다: 사람이 frontmatter 에 적은 행위가 편집 시점 기록이고, 9.11절 규칙(구축(+) 또는 실행(+)
    없이 확정 불가)을 verify 질의 confirmed-without-evidence 가 강제하므로 proposal 만으로는 확정이 성립하지 않는다. 상태는 둘 다 확정이다.
    IRI 는 (출발, 종류, 도착)의 해시라 결정적이고, 제안 증거의 IRI 는 같은 해시에 접미 -proposal 이다. 여기서는 원 IRI 로 해시한다 —
    뿌리 uuid(work_id)는 묶음 전체를 알아야 하므로 rebase_links 가 --merge·단일 실행에서 다시 계산한다.
    """
    out = []
    restored = set(meta.get(RESTORED_KEY) or []) if isinstance(meta.get(RESTORED_KEY), list) else set()
    for key in LINK_KEYS:
        for to in meta.get(key, []) or []:
            h = link_hash(meta["id"], key, to)
            link = f"{ID_BASE}link/{h}"
            evidences = [(f"{ID_BASE}evidence/{h}", EVIDENCE_BUILT)]
            if to in restored:
                evidences.append((f"{ID_BASE}evidence/{h}-proposal", EVIDENCE_RESTORED))
            out.append((link, f"<{link}>\n    a agt:Link , agt:ConfirmedLink ;\n    agt:linkFrom <{meta['id']}> ;\n    agt:linkTo <{to}> ;\n"
                              f"    agt:linkKind agt:{key} ;\n    agt:linkState \"{LINK_STATE_CONFIRMED}\" ;\n    agt:hasEvidence " + " , ".join(f"<{e}>" for e, _ in evidences) + " ."))
            for ev, kind in evidences:
                out.append((ev, f"<{ev}>\n    a agt:Evidence ;\n    agt:evidenceKind {kind} ;\n    agt:evidenceRef <{meta['id']}> ;\n    agt:polarity \"+\" ."))
    return out
```
<!-- 인용 끝 -->
