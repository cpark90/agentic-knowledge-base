---
id: https://agentic-knowledge-base.dev/id/chunk/f535cb9d-5732-45d9-857d-ac0129c7eead
type: artifact
level: executable
title_ko: 함수 generate (tools/gen_norms.py)
title: function generate in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0eed9071-0543-4627-8e10-d058808ca3cc, https://agentic-knowledge-base.dev/id/chunk/412335c9-3334-4503-8547-23227e453d66, https://agentic-knowledge-base.dev/id/chunk/b036d7e1-16f6-449e-a9cd-4ad07e213b53, https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `generate(root, docs, only)` 다. {출력 경로(루트 상대): 내용} — `only` 가 있으면 그 문서만 낸다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def generate(root: Path, docs: dict[str, str], only: str = "") -> dict[str, str]:
    """{출력 경로(루트 상대): 내용} — `only` 가 있으면 그 문서만 낸다. 판정은 언제나 문서 전체로 한다(고아·이중 소비)."""
    norm_dirs = sorted(p.name for p in (root / NORM_ROOT).iterdir() if p.is_dir()) if (root / NORM_ROOT).is_dir() else []
    if sorted(docs) != norm_dirs:
        raise GenNormsError(f"{NORM_ROOT}: 문서 디렉토리 {norm_dirs} 와 defs/kb.bzl 의 {NORM_DOCS_NAME} 키 {sorted(docs)} 가 다르다 — "
                            f"문서 목록의 단일 정의처는 {NORM_DOCS_NAME} 이고 디렉토리마다 항목 하나다")
    outs = list(docs.values())
    bad = [o for o in outs if not o.endswith(".md") or o.startswith(("/", "../")) or outs.count(o) > 1]
    if bad:
        raise GenNormsError(f"defs/kb.bzl {NORM_DOCS_NAME}: 출력 경로는 저장소 상대의 서로 다른 .md 파일이다 — {sorted(set(bad))}")
    if only and only not in docs:
        raise GenNormsError(f"--doc {only}: {NORM_DOCS_NAME} 에 없는 문서다 — {sorted(docs)}")
    conventions = load_conventions(root)
    loaded, _uses = plan(root, docs, conventions)
    return {docs[s]: render(s, docs[s], loaded[s], conventions) for s in sorted(docs) if not only or s == only}
```
<!-- 인용 끝 -->
