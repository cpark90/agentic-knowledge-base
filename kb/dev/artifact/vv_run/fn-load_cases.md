---
id: https://agentic-knowledge-base.dev/id/chunk/4819f0e8-1ed9-43cb-b206-366b65a7f00f
type: artifact
level: executable
title_ko: 함수 load_cases (tools/vv_run.py)
title: function load_cases in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5f53b16a-56e0-4dc8-886e-c0e202e515c8]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `load_cases(root, only, waivers)` 다. 케이스 파일 → [{slug, path, label, iri, spec, errors, commands: [{cmd, skip}]}], 실행 명령 줄이 없는 케이스 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_cases(root: Path, only: list[str], waivers: list[dict]) -> tuple[list[dict], list[str]]:
    """케이스 파일 → [{slug, path, label, iri, spec, errors, commands: [{cmd, skip}]}], 실행 명령 줄이 없는 케이스 목록.

    형식 오류(`FAIL [vv-case]`)를 가진 케이스는 오류를 달아 돌려준다 — 판정은 main 이 한다. waivers.md 가 게이트 id
    `vv-case` 로 면제를 선언한 케이스는 오류를 집계에서 빼되 목록에 남기고, 펜스를 읽지 않은 것으로 본다(점진 도입과 같은 자리).
    """
    return load_items(root, "case", only, waivers)
```
<!-- 인용 끝 -->
