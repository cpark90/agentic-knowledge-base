---
id: https://agentic-knowledge-base.dev/id/chunk/00df23de-726e-45ab-a8e1-5e8a278a2020
type: artifact
level: executable
title_ko: 절 -id-line (tools/label_sample.py)
title: section -id-line in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
composite: {id: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7, title_ko: 절 복합체 -id-line (tools/label_sample.py), title: section composite -id-line in tools/label_sample.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/00df23de-726e-45ab-a8e1-5e8a278a2020, https://agentic-knowledge-base.dev/id/chunk/46efd740-da05-4865-b292-1d80e216e5b3, https://agentic-knowledge-base.dev/id/chunk/ab2cbe51-0701-4753-859c-1019a3b9808f, https://agentic-knowledge-base.dev/id/chunk/db984d6d-3345-4aed-bb9c-6fb4465d7923, https://agentic-knowledge-base.dev/id/chunk/aa162d57-f8c9-4997-886c-33e23f8cab0a, https://agentic-knowledge-base.dev/id/chunk/a614648d-b67b-4026-ba49-0d8fa41d0a09, https://agentic-knowledge-base.dev/id/chunk/8d6f25bd-f8f1-47b2-a82d-4f2b6d19cd91, https://agentic-knowledge-base.dev/id/chunk/a1fe4e07-ebf7-4d59-8408-970b8c42755d, https://agentic-knowledge-base.dev/id/chunk/81b17e03-73ce-4c98-82c3-5847b168ced5], part_of: https://agentic-knowledge-base.dev/id/composite/06cd565d-e749-42fe-88da-1a56fd71a2a5}
---
**절** — `tools/label_sample.py` 의 절 `-id-line` 다. 쌍 판정지 (--pair-sheet)

**정의** — `view_candidates` · `pair_judge_targets` · `index_items` · `kind_definitions` · `item_of` · `write_pair_sheet` · `pair_sheet` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 쌍 판정지 (--pair-sheet) ────────────────────

_ID_LINE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)










_ITEMS: dict = {}










if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
