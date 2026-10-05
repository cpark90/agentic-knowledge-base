---
id: https://agentic-knowledge-base.dev/id/chunk/3cc76427-9237-41d7-b070-9dd0fc86381c
type: artifact
level: executable
title_ko: 함수 main (tools/channel_lint.py)
title: function main in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/106ecd5a-7ab2-49db-b822-0e3c51a30083, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/8857ba5c-fc60-4ee1-a15b-2a87ed72940f, https://agentic-knowledge-base.dev/id/chunk/cce5ab35-03b9-4926-85ac-b6434fe2ecfd, https://agentic-knowledge-base.dev/id/chunk/d2fdf1e1-52ea-4b4d-a14f-5882bfe4b8f8, https://agentic-knowledge-base.dev/id/chunk/e5e73fb0-c433-4d73-af9c-7c61ec8e4187]
part_of: https://agentic-knowledge-base.dev/id/composite/d356c13f-12da-449f-8621-56cdffd536e1
---
**함수** — `main(argv)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
