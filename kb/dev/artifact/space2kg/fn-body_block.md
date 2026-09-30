---
id: https://agentic-knowledge-base.dev/id/chunk/d3b6910f-bf07-4997-9d87-d61f68beb577
type: artifact
level: executable
title_ko: 함수 body_block (tools/space2kg.py)
title: function body_block in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/fc3f9858-3941-435d-b741-071b871ce613
---
**함수** — `body_block(path, body)` 다. 본문의 `yaml` 펜스 블록 하나를 읽어 매핑으로 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_block(path: str, body: str) -> dict:
    """본문의 `yaml` 펜스 블록 하나를 읽어 매핑으로 돌려준다. 블록이 없거나 둘이면 거부한다."""
    lines, blocks, cur, fence = body.split("\n"), [], None, None
    for line in lines:
        m = kb_lib.MD_FENCE.match(line)
        if fence is None:
            if m:
                fence, cur = m.group(1), []
                if line.strip()[len(fence):].strip() != "yaml":
                    raise SpaceError(f"{path}: 본문 펜스에 언어 태그 `yaml` 이 없다 — 설계 공간의 본문은 yaml 블록 하나다")
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            blocks.append("\n".join(cur))
            fence, cur = None, None
            continue
        cur.append(line)
    if fence is not None:
        raise SpaceError(f"{path}: 본문의 펜스가 닫히지 않았다")
    if len(blocks) != 1:
        raise SpaceError(f"{path}: 본문에 `yaml` 펜스 블록이 정확히 하나여야 한다 — 실제 {len(blocks)}개 (p9-design-space-file)")
    try:
        data = yaml.safe_load(blocks[0])
    except yaml.YAMLError as e:
        raise SpaceError(f"{path}: 본문 yaml 을 읽을 수 없다 — {e}")
    if not isinstance(data, dict):
        raise SpaceError(f"{path}: 본문 yaml 은 매핑이어야 한다 — 키는 {' · '.join(BODY_KEYS)} 다")
    unknown = sorted(set(data) - set(BODY_KEYS))
    if unknown:
        raise SpaceError(f"{path}: 알 수 없는 본문 키 {unknown} — 키는 {' · '.join(BODY_KEYS)} 다 (p9-candidate-storage)")
    return data
```
<!-- 인용 끝 -->
