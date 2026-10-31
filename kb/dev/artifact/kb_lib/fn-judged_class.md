---
id: https://agentic-knowledge-base.dev/id/chunk/8c071cee-5922-4176-a0d9-848167ee9316
type: artifact
level: executable
title_ko: 함수 judged_class (tools/kb_lib.py)
title: function judged_class in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/940cfa49-d6bf-444b-93a1-ee4441b63501
---
**함수** — `judged_class(polarities)` 다. 판정 증거의 극성 목록 → 판정 넷 가운데 하나.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judged_class(polarities: list) -> str:
    """판정 증거의 극성 목록 → 판정 넷 가운데 하나. 판정자 둘 미만이면 판정 없음이다 — 단독 응답은 일치를 이루지 못한다."""
    if len(polarities) < 2:
        return JUDGED_NONE
    if set(polarities) == {"+"}:
        return JUDGED_AGREE_YES
    if set(polarities) == {"-"}:
        return JUDGED_AGREE_NO
    return JUDGED_DISAGREE
```
<!-- 인용 끝 -->
