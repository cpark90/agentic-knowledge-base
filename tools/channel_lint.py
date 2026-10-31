#!/usr/bin/env python3
"""채널 게이트 — 하네스 채널(harness/channel 메시지 · harness/user 질문지)의 프로토콜을 기계로 강제한다.

규약 원본은 harness/README.md(에이전트 채널·메시지)와 harness/user/README.md(유저 채널·질문지)다. 두 세션(interpreter ·
orchestrator)은 파일 채널로만 소통한다. hci 는 interpreter 의 유저 대상 하위 역할이고 같은 세션이 맡으며, 소통만 한다 — 유저의 답을 수행하지 않고 메시지로 orchestrator 에
넘긴다(유저 교정 2026-09-11). 반영 허가 신호는 `답:` 줄이 채워진 질문지에 유저가 직접 `status: answered` 를 태깅하거나, 유저가 hci 세션에서 "답 적었어"라고 알려 hci 가 대신 태깅하는 것이다(유저 답 2026-10-04).

입력은 하네스 루트(`--harness`)이고 그 아래 디렉토리를 **실행 시점에** 읽는다(유저 답 Q-0061 Q152-a). 메시지는 git 밖
런타임 파일이라 빌드가 분석 단계에 잡은 목록은 실행 때 이미 낡았을 수 있다(mark.sh 의 archive 이동). 경로로 종류를 가른다.
  메시지   channel/to_<역할>/<id>.md · channel/archive/<id>.md — 수신함은 역할 어휘 ROLES 에서 끌어낸다(INBOXES)
  질문지   user/Q-*.md · user/archive/Q-*.md
  legacy/(옛 채널 기록)는 읽지 않는다. 파일 목록을 직접 주면(고정물 시험) 그 목록만 보고, 그 밖 경로는 배선 문제다 → CONFIG
읽는 동안 파일이 사라지거나 목록·파일 서명(inode·mtime·크기)이 바뀌면 이동 경쟁으로 보고 디렉토리를 다시 읽는다. 판정이
PASS 가 아니면 한 번 더 읽어 서명이 같은 상태에서 같은 판정이 나야 그 판정을 낸다 — 진짜 결함은 두 번 읽어도 남는다.
검사 (게이트 id `channel`) — 메시지:
  fields      필수 필드 id from to type status subject created. id 는 네 자리, 파일명은 `<id>.md`, id 는 채널 전역에서 유일
  vocab       from·to ∈ interpreter|orchestrator 이고 서로 다르다. 옛 이름 hci 는 interpreter 로 읽는다(ROLE_ALIASES). type ∈ task|question|answer|result|knowledge|status|ack,
              status ∈ new|read|in_progress|done|blocked
  writer      단일 작성자 — to_<역할>/ 의 메시지는 to: <역할>. hci 와 interpreter 는 같은 작성자다
  direction   task 는 interpreter → orchestrator, result·status 는 orchestrator → interpreter
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
  directive   대화 지시 기록 꼴(질문지 규약의 §대화 지시 기록, Q114-a) — `답:` 줄이 `(유저의 대화 지시` 로 시작하는
              질문을 가진 질문지는 넷을 갖춘다. ① 첫 `## ` 절 앞에 원문을 옮긴 인용 블록(`>`)이 있다 ② 답 줄 머리가
              `답: (유저의 대화 지시 원문, YYYY-MM-DD)` 이고 날짜가 실재한다 ③ 그 뒤 같은 줄이나 바로 다음 줄에 원문 또는
              "위 인용 그대로"가 있다 ④ 그 답부터 다음 질문 절(`## Q<번호>`) 전까지 `hci의 읽기` 로 시작하는 줄이나 절이 있다.
              subject 의 꼬리표와 인용 첫 줄의 문구는 보지 않는다 — 옛 기록의 문구가 조금씩 달라 핵심만 본다
  hci-reflect 닫히지 않은 질문지에 hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있으면 그
              질문지를 source 로 갖는 task 에 result 가 돌아와 있어야 한다. 괄호 서명 "(hci, 날짜)" 는 잡지 않는다
검사 — 메시지·질문지 공통 (유저 답 Q103 3번, 2026-10-24):
  register    경어·감탄 — 게이트 `prose` 의 판정(kb_lib.check_prose: PROSE_FORBIDDEN_ENDINGS · PROSE_EXCLAMATION, 대상
              분절은 prose_segments)을 그대로 건다. frontmatter·코드 펜스·백틱 인용·따옴표 안은 prose_segments 가, 인용
              블록(`>`)은 여기서 뺀다 — 인용 블록에는 유저 원문이 있다
  names       식별자 옆 한글 이름 — 백틱 토큰이 KB 안의 항목으로 풀리면(결정 slug · `agt:<Term>` · `id:<name>`) 같은 줄에
              그 항목의 한글 이름이 정확히 있어야 한다. 한 줄에 같은 식별자가 여러 번 나오면 이름은 한 번이면 된다. 이름은
              결정 slug 가 결정 기록(복합체)의 `composite.title_ko`, `agt:`·`id:` 가 `rdfs:label`·`skos:prefLabel` 의 @ko 다.
              이름이 바뀐 항목은 옛 이름(결정은 `former_title_ko`, `agt:`·`id:` 는 `skos:hiddenLabel` @ko)도 받는다 — 메시지는
              쓴 뒤 고치지 않는 기록이라 그때의 이름이 맞는 이름이다. 발신 전 검사(--message)는 현재 이름만 받는다.
              풀리지 않는 토큰(경로·명령·게이트 id)은 대상이 아니다. 소급하지 않는다 — `created` 가 NAMES_SINCE 이상인
              항목에만 건다. 질문지의 `created` 는 날짜뿐이라 그날 0시(NAMES_SINCE 의 시간대)로 읽는다
WAIT(FAIL 아님): open 질문지 = 유저 답 대기 · answered 질문지 = hci 처리 대기(빈 `답:` 수를 적는다) · 수신함의 done 이 아닌
  메시지 = 수신자 대기(blocked 는 따로 표시).
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일. 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음, 경로 밖) · 3 검사 미실행(입력 0건).
SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md --decisions <kb/dev 파일...> --ontology <온톨로지 ttl...>
      --graphs <id: 그래프 ttl...> --harness <하네스 루트 | 그 루트의 파일> [-- <메시지·질문지 md 파일...>]
발신 전 검사: channel_lint.py --decisions … --ontology … --graphs … --message <보낼 메시지 md>
  send.sh 가 수신함에 놓기 전의 임시 파일 하나에 메시지 단위 검사(fields · vocab · direction · re 필수 · sections ·
  register · names)를 건다. 채널 전체를 보는 검사(re 대상·source 의 실재, pair, place, id 유일, 단일 작성자)는 게이트에
  남는다 — re·source 의 실재는 send.sh 가 먼저 본다. 면제는 경로 단위라 아직 놓이지 않은 메시지에는 없다(--waivers 불요).
  인수는 `@<파일>` 로 줄 단위 파일에서 읽을 수 있다 — //harness:channel_send_check 가 이름 원천을 그렇게 싣는다
  이름 원천 셋은 필수다(없으면 CONFIG). --decisions 에서는 `kb/dev/decision/<slug>/conclusion.md` 만 읽는다.
  --harness 에 파일을 주면 그 실경로의 부모가 루트다 — `bazel test` 는 runfiles 의 심볼릭 링크를 따라 소스 트리에 닿는다.
  --harness 도 파일 목록도 없으면 `bazel run` 의 BUILD_WORKSPACE_DIRECTORY 아래 harness/ 를 본다
"""
import argparse
import datetime
import os
import re
import sys
import time
from pathlib import Path

from rdflib import RDFS, Graph, URIRef
from rdflib.namespace import SKOS

try:
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # frontmatter 의 단일 판독처
    from tools.kb_lib import (AGT, CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, FORMER_TITLE_KEY, ID,  # bazel runfiles 경로
                              MD_CODE_SPAN, check_prose, gates_bzl_path, load_graph, load_waivers, md_lines, waived)
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # 직접 실행
    from kb_lib import (AGT, CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, FORMER_TITLE_KEY, ID,
                        MD_CODE_SPAN, check_prose, gates_bzl_path, load_graph, load_waivers, md_lines, waived)

GATE = CHANNEL_GATE
ROLES = ("interpreter", "orchestrator")  # 채널의 역할 어휘 — 수신함 디렉토리·from·to 가 모두 여기서 나온다. 역할을 바꾸면 이 줄만 고친다
ROLE_ALIASES = {"hci": "interpreter"}  # 옛 이름 → 정규 이름. hci 는 interpreter 의 유저 대상 하위 역할이고 옛 메시지(archive)의 from·to 에 남는다
INBOXES = {f"to_{r}": r for r in ROLES}  # 수신함 디렉토리 → 그 수신함의 to (단일 작성자)
ARCHIVE = "archive"
SNAPSHOT_TRIES = 5  # 이동 경쟁에서 디렉토리를 다시 읽는 최대 횟수 — 넘으면 마지막 판정을 그대로 낸다
SETTLE_SECONDS = 0.2  # 다시 읽기 전에 기다리는 시간 — mark.sh 의 rename 과 rm 사이가 지나가게 한다
MSG_FIELDS = ("id", "from", "to", "type", "status", "subject", "created")
MSG_TYPES = {"task", "question", "answer", "result", "knowledge", "status", "ack"}
MSG_STATES = {"new", "read", "in_progress", "done", "blocked"}
DIRECTION = {"task": ("interpreter", "orchestrator"), "result": ("orchestrator", "interpreter"),
             "status": ("orchestrator", "interpreter")}
REPLY_TO = {"answer": "question", "result": "task"}  # re 가 필수인 type → re 대상의 type
CLOSED_BY = {"task": "result", "question": "answer"}  # done 이 되려면 이 type 의 회신이 re 로 가리켜야 한다
TASK_SECTIONS = ("## 배경", "## 목표", "## 완료조건", "## 제약", "## 파급효과", "## 확인 못 한 것")
Q_FIELDS = ("id", "status", "subject", "created")
Q_STATES = {"open", "answered", "closed"}
MSG_ID = re.compile(r"^\d{4}$")
Q_ID = re.compile(r"^Q-\d{4}$")
ANSWER_LINE = re.compile(r"^답:(.*)$", re.M)
DIRECTIVE_ANSWER = re.compile(r"^답:\s*\(유저의 대화 지시")  # 대화 지시 기록 꼴의 표지 — 머리가 이것이면 꼴 전체를 본다
DIRECTIVE_HEAD = re.compile(r"^답: \(유저의 대화 지시 원문, (\d{4}-\d{2}-\d{2})\)(.*)$")
DIRECTIVE_READING = re.compile(r"^(?:#+\s*|>\s*)?hci의 읽기")
QUESTION_HEADING = re.compile(r"^## Q\d+")
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
# 식별자 옆 한글 이름(names)의 시행 시각 — `created` 가 이 시각 이상인 항목에만 건다. 소급하지 않는다 (유저 답 Q103 3번)
NAMES_SINCE = "2026-10-24T08:20:24+09:00"
DECISION_RECORD = re.compile(r"(?:^|/)kb/dev/decision/([^/]+)/conclusion\.md$")  # 결정 기록의 자리 — 디렉토리 이름이 slug 다
NAME_PREDICATES = (RDFS.label, SKOS.prefLabel)  # agt:·id: 의 한글 이름 — @ko 만 읽는다
FORMER_PREDICATE = SKOS.hiddenLabel  # agt:·id: 의 옛 한글 이름 — 과거 표기다(p0-skos-label-synonyms). 이미 보낸 기록에만 받는다


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
        if val and val not in ROLES and val not in ROLE_ALIASES:
            errs.append(f"{path}: {key} {val!r} 는 어휘 밖이다 ({'|'.join(ROLES)}, 옛 이름 {'|'.join(ROLE_ALIASES)})")
    frm, to = ROLE_ALIASES.get(frm, frm), ROLE_ALIASES.get(to, to)  # 옛 이름은 정규 이름과 같은 작성자다 — 아래 검사는 정규 이름으로 본다
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
    errs += check_directive_record(path, it["text"])
    return errs


def check_directive_record(path: str, text: str) -> list[str]:
    """대화 지시 기록 꼴의 네 요건 (질문지 규약의 §대화 지시 기록, Q114-a). 꼴의 답 줄이 없으면 빈 목록이다."""
    body = body_of(text)
    base = text[:len(text) - len(body)].count("\n")  # 오류 줄 번호를 파일 기준으로 — frontmatter 의 줄 수
    lines = body.splitlines()
    marks = [i for i, ln in enumerate(lines) if DIRECTIVE_ANSWER.match(ln)]
    if not marks:
        return []
    errs = []
    first_section = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
    if not any(ln.startswith(">") for ln in lines[:first_section]):
        errs.append(f"{path}: 대화 지시 기록인데 첫 `## ` 절 앞에 원문을 옮긴 인용 블록(`>`)이 없다")
    for i in marks:
        ln = lines[i]
        m = DIRECTIVE_HEAD.match(ln)
        if not m:
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답 줄 머리가 `답: (유저의 대화 지시 원문, YYYY-MM-DD)` 가 아니다 — {ln.strip()[:60]!r}")
            continue
        try:
            datetime.date.fromisoformat(m.group(1))
        except ValueError:
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 날짜 {m.group(1)!r} 가 실재하는 날이 아니다")
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if not m.group(2).strip() and (not nxt or DIRECTIVE_READING.match(nxt) or nxt.startswith("#")):
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답에 원문이 없다 — 같은 줄이나 바로 다음 줄에 원문 또는 \"위 인용 그대로\"를 적는다")
        end = next((j for j in range(i + 1, len(lines)) if QUESTION_HEADING.match(lines[j])), len(lines))
        if not any(DIRECTIVE_READING.match(x.strip()) for x in lines[i + 1:end]):
            errs.append(f"{path}:{base + i + 1}: 대화 지시 기록의 답 아래에 `hci의 읽기:` 가 없다 — 유저의 원문과 hci 의 해석을 섞지 않는다")
    return errs


# ── 문체·이름 — 경어·감탄과 식별자 옆 한글 이름 (유저 답 Q103 3번) ────────────────────

def check_register(it: dict) -> list[str]:
    """경어·감탄 — 게이트 `prose` 의 판정(kb_lib.check_prose)을 그대로 건다. 인용 블록(`>`)은 유저 원문이라 비워서 넘긴다.

    줄을 지우지 않고 비우므로 줄 번호는 파일 기준 그대로다. 면제는 게이트 `channel` 의 것만 본다(main 이 먼저 거른다).
    """
    text = "\n".join("" if ln.lstrip().startswith(">") else ln for ln in it["text"].split("\n"))
    errors, _, _ = check_prose(it["path"], text)
    return [f"{it['path']}:{ln}: {msg}" for ln, msg in errors]


def load_names(decisions: list[str], ontology: list[str], graphs: list[str]) -> dict[str, tuple[str, list[str], list[str]]]:
    """식별자 → (꼴, 현재 한글 이름들, 옛 한글 이름들). 꼴은 slug·agt·id 다.

    결정 slug 의 이름은 결정 기록(복합체)의 `composite.title_ko` 다 — slug 는 결정 기록의 디렉토리 이름이고 결론 하나의
    이름이 아니다. 복합체 선언이 없으면 결론의 `title_ko` 로 갈음한다. 옛 이름은 같은 자리의 `former_title_ko` 다.
    `agt:`·`id:` 는 온톨로지·그래프의 @ko 라벨(NAME_PREDICATES)이고 옛 이름은 `skos:hiddenLabel` @ko 다.
    `id:` 는 경로 없는 이름(`id:<name>`)만 받는다 — 단위 지식·복합체의 uuid IRI 는 백틱 식별자로 쓰이지 않는다.
    """
    names: dict[str, tuple[str, list[str], list[str]]] = {}
    if any(DECISION_RECORD.search(p) for p in decisions):  # parse_chunk 의 수준·상태 어휘 — 등록부와 같은 defs/kb.bzl 이다
        apply_plane_level_state(*load_plane_level_state(gates_bzl_path()))
    for path in decisions:
        m = DECISION_RECORD.search(path)
        if not m:
            continue
        meta, _ = parse_chunk(path)
        comp = meta.get("composite")
        src = comp if isinstance(comp, dict) and comp.get("title_ko") else meta
        names[m.group(1)] = ("slug", [src["title_ko"]], list(src.get(FORMER_TITLE_KEY) or []))
    g = Graph()
    for path in [*ontology, *graphs]:
        g += load_graph(path)
    for slot, preds in ((1, NAME_PREDICATES), (2, (FORMER_PREDICATE,))):
        for s, o in (so for pred in preds for so in g.subject_objects(pred)):
            if not isinstance(s, URIRef) or getattr(o, "language", None) != "ko":
                continue
            for kind, ns in (("agt", AGT), ("id", ID)):
                local = str(s)[len(str(ns)):] if str(s).startswith(str(ns)) else ""
                if local and "/" not in local:
                    ko = names.setdefault(f"{kind}:{local}", (kind, [], []))[slot]
                    if str(o) not in ko:
                        ko.append(str(o))
    return {k: v for k, v in names.items() if v[1]}  # 현재 이름이 없는 식별자(hiddenLabel 만 있는 것)는 풀리지 않는 토큰이다


def created_at(value: str, tz) -> datetime.datetime | None:
    """`created` → 시각. 날짜뿐이면(질문지) 그날 0시(tz)로 읽는다. 읽을 수 없으면 None."""
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return datetime.datetime.combine(datetime.date.fromisoformat(value), datetime.time(), tz)
        when = datetime.datetime.fromisoformat(value)
    except ValueError:
        return None
    return when if when.tzinfo else when.replace(tzinfo=tz)


def check_names(it: dict, names: dict, former: bool = True) -> list[str]:
    """식별자 옆 한글 이름 — `created` 가 NAMES_SINCE 이상인 항목에서, KB 항목으로 풀리는 백틱 토큰의 줄에 그 한글 이름이 있는가.

    former 가 참이면(게이트 — 이미 보낸 기록) 옛 이름도 받는다. 발신 전 검사는 거짓을 넘겨 현재 이름만 받는다.
    """
    since = datetime.datetime.fromisoformat(NAMES_SINCE)
    path, value = it["path"], it["meta"].get("created", "")
    when = created_at(value, since.tzinfo)
    if when is None:
        return [f"{path}: created {value!r} 를 시각으로 읽을 수 없다 — 이름 검사의 시행 시각({NAMES_SINCE})과 비교하지 못한다"] if value else []
    if when < since:
        return []
    errs = []
    for ln, line in md_lines(it["text"].split("\n")):
        seen = set()
        for m in MD_CODE_SPAN.finditer(line):
            tok = m.group(2).strip()
            if tok in seen or tok not in names:
                continue
            seen.add(tok)
            kind, ko, old = names[tok]
            if any(n in line for n in ko) or (former and any(n in line for n in old)):
                continue
            want = " 또는 ".join(f'"{n}"' for n in ko)
            why = "옛 이름만 있다 — 새 메시지는 현재 이름을 적는다" if any(n in line for n in old) else "한글 이름이 없다"
            errs.append(f"{path}:{ln}: 식별자 `{tok}`({kind}) 옆에 {why} — 같은 줄에 한글 이름을 그대로 적는다: {want}")
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
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                 fromfile_prefix_chars="@")  # `@<인수 파일>` — 발신 전 검사의 이름 원천
    ap.add_argument("--waivers", default="", help="docs/waivers.md — 게이트 id `channel`, 축 파일")
    ap.add_argument("--decisions", nargs="*", help="이름 원천 — kb/dev 파일들 (결정 기록의 conclusion.md 만 읽는다)")
    ap.add_argument("--ontology", nargs="*", help="이름 원천 — 온톨로지 모듈 ttl (agt:)")
    ap.add_argument("--graphs", nargs="*", help="이름 원천 — 개체 그래프 ttl (id:)")
    ap.add_argument("--harness", default="", help="하네스 루트 — 그 아래 channel/·user/ 를 실행 시점에 읽는다. 파일이면 실경로의 부모")
    ap.add_argument("--message", default="", help="발신 전 검사 — 보낼 메시지 하나에 메시지 단위 검사만 건다(send.sh)")
    ap.add_argument("files", nargs="*", help="메시지·질문지 md 파일 — 주면 이 목록만 본다(고정물 시험). 이름 원천 뒤에는 `--` 로 가른다")
    a = ap.parse_args(argv)
    if not a.waivers and not a.message:  # 보낼 메시지는 아직 자리가 없어 면제 대상이 아니다
        print(f"CONFIG [{GATE}] --waivers <docs/waivers.md> 가 필요하다 — 면제는 코드가 아니라 선언으로", file=sys.stderr)
        return EXIT_CONFIG
    if a.decisions is None or a.ontology is None or a.graphs is None:
        print(f"CONFIG [{GATE}] 이름 원천 --decisions · --ontology · --graphs 가 필요하다 — 식별자 옆 한글 이름 검사의 입력", file=sys.stderr)
        return EXIT_CONFIG
    workspace = os.environ.get("BUILD_WORKSPACE_DIRECTORY", "")  # `bazel run` 만 준다 — 상대 경로를 워크스페이스 기준으로 읽는다
    if a.message and (a.files or a.harness):
        print(f"CONFIG [{GATE}] --message 는 --harness · 파일 목록과 함께 주지 않는다", file=sys.stderr)
        return EXIT_CONFIG
    if a.files and a.harness:
        print(f"CONFIG [{GATE}] --harness 와 파일 목록은 함께 주지 않는다 — 하나만 입력이다", file=sys.stderr)
        return EXIT_CONFIG
    if not a.message and not a.files and not a.harness and not workspace:
        print(f"CONFIG [{GATE}] --harness <하네스 루트> 가 필요하다 — `bazel run` 밖에서는 루트를 알 수 없다", file=sys.stderr)
        return EXIT_CONFIG
    try:
        waivers = load_waivers(a.waivers) if a.waivers else []
        names = load_names(a.decisions, a.ontology, a.graphs)
    except Exception as e:  # noqa: BLE001 — 원천 파일의 읽기·파싱 실패는 판정이 아니라 설정 문제다
        print(f"CONFIG [{GATE}] {e}", file=sys.stderr)
        return EXIT_CONFIG

    if a.message:  # 발신 전 검사 — 채널 전체를 보는 검사는 게이트의 몫이다
        try:
            text = Path(a.message).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"CONFIG [{GATE}] {a.message}: 읽을 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
        meta = frontmatter(text) or {}
        to = ROLE_ALIASES.get(meta.get("to"), meta.get("to"))
        it = {"path": a.message, "stem": Path(a.message).stem, "meta": meta, "text": text,
              "where": f"to_{to}" if to in ROLES else ""}  # 놓일 자리는 to 의 수신함이다
        errors = check_message(it) + check_register(it) + check_names(it, names, False)
        for e in errors:
            print(f"FAIL [{GATE}] {e}", file=sys.stderr)
        if errors:
            print(f"FAIL [{GATE}] {len(errors)}건 — 프로토콜 원본은 harness/README.md", file=sys.stderr)
            return EXIT_FAIL
        print(f"OK {GATE}: 발신 전 검사 {a.message}")
        return EXIT_OK

    def read(p: Path, moving: bool):
        """파일 하나의 본문. 읽기 실패는 값으로 낸다 — 단 디렉토리를 읽는 중(moving)에 사라진 파일은 이동 경쟁이라 올린다."""
        try:
            return p.read_text(encoding="utf-8")
        except FileNotFoundError:
            if moving:
                raise
            return FileNotFoundError(2, "No such file or directory")
        except (OSError, UnicodeDecodeError) as e:
            return e

    def snapshot(root: Path):
        """디렉토리를 읽어 (서명, 항목들) 을 낸다. 읽는 사이 파일이 사라지거나 목록·서명이 바뀌면 None — 이동 경쟁이다."""
        dirs = [(root / "channel" / d, "*.md") for d in (*INBOXES, ARCHIVE)] + \
               [(root / "user", "Q-*.md"), (root / "user" / ARCHIVE, "Q-*.md")]

        def listing():
            out = []
            for d, pat in dirs:
                for p in sorted(d.glob(pat)):
                    try:
                        st = p.stat()
                    except FileNotFoundError:
                        continue  # 목록을 잡은 뒤 옮겨졌다 — 서명이 달라져 다시 읽게 된다
                    out.append((p, st.st_ino, st.st_mtime_ns, st.st_size))
            return out
        sig = listing()
        try:
            entries = [(f"{root.name}/{p.relative_to(root).as_posix()}", p, read(p, True)) for p, *_ in sig]
        except FileNotFoundError:
            return None
        return (sig, entries) if listing() == sig else None

    def judge(entries) -> tuple[int, list[str], list[str]]:
        """항목들 (표시 경로, 경로, 본문 또는 읽기 오류) 를 판정한다 → (종료 코드, stdout 줄, stderr 줄)."""
        msgs, qs, errors, config, exempt = {}, {}, [], [], []
        for path, p, text in entries:
            kind = kind_of(p)
            if p.suffix != ".md" or kind is None or "legacy" in p.parts:
                config.append(f"{path}: 메시지(channel/{{{','.join((*INBOXES, ARCHIVE))}}}/<id>.md)도 질문지(user/·user/archive/)도 아니다")
                continue
            if waived(waivers, GATE, path, "파일"):
                exempt.append(path)
                continue
            if isinstance(text, Exception):
                config.append(f"{path}: 읽을 수 없다 — {getattr(text, 'strerror', None) or text}")
                continue
            it = {"path": path, "stem": p.stem, "where": kind[1], "meta": frontmatter(text) or {}, "text": text}
            errors += check_register(it) + check_names(it, names)
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

        out = [f"WAIT [{GATE}] {w}" for w in waits]
        err = [f"CONFIG [{GATE}] {c}" for c in config] + [f"FAIL [{GATE}] {e}" for e in errors]
        if config:
            return EXIT_CONFIG, out, err + [f"CONFIG [{GATE}] 입력 문제 {len(config)}건 — 판정하지 않았다"]
        if errors:
            return EXIT_FAIL, out, err + [f"FAIL [{GATE}] {len(errors)}건 — 프로토콜 원본은 harness/README.md · harness/user/README.md"]
        inbox = sum(1 for it in msgs.values() if it["where"] in INBOXES)
        blocked = sum(1 for it in msgs.values() if it["meta"].get("status") == "blocked")
        by_q = {s: sum(1 for it in qs.values() if it["meta"].get("status") == s) for s in ("open", "answered", "closed")}
        if not msgs and not qs:
            return EXIT_SKIP, out, [f"SKIP [{GATE}] 검사한 메시지·질문지가 0건이다 — 통과가 아니다 (면제 {len(exempt)}건)"]
        return EXIT_OK, out + [
            f"OK {GATE}: 메시지 {len(msgs)}(수신함 {inbox} · archive {len(msgs) - inbox} · blocked {blocked}) · "
            f"질문지 {len(qs)}(open {by_q['open']} · answered {by_q['answered']} · closed {by_q['closed']}), "
            f"대기 {len(waits)}건 · 면제 {len(exempt)}건(waivers.md) · 이름 원천 "
            f"{' · '.join(f'{k} {sum(1 for v in names.values() if v[0] == k)}' for k in ('slug', 'agt', 'id'))}"], []

    if a.files:  # 고정물 시험 — 준 목록만 본다. 없는 파일은 경쟁이 아니라 배선 문제다
        result = judge([(path, Path(path), read(Path(path), False)) for path in a.files])
    else:
        root = Path(os.path.realpath(Path(workspace or ".") / (a.harness or "harness")))
        root = root.parent if root.is_file() else root
        if not (root / "channel").is_dir() or not (root / "user").is_dir():
            print(f"CONFIG [{GATE}] {root}: 하네스 루트가 아니다 — channel/ 과 user/ 가 있어야 한다", file=sys.stderr)
            return EXIT_CONFIG
        result, prev, reread = None, None, 0
        for _ in range(SNAPSHOT_TRIES):
            snap = snapshot(root)
            if snap is not None:
                result = judge(snap[1])
                if result[0] == EXIT_OK or snap[0] == prev:  # 같은 서명에서 판정이 거듭 났다 — 경쟁이 아니라 진짜 결함이다
                    break
                prev = snap[0]
            reread += 1
            time.sleep(SETTLE_SECONDS)
        if result is None:
            print(f"CONFIG [{GATE}] {root}: 읽는 동안 채널이 {SNAPSHOT_TRIES}번 모두 바뀌었다 — 판정하지 않았다", file=sys.stderr)
            return EXIT_CONFIG
        if reread:
            print(f"{GATE}: 읽는 동안 채널이 바뀌었거나 판정을 확인하려고 디렉토리를 {reread}번 다시 읽었다")
    code, out, err = result
    for line in out:
        print(line)
    for line in err:
        print(line, file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
