---
id: https://agentic-knowledge-base.dev/id/chunk/d1ca967e-c2f5-4f0e-8d10-03adbb6b5c13
type: artifact
level: executable
title_ko: 함수 agreement (tools/judge.py)
title: function agreement in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/8f3b4eaf-dced-410d-98cc-6771157e17c6
---
**함수** — `agreement(rows)` 다. 행마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def agreement(rows: list[dict]) -> None:
    """행마다 `일치` 열을 채운다 — 같은 (대상, 입력 지문)에 둘 이상의 판정자 응답이 있을 때만 일치·불일치, 단독이면
    해당 없음이다(규칙: 확신도는 자기 보고이므로 단독 응답으로는 자동 적용이 없다)."""
    groups = defaultdict(list)
    for r in rows:
        groups[(r["iri"], r["fingerprint"])].append(r)
    for grp in groups.values():
        if len(grp) < 2:
            tag = kb_lib.JUDGE_AGREEMENT[2]
        else:
            tag = kb_lib.JUDGE_AGREEMENT[0] if len({g["value"] for g in grp}) == 1 else kb_lib.JUDGE_AGREEMENT[1]
        for g in grp:
            g["agree"] = tag
```
<!-- 인용 끝 -->
