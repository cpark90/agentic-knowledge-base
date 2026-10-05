---
id: https://agentic-knowledge-base.dev/id/chunk/575bb79d-bb07-4c7f-ade1-9f09032e28fc
type: artifact
level: executable
title_ko: 절 -gendoc-head-errors (tools/kb_lib.py)
title: section -gendoc-head-errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
composite: {id: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09, title_ko: 절 복합체 -gendoc-head-errors (tools/kb_lib.py), title: section composite -gendoc-head-errors in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/575bb79d-bb07-4c7f-ade1-9f09032e28fc, https://agentic-knowledge-base.dev/id/chunk/2c1b164b-eed1-4874-8bee-b8c56033e286, https://agentic-knowledge-base.dev/id/chunk/532a2677-5c0a-4466-b71b-87289153985f, https://agentic-knowledge-base.dev/id/chunk/845f9424-b055-43c1-bbc8-afa6627dffe2, https://agentic-knowledge-base.dev/id/chunk/3140660f-80b6-4277-88a8-ef61335d1da5, https://agentic-knowledge-base.dev/id/chunk/e95cd557-a497-404a-9265-5ebfe0776084], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `-gendoc-head-errors` 다. 규약 판정 — 규칙군마다 함수 하나이고 `check_gendoc` 이 그것을 합친다 (gendoc 게이트의 본체)

**정의** — `_gendoc_head_errors` · `_gendoc_outline_errors` · `_gendoc_block_errors` · `_gendoc_prose_errors` · `check_gendoc` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 규약 판정 — 규칙군마다 함수 하나이고 `check_gendoc` 이 그것을 합친다 (gendoc 게이트의 본체) ────────────
# 군을 넷으로 가른 기준은 **무엇을 입력으로 보는가**다 — 머리 블록은 본문 앞 몇 줄, 뼈대는 행 목록,
# 블록은 펜스·목차·링크(문서 밖까지), 산문은 산문 조각이다. 합계는 정렬해 내므로 군의 순서가 결과를 바꾸지 않는다.
```
<!-- 인용 끝 -->
