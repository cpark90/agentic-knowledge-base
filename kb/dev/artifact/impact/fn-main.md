---
id: https://agentic-knowledge-base.dev/id/chunk/9cf8cd96-ac27-4df3-b338-22a13d71ed35
type: artifact
level: executable
title_ko: 함수 main (tools/impact.py)
title: function main in tools/impact.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-impact}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/44b63663-ac34-40f1-92c6-a6281c93c7a6
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--universe", default="//kb/... + //chunks/...")
    a = ap.parse_args()
    cwd = os.environ.get("BUILD_WORKSPACE_DIRECTORY", ".")
    is_item = lambda l: ":kg" not in l and not l.endswith(":bodies") and l != a.target
    direct = [l for l in q(f"rdeps({a.universe}, {a.target}, 1)", cwd) if is_item(l)]
    trans = [l for l in q(f"rdeps({a.universe}, {a.target})", cwd) if is_item(l)]
    planes = Counter(plane_of(l) for l in trans)
    decisions = [l for l in trans if plane_of(l).startswith("decision") and "deprecated" not in plane_of(l)]
    head = kb_lib.gendoc_header(
        "impact", f"{a.target} 의 영향 집합", "tools/impact.py",
        f"`rdeps({a.universe}, {a.target})` 로 이 타깃에 (전이적으로) 의존하는 지식 항목 — 직접 의존자는 고치면 suspect 가 될 링크이고, "
        "그중 결정은 유저 승인이 stable 전이 조건이다 (5.4절)",
        f"bazel run //tools:impact -- {a.target}", [], f"영향 항목 {len(trans)}",
        kb_lib.gendoc_view_notice("각 청크의 frontmatter 링크 (BUILD 는 그 뷰다)"),
        input_note=f"`bazel query` 결과 — 파일이 아니라 질의다 (universe `{a.universe}`)")
    body = []
    body.append(f"- 영향 항목(전이): **{len(trans)}** · 직접 의존자(= suspect 가 될 링크): **{len(direct)}**")
    body.append("- plane 분포: " + (" · ".join(f"{k} {v}" for k, v in planes.most_common()) or kb_lib.NONE_MARK))
    body.append(f"- 유저 승인이 필요한 결정: **{len(decisions)}** (decision 은 유저 승인이 stable 전이 조건, 5.4절)")
    body += [f"- 자율 진행 범위: {'안' if not decisions else '**밖** — 승인 필요 수가 0이 아니다'} (method §12)", ""]
    body += ["## 직접 의존자", ""]
    body += [f"- {l}" for l in sorted(direct)[:40]] or [f"- {kb_lib.NONE_MARK}"]
    if len(direct) > 40:
        body.append(f"- … 외 {len(direct)-40}")
    body.append("")
    print(kb_lib.gendoc_assemble(head, body, []), end="")
    return 0
```
<!-- 인용 끝 -->
