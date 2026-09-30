---
id: https://agentic-knowledge-base.dev/id/chunk/135475ce-ddaa-4fff-8e37-dd26b1e3277d
type: artifact
level: executable
title_ko: 함수 read (tools/extract_refs.py)
title: function read in tools/extract_refs.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract-refs}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-19T14:57:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/444fc7bd-680b-4c09-aec8-0e5de0cc1175
---
**함수** — `read(path)` 다. (자기 IRI, specializationOf 대상 IRI 또는 "", 본문).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def read(path: str) -> tuple[str, str, str]:
    """(자기 IRI, specializationOf 대상 IRI 또는 "", 본문). frontmatter는 인용 대상이 아니므로 뺀다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: frontmatter가 없다")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError(f"{path}: frontmatter가 닫히지 않았다")
    iri, spec = "", ""
    for l in lines[1:end]:
        if l.startswith("id:"):
            iri = l.split(":", 1)[1].strip()
        elif l.startswith(SPECIALIZATION_KEY + ":"):  # 뿌리 uuid 계산용 — 값 검증은 chunk2kg 의 몫
            spec = l.split(":", 1)[1].strip().strip("'\"")
    if not iri:
        raise ValueError(f"{path}: frontmatter에 id 가 없다 (OKF 확장 키, uuid IRI)")
    return iri, spec, "\n".join(lines[end + 1 :])
```
<!-- 인용 끝 -->
