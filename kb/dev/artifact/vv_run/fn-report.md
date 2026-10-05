---
id: https://agentic-knowledge-base.dev/id/chunk/b79a944c-fcdd-4100-baf7-9f03da3576b1
type: artifact
level: executable
title_ko: 함수 report (tools/vv_run.py)
title: function report in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/6571b574-6129-4cb6-8626-ee254df01e2a, https://agentic-knowledge-base.dev/id/chunk/82fb6ab2-dfdf-4445-9207-e0a74ab2ab02, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/d28af6b7-569b-4e83-b929-346995aa2fcb, https://agentic-knowledge-base.dev/id/chunk/ddab0191-16a5-4584-9734-a7d026cb29f8, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e]
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `report(now, cases, missing, rev, dirty, env, verifiers, idle)` 다. 보고 — 케이스 절 다음에 검증기 절을 둔다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report(now: datetime, cases: list[dict], missing: list[str], rev: str, dirty: int, env: str,
           verifiers: list[dict] | None = None, idle: list[str] | None = None) -> str:
    """보고 — 케이스 절 다음에 검증기 절을 둔다. 검증기가 없으면 케이스만의 꼴 그대로다.

    `idle` 은 실행 명령 줄이 없는 검증기다 — 케이스와 달리 그 줄이 필수가 아니다(도구 자신을 서술하는 검증기). 결함이 아니라 실행 대상 밖이다.
    """
    verifiers, idle = list(verifiers or []), list(idle or [])
    items = list(cases) + verifiers
    n, nc, nv = counts(items), counts(cases), counts(verifiers)
    verdict = ("**fail 있음**" if n["fail"] else "pass 없음 — 전부 skip" if not n["pass"] else "pass" + (" (skip 있음)" if n["skip"] else ""))
    skip_note = (f"- 건너뛴 명령: **{n['건너뜀']}** / 명령 {n['명령']} — 건너뛴 명령이 있는 케이스는 pass 가 아니라 skip 이다 "
                 f"(음성 자극이 건너뛰어지면 \"게이트가 거부한다\" 를 보이는 절반이 빈다)")
    expect_line = (f"- 기대 대조: **{n['대조']}** / 실행 {n['실행']} — 기대(`exit`·`contains`)를 적은 명령은 종료 코드와 문구가 둘 다 맞아야 "
                   f"맞은 것이다. 어긋난 명령 {n['어긋남']}건 (`yaml` 펜스가 없는 케이스는 종료 0 만 본다 — 점진 도입)")
    paths = [c["path"] for c in items]
    what = ("V&V 케이스 청크(`kb/vv/case/`)와 검증기 청크(`kb/vv/verifier/`)" if verifiers else "V&V 케이스 청크(`kb/vv/case/`)")
    input_kind = "케이스·검증기 파일" if verifiers else "케이스 파일"
    verifier_count = f"검증기 {len(verifiers)} (pass {nv['pass']} · fail {nv['fail']} · skip {nv['skip']}) · " if verifiers else ""
    rep = kb_lib.gendoc_header(
        "vv_run", "V&V 케이스 실행 판정", "tools/vv_run.py",
        f"{what}의 실행 명령 중 허용 목록의 읽기 전용 검증기만 실제로 돌려 케이스의 기대와 대조해 "
        "케이스마다 pass·fail·skip 을 — SKIP 은 PASS 가 아니다 (8.20절)",
        "bazel run //tools:vv_run", paths,
        f"케이스 {len(cases)} (pass {nc['pass']} · fail {nc['fail']} · skip {nc['skip']}) · {verifier_count}명령 {n['명령']} "
        f"(실행 {n['실행']} · 건너뜀 {n['건너뜀']})",
        kb_lib.gendoc_view_notice("V&V 케이스 청크의 본문"), input_kind=input_kind,
        extra=[f"- 결과: {verdict}", skip_note, expect_line,
               f"- 초기 상태: 리비전 `{rev}` (워킹트리 추적 파일 변경 {revision_note(dirty)}) · {env}",
               f"- 재현 불가 후보: **{kb_lib.pct(len(items) if dirty else 0, len(items))}** (목표 0) — 워킹트리에 추적 파일 변경이 "
               f"있는 실행의 케이스 판정은 같은 리비전을 다시 체크아웃해도 같은 입력에서 나오지 않는다 (현상 `agt:concurrentSessionState`)"])
    body = ["## 케이스 — 실행 대상은 허용 목록의 읽기 전용 검증기뿐. SKIP 은 PASS 가 아니다", "",
            "| 케이스 | 라벨 | 명령 | 자극·기대 | 결과 | 소요 |", "|---|---|---|---|---|---|"] + item_table(cases)
    body += ["", "## 명령", "", "| 케이스 | 명령 | 종료 | 기대 | 소요 | 비고 |", "|---|---|---|---|---|---|"] + command_table(cases)
    if verifiers:
        body += ["", f"## 검증기 — `{VERIFIER_DIR}/` 의 실행 명령. 허용 목록·기대 대조·판정 규칙은 케이스와 같다", "",
                 "| 검증기 | 라벨 | 명령 | 자극·기대 | 결과 | 소요 |", "|---|---|---|---|---|---|"] + item_table(verifiers)
        body += ["", "## 검증기 명령", "", "| 검증기 | 명령 | 종료 | 기대 | 소요 | 비고 |", "|---|---|---|---|---|---|"] + command_table(verifiers)
    off = [(c["kind"], c["slug"], x) for c in items for x in c["commands"] if x["mismatch"]]
    if off:
        body += ["", "## 어긋난 명령 — 기대와 실제", ""]
        for kind, slug, x in off:
            who = "검증기 " if kind == "verifier" else ""
            body += [f"### {who}`{slug}` — `{x['cmd']}` (종료 {x['rc']})", ""] + [f"- {b}" for b in x["mismatch"]] + ["", "```text", x["tail"], "```", ""]
    if missing:
        body += ["", f"실행 명령 줄이 없는 케이스 {len(missing)}건: " + ", ".join(f"`{m}`" for m in missing) + " — 케이스 본문에 `**실행 명령**` 줄(대시 뒤 코드 스팬 하나)이 있어야 한다"]
    if idle:
        body += ["", f"실행 명령 줄이 없는 검증기 {len(idle)}건: " + ", ".join(f"`{m}`" for m in idle) +
                 " — 실행 대상 밖이다. 검증기는 케이스와 달리 그 줄이 필수가 아니다(도구 자신을 서술하는 검증기)"]
    return kb_lib.gendoc_assemble(rep, body, paths, input_kind=input_kind)
```
<!-- 인용 끝 -->
