---
id: https://agentic-knowledge-base.dev/id/chunk/cce5ab35-03b9-4926-85ac-b6434fe2ecfd
type: artifact
level: executable
title_ko: 함수 check_message (tools/channel_lint.py)
title: function check_message in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/45faf691-73c6-43a3-b8c9-25f7a11782bc
---
**함수** — `check_message(it)` 다. 메시지 하나의 자기 완결 검사.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_message(it: dict) -> list[str]:
    """메시지 하나의 자기 완결 검사. 다른 메시지를 보는 re·짝 검사는 check_links 가 한다."""
    m, path, where, errs = it["meta"], it["path"], it["where"], []
    missing = [f for f in MSG_FIELDS if not m.get(f)]
    if missing:
        errs.append(f"{path}: 필수 필드가 없다 — {' · '.join(missing)}")
    mid = m.get("id", "")
    if mid and not MSG_ID.match(mid):
        errs.append(f"{path}: id {mid!r} 는 네 자리 번호가 아니다")
    if it["stem"] != mid:
        errs.append(f"{path}: 파일명이 `<id>.md` 가 아니다 (id {mid!r})")
    frm, to, typ, st = m.get("from"), m.get("to"), m.get("type"), m.get("status")
    for key, val in (("from", frm), ("to", to)):
        if val and val not in ROLES:
            errs.append(f"{path}: {key} {val!r} 는 어휘 밖이다 ({'|'.join(ROLES)})")
    if frm and frm == to:
        errs.append(f"{path}: from 과 to 가 같다 ({frm})")
    if typ and typ not in MSG_TYPES:
        errs.append(f"{path}: type {typ!r} 는 어휘 밖이다 ({'|'.join(sorted(MSG_TYPES))})")
    if st and st not in MSG_STATES:
        errs.append(f"{path}: status {st!r} 는 어휘 밖이다 ({'|'.join(sorted(MSG_STATES))})")
    if where in INBOXES and to and to != INBOXES[where]:
        errs.append(f"{path}: 단일 작성자 위반 — {where}/ 의 메시지는 to: {INBOXES[where]} 여야 한다 (to: {to})")
    if typ in DIRECTION and (frm, to) != DIRECTION[typ] and frm and to:
        errs.append(f"{path}: {typ} 는 {' → '.join(DIRECTION[typ])} 로만 보낸다 ({frm} → {to})")
    if typ in REPLY_TO and not m.get("re"):
        errs.append(f"{path}: {typ} 는 re 가 필수다 — 답하는 {REPLY_TO[typ]} 의 id")
    if typ == "task":
        lack = [h for h in TASK_SECTIONS if not re.search(rf"^{re.escape(h)}(\s|$)", it["text"], re.M)]
        if lack:
            errs.append(f"{path}: task 의 필수 절이 없다 — {' · '.join(lack)}")
    if st == "done" and where != ARCHIVE:
        errs.append(f"{path}: done 인데 수신함에 있다 — mark.sh 가 archive/ 로 옮긴다")
    if st and st != "done" and where == ARCHIVE:
        errs.append(f"{path}: status {st} 인데 archive/ 에 있다 — archive 는 done 만 둔다")
    return errs
```
<!-- 인용 끝 -->
