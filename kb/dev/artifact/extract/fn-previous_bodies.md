---
id: https://agentic-knowledge-base.dev/id/chunk/a03ca02f-5735-4455-b2c7-bbc695c5bf35
type: artifact
level: executable
title_ko: 함수 previous_bodies (tools/extract.py)
title: function previous_bodies in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/bdbaec34-7407-4d5e-83f8-0706026f0b98
---
**함수** — `previous_bodies(pkg_dir)` 다. 트리의 생성 청크 → {파일 이름: (본문, generated.at)}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def previous_bodies(pkg_dir: Path) -> dict:
    """트리의 생성 청크 → {파일 이름: (본문, generated.at)}. `generated.at` 의 보존 규칙이 이 값을 쓴다.

    청크의 `generated.at` 은 **그 청크의 본문이 바뀐 추출에서만** 갱신된다. 소스 파일의 시각(등록부 `at`)을 모든 청크에
    다시 찍으면 실제 변경 한 건이 diff 96건이 되어 무엇이 바뀌었는지가 보이지 않는다 — 생성물의 diff 는 변경의 크기를
    말해야 한다. 값의 원본은 트리이므로 `--check` 의 재생성은 그대로 결정론이다.
    """
    out = {}
    if not pkg_dir.is_dir():
        return out
    for f in sorted(pkg_dir.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            continue
        m = re.search(r"^generated: \{by: [^,]+, at: ([^}]+)\}$", parts[1], re.M)
        out[f.name] = (parts[2], m.group(1).strip() if m else "")
    return out
```
<!-- 인용 끝 -->
