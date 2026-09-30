---
id: https://agentic-knowledge-base.dev/id/chunk/cf1b3c55-9f8f-446c-87d0-87ab5c66320f
type: artifact
level: executable
title_ko: 함수 owner_labels (tools/revalidate.py)
title: function owner_labels in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f
---
**함수** — `owner_labels(root)` 다. IRI → 소유 Bazel 타깃 라벨.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def owner_labels(root: Path) -> dict:
    """IRI → 소유 Bazel 타깃 라벨. 규칙의 원본은 `gen_build` 의 `iri_to_label` 이다 — 여기서 다시 적지 않는다.

    복합체 묶음(`kb_composite`·`kb_decision`) 뒤에는 **부분마다의 개별 타깃이 없다**. 파일 경로에서 라벨을 지어내면
    추출된 코드 청크(`kb/dev/artifact/<모듈>/fn-*.md`)가 존재하지 않는 타깃을 가리켜 `bazel query rdeps` 가 늘 0/0 이
    된다. 생성기를 그대로 불러 사상을 얻는다. 생성 시점 거부(끊긴 링크 등)가 있으면 빈 사상을 돌려주고 경고만 남긴다.
    """
    try:
        from gen_build import GenBuildError, scan
    except ImportError:
        from tools.gen_build import GenBuildError, scan
    try:
        return scan(root)[1]
    except (GenBuildError, ValueError, OSError) as e:
        print(f"WARN [revalidate] 타깃 라벨 사상을 얻지 못했다 — 하류 의존자 없이 보고한다: {e}")
        return {}
```
<!-- 인용 끝 -->
