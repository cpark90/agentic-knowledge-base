---
id: https://agentic-knowledge-base.dev/id/chunk/c2012ece-9826-4be9-bfdc-24eaf1fda875
type: artifact
level: executable
title_ko: 함수 check_gate_inputs (tools/gen_build.py)
title: function check_gate_inputs in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/13aadb6d-6816-4906-8368-5b13dc8dd3f2, https://agentic-knowledge-base.dev/id/chunk/9ea0c3bb-9662-498e-a0ad-c8a481ad765f]
part_of: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce
---
**함수** — `check_gate_inputs(root)` 다. kb/ 아래 지식 파일 중 소유 패키지의 BUILD 가 이름으로도 glob 으로도 담지 않은 것 → FAIL 줄 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gate_inputs(root: Path) -> list[str]:
    """kb/ 아래 지식 파일 중 소유 패키지의 BUILD 가 이름으로도 glob 으로도 담지 않은 것 → FAIL 줄 목록.

    BUILD 자신과 `.bzl`(생성 modules.bzl)은 지식 파일이 아니다. 판정은 BUILD 본문의 문자열 대조다 — 따옴표 친 상대
    경로 하나, 또는 exclude 를 뺀 glob 패턴의 일치. 소스 트리를 직접 걷는다(샌드박스에는 선언된 입력만 있다).
    """
    errors = []
    for top in GATE_INPUT_ROOTS:
        for f in sorted(p for p in (root / top).rglob("*") if p.is_file()):
            if f.name in ("BUILD.bazel", "BUILD") or f.suffix == ".bzl":
                continue
            d = f.parent
            while _build_of(d) is None and d != root:
                d = d.parent
            build = _build_of(d)
            rel = f.relative_to(d).as_posix()
            text = build.read_text(encoding="utf-8") if build else ""
            covered = f'"{rel}"' in text or any(
                any(_glob_pattern(p).match(rel) for p in _QUOTED.findall(m.group(1)))
                and not any(_glob_pattern(p).match(rel) for p in _QUOTED.findall(m.group(2) or ""))
                for m in _GLOB_CALL.finditer(text))
            if not covered:
                where = build.relative_to(root).as_posix() if build else "없음"
                errors.append(f"{f.relative_to(root).as_posix()}: 어느 filegroup·kb_chunk 에도 들지 않는다 — 소유 패키지의 "
                              f"BUILD({where})가 이 파일을 이름으로도 glob 으로도 담지 않아 어떤 게이트도 보지 않는다. "
                              f"gen_build 가 아는 패키지로 옮기거나 그 디렉토리를 생성기에 더한다 (pe-knowledge-files-are-gate-inputs)")
    return errors
```
<!-- 인용 끝 -->
