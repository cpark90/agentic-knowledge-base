---
id: https://agentic-knowledge-base.dev/id/chunk/9ba49f50-c949-45ae-816e-d24210ec8af6
type: artifact
level: executable
title_ko: 함수 pair_record_fingerprint (tools/kb_lib.py)
title: function pair_record_fingerprint in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/940cfa49-d6bf-444b-93a1-ee4441b63501
---
**함수** — `pair_record_fingerprint(anchor_bytes, target_bytes)` 다. 쌍 판정 로그의 `입력 해시값` — sha256(앵커 파일 바이트 ∥ 대상 파일 바이트).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_record_fingerprint(anchor_bytes: bytes, target_bytes: bytes) -> str:
    """쌍 판정 로그의 `입력 해시값` — sha256(앵커 파일 바이트 ∥ 대상 파일 바이트). 두 파일 중 하나라도 바뀌면 판정이 낡는다."""
    return hashlib.sha256(anchor_bytes + target_bytes).hexdigest()
```
<!-- 인용 끝 -->
