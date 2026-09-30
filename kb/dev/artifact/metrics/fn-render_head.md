---
id: https://agentic-knowledge-base.dev/id/chunk/ab27c783-b7b3-4ed2-8fa4-cb2b76c861b7
type: artifact
level: executable
title_ko: 함수 render_head (tools/metrics.py)
title: function render_head in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/88384d9b-995e-4115-9d90-fa034193e045
---
**함수** — `render_head(g, chunks, live, siblings, inputs)` 다. 생성 문서의 머리 블록 — 생성기·질의·입력·규모와 뷰 통지다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_head(g, chunks, live, siblings, inputs):
    """생성 문서의 머리 블록 — 생성기·질의·입력·규모와 뷰 통지다."""
    head = kb_lib.gendoc_header(
        "metrics", "코어 지표", "tools/metrics.py",
        "그래프 union 과 청크 본문에서 — plane × level 분포 · 고아율 · 도입 단계 세 축의 대리 · 링크 밀도 · 크기 분포 · "
        "정제 완주(CQ19) · 후방 추적 귀속(CQ20) · 가정과 신뢰 등급. 연결 성분과 후방 추적 귀속은 **관측·주석 제외**다 — "
        "관측(memory plane)은 실행의 부산물, 판정 주석(annotation plane)은 산출물에 대한 리뷰라 둘 다 저작된 지식의 "
        "고립을 재는 지표의 대상이 아니다 (유저 승인 2026-09-23 · 2026-09-29, kb_lib.LINKAGE_EXCLUDED_PLANES). "
        "수치를 문서에 적지 않고 여기서 인용한다 (4.6절 뷰 원칙)",
        "bazel build //kg:metrics", inputs,
        f"트리플 {len(g)} ({kb_lib.gendoc_union(inputs)}) · 청크 {len(chunks)}", kb_lib.gendoc_view_notice("청크의 frontmatter 와 본문"),
        input_kind="입력 파일",
        extra=[f"- 청크 {len(chunks)} (살아 있는 것 {len(live)}, deprecated {len(chunks)-len(live)}) · 복합체 {len(siblings)} · 트리플 {len(g)}"])
    return head
```
<!-- 인용 끝 -->
