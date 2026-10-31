---
id: https://agentic-knowledge-base.dev/id/chunk/3cc76427-9237-41d7-b070-9dd0fc86381c
type: artifact
level: executable
title_ko: 함수 main (tools/channel_lint.py)
title: function main in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/106ecd5a-7ab2-49db-b822-0e3c51a30083, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/8857ba5c-fc60-4ee1-a15b-2a87ed72940f, https://agentic-knowledge-base.dev/id/chunk/cce5ab35-03b9-4926-85ac-b6434fe2ecfd, https://agentic-knowledge-base.dev/id/chunk/d2fdf1e1-52ea-4b4d-a14f-5882bfe4b8f8, https://agentic-knowledge-base.dev/id/chunk/d5916f30-3b18-49c6-8f72-8ef1cbcf9bec, https://agentic-knowledge-base.dev/id/chunk/e5e73fb0-c433-4d73-af9c-7c61ec8e4187, https://agentic-knowledge-base.dev/id/chunk/e73edb2b-4f7b-4947-a808-37ba4d35d8d5, https://agentic-knowledge-base.dev/id/chunk/eca585ee-464a-4c02-a09c-f68a54900ecb]
part_of: https://agentic-knowledge-base.dev/id/composite/d356c13f-12da-449f-8621-56cdffd536e1
---
**함수** — `main(argv)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
