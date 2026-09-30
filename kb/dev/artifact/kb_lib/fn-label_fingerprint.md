---
id: https://agentic-knowledge-base.dev/id/chunk/48ed45d6-a852-4def-9baa-eee654691bc7
type: artifact
level: executable
title_ko: 함수 label_fingerprint (tools/kb_lib.py)
title: function label_fingerprint in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `label_fingerprint(item)` 다. 세션 판정자에게 실제로 보인 입력(라벨 + 본문)의 지문 — sha256(제목 ko \n 제목 en \n\n 본문).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def label_fingerprint(item: dict) -> str:
    """세션 판정자에게 실제로 보인 입력(라벨 + 본문)의 지문 — sha256(제목 ko \\n 제목 en \\n\\n 본문).

    단일 정의처(2026-09-30 vnv 결함 보고 ①) — `tools/judge.py`(판정 응답의 대조 키)와 `tools/label_sample.py`
    (`--judge-sheet`의 `labels.md`가 싣는 지문)가 이 함수 하나를 쓴다. 청크 파일을 다시 읽어 만드는 지문(바이트
    sha256)과 다르다 — 라벨 대표성 실험의 미끼는 파일 내용과 판정자에게 보인 내용이 다르므로, 대조 키는 항상
    "보인 것"이어야 한다. `item`은 `title_ko`·`title`·`body` 키를 갖는 딕셔너리다(label_sample.py의 표본 항목,
    judge.py의 --decoys key.json 항목과 같은 모양)."""
    return hashlib.sha256(f"{item.get('title_ko', '')}\n{item.get('title', '')}\n\n{item.get('body', '')}"
                          .encode("utf-8")).hexdigest()
```
<!-- 인용 끝 -->
