---
id: https://agentic-knowledge-base.dev/id/chunk/62282fc9-a79e-49d7-bfc5-535eee72d480
type: artifact
level: executable
title_ko: 함수 check_frozen (tools/doccheck.py)
title: function check_frozen in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2674f907-6204-42f7-a25e-6789137904d6]
part_of: https://agentic-knowledge-base.dev/id/composite/00affe30-5483-412c-9fa9-9df66b0b6eaf
---
**함수** — `check_frozen(files, root, workdir)` 다. 동결 문서의 sha256 이 `kb_lib.FROZEN_DOCS` 의 고정값과 같은지 본다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_frozen(files: list[str], root: Path, workdir: str | None) -> list[str]:
    """동결 문서의 sha256 이 `kb_lib.FROZEN_DOCS` 의 고정값과 같은지 본다 — 고치려면 상수를 같은 커밋에서 바꿔야 한다.

    입력에 없는 등록 문서도 위반이다 — 대조할 파일이 runfiles 에 없으면 동결이 판정되지 않는다.
    """
    import hashlib

    errors = []
    given = {to_rel(f, root, workdir).as_posix() for f in files}
    for rel in sorted(set(kb_lib.FROZEN_DOCS) - given):
        errors.append(f"{rel}: 동결 문서가 입력에 없다 — kb_frozen_docs_test 의 docs 에 넣는다")
    for rel in sorted(given):
        want = kb_lib.FROZEN_DOCS.get(rel)
        if want is None:
            errors.append(f"{rel}: kb_lib.FROZEN_DOCS 에 없는 문서다 — 동결하려면 해시를 등록한다")
            continue
        got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if got != want:
            errors.append(f"{rel}: sha256 {got[:12]} 이 고정값 {want[:12]} 과 다르다 — 동결 문서는 고치지 않는다. "
                          f"의도한 정정이면 kb_lib.FROZEN_DOCS 의 값을 같은 커밋에서 바꾼다")
    return errors
```
<!-- 인용 끝 -->
