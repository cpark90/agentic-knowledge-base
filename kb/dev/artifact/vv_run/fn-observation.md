---
id: https://agentic-knowledge-base.dev/id/chunk/4dc64a35-fb4f-4396-838d-acef3f4e186c
type: artifact
level: executable
title_ko: 함수 observation (tools/vv_run.py)
title: function observation in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `observation(now, cases, rev, dirty, env)` 다. 실행 기록 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def observation(now: datetime, cases: list[dict], rev: str, dirty: bool, env: str) -> str:
    """실행 기록 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory). frontmatter 는 assume_check 의 관측과 같은 형식이다."""
    stamp = kb_lib.utc_stamp(now)  # G3 표기 하나 — frontmatter 와 본문이 같은 꼴을 쓴다 (유저 승인 2026-09-23)
    n = counts(cases)
    ko = f"V&V 실행 {stamp}: pass {n['pass']} · fail {n['fail']} · skip {n['skip']}"
    en = f"V&V run {stamp}: {n['pass']} pass, {n['fail']} fail, {n['skip']} skip"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    body = [f"**관측** — {stamp} 에 `vv_run` 이 케이스 {len(cases)}건의 실행 명령 {n['명령']}건 중 "
            f"허용 목록의 검증기 {n['실행']}건을 실행하고 그중 {n['대조']}건을 케이스의 기대(`exit`·`contains`)와 대조했다. "
            f"리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else '없음'}) · {env} · seed 없음.", "",
            kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        skipped = len(c["commands"]) - ran
        note = tests_note(c["commands"])
        body.append(f"| `{c['slug']}` | {ran} 실행 · {skipped} 건너뜀{' (' + note + ')' if note else ''} | {c['verdict']} | {c['secs']:.1f}s |")
    skips = [(c["slug"], x) for c in cases for x in c["commands"] if x["skip"] is not None]
    if skips:
        body += ["", "| 케이스 | 건너뛴 명령 | 사유 |", "|---|---|---|"]
        rows = [f"| `{slug}` | `{x['cmd'][:60]}{'…' if len(x['cmd']) > 60 else ''}` | {x['skip']} |" for slug, x in skips]
        budget = MAX_BODY_LINES - len(body) - 3  # 남는 줄 — 요약 2줄과 여유
        if len(rows) > budget:
            rows = rows[:max(budget - 1, 0)] + [f"| … | 외 {len(rows) - max(budget - 1, 0)}건 | 보고(`vv_run` 출력)에 전부 있다 |"]
        body += rows
    body += ["", f"판정 요약 — 케이스 pass {n['pass']} · fail {n['fail']} · skip {n['skip']} · 명령 실행 {n['실행']} · 건너뜀 {n['건너뜀']} · "
             f"기대 대조 {n['대조']} · 어긋남 {n['어긋남']}. SKIP 은 PASS 가 아니다 — 건너뛴 명령이 있는 케이스는 skip 이다. "
             f"기대를 적은 명령은 종료 코드와 `contains` 문구가 둘 다 맞아야 맞은 것이고, 적지 않은 명령은 종료 0 만 본다."]
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
