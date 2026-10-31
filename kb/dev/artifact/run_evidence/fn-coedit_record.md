---
id: https://agentic-knowledge-base.dev/id/chunk/871169c2-b1e9-4386-8e2c-e9140c2becff
type: artifact
level: executable
title_ko: 함수 coedit_record (tools/run_evidence.py)
title: function coedit_record in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/f5c8131e-c94d-4c0b-82fe-9e7ad9d36c69]
part_of: https://agentic-knowledge-base.dev/id/composite/241f90fa-0b02-4c28-a23e-8e84aecaf4da
---
**함수** — `coedit_record(root)` 다. git 이력에서 동시 편집 쌍을 뽑아 관측 하나(kb/dev/memory/obs-coedit-<UTC>.md)로 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def coedit_record(root: Path) -> int:
    """git 이력에서 동시 편집 쌍을 뽑아 관측 하나(kb/dev/memory/obs-coedit-<UTC>.md)로 쓴다 (p10-co-edit-evidence-from-small-commits).

    커밋마다 바뀐 단위 지식 파일(kb_lib.COEDIT_ITEM_PATH)을 세고, 그 수가 kb_lib.COEDIT_MAX_FILES 이하인 커밋만 쓴다. 항목은 지금
    트리의 frontmatter `id` 로 풀고, 지금 없거나 `id` 가 없는 파일은 쌍에서 빼고 센다. 행마다 함께 바뀐 항목들의 모든 두 조합이 쌍이다 —
    쌍을 하나씩 적지 않고 커밋 묶음으로 적어 관측이 memory 의 토큰 상한 안에 든다. 이미 있는 파일은 덮지 않는다.
    """
    log = subprocess.run(["git", "log", "--no-renames", "--name-only", "--format=@@%h %cI"], cwd=root,
                         capture_output=True, text=True, check=True).stdout
    commits: list[tuple[str, str, list[str]]] = []
    for ln in log.splitlines():
        if ln.startswith("@@"):
            sha, at = ln[2:].split(" ", 1)
            commits.append((sha, at, []))
        elif ln.strip() and commits and kb_lib.COEDIT_ITEM_PATH.match(ln.strip()):
            commits[-1][2].append(ln.strip())
    id_line = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
    iri_of: dict[str, str] = {}
    for f in sorted(p.relative_to(root).as_posix() for d in ("kb", "space") if (root / d).is_dir() for p in (root / d).rglob("*.md")):
        text = (root / f).read_text(encoding="utf-8")
        head = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
        m = id_line.search(head)
        if kb_lib.COEDIT_ITEM_PATH.match(f) and m:
            iri_of[f] = m.group(1)
    short_n = Counter(kb_lib.coedit_short(i) for i in iri_of.values())
    form = {i: kb_lib.coedit_short(i) if short_n[kb_lib.coedit_short(i)] == 1 else i[len(ID_BASE):] for i in iri_of.values()}
    touched = [c for c in commits if c[2]]
    small = [c for c in touched if len(set(c[2])) <= kb_lib.COEDIT_MAX_FILES]
    rows, pairs, gone = [], set(), 0
    for sha, at, files in small:
        items = sorted({iri_of[f] for f in set(files) if f in iri_of}, key=lambda i: form[i])
        gone += len(set(files)) - sum(1 for f in set(files) if f in iri_of)
        here = {frozenset((a, b)) for k, a in enumerate(items) for b in items[k + 1:]}
        pairs |= here
        rows.append(f"| `{sha}` | {at} | {len(set(files))} | {len(here)} | " + (" · ".join(f"`{form[i]}`" for i in items) or kb_lib.NONE_MARK) + " |")
    stamp = kb_lib.utc_stamp(datetime.now(timezone.utc))
    span = f"`{commits[-1][0]}`..`{commits[0][0]}`" if commits else kb_lib.NONE_MARK
    out = root / kb_lib.DEV_MEMORY_DIR / f"{kb_lib.COEDIT_PREFIX}{stamp.replace('-', '').replace(':', '')}.md"
    if out.exists():
        print(f"FAIL [run-evidence] {out}: 이미 있다 — 관측은 추가 전용이다", file=sys.stderr)
        return kb_lib.EXIT_CONFIG
    head = ["---", f"id: {ID_BASE}chunk/{uuid.uuid4()}", "type: memory", "level: concrete",
            f"title_ko: 동시 편집 관측 {stamp}: 커밋 {len(small)} · 쌍 {len(pairs)}",
            f"title: Co-edit observation {stamp}: {len(small)} commits, {len(pairs)} pairs", "status: stable",
            f"sources: [{{resource: {ID_BASE}odd-agentic-knowledge-base}}]", f"assumes: [{ID_BASE}asm-chunk-conventions]",
            f"generated: {{by: {kb_lib.COEDIT_GENERATOR}, at: {stamp}}}", "---"]
    body = [f"**관측** — {stamp} 에 `run_evidence --coedit-record` 가 git 이력 {span}(커밋 {len(commits)}개)을 읽었다. 단위 지식 파일"
            f"(`kb/**/*.md` · `space/*.md` · `chunks/**/*.md`)을 바꾼 커밋은 {len(touched)}개다. 그 가운데 바뀐 단위 지식 파일이 "
            f"{kb_lib.COEDIT_MAX_FILES}개 이하인 커밋 {len(small)}개에서 쌍을 뽑았고, 쌍은 중복을 빼고 {len(pairs)}개다. "
            f"지금 트리에 없거나 `id` 가 없어 뺀 파일은 {gone}건이다.", "",
            "항목은 단위 지식 IRI 의 짧은 꼴이다. `chunk/` 뒤의 8자는 uuid 의 앞 8자이고, 짧은 꼴이 겹치는 항목은 `id/` 뒤의 이름 전체로 적었다. "
            "행마다 함께 바뀐 항목들의 모든 두 조합이 쌍이다.", "",
            kb_lib.COEDIT_TABLE_HEADER, "|---|---|---|---|---|"] + rows
    out.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    print(f"[run-evidence] {out.relative_to(root)} — 커밋 {len(small)}/{len(touched)} · 쌍 {len(pairs)} · 뺀 파일 {gone}", file=sys.stderr)
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
