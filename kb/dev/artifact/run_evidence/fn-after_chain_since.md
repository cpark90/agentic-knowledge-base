---
id: https://agentic-knowledge-base.dev/id/chunk/3149b98e-06cf-4a59-94b6-8bb92aef0b70
type: artifact
level: executable
title_ko: 함수 after_chain_since (tools/run_evidence.py)
title: function after_chain_since in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f
---
**함수** — `after_chain_since(at)` 다. 실행 기록의 generated.at 이 `CHAIN_SINCE` 이후인가 — 시각을 읽지 못하면 옛 기록으로 본다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def after_chain_since(at) -> bool:
    """실행 기록의 generated.at 이 `CHAIN_SINCE` 이후인가 — 시각을 읽지 못하면 옛 기록으로 본다."""
    try:
        when = datetime.fromisoformat(str(at).replace("Z", "+00:00"))
    except ValueError:
        return False
    when = when if when.tzinfo else when.replace(tzinfo=timezone.utc)
    return when >= datetime.fromisoformat(CHAIN_SINCE.replace("Z", "+00:00"))
```
<!-- 인용 끝 -->
