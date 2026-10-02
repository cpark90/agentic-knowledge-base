---
id: https://agentic-knowledge-base.dev/id/chunk/26cee9d2-6c23-40eb-ada2-4d5b1ae63d0c
type: artifact
level: executable
title_ko: 함수 main (tools/chunk_lint.py)
title: function main in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/4978379c-7c15-4dc1-9832-9ada51fe6cf0, https://agentic-knowledge-base.dev/id/chunk/608da358-1b32-4e5f-b999-82b185e41ef4, https://agentic-knowledge-base.dev/id/chunk/77d9a605-dbe6-47d6-a87e-5c042030404f, https://agentic-knowledge-base.dev/id/chunk/8f6003ae-4fdf-49cc-b1d5-d299b6f34395, https://agentic-knowledge-base.dev/id/chunk/9995ae36-ac6f-4afb-9596-0ef58fa2a582, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5, https://agentic-knowledge-base.dev/id/chunk/b2c2e02d-e0ff-47a5-ae59-c97c4f96b895, https://agentic-knowledge-base.dev/id/chunk/b61b3d07-041e-43c2-bb5d-cf3239db7602, https://agentic-knowledge-base.dev/id/chunk/db4948aa-0374-4100-8ea3-fcc9111717da]
part_of: https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--ttl", nargs="*", default=[])
    ap.add_argument("--vocab", default="", metavar="FILE",
                    help="토큰 계수기의 어휘 파일 — 없으면 runfiles 의 고정 파일을 쓴다 (p1-chunk-unit-is-tokens)")
    ap.add_argument("--waivers", default="", metavar="FILE",
                    help=f"docs/waivers.md — 게이트 id {CHUNK}·{PROSE}·{ADDITION}·{EMPTY_VALUE}·{LIST_RULES}·{BLOCKING_COMMENT}·"
                         f"{JUDGE_LOG}·{SUMMARY_SUPPORT}(축 파일)로 면제된 파일의 위반은 세지 않는다. 없으면 면제 없음")
    args = ap.parse_args()

    if not args.chunks and not args.ttl:
        print("SKIP [chunk_lint] 검사 대상 0건 — PASS 가 아니다")
        return EXIT_SKIP

    try:
        waivers = kb_lib.load_waivers(args.waivers) if args.waivers else []
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk_lint] waiver 표 — {e}")
        return EXIT_CONFIG

    try:  # 어휘는 한 번만 적재한다 — 크기 판정이 이 계수기 하나로 재현된다 (ODD id:cond-tokenizer-lock)
        enc = kb_lib.load_tokenizer(args.vocab or None)
    except FileNotFoundError as e:
        print(f"FAIL [chunk_lint] 어휘 파일 — {e}")
        return EXIT_CONFIG
    except ValueError as e:  # 해시가 고정값과 다르다 — 계수기가 재현되지 않는다
        print(f"FAIL [{CHUNK}] {e}")
        return EXIT_FAIL

    errors = []
    waived_notes = []  # 면제된 위반 — 집계에서 빼되 목록에는 남긴다 (docs/waivers.md 머리의 규약, ⑥ 이 선례)
    prose_files = 0
    decision_files = 0  # 역할 표지 검사 대상(살아 있는 결정)의 수 — PASS 줄의 실태
    live_files = 0      # 첨가·목록 검사 대상(살아 있는 .md 청크)의 수
    comment_files = 0   # 주석 검사 대상(살아 있는 annotation 청크)의 수
    judge_logs = 0      # 판정 로그 검사 대상의 수 — 0 이면 거부할 것이 없고 그것은 SKIP 이 아니라 PASS 다
    summary_files = 0   # 요약 지지 참조 검사 대상(`핵심:` 슬롯을 쓴 살아 있는 청크)의 수

    for f in args.chunks:
        p = Path(f)
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            print(f"FAIL [{CHUNK}] {f}: 읽을 수 없다 — {e}")
            return EXIT_CONFIG
        n = kb_lib.token_count(kb_lib.body_text(p, text), enc)
        plane = split_frontmatter(text)[0].get("type") if p.suffix == ".md" else None
        limit = kb_lib.body_token_limit(plane)  # plane 별 프로파일 파라미터 — 정의처는 kb_lib.BODY_TOKEN_LIMITS 하나다
        if n > limit:
            line = (
                f"[{CHUNK}] {f}: 본문 {n}토큰 > {limit}토큰 — 분할하라 (4.10절 분할 신호"
                + (f"; plane {plane} 의 상한은 프로파일 파라미터다 — kb_lib.BODY_TOKEN_LIMITS)" if limit != MAX_BODY_TOKENS else ")")
            )
            (waived_notes if kb_lib.waived(waivers, CHUNK, f, "파일") else errors).append(line)
        if p.suffix == ".md":  # 산문 문체·결정 역할 표지 — TTL 은 대상이 아니다
            prose_files += 1
            prose_errors, _, _ = kb_lib.check_prose(f, text, waivers)
            errors += [f"[{PROSE}] {f}:{ln}: {reason}" for ln, reason in prose_errors]
            fields, _, _ = split_frontmatter(text)
            if fields.get("type") == "decision" and fields.get("status") != "deprecated":
                decision_files += 1
            errors += [f"[{DECISION_ROLE}] {f}:{ln}: {reason}" for ln, reason in check_decision_role(p, text)]
            if is_judge_log(fields):  # 판정 로그 — 게이트는 판정을 부르지 않고 로그의 형식만 본다
                judge_logs += 1
                for ln, reason in check_judge_log(text):
                    line = f"[{JUDGE_LOG}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, JUDGE_LOG, f, "파일") else errors).append(line)
            if fields.get("type") == "annotation" and fields.get("status") in kb_lib.LIVE_STATES:
                comment_files += 1
            for ln, reason in check_blocking_comment(text):  # 해소되지 않은 issue (blocking) — 주석의 유일한 게이트 효과
                line = f"[{BLOCKING_COMMENT}] {f}:{ln}: {reason}"
                (waived_notes if kb_lib.waived(waivers, BLOCKING_COMMENT, f, "파일") else errors).append(line)
            if fields.get("status") in kb_lib.LIVE_STATES:  # 보고(consistency)와 같은 대상 집합 — invalidated·deprecated 는 기록이다
                live_files += 1
                for gate, ln, reason in check_spec_form(text):
                    line = f"[{gate}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, gate, f, "파일") else errors).append(line)
                if any(l.strip() == SUMMARY_KEY_MARKER or l.strip().startswith(SUMMARY_KEY_MARKER + " ")
                       for l in text.splitlines()):
                    summary_files += 1
                for ln, reason in check_summary_support(text):
                    line = f"[{SUMMARY_SUPPORT}] {f}:{ln}: {reason}"
                    (waived_notes if kb_lib.waived(waivers, SUMMARY_SUPPORT, f, "파일") else errors).append(line)

    for f in args.ttl:
        stem = Path(f).stem
        if not any(stem == s.lstrip("-") or stem.endswith(s) for s in ALLOWED_TTL_SUFFIXES):
            errors.append(
                f"[{NAMING}] {f}: 접미사 규약 위반 — {', '.join(ALLOWED_TTL_SUFFIXES)} 중 하나로 끝나야 한다 (0.2절)"
            )

    for w in waived_notes:
        print(f"WAIVED {w} (waivers.md — 집계에서 뺐다)")
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [chunk_lint] — {len(errors)}건 (면제 {len(waived_notes)}건)")
        return EXIT_FAIL

    print(f"PASS [chunk_lint] — 청크 {len(args.chunks)}개 (산문 검사 {prose_files}개, 결정 역할 표지 {decision_files}개, "
          f"첨가·목록 {live_files}개, 주석 {comment_files}개, 판정 로그 {judge_logs}개, 요약 지지 참조 {summary_files}개, "
          f"면제 {len(waived_notes)}건), TTL {len(args.ttl)}개")
    return 0
```
<!-- 인용 끝 -->
