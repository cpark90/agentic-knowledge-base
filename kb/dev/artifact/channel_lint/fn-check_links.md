---
id: https://agentic-knowledge-base.dev/id/chunk/d2fdf1e1-52ea-4b4d-a14f-5882bfe4b8f8
type: artifact
level: executable
title_ko: 함수 check_links (tools/channel_lint.py)
title: function check_links in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/3740ef5b-1def-406b-ab6d-bbb40f9c7329
---
**함수** — `check_links(msgs, qs)` 다. 메시지·질문지 사이의 참조를 대조한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_links(msgs: dict, qs: dict) -> list[str]:
    """메시지·질문지 사이의 참조를 대조한다. msgs 는 id → 항목, qs 는 질문지 id → 항목."""
    errs = []
    replies = {}  # (re 대상 id, 회신 type) → 회신 메시지 id 들
    for mid, it in msgs.items():
        m = it["meta"]
        if m.get("re"):
            replies.setdefault((m["re"], m.get("type")), []).append(mid)
    for mid, it in msgs.items():
        m, path = it["meta"], it["path"]
        ref, typ = m.get("re"), m.get("type")
        if ref:
            target = msgs.get(ref)
            if target is None:
                errs.append(f"{path}: re {ref!r} 가 실재하는 메시지가 아니다")
            elif typ in REPLY_TO and target["meta"].get("type") != REPLY_TO[typ]:
                errs.append(f"{path}: {typ} 의 re {ref} 는 {REPLY_TO[typ]} 여야 한다 ({target['meta'].get('type')})")
        src = m.get("source")
        if src and src not in qs:
            errs.append(f"{path}: source {src!r} 가 실재하는 질문지가 아니다 (user/ · user/archive/)")
        if m.get("status") == "done" and typ in CLOSED_BY and not replies.get((mid, CLOSED_BY[typ])):
            errs.append(f"{path}: 짝 없는 완료 — done 인 {typ} {mid} 를 re 로 가리키는 {CLOSED_BY[typ]} 가 없다")
    for qid, it in qs.items():
        m, path = it["meta"], it["path"]
        if m.get("status") == "closed":
            continue
        if m.get("re") and m["re"] not in msgs:
            errs.append(f"{path}: re {m['re']!r} 가 실재하는 메시지가 아니다")
        if HCI_REFLECTED.search(it["text"]):
            tasks = [t for t, x in msgs.items() if x["meta"].get("type") == "task" and x["meta"].get("source") == qid]
            if not any(replies.get((t, "result")) for t in tasks):
                errs.append(f"{path}: hci 가 채널 밖에 반영했다는 서술이 있다 — 이 질문지를 source 로 갖는 task 에 result 가 "
                            f"돌아와야 한다(담당 역할의 수행). 아니면 서술을 되돌린다 (hci 는 소통만 한다)")
    return errs
```
<!-- 인용 끝 -->
