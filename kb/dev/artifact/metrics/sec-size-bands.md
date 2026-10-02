---
id: https://agentic-knowledge-base.dev/id/chunk/a06576f5-13b5-4fff-9209-3e6fefa2667f
type: artifact
level: executable
title_ko: 절 size-bands (tools/metrics.py)
title: section size-bands in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f, https://agentic-knowledge-base.dev/id/chunk/1f7d15d7-e85d-42dd-bef3-fb9c9a6d0365]
part_of: https://agentic-knowledge-base.dev/id/composite/dcc3c5a3-a8bd-4eb2-8d59-01f4ab1d6e3a
composite: {id: https://agentic-knowledge-base.dev/id/composite/dcc3c5a3-a8bd-4eb2-8d59-01f4ab1d6e3a, title_ko: 절 복합체 size-bands (tools/metrics.py), title: section composite size-bands in tools/metrics.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/a06576f5-13b5-4fff-9209-3e6fefa2667f, https://agentic-knowledge-base.dev/id/chunk/32847258-f1c4-4168-8add-3c90daa63de3, https://agentic-knowledge-base.dev/id/chunk/3da75bed-e0cb-4848-a438-30001f43fea2], part_of: https://agentic-knowledge-base.dev/id/composite/c6d68e53-8445-4ac7-a4d6-7d59dd3b3ca6}
---
**절** — `tools/metrics.py` 의 절 `size-bands` 다. 신뢰 등급과 크기 분포

**정의** — `size_bucket` · `trust_and_size` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 신뢰 등급과 크기 분포 ────────────────────

SIZE_BANDS = (0.25, 0.50, 0.75, 0.90)  # 상한에 대한 비율의 칸 경계 — 마지막 칸이 "상한의 9/10 초과"다
# 칸의 제목 — 분모는 그 청크의 plane 상한이다. 분수로 적는 이유는 생성 문서 규약 G15 다: 백분율은 `n/d = p.p%`
# 꼴이어야 하고 분모 없는 `25%` 는 거부된다 — 칸 이름은 측정값이 아니라 구간이므로 분수·구간 서술로 적는다
SIZE_HEADER = "| 상한의 1/4 이하 | 1/2 이하 | 3/4 이하 | 9/10 이하 | 9/10 초과 |"
```
<!-- 인용 끝 -->
