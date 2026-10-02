---
id: https://agentic-knowledge-base.dev/id/chunk/8ff423dc-3a52-4a82-83f5-c41d0305a753
type: artifact
level: executable
title_ko: 장 link-targets (tools/chunk2kg.py)
title: chapter link-targets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/067a8c81-640e-4b58-8235-c18119d80f2e
composite: {id: https://agentic-knowledge-base.dev/id/composite/067a8c81-640e-4b58-8235-c18119d80f2e, title_ko: 장 복합체 link-targets (tools/chunk2kg.py), title: chapter composite link-targets in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/8ff423dc-3a52-4a82-83f5-c41d0305a753, https://agentic-knowledge-base.dev/id/composite/eb257ae0-1a24-4c24-8425-e44c940a91b2, https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828, https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**장** — `tools/chunk2kg.py` 의 장 `link-targets` 다. 링크 — 방출·정체성·재기저

**정의** — 없음. 선언과 상수만 있는 구역이다.

**하위 구역** — `link-targets` · `is-link-block` · `merge` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ══ 링크 — 방출·정체성·재기저 ════════════════════
# 링크를 트리플로 내고, 분할 조각의 링크를 뿌리 uuid 로 되돌린다. 두 절이 한 장인 까닭은 링크의 정체성
# 규칙(`link_hash`·`work_id`)이 재기저의 입력이기 때문이다 — 파일 복합체의 직접 부분 상한 9(4.5절)에
# 맞추려고 자른 묶음이 아니다 (p7-code-links-on-file-composite).
```
<!-- 인용 끝 -->
