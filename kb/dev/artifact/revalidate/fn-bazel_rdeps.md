---
id: https://agentic-knowledge-base.dev/id/chunk/98b89c74-895c-4fc5-94d8-8db422c2b0f4
type: artifact
level: executable
title_ko: 함수 bazel_rdeps (tools/revalidate.py)
title: function bazel_rdeps in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `bazel_rdeps(cwd, owners, universe)` 다. 소유 타깃마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def bazel_rdeps(cwd: str, owners: list, universe: str) -> dict:
    """소유 타깃마다 (직접 의존자, 전이 의존자). 질의 한 번 — 유도 부분그래프를 받아 여기서 닫는다."""
    if not owners:
        return {}
    expr = f'kind("{ITEM_KINDS}", rdeps({universe}, set({" ".join(owners)})))'
    r = subprocess.run(["bazel", "query", expr, "--noshow_progress", "--output=graph", "--nograph:factored"], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        print(f"WARN [revalidate] bazel query 실패 — 하류 의존자 없이 보고한다: {expr}")
        return {o: (None, None) for o in owners}
    rdep = defaultdict(set)  # 대상 → 그것에 직접 의존하는 타깃
    for a, b in re.findall(r'"([^"]+)"\s*->\s*"([^"]+)"', r.stdout):
        rdep[b].add(a)
    out = {}
    for o in owners:
        direct = set(rdep.get(o, ()))
        seen, stack = set(), [o]
        while stack:
            x = stack.pop()
            for y in rdep.get(x, ()):
                if y not in seen:
                    seen.add(y); stack.append(y)
        out[o] = (sorted(direct), sorted(seen - direct))
    return out
```
<!-- 인용 끝 -->
