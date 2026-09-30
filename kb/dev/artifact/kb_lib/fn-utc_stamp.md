---
id: https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a
type: artifact
level: executable
title_ko: 함수 utc_stamp (tools/kb_lib.py)
title: function utc_stamp in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `utc_stamp(when)` 다. 주어진 시각의 G3 표기 — ISO 8601 UTC 초 해상도.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def utc_stamp(when: datetime) -> str:
    """주어진 시각의 G3 표기 — ISO 8601 UTC 초 해상도.

    관측 생성기(`assume_check`·`vv_run`)가 자기 `now` 를 frontmatter 와 본문 두 자리에 같은 꼴로 적을 때 쓴다.
    커밋된 관측 기록은 append-only 라 표기가 바뀌어도 소급하지 않는다 (유저 승인 2026-09-23).
    """
    return when.astimezone(timezone.utc).strftime(GENDOC_TIME_FORMAT)
```
<!-- 인용 끝 -->
