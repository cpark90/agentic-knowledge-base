---
id: https://agentic-knowledge-base.dev/id/chunk/c67dfe43-f624-4e13-a813-64f0733fbfd6
type: artifact
level: executable
title_ko: 절 link-targets (tools/chunk2kg.py)
title: section link-targets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2
composite: {id: https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2, title_ko: 절 복합체 link-targets (tools/chunk2kg.py), title: section composite link-targets in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c67dfe43-f624-4e13-a813-64f0733fbfd6, https://agentic-knowledge-base.dev/id/chunk/583a95ea-746e-4243-a6d9-108c18a3c9d8, https://agentic-knowledge-base.dev/id/chunk/dae11730-e07f-47c6-becd-61b72a819b12, https://agentic-knowledge-base.dev/id/chunk/4dcdeb22-0819-48a5-96a4-72da225a3003, https://agentic-knowledge-base.dev/id/chunk/1b8a9132-b68b-46c7-a14e-55e7048494e2, https://agentic-knowledge-base.dev/id/chunk/8a9578b7-a0d9-4b0a-951e-aed33d8b8825, https://agentic-knowledge-base.dev/id/chunk/e40d0ed3-5060-4b0e-9dd9-d76acde18c0e], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**절** — `tools/chunk2kg.py` 의 절 `link-targets` 다. 링크의 방출과 정체성

**정의** — `link_targets` · `check_restored` · `link_hash` · `spec_cycles` · `work_id` · `emit_links` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 링크의 방출과 정체성 ────────────────────













LINK_PREFIX = f"{ID_BASE}link/"
EVIDENCE_PREFIX = f"{ID_BASE}evidence/"
_SPEC_LINE = re.compile(r"^    prov:specializationOf <([^>]+)>", re.MULTILINE)
```
<!-- 인용 끝 -->
