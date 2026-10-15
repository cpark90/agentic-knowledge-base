---
id: https://agentic-knowledge-base.dev/id/chunk/7d400d4e-5ef5-4ec7-9efa-3c9fb35c0aea
type: contract
level: logical
title_ko: parse_chunk 함수는 frontmatter·본문·위반을 필드로 가진 결과 객체를 언제나 반환한다
title: The parse_chunk function always returns a result object whose fields are the frontmatter, the body and the violations
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-15T15:56:22+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/87506246-db94-40b9-8b81-adb8ebe7bd21]
---
결과 객체를 반환하는 시그니처다.

```python
@dataclass(frozen=True)
class ParsedChunk:
    meta: dict
    body: str
    violations: tuple[str, ...]  # 각 항목은 "<경로>: <근거>"

def parse_chunk(path: str) -> ParsedChunk: ...
```

- 사전조건: `path`는 읽을 수 있는 파일이다. 읽기 실패는 `OSError`로 올라간다.
- 사후조건: 위반이 있어도 반환한다. `violations`가 비면 `meta`는 필수 키 일곱을 다 갖고 값이 어휘 안이다. 비지 않으면 `meta`는 부분 결과다.
- 사후조건: 한 파일의 위반 전부가 `violations`에 담긴다. 한 실행에서 한 파일의 위반이 모두 드러난다.
- 호출자 비용: 22곳의 `meta, body = parse_chunk(p)` 언패킹이 속성 접근과 `violations` 검사로 바뀐다. 검사를 빠뜨린 호출자에게는 부분 결과가 조용히 흐른다.
- 저장소 안 선례: 필드를 가진 객체를 돌려주는 형태는 `tools/extract.py`의 `Chunk`·`Region`과 `tools/query.py`의 `CqQuery`에 있다.
- 판정 수단: 타입 체커가 반환형 `ParsedChunk`와 호출 자리의 속성 접근을 대조한다.
