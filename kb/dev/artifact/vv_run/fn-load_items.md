---
id: https://agentic-knowledge-base.dev/id/chunk/5f53b16a-56e0-4dc8-886e-c0e202e515c8
type: artifact
level: executable
title_ko: 함수 load_items (tools/vv_run.py)
title: function load_items in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2c7856fb-c6fb-42fb-bc34-c18e19362e57, https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/4fa89da6-040b-46a2-8dda-692155b66811, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e, https://agentic-knowledge-base.dev/id/chunk/fad9cc7c-a705-42d5-adcc-e124bff2c57c]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `load_items(root, kind, only, waivers)` 다. `kind`(case · verifier) 자리의 청크 → 항목 목록과 실행 명령 줄이 없는 항목 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_items(root: Path, kind: str, only: list[str], waivers: list[dict]) -> tuple[list[dict], list[str]]:
    """`kind`(case · verifier) 자리의 청크 → 항목 목록과 실행 명령 줄이 없는 항목 목록. 항목의 꼴은 `load_cases` 와 같고 `kind` 를 더한다.

    검증기는 케이스와 같은 파서·같은 형식 검사(`case_spec`·`check_case`)·같은 분류(`classify`)를 지난다 — 읽는 꼴이 같아야
    판정 규칙이 같다. 자리가 없으면(검증기 디렉토리가 없는 트리) 빈 목록이다.
    """
    files = sorted((root / KINDS[kind]).glob("*.md"))
    if only:
        files = [f for f in files if f.stem in only]
    cases, missing = [], []
    for f in files:
        meta, _ = parse_chunk(str(f))
        body = kb_lib.chunk_body(f.read_text(encoding="utf-8"))
        line = next((m for ln in body.splitlines() if (m := COMMAND_LINE.match(ln.strip()))), None)
        if line is None:
            missing.append(f.stem)
            continue
        cmds = [c for c in SPLIT.split(line.group(1).strip()) if c]
        spec, errs = case_spec(body)
        errs += check_case(spec, cmds)
        waived = bool(errs) and (kb_lib.waived(waivers, CASE_GATE, f.as_posix(), "파일") or kb_lib.waived(waivers, CASE_GATE, f.stem, "stem"))
        if waived:
            spec = {}
        cases.append({"kind": kind, "slug": f.stem, "path": f.as_posix(), "label": meta["title_ko"], "iri": meta["id"], "status": meta["status"],
                      "spec": spec, "errors": errs, "waived": waived,
                      "commands": [{"cmd": c, "skip": classify(c, spec), "mismatch": []} for c in cmds]})
    return cases, missing
```
<!-- 인용 끝 -->
