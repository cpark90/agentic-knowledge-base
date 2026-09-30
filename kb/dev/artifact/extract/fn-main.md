---
id: https://agentic-knowledge-base.dev/id/chunk/53e7f5a3-9d6a-4ee0-aa48-22bb700759c8
type: artifact
level: executable
title_ko: 함수 main (tools/extract.py)
title: function main in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
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
    a = ap.parse_args()
    root = Path(os.path.abspath(a.root or os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    src_rel = Path(a.source).as_posix()
    src = root / src_rel
    reg_path = src.with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX)
    try:
        lines, head_end, top = parse_source(src)
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
        b = Builder(src_rel, lines, head_end, top, ids)
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
    return 0
```
<!-- 인용 끝 -->
