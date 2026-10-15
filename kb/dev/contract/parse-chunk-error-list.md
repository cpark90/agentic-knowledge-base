---
id: https://agentic-knowledge-base.dev/id/chunk/438d6c82-6afd-421b-bd64-8343053438ce
type: contract
level: logical
title_ko: parse_chunk 함수는 frontmatter·본문과 함께 위반 문자열 목록을 반환한다
title: The parse_chunk function returns a list of violation strings alongside the frontmatter and body
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-15T15:56:22+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/87506246-db94-40b9-8b81-adb8ebe7bd21]
---
오류 목록을 셋째 값으로 반환하는 시그니처다.

```python
def parse_chunk(path: str) -> tuple[dict, str, list[str]]: ...
# 셋째 값: 위반 문자열 목록, 각 항목은 "<경로>: <근거>". 비면 위반이 없다
```

- 사전조건: `path`는 읽을 수 있는 파일이다. 읽기 실패는 `OSError`로 올라간다.
- 사후조건: 위반이 있어도 반환한다. 목록이 비면 frontmatter 사전은 필수 키 일곱을 다 갖고 값이 어휘 안이다.
- 사후조건: 한 파일의 위반 전부가 목록에 담긴다. 목록의 꼴은 검사 함수 `check_*() -> list[str]`와 같아서 `main`의 합류가 그대로 쓰인다.
- 호출자 비용: 22곳의 언패킹이 셋째 값을 받도록 바뀐다. 목록을 버리는 호출자에게는 부분 결과가 조용히 흐른다.
- 저장소 안 선례: `tools/chunk2kg.py`의 `norm_bundle_errors`, `tools/channel_lint.py`의 `check_message`가 위반 문자열 목록을 반환한다.
- 판정 수단: 타입 체커가 반환형의 셋째 원소 `list[str]`와 22곳의 세 값 언패킹을 대조한다.
