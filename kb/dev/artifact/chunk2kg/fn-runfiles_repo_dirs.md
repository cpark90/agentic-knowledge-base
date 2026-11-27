---
id: https://agentic-knowledge-base.dev/id/chunk/a521ceb8-1a46-412a-a169-2cb07a11c69a
type: artifact
level: executable
title_ko: 함수 runfiles_repo_dirs (tools/chunk2kg.py)
title: function runfiles_repo_dirs in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/c0a24368-1326-49c2-a33a-29918b01c696]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `runfiles_repo_dirs(apparent)` 다. apparent 저장소 이름 → runfiles 안의 저장소 디렉토리 후보 (task 0327 손질 4).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def runfiles_repo_dirs(apparent: str) -> list[Path]:
    """apparent 저장소 이름 → runfiles 안의 저장소 디렉토리 후보 (task 0327 손질 4).

    `<뿌리>/_repo_mapping` 의 행(`<출발 canonical>,<apparent>,<대상 canonical>`)에서 apparent 이름이 같은 행의 대상을
    먼저 보고, 매핑 파일이 없으면 이름이 `apparent` 이거나 `+<apparent>` 로 끝나는 디렉토리를 본다. 같은 apparent 이름을
    다른 모듈이 다른 저장소에 쓸 수 있으나 어휘 파일은 sha256 대조(`load_tokenizer`)가 거부하므로 후보가 여럿이어도 된다.
    """
    out: list[Path] = []
    for root in runfiles_roots() + [Path("external")]:
        names: list[str] = []
        mapping = root / "_repo_mapping"
        if mapping.is_file():
            for line in mapping.read_text(encoding="utf-8").splitlines():
                parts = line.split(",")
                if len(parts) == 3 and parts[1] == apparent and parts[2] not in names:
                    names.append(parts[2])
        if root.is_dir():
            names += sorted(d.name for d in root.iterdir()
                            if d.is_dir() and (d.name == apparent or d.name.endswith("+" + apparent)) and d.name not in names)
        out += [root / n for n in names if (root / n).is_dir() and root / n not in out]
    return out
```
<!-- 인용 끝 -->
