---
id: https://agentic-knowledge-base.dev/id/chunk/27bfede1-26a6-411f-9cae-30561bf44dac
type: artifact
level: executable
title_ko: 절 -audit-links (tools/weave.py)
title: section -audit-links in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ebcf6e73-cc0b-447d-ac23-00290abee9ca
composite: {id: https://agentic-knowledge-base.dev/id/composite/ebcf6e73-cc0b-447d-ac23-00290abee9ca, title_ko: 절 복합체 -audit-links (tools/weave.py), title: section composite -audit-links in tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/27bfede1-26a6-411f-9cae-30561bf44dac, https://agentic-knowledge-base.dev/id/chunk/abdec406-8c7d-4178-9fd6-73bc42cea633, https://agentic-knowledge-base.dev/id/chunk/dc36a14b-aeb6-4275-97fc-74eb0e0a9b25, https://agentic-knowledge-base.dev/id/chunk/54a6b278-cb6f-4c88-8935-01b236a2b7ba], part_of: https://agentic-knowledge-base.dev/id/composite/027b8f3a-1382-4deb-a204-543e912d8e6a}
---
**절** — `tools/weave.py` 의 절 `-audit-links` 다. 링크와 증거 — 링크 근거·draft 끝 링크·증거 극성

**정의** — `_audit_links` · `_audit_draft_ends` · `_audit_polarity` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 링크와 증거 — 링크 근거·draft 끝 링크·증거 극성 ────────────────────
# 셋 다 링크 개체와 그 끝·증거를 센다. 앞 절과 가른 까닭은 직접 부분 상한 9 이고, 이 절은 보고의 순서로도 이어진다.





# 설계 공간 파일의 증거 출처 — space2kg 가 `evidence` 를 (+)로, `eliminated_by` 를 (−)로 낸다 (단일 정의 위치 space2kg.evidence_of 의 호출부)
SPACE_EVIDENCE_SOURCE = {"+": "설계 공간 `evidence`", "-": "설계 공간 `eliminated_by`"}
```
<!-- 인용 끝 -->
