---
id: https://agentic-knowledge-base.dev/id/chunk/00000000-0000-4000-8000-0000000f0002
type: artifact
level: executable
title_ko: 고정물 검증기는 읽기 전용 검증기 하나의 도움말을 종료 0으로 낸다
title: The fixture verifier gets the help text of one read-only verifier with exit 0
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-04T00:00:00+09:00}
layer: process
---
**검증기** — 읽기 전용 검증기 하나를 부른다.

**기대** — 종료 코드가 0이고 출력에 `usage: chunk2kg.py`가 있다.

```yaml
expect:
  - exit: 0
    contains: ["usage: chunk2kg.py"]
```

**실행 명령** — `python3 tools/chunk2kg.py --help`

**판정 범위** — 실행 경로 하나만 본다.

**검증 대응물** — 없음.
