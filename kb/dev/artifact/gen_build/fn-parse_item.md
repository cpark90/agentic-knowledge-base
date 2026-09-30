---
id: https://agentic-knowledge-base.dev/id/chunk/be13ce99-9dc5-4abe-8367-5558f1aa4b02
type: artifact
level: executable
title_ko: 함수 parse_item (tools/gen_build.py)
title: function parse_item in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd
---
**함수** — `parse_item(path)` 다. 청크 파일 하나 → (메타, 본문 줄 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_item(path: str):
    """청크 파일 하나 → (메타, 본문 줄 수). 설계 공간 청크는 여기서 거부한다.

    `-space` 는 청크 패키지에 살지 않는다 — kb_chunk 타깃이 되면 후보 링크가 deps 로 새기 때문이다
    (결정 p9-candidate-storage). 올리는 곳은 `//space:design_space`(tools/space2kg.py)다.
    """
    meta, n = parse_chunk(path)
    if meta["type"] == SPACE_TYPE:
        raise GenBuildError(f"{path}: 설계 공간 청크(type: {SPACE_TYPE})는 청크 패키지에 둘 수 없다 — space/ 에 두면 "
                            f"//space:design_space 가 올린다. 후보는 결코 deps 가 되지 않는다 (p9-candidate-storage)")
    return meta, n
```
<!-- 인용 끝 -->
