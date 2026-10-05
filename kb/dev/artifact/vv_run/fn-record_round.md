---
id: https://agentic-knowledge-base.dev/id/chunk/d213b57a-b3ec-4271-aba1-114f98f7a4c7
type: artifact
level: executable
title_ko: 함수 record_round (tools/vv_run.py)
title: function record_round in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2393909a-601a-49e0-bc99-833dc33318cb, https://agentic-knowledge-base.dev/id/chunk/9cb93d1c-7ae3-49f8-8812-213367f8a3e4, https://agentic-knowledge-base.dev/id/chunk/cad21a57-2adb-46fe-b8c7-82cd106906ed, https://agentic-knowledge-base.dev/id/chunk/f0e6f002-4d5d-46c0-abba-ab242b4572e4]
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `record_round(root, reason, now)` 다. 라운드 하나를 닫는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def record_round(root: Path, reason: str, now: datetime | None = None) -> int:
    """라운드 하나를 닫는다 — `kb/vv/run/round-<UTC>.md` 를 append-only 로 쓴다. 이미 있으면 덮지 않는다."""
    now = now or datetime.now(timezone.utc).replace(microsecond=0)
    try:
        bounds = [b for b in round_records(root) if b < now]
        defects = defect_times(root)
    except ValueError as e:
        print(f"FAIL [vv_run] {e}")
        return EXIT_CONFIG
    counts_ = round_counts(bounds + [now], defects)
    n, k = len(bounds) + 1, counts_[-1]
    prev_k = counts_[-2] if n > 1 else None
    target = root / RUN_DIR / f"{ROUND_PREFIX}{now.strftime('%Y%m%dT%H%M%SZ')}.md"
    if target.exists():
        print(f"FAIL [vv_run] {target.relative_to(root)}: 이미 있다 — 라운드 기록은 append-only 다 (r-026)")
        return EXIT_CONFIG
    if n > 2 and counts_[-2] >= counts_[-3] and reason != "stop-rule":
        print(f"WARN [vv_run] 라운드 {n - 1} 에서 정지 규칙이 성립했다(신규 {counts_[-3]} → {counts_[-2]}) — 라운드 {n} 을 "
              f"`{reason}` 로 닫으면 verify 질의 `{STOP_RULE_QUERY}` 가 게이트에서 거부한다. 사유는 `stop-rule` 이다")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(round_observation(now, n, bounds[-1] if bounds else None, k, reason, prev_k), encoding="utf-8")
    print(f"라운드 기록: {target.relative_to(root)} — 라운드 {n} · 신규 결함 {k} · 종료 사유 {ROUND_REASONS[reason][1]}. "
          f"python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    return EXIT_OK
```
<!-- 인용 끝 -->
