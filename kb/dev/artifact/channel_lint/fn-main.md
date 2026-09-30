---
id: https://agentic-knowledge-base.dev/id/chunk/3cc76427-9237-41d7-b070-9dd0fc86381c
type: artifact
level: executable
title_ko: 함수 main (tools/channel_lint.py)
title: function main in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T11:29:42Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `main(argv)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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

    # hci-reflect (유저 lane 만) · pending
    for it in items.values():
        if it["status"] == "closed":
            continue
        text = it["text"]
        if it["lane"] == USER and HCI_REFLECTED.search(text):
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
```
<!-- 인용 끝 -->
