---
id: https://agentic-knowledge-base.dev/id/chunk/f5c8131e-c94d-4c0b-82fe-9e7ad9d36c69
type: artifact
level: executable
title_ko: 함수 coedit_short (tools/kb_lib.py)
title: function coedit_short in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb
---
**함수** — `coedit_short(iri)` 다. 관측에 적는 단위 지식 IRI 의 짧은 꼴 — `id/` 뒤의 국소 이름이고, `chunk/<uuid>` 는 uuid 앞 8자로 줄인다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def coedit_short(iri: str) -> str:
    """관측에 적는 단위 지식 IRI 의 짧은 꼴 — `id/` 뒤의 국소 이름이고, `chunk/<uuid>` 는 uuid 앞 8자로 줄인다.

    짧은 꼴이 겹치는 항목은 관측을 쓰는 쪽이 국소 이름 전체로 적는다. 읽는 쪽(`coedit_pairs`)은 두 꼴을 다 푼다.
    """
    local = iri[len(str(ID)):] if iri.startswith(str(ID)) else iri
    m = _COEDIT_UUID.match(local)
    return f"chunk/{m.group(1)}" if m else local
```
<!-- 인용 끝 -->
