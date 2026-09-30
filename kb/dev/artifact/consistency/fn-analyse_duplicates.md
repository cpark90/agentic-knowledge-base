---
id: https://agentic-knowledge-base.dev/id/chunk/7ccf9db7-dc13-4351-a4ce-d836075e0330
type: artifact
level: executable
title_ko: 함수 analyse_duplicates (tools/consistency.py)
title: function analyse_duplicates in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/624a2c05-f9ee-442f-a725-cf7c16ed139a
---
**함수** — `analyse_duplicates(items, theta)` 다. ① 정확 중복 · ② 라벨 중복 · ③ 근사 중복 후보와 shingle 집합을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_duplicates(items, theta):
    """① 정확 중복 · ② 라벨 중복 · ③ 근사 중복 후보와 shingle 집합을 돌려준다."""
    # ① 정확 중복
    by_hash = defaultdict(list)
    for it in items:
        by_hash[it["hash"]].append(it)
    exact = [grp for grp in by_hash.values() if len(grp) > 1]

    # ② 라벨 중복
    by_label = defaultdict(list)
    for it in items:
        for key in ("title_ko", "title"):
            if it[key]:
                by_label[(key, it[key])].append(it)
    label_dups = [(k, grp) for k, grp in by_label.items() if len(grp) > 1]

    # ③ 근사 중복 후보 (정확 중복 제외)
    sh = {it["id"]: shingles(it["body"]) for it in items}
    near = []
    for x, y in combinations(items, 2):
        if x["hash"] == y["hash"]:
            continue
        sx, sy = sh[x["id"]], sh[y["id"]]
        if not sx or not sy:
            continue
        j = jaccard(sx, sy)
        if j >= theta:
            near.append((j, x, y))
    near.sort(key=lambda t: -t[0])
    return exact, label_dups, near, sh
```
<!-- 인용 끝 -->
