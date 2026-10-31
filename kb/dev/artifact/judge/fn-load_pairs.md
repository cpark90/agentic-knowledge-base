---
id: https://agentic-knowledge-base.dev/id/chunk/d5ec017d-0162-43dd-bd2e-06bb28ffe5d2
type: artifact
level: executable
title_ko: 함수 load_pairs (tools/judge.py)
title: function load_pairs in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/13c498a5-52b6-4be6-a555-4099859edbbf, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `load_pairs(path)` 다. 쌍 판정지의 정답 key — [{n, question, kind, fingerprint, decoy, anchor:{path,id,title_ko,title,body}, target:{…}}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_pairs(path: Path) -> list[dict]:
    """쌍 판정지의 정답 key — [{n, question, kind, fingerprint, decoy, anchor:{path,id,title_ko,title,body}, target:{…}}]."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise JudgeError(f"{path}: 쌍 key 를 읽을 수 없다 — {e}")
    if not isinstance(data, list) or not all(isinstance(p, dict) and {"anchor", "target", "fingerprint", "question", "kind"} <= set(p)
                                             for p in data):
        raise JudgeError(f"{path}: 쌍 key 는 label_sample.py --pair-sheet 가 낸 목록이다 — 항목마다 anchor·target·fingerprint·question·kind")
    for p in data:
        fp = kb_lib.pair_fingerprint(p["question"], p["kind"], p["anchor"], p["target"])
        if fp != p["fingerprint"]:
            raise JudgeError(f"{path}: 쌍 {p.get('n')} 의 해시값이 그 내용과 다르다 — key 가 손으로 고쳐졌다. 판정지를 다시 만든다")
    return data
```
<!-- 인용 끝 -->
