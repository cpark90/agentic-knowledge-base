---
id: https://agentic-knowledge-base.dev/id/chunk/5da3c712-5990-4584-8692-01c92cb88b80
type: artifact
level: executable
title_ko: 절 main (tools/gendoc.py)
title: section main in tools/gendoc.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gendoc}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b6587551-3784-48fb-ae97-e98493afa24b
composite: {id: https://agentic-knowledge-base.dev/id/composite/b6587551-3784-48fb-ae97-e98493afa24b, title_ko: 절 복합체 main (tools/gendoc.py), title: section composite main in tools/gendoc.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5da3c712-5990-4584-8692-01c92cb88b80, https://agentic-knowledge-base.dev/id/chunk/20316b94-1015-4306-8624-0463e63dd849], part_of: https://agentic-knowledge-base.dev/id/composite/f2a94f2c-1866-41da-848c-d018a7dfc647}
---
**절** — `tools/gendoc.py` 의 절 `main` 다. 생성 문서 규약 G1~G18 을 판정한다

**정의** — `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 생성 문서 규약 G1~G18 을 판정한다 ────────────────────



if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
