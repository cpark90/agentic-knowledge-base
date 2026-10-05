---
id: https://agentic-knowledge-base.dev/id/chunk/a431ac65-77e6-4bb7-a69b-86fc24579df6
type: artifact
level: executable
title_ko: 절 query-lang (tools/extract.py)
title: section query-lang in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166
composite: {id: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166, title_ko: 절 복합체 query-lang (tools/extract.py), title: section composite query-lang in tools/extract.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/a431ac65-77e6-4bb7-a69b-86fc24579df6, https://agentic-knowledge-base.dev/id/chunk/46409669-5368-4022-9a90-fbf7d0d56eaa, https://agentic-knowledge-base.dev/id/chunk/c60ce666-a684-4dc4-8022-ed23dbd14935, https://agentic-knowledge-base.dev/id/chunk/6fd0167b-9fe9-4a4f-96c0-08a4efc53eda, https://agentic-knowledge-base.dev/id/chunk/bea10200-8d45-4fa2-9999-bda8c1935253], part_of: https://agentic-knowledge-base.dev/id/composite/99abae51-6823-4ed8-9bfe-4255801d4681}
---
**절** — `tools/extract.py` 의 절 `query-lang` 다. 질의 디렉토리 — 질의 파일 하나 = 청크 하나 (EXTRACTED_QUERY_DIRS, 2026-10-03)

**정의** — `source_digest` · `collect_queries` · `previous_query_hashes` · `build_queries` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 질의 디렉토리 — 질의 파일 하나 = 청크 하나 (EXTRACTED_QUERY_DIRS, 2026-10-03) ──────────────
# //kg:cq 뷰의 내용 원본(역량 질문 질의)과 //kg:gate_test 의 검증 질의가 코드 청크 밖에 있었다. 파이썬 소스와 같은 방향
# (p7-code-extraction-direction)으로 추출하되 질의는 정의로 나뉘지 않으므로 파일 하나가 청크 하나이고 복합체가 없다.
QUERY_LANG = "sparql"
```
<!-- 인용 끝 -->
