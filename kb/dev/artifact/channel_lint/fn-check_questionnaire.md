---
id: https://agentic-knowledge-base.dev/id/chunk/106ecd5a-7ab2-49db-b822-0e3c51a30083
type: artifact
level: executable
title_ko: 함수 check_questionnaire (tools/channel_lint.py)
title: function check_questionnaire in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/7ea462e4-8c9b-4768-98eb-df193fcee568]
part_of: https://agentic-knowledge-base.dev/id/composite/f4e440cf-7d39-4f1b-9334-79189a47b8a2
---
**함수** — `check_questionnaire(it)` 다. 질문지 하나의 자기 완결 검사.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_questionnaire(it: dict) -> list[str]:
    """질문지 하나의 자기 완결 검사. re·hci 반영 흔적은 check_links 가 한다."""
    m, path, where, errs = it["meta"], it["path"], it["where"], []
    missing = [f for f in Q_FIELDS if not m.get(f)]
    if missing:
        errs.append(f"{path}: 필수 필드가 없다 — {' · '.join(missing)}")
    qid, st = m.get("id", ""), m.get("status")
    if not Q_ID.match(it["stem"]):
        errs.append(f"{path}: 파일명이 `Q-<네 자리>.md` 가 아니다")
    if qid and qid != it["stem"]:
        errs.append(f"{path}: id {qid!r} 가 파일명 {it['stem']!r} 와 다르다")
    if st and st not in Q_STATES:
        errs.append(f"{path}: status {st!r} 는 어휘 밖이다 ({'|'.join(sorted(Q_STATES))})")
    if st == "closed" and where != ARCHIVE:
        errs.append(f"{path}: closed 인데 user/ 에 있다 — 닫은 질문지는 user/archive/ 로 옮긴다")
    if st and st != "closed" and where == ARCHIVE:
        errs.append(f"{path}: status {st} 인데 user/archive/ 에 있다 — archive 는 closed 만 둔다")
    answers = ANSWER_LINE.findall(body_of(it["text"]))
    if not answers:
        errs.append(f"{path}: `답:` 줄이 없다 — 질문마다 유저가 적을 `답:` 줄을 둔다")
    blank = sum(1 for a in answers if not a.strip())
    if st == "closed" and blank:
        errs.append(f"{path}: closed 인데 빈 `답:` 줄이 {blank}개다 — 답을 받지 않은 질문을 닫지 않는다 (보류면 `보류` 라 적는다)")
    it["blank"] = blank
    return errs
```
<!-- 인용 끝 -->
