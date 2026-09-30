---
id: https://agentic-knowledge-base.dev/id/chunk/ddab0191-16a5-4584-9734-a7d026cb29f8
type: artifact
level: executable
title_ko: 함수 counts (tools/vv_run.py)
title: function counts in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `counts(cases)` 다. 케이스 판정별 수 + 명령 단위 집계.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def counts(cases: list[dict]) -> dict:
    """케이스 판정별 수 + 명령 단위 집계. 명령 단위를 따로 내는 까닭은 케이스 판정 하나가 절반만 실행된 사실을 감추기 때문이다."""
    out = {v: sum(1 for c in cases if c["verdict"] == v) for v in kb_lib.RUN_VERDICTS}
    out["실행"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is None)
    out["건너뜀"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is not None)
    out["명령"] = out["실행"] + out["건너뜀"]
    out["대조"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is None and x.get("expect"))
    out["어긋남"] = sum(1 for c in cases for x in c["commands"] if x["mismatch"])
    return out
```
<!-- 인용 끝 -->
