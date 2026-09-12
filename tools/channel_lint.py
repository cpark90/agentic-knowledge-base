#!/usr/bin/env python3
"""채널 게이트 — 유저 피드백 채널(docs/feedback)의 역할 규약을 기계로 강제한다.

규약(docs/feedback/README.md, .claude/agents/hci.md): hci 는 소통만 한다. 유저의 구두 답은 담당 역할(orchestrator 등)에게
유효한 지시이지만, **hci 는 어떤 답이든 채널 밖에 반영하지 않는다** — 답을 `## 답` 에 옮기고 담당 역할에 넘긴다
(유저 교정 2026-09-11: "구두로 답을 줬더라도 orchestrator 는 수행해도 되는데 hci 는 작업을 수행하면 안 됨").

검사:
  status      허용 값 안인가 (open | approved | answered | relayed | closed)
  hci-reflect hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있는 항목은
              담당 역할의 인수 줄(`인수: <역할> …`)이 있거나 `closed`(되돌림)여야 한다 → 아니면 FAIL.
              절 제목의 서명 "(hci, 2026-09-12)"·"(hci 2026-09-12)" 는 소통의 표기이지 반영 표지가 아니다
  pending     `## 답` 에 유저 답이 옮겨졌으나 반영 기록이 없는 항목 → 담당 역할 대기로 보고
사용: channel_lint.py <채널 md 파일...>
"""
import re
import sys
from pathlib import Path

STATES = {"open", "approved", "answered", "relayed", "closed"}
EXEMPT = {"README.md", "TEMPLATE.md", "purpose-statement.md"}  # 규약 문서·원장은 반영 항목이 아니다
HCI_REFLECTED = re.compile(r"hci 반영|hci ?가 ?(반영|수행)", re.M)  # 서술형만 — 괄호 서명 "(hci, 날짜)" 는 잡지 않는다 (유저 승인 2026-09-12)
TAKEN_OVER = re.compile(r"^인수:\s*(orchestrator|developer|vnv)", re.M)
ANSWERED = re.compile(r"^\*\*유저\(", re.M)


def main() -> int:
    errors, pending = [], []
    for path in sys.argv[1:]:
        p = Path(path)
        if p.name in EXEMPT or (p.parent.name in ("inquiries", "agents") and p.name == "README.md"):
            continue
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^status:\s*(\w+)", text, re.M)
        if not m:
            continue
        status = m.group(1)
        if status not in STATES:
            errors.append(f"{path}: status {status!r} 는 허용 값이 아니다 ({'|'.join(sorted(STATES))})")
            continue
        if HCI_REFLECTED.search(text) and not TAKEN_OVER.search(text) and status != "closed":
            errors.append(f"{path}: hci 가 채널 밖에 반영했다 — 담당 역할이 검토 뒤 `인수: <역할> <날짜>` 줄을 남기거나(유지) 되돌리고 closed 로 (hci 는 소통만 한다)")
        elif ANSWERED.search(text) and not HCI_REFLECTED.search(text) and status != "closed":
            pending.append(f"{path}: 유저 답이 옮겨졌다 — 담당 역할의 반영 대기")
    for w in pending:
        print(f"WAIT [channel] {w}")
    for e in errors:
        print(f"FAIL [channel] {e}", file=sys.stderr)
    if errors:
        print(f"FAIL [channel] {len(errors)}건 — hci 는 반영하지 않는다. 담당 역할이 인수하거나 되돌린다", file=sys.stderr)
        return 1
    print(f"OK channel: 항목 {len(sys.argv)-1}개, 담당 역할 대기 {len(pending)}건")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
