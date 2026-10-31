---
id: https://agentic-knowledge-base.dev/id/chunk/13c498a5-52b6-4be6-a555-4099859edbbf
type: artifact
level: executable
title_ko: 함수 pair_fingerprint (tools/kb_lib.py)
title: function pair_fingerprint in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/940cfa49-d6bf-444b-93a1-ee4441b63501
---
**함수** — `pair_fingerprint(question, kind, anchor, target)` 다. 쌍 판정의 대조 해시값 — sha256(질문 id ∣ 링크 종류 ∣ 앵커 라벨·본문 ∣ 대상 라벨·본문).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_fingerprint(question: str, kind: str, anchor: dict, target: dict) -> str:
    """쌍 판정의 대조 해시값 — sha256(질문 id ∣ 링크 종류 ∣ 앵커 라벨·본문 ∣ 대상 라벨·본문).

    `label_fingerprint` 와 같은 원칙이다 — 판정자에게 **보인 것**의 해시값이고, 쌍 판정지(`label_sample.py --pair-sheet`)가 싣고
    `judge.py --pairs` 가 응답을 찾는 데 쓴다. 두 항목은 `title_ko`·`title`·`body` 키의 딕셔너리다."""
    def shown(it: dict) -> str:
        return f"{it.get('title_ko', '')}\n{it.get('title', '')}\n\n{it.get('body', '')}"
    return hashlib.sha256("\x1f".join((question, kind, shown(anchor), shown(target))).encode("utf-8")).hexdigest()
```
<!-- 인용 끝 -->
