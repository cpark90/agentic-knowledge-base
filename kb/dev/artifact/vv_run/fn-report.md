---
id: https://agentic-knowledge-base.dev/id/chunk/b79a944c-fcdd-4100-baf7-9f03da3576b1
type: artifact
level: executable
title_ko: 함수 report (tools/vv_run.py)
title: function report in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `report(now, cases, missing, rev, dirty, env)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report(now: datetime, cases: list[dict], missing: list[str], rev: str, dirty: bool, env: str) -> str:
    n = counts(cases)
    verdict = ("**fail 있음**" if n["fail"] else "pass 없음 — 전부 skip" if not n["pass"] else "pass" + (" (skip 있음)" if n["skip"] else ""))
    skip_note = (f"- 건너뛴 명령: **{n['건너뜀']}** / 명령 {n['명령']} — 건너뛴 명령이 있는 케이스는 pass 가 아니라 skip 이다 "
                 f"(음성 자극이 건너뛰어지면 \"게이트가 거부한다\" 를 보이는 절반이 빈다)")
    expect_line = (f"- 기대 대조: **{n['대조']}** / 실행 {n['실행']} — 기대(`exit`·`contains`)를 적은 명령은 종료 코드와 문구가 둘 다 맞아야 "
                   f"맞은 것이다. 어긋난 명령 {n['어긋남']}건 (`yaml` 펜스가 없는 케이스는 종료 0 만 본다 — 점진 도입)")
    rep = kb_lib.gendoc_header(
        "vv_run", "V&V 케이스 실행 판정", "tools/vv_run.py",
        "V&V 케이스 청크(`kb/vv/case/`)의 실행 명령 중 허용 목록의 읽기 전용 검증기만 실제로 돌려 케이스의 기대와 대조해 "
        "케이스마다 pass·fail·skip 을 — SKIP 은 PASS 가 아니다 (8.20절)",
        "bazel run //tools:vv_run", [c["path"] for c in cases],
        f"케이스 {len(cases)} (pass {n['pass']} · fail {n['fail']} · skip {n['skip']}) · 명령 {n['명령']} "
        f"(실행 {n['실행']} · 건너뜀 {n['건너뜀']})",
        kb_lib.gendoc_view_notice("V&V 케이스 청크의 본문"), input_kind="케이스 파일",
        extra=[f"- 결과: {verdict}", skip_note, expect_line,
               f"- 초기 상태: 리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else kb_lib.NONE_MARK}) · {env}"])
    body = ["## 케이스 — 실행 대상은 허용 목록의 읽기 전용 검증기뿐. SKIP 은 PASS 가 아니다", "",
            "| 케이스 | 라벨 | 명령 | 자극·기대 | 결과 | 소요 |", "|---|---|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        spec = c["spec"]
        machine = " · ".join(filter(None, [f"자극 {len(spec['files'])}" if spec.get("files") else "",
                                           f"기대 {len(spec['expect'])}" if spec.get("expect") else ""])) or kb_lib.NONE_MARK
        body.append(f"| `{c['slug']}` | {c['label']} | {ran} 실행 · {len(c['commands']) - ran} 건너뜀 | {machine} | **{c['verdict']}** | {c['secs']:.1f}s |")
    body += ["", "## 명령", "", "| 케이스 | 명령 | 종료 | 기대 | 소요 | 비고 |", "|---|---|---|---|---|---|"]
    for c in cases:
        for x in c["commands"]:
            if x["skip"] is None:
                t = x.get("tests")
                note = (f"테스트 {t[0]} · 실행 {t[1]} · 캐시 {t[0] - t[1]}" if t else "요약 줄 없음" if x["cmd"].startswith("bazel test ") else "") + \
                       ("" if not x["mismatch"] else " · **어긋남**")
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | {x['rc']} | {expect_note(x.get('expect'))} | {x['secs']:.1f}s | {note or kb_lib.NONE_MARK} |")
            else:
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | SKIP | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {x['skip']} |")
    off = [(c["slug"], x) for c in cases for x in c["commands"] if x["mismatch"]]
    if off:
        body += ["", "## 어긋난 명령 — 기대와 실제", ""]
        for slug, x in off:
            body += [f"### `{slug}` — `{x['cmd']}` (종료 {x['rc']})", ""] + [f"- {b}" for b in x["mismatch"]] + ["", "```text", x["tail"], "```", ""]
    if missing:
        body += ["", f"실행 명령 줄이 없는 케이스 {len(missing)}건: " + ", ".join(f"`{m}`" for m in missing) + " — 케이스 본문에 `**실행 명령**` 줄(대시 뒤 코드 스팬 하나)이 있어야 한다"]
    return kb_lib.gendoc_assemble(rep, body, [c["path"] for c in cases], input_kind="케이스 파일")
```
<!-- 인용 끝 -->
