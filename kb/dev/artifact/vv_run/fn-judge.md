---
id: https://agentic-knowledge-base.dev/id/chunk/388a8426-2072-4508-a920-535321ed7eaa
type: artifact
level: executable
title_ko: 함수 judge (tools/vv_run.py)
title: function judge in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/13d0468f-ac80-47c0-9d27-cafd3ef8ffaf, https://agentic-knowledge-base.dev/id/chunk/8809d561-f915-420c-93b5-382d7dd4867c]
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `judge(c, exp)` 다. 명령 하나의 기대 대조 — 어긋남 목록(빈 목록이면 맞다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge(c: dict, exp: dict | None) -> list[str]:
    """명령 하나의 기대 대조 — 어긋남 목록(빈 목록이면 맞다). 메시지에 기대와 실제를 함께 적어 수정 방향이 되게 한다."""
    want = 0 if not exp or exp.get("exit") is None else exp["exit"]
    bad = []
    if c["rc"] != want:
        bad.append(f"종료 코드 — 기대 {want} · 실제 {c['rc']}")
    for ph in phrases(exp.get("contains") if exp else None):
        if ph not in c["out"]:
            bad.append(f"기대 문구가 출력에 없다 — 기대 `{ph}` · 실제로 가장 가까운 줄 `{near_miss(c['out'], ph)}`")
    return bad
```
<!-- 인용 끝 -->
