---
id: https://agentic-knowledge-base.dev/id/chunk/6550bab7-f62f-40fd-893e-4d46be446f2f
type: artifact
level: executable
title_ko: 함수 report_numbers (tools/doccheck.py)
title: function report_numbers in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/145ba81b-fdd4-4cf8-aa11-b8ceb3165a08, https://agentic-knowledge-base.dev/id/chunk/204439f0-e005-4a79-befc-167bfd308ec9, https://agentic-knowledge-base.dev/id/chunk/6d777811-ef05-4ecd-a3c1-78c66baba749, https://agentic-knowledge-base.dev/id/chunk/9ad037aa-26ed-4502-92a5-7bc7dd0855a3]
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `report_numbers(root, repo, docs)` 다. (보고 줄, 대조 쌍 수, 어긋난 쌍 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def report_numbers(root: Path, repo: Repo, docs: tuple[str, ...] = REPORT_DOCS) -> tuple[list[str], int, int]:
    """(보고 줄, 대조 쌍 수, 어긋난 쌍 수). 쌍은 (문서, 이름) 하나이고 창의 수치 중 하나가 생성물 값과 같으면 일치다.

    `docs` 를 안 주면 진입점 문서 넷(`REPORT_DOCS`)이다. 주면 그 목록으로 바꾼다 — vv_run 처럼 자극을 워크스페이스
    밖 임시 경로에 두는 호출자를 위해 이 목록의 각 항목은 루트 밖 절대 경로일 수 있다(2026-10-01, vnv 요청).
    """
    values, missing, skipped = generated_values(root)
    lines_out = [f"REPORT [{TAG}] 문서 수치 대 생성물 수치 — 원본은 V&V 기준 `kb/vv/criteria/document-table-matches-generated.md` 다"]
    if missing:
        lines_out.append(f"  생성물 없음 {' · '.join(missing)} — 그 이름은 건너뛴다. 먼저 `{VIEW_BUILD}`")
    pairs = off = 0
    for rel in docs:
        if not repo.exists(rel):
            lines_out.append(f"  {rel}: 문서가 없다 — 대조 밖")
            continue
        lines = repo.read(rel)
        skip = snapshot_lines(lines)
        for label, doc_re, _sources in NUMBER_NAMES:
            name = re.compile(doc_re)
            hits = [(ln, raw, key, bool(CITED.search(line)))
                    for ln, line in prose_lines(lines) if ln not in skip
                    for raw, key in name_values(line, name)]
            if not hits:
                continue
            gen = values.get(label) or []
            if label in skipped:  # 생성물이 없어 값을 못 얻은 이름 — 쌍으로 세지 않는다
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} — 생성물 미빌드로 건너뜀")
                continue
            pairs += 1
            if not gen:
                mark = "생성물 원본 없음 · 명령·시각 병기" if any(h[3] for h in hits) else "생성물 원본 없음 · 병기 없음"
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} — {mark}")
                continue
            agree = [g for g in gen if any(h[2] == g[1] for h in hits)]
            shown = " · ".join(f"{g[0]}({g[2]})" for g in gen)
            if agree:
                lines_out.append(f"  {rel} {label}: 문서 {' · '.join(h[1] for h in hits)} ↔ 생성물 {shown} — 일치")
            else:
                off += 1
                where = " · ".join(f"{rel}:{h[0]} {h[1]}" for h in hits)
                lines_out.append(f"  {rel} {label}: 문서 {where} ↔ 생성물 {shown} — **어긋남**")
    lines_out.append(f"REPORT [{TAG}] 대조 문서 {len(docs)} · 이름 {len(NUMBER_NAMES)} · "
                     f"대조 쌍 {pairs} · 어긋난 쌍 {off} — 판정이 아니라 보고다. 고칠 것은 문서다")
    return lines_out, pairs, off
```
<!-- 인용 끝 -->
