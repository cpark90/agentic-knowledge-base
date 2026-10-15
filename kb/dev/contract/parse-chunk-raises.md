---
id: https://agentic-knowledge-base.dev/id/chunk/ed5b49af-8e81-4f81-b74e-9f795c588072
type: contract
level: logical
title_ko: parse_chunk 함수는 첫 위반을 ValueError로 던지고 위반이 없을 때만 frontmatter와 본문의 쌍을 반환한다
title: The parse_chunk function raises the first violation as ValueError and returns the frontmatter and body pair only when there is none
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-15T15:56:22+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/87506246-db94-40b9-8b81-adb8ebe7bd21]
satisfies: [https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
---
위반을 예외로 던지는 시그니처다.

```python
class SpecializationError(ValueError): ...  # specializationOf 위반

def parse_chunk(path: str) -> tuple[dict, str]:
    """위반이면 raise ValueError(f"{path}: <근거>"). 읽기 실패는 OSError 를 그대로 올린다."""
```

- 사전조건: `path`는 읽을 수 있는 파일이다. 읽기 실패는 위반이 아니라 입력 오류이고 `OSError`로 올라간다.
- 사후조건: 반환하면 frontmatter 사전은 필수 키 일곱을 다 갖고 값이 어휘 안이다. 위반이 하나라도 있으면 반환하지 않는다.
- 사후조건: 첫 위반 하나만 던진다. 메시지는 `<경로>: <근거>`이고 호출자가 `FAIL [<게이트 id>]`를 붙이고 종료 코드를 고른다. 이것이 결정 `p6-gate-catalogue`의 실패 메시지·종료 코드 규약을 채운다.
- 호출자 비용: 파일 여럿의 위반을 모으는 호출자는 반복문 안에서 예외를 잡아 목록에 더한다(`chunk2kg.main`). 한 파일의 둘째 위반은 첫 위반을 고친 다음 실행에서 드러난다.
- 판정 수단: 타입 체커가 반환형 `tuple[dict, str]`과 22곳의 두 값 언패킹을 대조한다. 현재 코드는 함수 청크 `kb/dev/artifact/chunk2kg/fn-parse_chunk.md`의 인용이다.
