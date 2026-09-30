---
id: https://agentic-knowledge-base.dev/id/chunk/19fecaa5-c478-45a8-9b31-82f53550f632
type: artifact
level: executable
title_ko: 절 check-links (tools/doccheck.py)
title: section check-links in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984
composite: {id: https://agentic-knowledge-base.dev/id/composite/9d5ac0bb-b9b3-4682-886f-6b87b409d984, title_ko: 절 복합체 check-links (tools/doccheck.py), title: section composite check-links in tools/doccheck.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/19fecaa5-c478-45a8-9b31-82f53550f632, https://agentic-knowledge-base.dev/id/chunk/4daa5f81-6009-493b-af58-f97f9a3f388c, https://agentic-knowledge-base.dev/id/chunk/d8304dd3-dfe1-49f3-bb99-12294f298b9c, https://agentic-knowledge-base.dev/id/chunk/2674f907-6204-42f7-a25e-6789137904d6, https://agentic-knowledge-base.dev/id/chunk/16c7fdef-8fd8-4248-95ec-85ff4668d9bd], part_of: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d}
---
**절** — `tools/doccheck.py` 의 절 `check-links` 다. 링크·앵커·경로 검사와 실행

**정의** — `check_links` · `check_paths` · `to_rel` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 링크·앵커·경로 검사와 실행 ────────────────────









if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
