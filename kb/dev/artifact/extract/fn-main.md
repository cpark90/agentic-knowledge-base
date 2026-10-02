---
id: https://agentic-knowledge-base.dev/id/chunk/53e7f5a3-9d6a-4ee0-aa48-22bb700759c8
type: artifact
level: executable
title_ko: 함수 main (tools/extract.py)
title: function main in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0ee2e47f-3e9a-4742-8506-41a3e3aec54e, https://agentic-knowledge-base.dev/id/chunk/0f9149bc-d39d-4624-bdc2-d97603407e8c, https://agentic-knowledge-base.dev/id/chunk/1f4895e9-23ea-421e-8218-237de7a42713, https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b, https://agentic-knowledge-base.dev/id/chunk/3310d256-a896-401a-ba40-e6bfdc0d474a, https://agentic-knowledge-base.dev/id/chunk/33680335-f485-4267-aa96-2bb505425eaa, https://agentic-knowledge-base.dev/id/chunk/4333655e-49b9-4be9-b2f1-8c28243d8390, https://agentic-knowledge-base.dev/id/chunk/73d61c8c-9a76-4703-8890-b1aa00936a4e, https://agentic-knowledge-base.dev/id/chunk/745c745f-7657-4a5c-8c72-ce2f06a4af0e, https://agentic-knowledge-base.dev/id/chunk/a03ca02f-5735-4455-b2c7-bbc695c5bf35, https://agentic-knowledge-base.dev/id/chunk/a83e5a5d-15ff-4e18-80b5-2c88dead1cfc, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5]
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="추출할 파이썬 소스 (저장소 상대 경로)")
    ap.add_argument("--root", default="", help="저장소 루트. 없으면 BUILD_WORKSPACE_DIRECTORY, 없으면 현재 디렉토리")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 트리와 비교. 어긋나면 1")
    ap.add_argument("--residency", default="", help="EXTRACTED_SOURCES 리터럴의 원본 defs/kb.bzl — 안 주면 --root 기준")
    ap.add_argument("--vocab", default="", help="토큰 계수기의 어휘 파일 — 생성 청크가 `artifact` 상한 안인지 보고하는 데 쓴다. "
                                               "--check 는 쓰지 않는다 (드리프트 판정에 크기가 들어가지 않는다)")
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    src_rel = Path(a.source).as_posix()
    src = root / src_rel
    reg_path = src.with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX)
    residency = a.residency or root / "defs" / "kb.bzl"
    uses_ids: dict = {}
    try:  # 방출 경계와 치역 경계 — 둘 다 defs/kb.bzl 의 리터럴이 단일 정의처다 (M1)
        uses_sources = frozenset(f"tools/{m}.py" for m in kb_lib.load_extracted_sources(residency))
        if src_rel in uses_sources:  # 치역 경계의 등록부는 `uses` 를 방출하는 소스에서만 입력이다
            uses_ids = {m: load_registry(root / f"tools/{m}{kb_lib.EXTRACT_REGISTRY_SUFFIX}")["ids"]
                        for m in kb_lib.load_extracted_sources(residency, kb_lib.USES_TARGETS_NAME)}
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {residency}: 경계 목록을 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    empty = sorted(m for m, ids_ in uses_ids.items() if not ids_)
    if empty:  # 조용히 비는 사고를 막는다 — 치역 경계 안의 등록부가 없으면 모듈 간 `uses` 가 말없이 0 이 된다
        print(f"FAIL [{TAG}] tools/{empty[0]}{kb_lib.EXTRACT_REGISTRY_SUFFIX}: 치역 경계"
              f"({kb_lib.USES_TARGETS_NAME}, {residency})의 등록부가 비었거나 없다 — {' · '.join(empty)}. "
              f"모듈 간 `{kb_lib.USES_KEY}` 가 조용히 비는 것과 같으므로 통과시키지 않는다", file=sys.stderr)
        return EXIT_CONFIG
    try:
        lines, head_end, top, imports = parse_source(src)
        reg = load_registry(reg_path)
    except (OSError, SyntaxError) as e:
        print(f"FAIL [{TAG}] {src}: 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    if not reg["resource"]:
        print(f"FAIL [{TAG}] {reg_path}: 등록부에 `resource`(소스 파일 개체 IRI)가 없다 — 출처는 kg/base-kg.ttl 의 "
              f"`id:src-…` 개체이고 손으로 세운다", file=sys.stderr)
        return EXIT_CONFIG
    reg["source"], reg["package"] = src_rel, reg["package"] or f"{kb_lib.EXTRACT_ROOT}/{src.stem}"
    pkg_dir = root / reg["package"]
    digest = hashlib.sha256(src.read_bytes()).hexdigest()[:16]
    if reg["source_hash"] != digest or not reg["at"]:
        if a.check:
            print(f"FAIL [{DRIFT_TAG}] {reg_path}: 등록부의 `source_hash` 가 소스와 어긋난다 — "
                  f"`bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 (소스가 원본, 청크는 뷰)", file=sys.stderr)
            return EXIT_FAIL
        reg["at"], reg["source_hash"] = source_stamp(root, src_rel), digest
    names, hashes = collect(top, lines)
    try:
        ids = resolve(reg, names, hashes, pkg_dir, a.check)
        b = Builder(src_rel, lines, head_end, top, ids, uses_sources, imports, uses_ids)
        b.build()
    except ExtractError as e:
        print(f"FAIL [{TAG}] {e}", file=sys.stderr)
        return EXIT_FAIL
    # 링크는 파일 복합체의 것이다 — 파일 청크와 구역 청크(절·장·모듈 머리)가 그 자리다. 정의 청크는 `part_of` 로만
    # 존재해 함수 churn 이 링크를 움직이지 않는다. 모듈 머리 구역에 정의가 없으면 그 청크는 복합체를 선언하지 않고
    # 파일 복합체의 직접 부분이 되는데, 형제가 절 복합체(청크 아님)뿐이라 링크가 없으면 저작된 지식의 연결 성분에서
    # 홀로 남는다 — 실측 2026-09-30(파일 10개 = 성분 +10). 구역 청크는 정의 청크가 아니므로 링크를 받는다.
    for c in b.chunks:
        if c.qname in ("module", "head") or c.composite:
            c.links = {"refines": reg["refines"], "serves": reg["serves"]}
    reg["ids"] = ids.ids
    prev = previous_bodies(pkg_dir)  # 본문이 그대로면 `generated.at` 을 유지한다 — diff 가 변경의 크기를 말해야 한다
    outputs = {}
    for c in b.chunks:
        body = "\n".join(c.body) + "\n"
        was = prev.get(c.fname)
        outputs[pkg_dir / c.fname] = render(c, reg, was[1] if was and was[0] == body and was[1] else "")
    outputs[reg_path] = dump_registry(reg)
    stale = sorted(f for f in pkg_dir.glob("*.md") if f not in outputs) if pkg_dir.exists() else []
    drift = [f for f, text in outputs.items() if not f.exists() or f.read_text(encoding="utf-8") != text] + stale
    if a.check:
        for f in drift:
            if f in stale:
                print(f"FAIL [{DRIFT_TAG}] {f}: 추출이 만들지 않는 파일이다 — 생성 트리에 손으로 둔 파일은 없다")
                continue
            old = f.read_text(encoding="utf-8").splitlines(True) if f.exists() else []
            sys.stdout.writelines(difflib.unified_diff(old, outputs[f].splitlines(True), f"{f} (커밋본)", f"{f} (생성)", n=1))
            print(f"FAIL [{DRIFT_TAG}] {f}: 소스와 어긋난다 — `bazel run //tools:extract -- {src_rel}` 를 돌려 커밋하라 "
                  f"(소스가 원본, 청크는 뷰)")
        if drift:
            print(f"\nFAIL [{DRIFT_TAG}] — {len(drift)}건 / 생성 청크 {len(b.chunks)}개")
            return EXIT_FAIL
        print(f"PASS [{DRIFT_TAG}] — {src_rel} 의 생성 청크 {len(b.chunks)}개와 등록부가 소스와 일치")
        return 0
    pkg_dir.mkdir(parents=True, exist_ok=True)
    for f in stale:
        f.unlink()
    for f, text in outputs.items():
        f.write_text(text, encoding="utf-8")
    comps = sum(1 for c in b.chunks if c.composite)
    print(f"생성 {len(b.chunks)}개 (복합체 {comps}개, 신설 uuid {len(ids.added)}개), 변경 {len(drift)}개: {pkg_dir}")
    # `artifact` 상한 보고 — 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens). 게이트가 아니라 보고다: 거부는
    # chunk_lint(게이트 id `chunk`)의 몫이고 여기서는 추출이 낸 청크 가운데 상한을 넘은 것을 바로 알려준다.
    limit = kb_lib.body_token_limit("artifact")
    enc = kb_lib.load_tokenizer(a.vocab or None)
    over = sorted(((kb_lib.token_count("\n".join(c.body), enc), c.fname) for c in b.chunks), reverse=True)
    high = [(n, f) for n, f in over if n > limit]
    print(f"`artifact` 상한 {limit} 토큰: 초과 {len(high)}개 / 생성 {len(b.chunks)}개 · 최대 {over[0][0] if over else 0} 토큰"
          + ("".join(f"\n  초과 {n} 토큰 — {f}" for n, f in high) if high else ""))
    return 0
```
<!-- 인용 끝 -->
