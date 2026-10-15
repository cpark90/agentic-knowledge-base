---
id: https://agentic-knowledge-base.dev/id/chunk/87506246-db94-40b9-8b81-adb8ebe7bd21
type: contract
level: abstract
title_ko: parse_chunk 함수는 청크 파일 경로 하나를 받아 frontmatter와 본문을 내고 규약 위반을 호출자에게 알린다
title: The parse_chunk function takes one chunk file path, yields its frontmatter and body, and reports convention violations to the caller
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-15T15:56:22+09:00}
---
`tools/chunk2kg.py`의 `parse_chunk`는 청크 파일 경로 하나를 받아 frontmatter 사전과 본문 문자열을 낸다. 위반을 알리는 형태는 이 수준에서 정하지 않는다. 그 후보는 logical 수준의 시그니처 셋이다.

```python
def parse_chunk(path: str) -> ...:  # 반환형과 위반 보고의 형태는 logical 수준의 시그니처가 정한다
    ...
```

- 사전조건: `path`는 청크 파일 하나의 경로 문자열이다.
- 사후조건: 위반이 없으면 frontmatter 사전은 필수 키 일곱(`id`·`type`·`level`·`title_ko`·`title`·`status`·`generated`)과 파생 키 `_content_hash`·`_body_slots`를 갖는다. 본문은 frontmatter를 뗀 문자열이고 크기는 호출자가 센다.
- 사후조건: 위반 범위의 각 항목이 호출자에게 알려진다. 위반 범위는 frontmatter의 부재·미종결·형식 위반, 필수 키 누락, `type`·`level`·`status`·`pattern`·`layer`의 어휘 밖 값, plane에 묶인 키의 오용, 라벨의 언어 위반, `specializationOf` 위반이다.
- 호출 자리: 22곳이다(`tools/` 20 · `defs/tests/` 2, 2026-10-15 실측).
- 판정 수단: 타입 체커다(`p7-dev-plane-substance`). 이 저장소에는 타입 체커 게이트가 없고, 위반 범위의 각 항목은 `bazel build //kg:chunks_kg`의 `FAIL [chunk2kg]` 한 줄로 드러난다.
