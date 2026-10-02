---
id: https://agentic-knowledge-base.dev/id/chunk/8737dba4-7aa0-467f-add3-14901ba38236
type: artifact
level: executable
title_ko: 함수 main (tools/revalidate.py)
title: function main in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1f76c401-7790-442a-8a89-cbeb275631a6, https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/4d7ba4f8-3559-4026-8352-97c8b9835a2b, https://agentic-knowledge-base.dev/id/chunk/520a6151-01ee-4804-9141-0829d19e2768, https://agentic-knowledge-base.dev/id/chunk/5e22443d-209f-4479-a064-9c08165f38f4, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/74004d79-dc3f-461f-85e1-3e42bfe1a332, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/d63b7431-1668-41dd-b872-475b380f0fd4]
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    a = parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    cwd = str(root)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"CONFIG [revalidate] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}", file=sys.stderr)
        return 2

    index, incoming, composite_parts, callers, unparsable = index_worktree(root)
    changed, head_only, base_by_iri, unread = base_diff(a.base, cwd, index)
    rows, per_chunk, label, iri_to_label = revalidation_rows(
        root, cwd, a.universe, changed, index, incoming, composite_parts, callers)

    # 4. 본문 해시 변경 → 링크 재판정. 본문이 바뀐 청크를 양 끝 중 하나로 갖는 링크 개체가 suspect 로 유도된다 (노트 9.11절)
    body_changed = {iri for _path, kind, iri, _m, _b, _n in changed if kind in ("본문 변경", "변경", "신규", "삭제")}
    objs = link_objects(index, body_changed)
    # 바뀐 끝이 **결정 결론**인 재판정 링크 — V&V 기준 decision-and-artifact-agree 의 판정 대상 행이고
    # 현상 agt:reasoningActionMismatch(P16)의 관측 자리다. 결론은 결정 복합체의 파일 이름으로 가른다 (kb_lib.DECISION_PART_FILES)
    conclusion_file = kb_lib.DECISION_PART_FILES["conclusion"]
    path_of = lambda iri: (index.get(iri) or base_by_iri.get(iri) or ("", {}))[0]
    is_conclusion = lambda iri: Path(path_of(iri)).name == conclusion_file
    n_conclusion = sum(1 for _l, _k, frm, to, side in objs if is_conclusion(frm if side == "출발" else to))

    rep = kb_lib.gendoc_header(
        "revalidate", f"base {a.base} 대비 재판정 대상", "tools/revalidate.py",
        f"base 리비전 `{a.base}` 와 워킹트리 사이에서 본문 해시가 바뀐 청크마다 — (a) frontmatter 링크의 상대(양방향) · "
        "(b) 복합체 형제 · (c) `bazel query rdeps` 의 하류 의존자 · (d) 그 정의를 `uses` 로 가리키는 **호출부** · "
        "(e) 그 청크를 양 끝 중 하나로 갖는 **링크 개체**(`agt:Link`)를 재판정 대상으로 (dependency-graph-design §5). 링크 개체의 상태는 저장하지 않고 여기서 물질화한다",
        f"bazel run //tools:revalidate -- --base {a.base}", [],
        f"변경 청크 {len(changed)} · 재판정 대상 {len(rows)} · 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} · "
        f"재판정 링크 개체 {len(objs)} (바뀐 끝이 결정 결론인 것 {n_conclusion})",
        kb_lib.gendoc_view_notice("각 청크의 본문과 frontmatter 링크"),
        input_note=f"`git show {a.base}:<청크>` 와 워킹트리의 청크 파일, `bazel query` 결과 — 리비전 대비 차이라 지문을 내지 않는다",
        extra=[f"- 호출부 {sum(r[4] == 'frontmatter uses' for r in rows)} — 본문이 바뀐 정의를 `uses`(agt:usesDefinition)로 "
               "가리키는 출발점이고 **코드 호출부 파손의 상한**이다. 모듈 안 호출과 치역 경계"
               f"(`{kb_lib.USES_TARGETS_NAME}`) 안의 모듈 간 호출을 세므로 경계 밖을 치역으로 하는 호출은 빠진다",
               f"- head 만 바뀐 청크 {len(head_only)} (본문 해시 동일 — 재판정 대상이 아니다)",
               f"- 본문이 바뀐 청크에 붙은 링크 개체 {len(objs)} — 유도 상태는 `{kb_lib.LINK_STATE_SUSPECT}` 다",
               f"- 그중 **바뀐 끝이 결정 결론**(`{conclusion_file}`)인 것 {n_conclusion} — 결정의 본문과 구현이 어긋나는 현상"
               f"(`agt:reasoningActionMismatch`)의 판정 대상 행이고 0 이면 공허 합격이다"])
    body = report_rows(per_chunk, rows, objs, head_only, unparsable, unread, label)
    text = kb_lib.gendoc_assemble(rep, body, [])
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if (rows or objs) else 0
```
<!-- 인용 끝 -->
