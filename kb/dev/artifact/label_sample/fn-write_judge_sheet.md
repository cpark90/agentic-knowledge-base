---
id: https://agentic-knowledge-base.dev/id/chunk/843527db-1776-4186-b34b-1b9da6b107be
type: artifact
level: executable
title_ko: 함수 write_judge_sheet (tools/label_sample.py)
title: function write_judge_sheet in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/fff3d0e5-ad0f-4eb4-b8c9-e9ae7d1ce791
---
**함수** — `write_judge_sheet(dirpath, items)` 다. 세션 판정자에게 줄 것 — labels.md(라벨+지문)·bodies.md(본문).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_judge_sheet(dirpath: Path, items: list[dict]) -> None:
    """세션 판정자에게 줄 것 — labels.md(라벨+지문)·bodies.md(본문). 생성 머리·경로·seed 없음."""
    dirpath.mkdir(parents=True, exist_ok=True)
    labels = ["라벨 대표성 판정 — 각 번호에 대해 (1) 라벨만 보고 본문의 주장을 한 문장으로 예측한다 "
              "(2) bodies.md 의 같은 번호를 열어 예측과 대조해 척도 하나와 확신도(0~1)를 정한다 "
              "(3) `judge` 질문 `labelRepresentsBody`·이 번호의 지문·값·확신도를 응답으로 남긴다.", ""]
    bodies = []
    for i, it in enumerate(items, 1):
        fp = kb_lib.label_fingerprint(it)
        labels.append(f"{i}. {it['title_ko']} | {it['title']} | 지문: {fp}")
        bodies += [f"## {i}", "", it["body"], ""]
    (dirpath / "labels.md").write_text("\n".join(labels) + "\n", encoding="utf-8")
    (dirpath / "bodies.md").write_text("\n".join(bodies), encoding="utf-8")
```
<!-- 인용 끝 -->
