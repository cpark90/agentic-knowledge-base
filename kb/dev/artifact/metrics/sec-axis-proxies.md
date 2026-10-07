---
id: https://agentic-knowledge-base.dev/id/chunk/ce2b87f3-39cd-49bd-a7ec-40ffceefda86
type: artifact
level: executable
title_ko: 절 axis-proxies (tools/metrics.py)
title: section axis-proxies in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/8fa054a4-1f2a-4d86-b98d-3c68ca9a4619
composite: {id: https://agentic-knowledge-base.dev/id/composite/8fa054a4-1f2a-4d86-b98d-3c68ca9a4619, title_ko: 절 복합체 axis-proxies (tools/metrics.py), title: section composite axis-proxies in tools/metrics.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/ce2b87f3-39cd-49bd-a7ec-40ffceefda86, https://agentic-knowledge-base.dev/id/chunk/ac4042d4-658b-4464-af33-c3e2da6754d5, https://agentic-knowledge-base.dev/id/chunk/a0050c7a-8e88-4a2e-8172-5ecfcd868dff], part_of: https://agentic-knowledge-base.dev/id/composite/c6d68e53-8445-4ac7-a4d6-7d59dd3b3ca6}
---
**절** — `tools/metrics.py` 의 절 `axis-proxies` 다. 연결 성분과 건너뜀

**정의** — `axis_proxies` · `skip_decomposition` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 연결 성분과 건너뜀 ────────────────────


# V&V 정제 계층 몫의 허용 쌍 — 이름 → (주어 plane, 주어 수준, 대상 plane, 대상 수준). 양 끝이 V&V KB(`kb/vv/`) 안일 때만 뺀다
VV_LADDER_SKIPS = {
    "합격 기준 → 검증 목표": ("contract", "logical", "requirement", "functional"),  # 유저 답 Q30-b
    "검증기 → 합격 기준": ("artifact", "executable", "contract", "logical"),  # 유저 답 Q41-a (2026-10-04)
}
```
<!-- 인용 끝 -->
