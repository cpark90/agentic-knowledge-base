#!/usr/bin/env python3
"""채널 게이트 — 유저 피드백 채널(docs/feedback)의 역할 규약을 기계로 강제한다.

규약(docs/feedback/README.md, .claude/agents/hci.md): hci 는 소통만 한다. 유저의 구두 답은 담당 역할(orchestrator 등)에게
유효한 지시이지만, **hci 는 어떤 답이든 채널 밖에 반영하지 않는다** — 답을 `## 답` 에 옮기고 `handoff/` 항목으로 담당 역할에
넘긴다(유저 교정 2026-09-11, agrtls-practices-review-2026-09-12 F).

검사 (게이트 id `channel`):
  lane        경로로 판별 — 유저 lane(docs/feedback/*.md) · agents/ · inquiries/ · handoff/. `*.wip.md` 는 작성 중 — 건너뛴다(집계만)
  status      lane 별 허용 값 — 유저 open|approved|rejected (approved·rejected 는 유저만 태깅; lint 는 값만 본다)
              · agents open|relayed|answered|closed · inquiries open|answered|closed · handoff open|closed. 어휘 밖 → FAIL.
              status 가 없는 파일(유저의 자유 서술)은 검사하지 않고 INFO 로 센다
  handoff     `source` 가 실재하는 유저 lane 파일, `verdict` ∈ apply|apply-with-changes|needs-decision,
              필수 절 `## 파급효과` `## 반영 계획` `## 확인 못 한 것` `## 판정` → 아니면 FAIL
  ref         agents 항목의 `ref`(선택)는 실재해야 한다 — `handoff/<파일>` 또는 유저 lane 파일 → 아니면 FAIL
  pair        verdict apply·apply-with-changes 이고 open 인 handoff 항목을 `ref` 하는 agents 항목이 있으면 "되돌아옴",
              없으면 "되돌아오지 않은 handoff N건" 으로 보고(FAIL 아님 — pending)
  hci-reflect hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있는 항목은 해소 기록이 있어야 한다 —
              `인수: <역할> …` 줄(2026-09-12 이전 관례) **또는** 그 항목(또는 그것을 source 로 갖는 handoff 항목)을 `ref` 하는
              agents 항목, 또는 closed(되돌림). 둘 다 없으면 FAIL. 절 제목의 서명 "(hci, 날짜)" 는 소통의 표기이지 반영 표지가 아니다
  pending     `## 답` 에 유저 답이 옮겨졌으나 반영 기록(인수·ref)이 없는 항목 → 담당 역할 대기로 보고
  placeholder 답 절에 placeholder(`(유저가 채움` · `(hci가 유저의 답을 채움`)가 남은 항목은 처리 대상 아님 — 집계만
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일(규약 문서·원장). 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음) · 3 검사 미실행(항목 0건). SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md <채널 md 파일...>
"""
import argparse
import re
import sys
from pathlib import Path

try:
    from tools.kb_lib import EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # bazel runfiles 경로
except ImportError:
    from kb_lib import EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # 직접 실행

GATE = "channel"
USER, AGENTS, INQUIRIES, HANDOFF = "user", "agents", "inquiries", "handoff"
STATES = {
    USER: {"open", "approved", "rejected"},
    AGENTS: {"open", "relayed", "answered", "closed"},
    INQUIRIES: {"open", "answered", "closed"},
    HANDOFF: {"open", "closed"},
}
VERDICTS = {"apply", "apply-with-changes", "needs-decision"}
RETURNABLE = {"apply", "apply-with-changes"}  # needs-decision 은 유저에게 돌아가는 것이라 agents 짝을 기다리지 않는다
HANDOFF_SECTIONS = ("## 파급효과", "## 반영 계획", "## 확인 못 한 것", "## 판정")
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
TAKEN_OVER = re.compile(r"^인수:\s*(orchestrator|developer|vnv)", re.M)
ANSWERED = re.compile(r"^\*\*유저\(", re.M)
PLACEHOLDER = re.compile(r"\((유저가 채움|hci가 유저의 답을 채움)")


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


def lane_of(p: Path) -> str:
    return p.parent.name if p.parent.name in (AGENTS, INQUIRIES, HANDOFF) else USER


def answer_section(text: str) -> str:
    m = re.search(r"^## 답\b.*$", text, re.M)
    return text[m.start():] if m else text


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--waivers", default="", help="docs/waivers.md — 게이트 id `channel`, 축 파일")
    ap.add_argument("files", nargs="*", help="채널 md 파일")
    a = ap.parse_args(argv)
    if not a.waivers:
        print(f"CONFIG [{GATE}] --waivers <docs/waivers.md> 가 필요하다 — 면제는 코드가 아니라 선언으로", file=sys.stderr)
        return EXIT_CONFIG
    try:
        waivers = load_waivers(a.waivers)
    except (OSError, ValueError) as e:
        print(f"CONFIG [{GATE}] {e}", file=sys.stderr)
        return EXIT_CONFIG

    items, errors, config, pending = {}, [], [], []
    wip, exempt, not_ready, no_status = [], [], [], []
    for path in a.files:
        p = Path(path)
        if p.suffix != ".md":
            continue
        if p.name.endswith(".wip.md"):
            wip.append(path)
            continue
        if waived(waivers, GATE, path, "파일"):
            exempt.append(path)
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            config.append(f"{path}: 읽을 수 없다 — {e.strerror}")
            continue
        lane = lane_of(p)
        meta = frontmatter(text) or {}
        status = meta.get("status")
        if not status:
            no_status.append(path)  # 유저의 자유 서술(형식 제약 없음, README)은 status 가 없을 수 있다 — 검사 밖이지만 침묵하지 않는다
            continue
        if status not in STATES[lane]:
            errors.append(f"{path}: {lane} lane 의 status {status!r} 는 허용 값이 아니다 ({'|'.join(sorted(STATES[lane]))})")
            continue
        it = {"path": path, "name": p.name, "lane": lane, "status": status, "meta": meta, "text": text,
              "root": p.parent.parent if lane != USER else p.parent}
        if PLACEHOLDER.search(answer_section(text)):
            not_ready.append(path)
            continue
        items[path] = it

    # lane 별 형식 검사 — handoff 는 source·verdict·필수 절, agents 는 ref 실재
    refs = set()  # agents 항목이 가리키는 대상: "handoff/<파일>" 또는 "<유저 lane 파일>"
    for it in items.values():
        m, root, path = it["meta"], it["root"], it["path"]
        if it["lane"] == HANDOFF:
            src = m.get("source", "")
            if not src or "/" in src or not (root / src).is_file():
                errors.append(f"{path}: source {src!r} 는 실재하는 유저 lane 파일이어야 한다")
            if m.get("verdict") not in VERDICTS:
                errors.append(f"{path}: verdict {m.get('verdict')!r} 는 {'|'.join(sorted(VERDICTS))} 중 하나여야 한다")
            missing = [h for h in HANDOFF_SECTIONS if not re.search(rf"^{re.escape(h)}(\s|$)", it["text"], re.M)]
            if missing:
                errors.append(f"{path}: 필수 절이 없다 — {' · '.join(missing)}")
        elif it["lane"] == AGENTS and m.get("ref"):
            ref = m["ref"]
            ok = (ref.startswith("handoff/") and ref.count("/") == 1 or "/" not in ref) and (root / ref).is_file()
            if ok:
                refs.add(ref)
            else:
                errors.append(f"{path}: ref {ref!r} 가 실재하지 않는다 — handoff/<파일> 또는 유저 lane 파일이어야 한다")

    handoffs = [it for it in items.values() if it["lane"] == HANDOFF]

    def returned(it) -> bool:
        """이 항목의 반영을 담당 역할이 자기 lane(agents/)에서 ref 로 인수했는가."""
        if it["lane"] == HANDOFF:
            return f"handoff/{it['name']}" in refs
        if it["lane"] == USER:
            return it["name"] in refs or any(
                h["meta"].get("source") == it["name"] and f"handoff/{h['name']}" in refs for h in handoffs)
        return False

    # 쌍 대조 — 반영하라는 handoff 가 되돌아왔는가 (보고)
    for h in handoffs:
        if h["meta"].get("verdict") in RETURNABLE and h["status"] == "open" and not returned(h):
            pending.append(f"{h['path']}: 되돌아오지 않은 handoff (verdict {h['meta']['verdict']}) — 담당 역할이 agents/ 에 ref 로 인수")
    unreturned = len(pending)

    # hci-reflect · pending
    for it in items.values():
        if it["status"] == "closed":
            continue
        text = it["text"]
        if HCI_REFLECTED.search(text):
            if not (TAKEN_OVER.search(text) or returned(it)):
                errors.append(f"{it['path']}: hci 가 채널 밖에 반영했다 — 담당 역할이 검토 뒤 agents/ 항목에서 ref 로 인수하거나(유지, "
                              f"옛 관례 `인수: <역할> <날짜>` 줄도 인정) 되돌리고 closed 로 (hci 는 소통만 한다)")
        elif ANSWERED.search(text) and not returned(it):
            pending.append(f"{it['path']}: 유저 답이 옮겨졌다 — 담당 역할의 반영 대기")

    for n in no_status:
        print(f"INFO [{GATE}] {n}: frontmatter 에 status 가 없다 — 유저 자유 서술로 보고 검사하지 않는다 (hci 항목이면 status 를 넣는다)")
    for w in pending:
        print(f"WAIT [{GATE}] {w}")
    for c in config:
        print(f"CONFIG [{GATE}] {c}", file=sys.stderr)
    for e in errors:
        print(f"FAIL [{GATE}] {e}", file=sys.stderr)
    if config:
        print(f"CONFIG [{GATE}] 입력 문제 {len(config)}건 — 판정하지 않았다", file=sys.stderr)
        return EXIT_CONFIG
    if errors:
        print(f"FAIL [{GATE}] {len(errors)}건 — hci 는 반영하지 않는다. 담당 역할이 인수하거나 되돌린다", file=sys.stderr)
        return EXIT_FAIL
    counts = {lane: sum(1 for it in items.values() if it["lane"] == lane) for lane in (USER, AGENTS, INQUIRIES, HANDOFF)}
    tally = (f"면제 {len(exempt)}건(waivers.md) · 작성 중 {len(wip)}건 · status 없음 {len(no_status)}건 · 처리 대상 아님 {len(not_ready)}건 · "
             f"담당 역할 대기 {len(pending) - unreturned}건 · 되돌아오지 않은 handoff {unreturned}건")
    if not items:
        print(f"SKIP [{GATE}] 검사한 항목이 0건이다 — 통과가 아니다 ({tally})", file=sys.stderr)
        return EXIT_SKIP
    print(f"OK {GATE}: 항목 {len(items)}개 (유저 {counts[USER]} · agents {counts[AGENTS]} · inquiries {counts[INQUIRIES]} · "
          f"handoff {counts[HANDOFF]}), {tally}")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
