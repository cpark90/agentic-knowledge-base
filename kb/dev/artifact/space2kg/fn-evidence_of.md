---
id: https://agentic-knowledge-base.dev/id/chunk/a17c39f7-acf4-442e-a8e3-c996b7156e77
type: artifact
level: executable
title_ko: 함수 evidence_of (tools/space2kg.py)
title: function evidence_of in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/fc3f9858-3941-435d-b741-071b871ce613
---
**함수** — `evidence_of(path, where, value, polarity)` 다. 증거 항목 → [(종류, 참조)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def evidence_of(path: str, where: str, value, polarity: str) -> list[tuple[str, str]]:
    """증거 항목 → [(종류, 참조)]. 종류는 evidence-ontology 의 개체 이름이어야 한다."""
    items = value if isinstance(value, list) else [value]
    out = []
    for item in items:
        if not isinstance(item, dict) or sorted(item) != sorted(EVIDENCE_KEYS):
            raise SpaceError(f"{path}: {where} 의 증거는 {{{', '.join(EVIDENCE_KEYS)}}} 여야 한다 — 실제 {item!r}")
        kind, ref = str(item["kind"]), str(item["ref"])
        if kind not in EVIDENCE_KINDS:
            raise SpaceError(f"{path}: {where} 의 증거 종류 {kind!r} 가 어휘 밖이다 — {' | '.join(EVIDENCE_KINDS)} 중 하나다 "
                             f"(evidence-ontology, 10.8절)")
        if not ref:
            raise SpaceError(f"{path}: {where} 의 증거에 ref 가 비어 있다 — 극성 {polarity} 의 증거는 실체를 가리켜야 한다 (9.11절)")
        out.append((kind, ref))
    return out
```
<!-- 인용 끝 -->
