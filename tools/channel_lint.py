#!/usr/bin/env python3
"""채널 게이트 — 하네스 채널(harness/channel 메시지 · harness/user 질문지)의 프로토콜을 기계로 강제한다.

규약 원본은 harness/README.md(에이전트 채널·메시지)와 harness/user/README.md(유저 채널·질문지)다. 두 세션(hci ·
orchestrator)은 파일 채널로만 소통하고, hci 는 소통만 한다 — 유저의 답을 수행하지 않고 메시지로 orchestrator 에
넘긴다(유저 교정 2026-09-11). 반영 허가 신호는 `답:` 줄이 채워진 질문지에 유저가 직접 `status: answered` 를 태깅하거나, 유저가 hci 세션에서 "답 적었어"라고 알려 hci 가 대신 태깅하는 것이다(유저 답 2026-10-04).

입력은 파일 목록이고 경로로 종류를 가른다.
  메시지   channel/{to_orchestrator,to_hci,archive}/<id>.md — 이 디렉토리의 .md 는 전부 메시지로 본다
  질문지   user/<id>.md · user/archive/<id>.md — 이 디렉토리의 .md 는 전부 질문지로 본다
  그 밖(legacy/ 아래 포함)의 입력은 배선 문제다 → CONFIG
검사 (게이트 id `channel`) — 메시지:
  fields      필수 필드 id from to type status subject created. id 는 네 자리, 파일명은 `<id>.md`, id 는 채널 전역에서 유일
  vocab       from·to ∈ hci|orchestrator 이고 서로 다르다. type ∈ task|question|answer|result|knowledge|status|ack,
              status ∈ new|read|in_progress|done|blocked
  writer      단일 작성자 — to_orchestrator/ 의 메시지는 to: orchestrator, to_hci/ 는 to: hci
  direction   task 는 hci → orchestrator, result·status 는 orchestrator → hci
  re          answer·result 는 re 필수. re 는 실재하는 메시지여야 하고 answer 의 대상은 question, result 의 대상은 task
  source      source 는 실재하는 질문지여야 한다
  sections    task 본문의 필수 절 여섯 — ## 배경 · ## 목표 · ## 완료조건 · ## 제약 · ## 파급효과 · ## 확인 못 한 것
  place       done 은 archive/ 에, done 이 아닌 것은 수신함에 있다
  pair        짝 없는 완료 — done 인 task 에 그것을 re 로 가리키는 result 가, done 인 question 에 answer 가 없으면 FAIL
검사 — 질문지:
  fields      필수 필드 id status subject created. id 는 파일명 stem(`Q-<네 자리>`)과 같다
  vocab       status ∈ open|answered|closed (answered 는 유저가 태깅하거나 유저 알림에 따라 hci 가 대신 태깅한다 — lint 는 값만 보고 행위자는 판별하지 않는다)
  place       closed 는 user/archive/ 에, closed 가 아닌 것은 user/ 에 있다
  answers     `답:` 줄이 하나 이상 있다. closed 인데 빈 `답:` 줄(콜론 뒤가 공백뿐)이 있으면 FAIL
  re          re(선택)는 실재하는 메시지여야 한다 — 닫히지 않은 질문지만 본다(메시지는 git 밖이라 archive 의 질문지가
              가리키던 메시지는 reset 뒤나 새 clone 에서 없다)
  hci-reflect 닫히지 않은 질문지에 hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있으면 그
              질문지를 source 로 갖는 task 에 result 가 돌아와 있어야 한다. 괄호 서명 "(hci, 날짜)" 는 잡지 않는다
WAIT(FAIL 아님): open 질문지 = 유저 답 대기 · answered 질문지 = hci 처리 대기(빈 `답:` 수를 적는다) · 수신함의 done 이 아닌
  메시지 = 수신자 대기(blocked 는 따로 표시).
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일. 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음, 경로 밖) · 3 검사 미실행(입력 0건).
SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md <메시지·질문지 md 파일...>
"""
import argparse
import re
import sys
from pathlib import Path

try:
    from tools.kb_lib import CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # bazel runfiles 경로
except ImportError:
    from kb_lib import CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # 직접 실행

GATE = CHANNEL_GATE
ROLES = ("hci", "orchestrator")
INBOXES = {"to_orchestrator": "orchestrator", "to_hci": "hci"}  # 수신함 디렉토리 → 그 수신함의 to (단일 작성자)
ARCHIVE = "archive"
MSG_FIELDS = ("id", "from", "to", "type", "status", "subject", "created")
MSG_TYPES = {"task", "question", "answer", "result", "knowledge", "status", "ack"}
MSG_STATES = {"new", "read", "in_progress", "done", "blocked"}
DIRECTION = {"task": ("hci", "orchestrator"), "result": ("orchestrator", "hci"), "status": ("orchestrator", "hci")}
REPLY_TO = {"answer": "question", "result": "task"}  # re 가 필수인 type → re 대상의 type
CLOSED_BY = {"task": "result", "question": "answer"}  # done 이 되려면 이 type 의 회신이 re 로 가리켜야 한다
TASK_SECTIONS = ("## 배경", "## 목표", "## 완료조건", "## 제약", "## 파급효과", "## 확인 못 한 것")
Q_FIELDS = ("id", "status", "subject", "created")
Q_STATES = {"open", "answered", "closed"}
MSG_ID = re.compile(r"^\d{4}$")
Q_ID = re.compile(r"^Q-\d{4}$")
ANSWER_LINE = re.compile(r"^답:(.*)$", re.M)
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)


# ── 입력 — frontmatter 와 경로로 가른 종류 ────────────────────

def frontmatter(text: str) -> dict | None:
    """`---` 블록의 key: value 를 읽는다(`#` 뒤 주석 제거). 블록이 없으면 None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    meta = {}
    for raw in lines[1:]:
        if raw.strip() == "---":
            return meta
        if ":" in raw and not raw.lstrip().startswith("#"):
            key, _, val = raw.partition(":")
            meta[key.strip()] = re.split(r"\s+#", val, 1)[0].strip()
    return None


def kind_of(p: Path) -> tuple[str, str] | None:
    """경로 → (종류, 자리). 종류는 message·questionnaire, 자리는 수신함 이름·archive·user. 규약 밖 경로면 None."""
    parent, grand = p.parent.name, p.parent.parent.name
    if grand == "channel" and (parent in INBOXES or parent == ARCHIVE):
        return "message", parent
    if parent == "user":
        return "questionnaire", "user"
    if parent == ARCHIVE and grand == "user":
        return "questionnaire", ARCHIVE
    return None


def body_of(text: str) -> str:
    """frontmatter 를 뗀 본문."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end >= 0 else ""


# ── 메시지 — 필드·어휘·단일 작성자·방향·필수 절·자리 ────────────────────

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


# ── 질문지 — 필드·어휘·자리·답 줄 ────────────────────

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


# ── 연결 — re·source 의 실재, 짝 없는 완료, hci 반영 흔적 ────────────────────

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


# ── 실행 — 입력 분류, 판정, 대기 보고 ────────────────────

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--waivers", default="", help="docs/waivers.md — 게이트 id `channel`, 축 파일")
    ap.add_argument("files", nargs="*", help="메시지·질문지 md 파일")
    a = ap.parse_args(argv)
    if not a.waivers:
        print(f"CONFIG [{GATE}] --waivers <docs/waivers.md> 가 필요하다 — 면제는 코드가 아니라 선언으로", file=sys.stderr)
        return EXIT_CONFIG
    try:
        waivers = load_waivers(a.waivers)
    except (OSError, ValueError) as e:
        print(f"CONFIG [{GATE}] {e}", file=sys.stderr)
        return EXIT_CONFIG

    msgs, qs, errors, config, exempt = {}, {}, [], [], []
    for path in a.files:
        p = Path(path)
        kind = kind_of(p)
        if p.suffix != ".md" or kind is None or "legacy" in p.parts:
            config.append(f"{path}: 메시지(channel/{{to_orchestrator,to_hci,archive}}/<id>.md)도 질문지(user/·user/archive/)도 아니다")
            continue
        if waived(waivers, GATE, path, "파일"):
            exempt.append(path)
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            config.append(f"{path}: 읽을 수 없다 — {e.strerror}")
            continue
        it = {"path": path, "stem": p.stem, "where": kind[1], "meta": frontmatter(text) or {}, "text": text}
        if kind[0] == "message":
            errors += check_message(it)
            key = it["meta"].get("id") or it["stem"]
            if key in msgs:
                errors.append(f"{path}: id {key} 가 {msgs[key]['path']} 와 겹친다 — 메시지 id 는 채널 전역에서 유일하다")
            msgs[key] = it
        else:
            errors += check_questionnaire(it)
            qs[it["meta"].get("id") or it["stem"]] = it
    errors += check_links(msgs, qs)

    waits = []
    for it in qs.values():
        st = it["meta"].get("status")
        if st == "open":
            waits.append(f"{it['path']}: 유저 답 대기 (open)")
        elif st == "answered":
            extra = f" — 빈 `답:` {it['blank']}개" if it.get("blank") else ""
            waits.append(f"{it['path']}: hci 처리 대기 (answered){extra}")
    for it in msgs.values():
        st, to = it["meta"].get("status"), it["meta"].get("to")
        if it["where"] in INBOXES and st != "done":
            mark = " — blocked: 질문의 answer 를 기다린다" if st == "blocked" else ""
            waits.append(f"{it['path']}: {to} 대기 ({it['meta'].get('type')}, {st}){mark}")

    for w in waits:
        print(f"WAIT [{GATE}] {w}")
    for c in config:
        print(f"CONFIG [{GATE}] {c}", file=sys.stderr)
    for e in errors:
        print(f"FAIL [{GATE}] {e}", file=sys.stderr)
    if config:
        print(f"CONFIG [{GATE}] 입력 문제 {len(config)}건 — 판정하지 않았다", file=sys.stderr)
        return EXIT_CONFIG
    if errors:
        print(f"FAIL [{GATE}] {len(errors)}건 — 프로토콜 원본은 harness/README.md · harness/user/README.md", file=sys.stderr)
        return EXIT_FAIL
    inbox = sum(1 for it in msgs.values() if it["where"] in INBOXES)
    blocked = sum(1 for it in msgs.values() if it["meta"].get("status") == "blocked")
    by_q = {s: sum(1 for it in qs.values() if it["meta"].get("status") == s) for s in ("open", "answered", "closed")}
    if not msgs and not qs:
        print(f"SKIP [{GATE}] 검사한 메시지·질문지가 0건이다 — 통과가 아니다 (면제 {len(exempt)}건)", file=sys.stderr)
        return EXIT_SKIP
    print(f"OK {GATE}: 메시지 {len(msgs)}(수신함 {inbox} · archive {len(msgs) - inbox} · blocked {blocked}) · "
          f"질문지 {len(qs)}(open {by_q['open']} · answered {by_q['answered']} · closed {by_q['closed']}), "
          f"대기 {len(waits)}건 · 면제 {len(exempt)}건(waivers.md)")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
