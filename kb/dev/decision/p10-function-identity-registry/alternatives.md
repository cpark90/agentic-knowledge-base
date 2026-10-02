---
id: https://agentic-knowledge-base.dev/id/chunk/216c6b43-98ab-4866-a800-b21e41211206
type: decision
level: logical
title_ko: 이름 기반 uuid·해시 정체성·소스 안 uuid 주석·개명 자동 확정은 기각된다
title: Name-derived uuid, hash identity, uuid comments in source, and auto-confirmed renames are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/fa336de6-3b07-45c0-9b66-b41ce2cdbcba
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 이름에서 uuid를 만든다(uuid5) | 개명 = 삭제 + 신설. 링크·이력이 끊긴다 |
| 본문 해시를 정체성으로 쓴다(Unison) | 이 저장소의 해시는 버전이다. 한 글자 수정이 새 항목이 되고 같은 본문의 두 함수가 하나가 된다 |
| 소스 파일에 uuid 주석을 심는다 | 코드 편집이 정체성 편집이 된다. 원본이 둘(코드와 주석)이라 tangle의 문제가 돌아온다 |
| 해시가 같으면 개명을 자동 확정한다 | 복제와 개명을 기계가 가르지 못한다. 제안까지만 기계가 하고 확정은 등록부 편집이다 |
