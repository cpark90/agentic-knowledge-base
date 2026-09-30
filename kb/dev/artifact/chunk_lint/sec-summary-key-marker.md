---
id: https://agentic-knowledge-base.dev/id/chunk/bf3a3a02-0578-4230-b071-968e7d887de1
type: artifact
level: executable
title_ko: 절 summary-key-marker (tools/chunk_lint.py)
title: section summary-key-marker in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/d93492e4-f343-4736-b4a5-d04f48a3a75f, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
composite: {id: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118, title_ko: 절 복합체 summary-key-marker (tools/chunk_lint.py), title: section composite summary-key-marker in tools/chunk_lint.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/bf3a3a02-0578-4230-b071-968e7d887de1, https://agentic-knowledge-base.dev/id/chunk/4978379c-7c15-4dc1-9832-9ada51fe6cf0, https://agentic-knowledge-base.dev/id/chunk/b61b3d07-041e-43c2-bb5d-cf3239db7602, https://agentic-knowledge-base.dev/id/chunk/8f6003ae-4fdf-49cc-b1d5-d299b6f34395, https://agentic-knowledge-base.dev/id/chunk/b2c2e02d-e0ff-47a5-ae59-c97c4f96b895], part_of: https://agentic-knowledge-base.dev/id/composite/f1d91f37-d353-405b-bd98-41132f8d5390}
---
**절** — `tools/chunk_lint.py` 의 절 `summary-key-marker` 다. 요약 지지 참조 (게이트 id summary-support, judge-without-service-2026-09-30 기계 환원 ①)

**정의** — `check_summary_support` · `split_frontmatter` · `check_decision_role` · `check_blocking_comment` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 요약 지지 참조 (게이트 id summary-support, judge-without-service-2026-09-30 기계 환원 ①) ──────────────────
# "요약은 집계다" — 요약 블록의 `핵심:` 항목마다 본문의 지지 블록을 가리키는 참조가 있어야 한다(유저 항목이 정의한
# 검사, docs/feedback/judge-without-service-2026-09-30.md "요약 — `핵심:` 항목을 지지하는 블록이 있는가"). 이 저장소는
# 아직 `[#id]` 참조 체계를 쓰지 않으므로 참조는 이미 통용되는 셋 중 하나로 받는다 — `[#id]` 앵커, `d-NNNN` 결정
# 식별자(백틱), IRI(백틱), 마크다운 링크. 슬롯이 없는 청크는 검사하지 않는다 — 판정 대상 0건은 PASS 다.
SUMMARY_KEY_MARKER = "핵심:"
SUMMARY_REF_RE = re.compile(r"\[#[^\]]+\]|`(?:d-\d{4}|https?://\S+|agt:\S+)`|\[[^\]]+\]\([^)]+\)")
```
<!-- 인용 끝 -->
