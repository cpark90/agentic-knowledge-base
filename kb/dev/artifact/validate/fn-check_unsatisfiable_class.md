---
id: https://agentic-knowledge-base.dev/id/chunk/19b5263d-b450-496e-a214-49f3f4b0c0be
type: artifact
level: executable
title_ko: 함수 check_unsatisfiable_class (tools/validate.py)
title: function check_unsatisfiable_class in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe, https://agentic-knowledge-base.dev/id/chunk/da2d5667-a0ed-4a3d-bfa8-6a83213f1d3f]
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
---
**함수** — `check_unsatisfiable_class(found, ontology, onto_files)` 다. 불만족 클래스 (게이트 `unsatisfiable-class`, 유저 결정 Q179-a) — `probe_unsatisfiable` 의 결과를 근원마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_unsatisfiable_class(found: dict, ontology: Graph, onto_files: dict[str, Graph]) -> list[str]:
    """불만족 클래스 (게이트 `unsatisfiable-class`, 유저 결정 Q179-a) — `probe_unsatisfiable` 의 결과를 근원마다 한 줄로 적는다.

    단언된 계층(`told_superclasses`)에서 불만족인 상위 클래스를 가진 불만족 클래스는 같은 근거를 물려받은 것이므로 따로 줄을 내지
    않고 근원 줄에 하위 클래스로 적는다. 단언된 계층에서 서로 상위인 둘은 각자 근원이다. <경로> 자리는 클래스를 선언한 온톨로지
    파일이다.
    """
    gate = UNSATISFIABLE_CLASS
    told = {c: told_superclasses(ontology, c) for c in found}

    def below(c, s):  # 단언된 계층에서 c 가 s 의 엄격한 하위다
        return c != s and s in told[c] and c not in told[s]

    errors = []
    for c in sorted(found, key=str):
        if any(below(c, s) for s in found):
            continue
        heirs = sorted((_term(ontology, d) for d in found if below(d, c)))
        tail = f" · 같은 근거로 불만족인 하위 클래스 {', '.join(heirs)}" if heirs else ""
        errors.append(f"[{gate}] {_axiom_file(onto_files, (c, RDF.type, OWL.Class))}: 클래스 {_term(ontology, c)} 는 개체를 가질 수 "
                      f"없다 — {'; '.join(found[c])}{tail}")
    return errors
```
<!-- 인용 끝 -->
