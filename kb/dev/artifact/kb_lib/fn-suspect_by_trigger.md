---
id: https://agentic-knowledge-base.dev/id/chunk/a171dc2a-1e86-477b-b9e7-4327ae6185f1
type: artifact
level: executable
title_ko: 함수 suspect_by_trigger (tools/kb_lib.py)
title: function suspect_by_trigger in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/a6fc9e1e-c79d-4e36-ac7b-36d17aaf0a0a, https://agentic-knowledge-base.dev/id/chunk/b92bd358-40c4-4414-b59c-70676927564b]
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `suspect_by_trigger(g)` 다. 켜진 트리거가 suspect 로 유도하는 확정 링크 → 사유.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def suspect_by_trigger(g: Graph) -> dict:
    """켜진 트리거가 suspect 로 유도하는 확정 링크 → 사유. 저장하지 않는다 (LINK_STATE_SUSPECT 주석)."""
    links = _confirmed_links(g)
    incoming: dict = {}
    for link, kind, f, t in links:
        incoming.setdefault(t, []).append((link, kind, f))
    out: dict = {}
    for kind, rule, _basis in suspect_triggers_on():
        if rule != TRIGGER_INCOMING_OF_TARGET:
            continue
        for link, k, f, t in links:
            if k != kind:
                continue
            for other, ok, of in incoming.get(t, ()):
                if other == link or ok == kind:  # 자기 자신과 같은 종류의 링크(시간축의 사슬)는 뺀다
                    continue
                out.setdefault(other, f"`{kind}` 전파 — {compact_iri(str(t))} 가 대체되었다 (트리거 {rule})")
    return out
```
<!-- 인용 끝 -->
