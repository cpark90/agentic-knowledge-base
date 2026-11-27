---
id: https://agentic-knowledge-base.dev/id/chunk/264d9fd1-b338-48ec-9eb9-9ca20577aecc
type: artifact
level: executable
title_ko: 함수 owl_rl_closure (tools/validate.py)
title: function owl_rl_closure in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `owl_rl_closure(asserted)` 다. 단언 그래프의 OWL 2 RL 폐포와 추론기의 오류 메시지 — 단언 그래프는 그대로 두고 사본을 넓힌다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def owl_rl_closure(asserted: Graph) -> tuple[Graph, list[str]]:
    """단언 그래프의 OWL 2 RL 폐포와 추론기의 오류 메시지 — 단언 그래프는 그대로 두고 사본을 넓힌다.

    owlrl 은 모순을 만나면 멈추지 않고 오류 노드(`err:ErrorMessage` 개체와 `err:error` 문자열)를 폐포에 더한다. 오류 노드는
    메시지로 꺼내고 폐포에서 지운다 — 단언 어휘 밖의 노드라 shape 적합성의 입력이 아니다.
    """
    import owlrl
    from owlrl.Namespaces import ERRNS

    closed = Graph()
    closed += asserted
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(closed)
    messages = set()
    for node in list(closed.subjects(RDF.type, ERRNS.ErrorMessage)):
        messages.update(str(m) for m in closed.objects(node, ERRNS.error))
        closed.remove((node, None, None))
    return closed, sorted(messages)
```
<!-- 인용 끝 -->
