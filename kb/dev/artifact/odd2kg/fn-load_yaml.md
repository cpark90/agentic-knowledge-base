---
id: https://agentic-knowledge-base.dev/id/chunk/8399b16f-1c78-445a-9ae6-89835f8bf293
type: artifact
level: executable
title_ko: 함수 load_yaml (tools/odd2kg.py)
title: function load_yaml in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d
---
**함수** — `load_yaml(path)` 다. YAML 문서 하나 — 파일 없음·파싱 실패는 판정 불가 입력(EXIT_CONFIG)이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_yaml(path: str):
    """YAML 문서 하나 — 파일 없음·파싱 실패는 판정 불가 입력(EXIT_CONFIG)이다."""
    try:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        print(f"FAIL [{TAG}] {path}: 읽거나 파싱할 수 없다 — {e}", file=sys.stderr)
        raise SystemExit(EXIT_CONFIG)
```
<!-- 인용 끝 -->
