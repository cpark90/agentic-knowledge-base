---
id: https://agentic-knowledge-base.dev/id/chunk/580b14fa-6057-4000-9927-c60a4acee79a
type: artifact
level: executable
title_ko: 함수 stamp_one (tools/stamp.py)
title: function stamp_one in tools/stamp.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-stamp}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:27:50Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/98e08ae7-f85a-4703-809f-fe20c8ac333a]
part_of: https://agentic-knowledge-base.dev/id/composite/9de96dc9-03ab-40b9-a90a-4481f8f9deb7
---
**함수** — `stamp_one(root, reg_path, rev, at)` 다. 등록부 하나에 도장을 찍는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def stamp_one(root: Path, reg_path: Path, rev: str, at: str) -> tuple[str, str]:
    """등록부 하나에 도장을 찍는다 → (소스 경로, 리비전). 커밋되지 않은 소스는 `--rev` 없이 거부한다."""
    reg = load_registry(reg_path)
    if not reg["source"]:
        raise ValueError(f"{reg_path}: 등록부에 `source` 가 없다 — 도장의 대상을 알 수 없다")
    src = root / reg["source"]
    if not src.exists():
        raise ValueError(f"{reg_path}: 소스 {reg['source']} 가 없다")
    if not rev:
        code, dirty = git(root, "status", "--porcelain", "--", reg["source"])
        if code != 0:
            raise ValueError(f"{reg_path}: git 상태를 읽을 수 없다 — {dirty}. 리비전을 아는 호출자가 `--rev` 로 준다")
        if dirty:
            raise ValueError(f"{reg_path}: 소스 {reg['source']} 가 커밋되지 않았다 — 도장의 리비전이 그 내용을 가리키지 "
                             f"않는다. 커밋한 뒤 다시 돌리거나, 리비전을 아는 호출자가 `--rev` 로 준다")
        code, rev = git(root, "rev-parse", "HEAD")
        if code != 0 or not rev:
            raise ValueError(f"{reg_path}: git 리비전을 읽을 수 없다 — `--rev` 로 준다")
    reg["tested"] = {"rev": rev, "at": at, "source_hash": hashlib.sha256(src.read_bytes()).hexdigest()[:16]}
    reg_path.write_text(dump_registry(reg), encoding="utf-8")
    return reg["source"], rev
```
<!-- 인용 끝 -->
