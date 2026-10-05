---
id: https://agentic-knowledge-base.dev/id/chunk/1939bb14-28c6-4fc3-a367-bf91e805c37e
type: artifact
level: executable
title_ko: 함수 render_vv_extra (tools/metrics.py)
title: function render_vv_extra in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/fa0aa6c4-7e2a-449b-9f07-9dd03faa3122
---
**함수** — `render_vv_extra(g, pct, vv_all, producers, outsiders, mutations)` 다. 7단계 대리의 독립성과 변이 검출률 행 (유저 결정 2026-10-04).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_vv_extra(g, pct, vv_all, producers, outsiders, mutations):
    """7단계 대리의 독립성과 변이 검출률 행 (유저 결정 2026-10-04)."""
    loc = lambda c: str(next(g.objects(c, AGT.assertionLocation), "")) or kb_lib.NONE_MARK
    o = [f"- 연결: 독립성 — V&V KB(`kb/vv/`) 청크 {len(vv_all)}건(deprecated 포함) 중 생성자가 vnv 역할(`{VNV_PRODUCER}`)도 프로세스(`{PROCESS_PRODUCER}`)도 "
         f"아닌 것 **{len(outsiders)}**건 (목표 0). git 커밋의 메시지·작성자는 역할을 담지 않으므로 frontmatter `generated.by` 의 접두로 센다. 생성자 접두: "
         + " · ".join(f"`{k_}` {v_}" for k_, v_ in producers.most_common())
         + ("; 해당 청크: " + " · ".join(f"`{loc(c)}`" for c in outsiders) if outsiders else "")]
    if mutations is None:
        o.append("- 의미 보존: 변이 검출률 — `--mutations` 없음")
        return o
    bound = [r for r in mutations if r[3]]
    kinds = Counter(r[0] for r in mutations)
    o.append(f"- 의미 보존: 변이 검출률 — `defs/tests` 의 변이(음성) 고정물 {len(mutations)}건 중 기대 FAIL 문구를 단 `//...` 시험에 묶인 것 "
             f"**{pct(len(bound), len(mutations))}** (목표 100.0%; 종류별 " + " · ".join(f"{k_} {v_}" for k_, v_ in kinds.most_common()) + "). "
             "잡힘의 판정은 묶인 시험의 통과다 — `bazel test //...` 가 초록이면 묶인 고정물이 전부 기대 FAIL 로 잡혔다. 묶이지 않은 고정물: "
             + (" · ".join(f"`{r[1]}`({r[0]})" for r in mutations if not r[3]) or "없음"))
    return o
```
<!-- 인용 끝 -->
