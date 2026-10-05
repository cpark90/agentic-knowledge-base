---
id: https://agentic-knowledge-base.dev/id/chunk/98497cab-a974-4398-9ff8-276884ea85f2
type: artifact
level: executable
title_ko: 함수 vv_independence (tools/metrics.py)
title: function vv_independence in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/281c4f1d-6048-495f-872e-1aa02b250baa
---
**함수** — `vv_independence(g, chunks)` 다. V&V KB(`kb/vv/`) 청크 중 생성자가 vnv 역할도 프로세스도 아닌 것을 돌려준다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def vv_independence(g, chunks):
    """V&V KB(`kb/vv/`) 청크 중 생성자가 vnv 역할도 프로세스도 아닌 것을 돌려준다 (유저 결정 2026-10-04 — 독립성).

    git 의 커밋 메시지·작성자는 역할을 담지 않으므로 frontmatter `generated.by` 의 역할 접두로 센다. 상태와 무관하게 센다 —
    쓴 사실은 deprecated 가 되어도 남는다. writer 게이트와 달리 인수(`verified`)로 면제하지 않는다.
    """
    loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in chunks}
    vv_all = [c for c in chunks if kb_lib.kb_of(loc[c]) == kb_lib.KB_VV]
    by = {c: str(next(g.objects(c, AGT.generatedBy), "")) for c in vv_all}
    producers = Counter(b_.split("/")[0] for b_ in by.values())
    outsiders = sorted((c for c in vv_all if not (by[c].startswith(VNV_PRODUCER) or by[c].startswith(PROCESS_PRODUCER))), key=str)
    return vv_all, producers, outsiders
```
<!-- 인용 끝 -->
