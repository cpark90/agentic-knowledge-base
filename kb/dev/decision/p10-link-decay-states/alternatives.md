---
id: https://agentic-knowledge-base.dev/id/chunk/9eeaf67c-a274-4127-a73b-a26b78eb1ef0
type: decision
level: logical
title_ko: 재판정 규칙 카탈로그
title: The rejudgement rule catalogue
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c88e9891-e992-4e33-a891-0dcba05746b3
---
**대안** `[안]` — "알려진 변경 패턴은 규칙으로 자동 갱신"의 초기 목록. 미확정이다.

| 변경 | 규칙 | 결과 |
|---|---|---|
| 청크 라벨만 변경 | 링크 영향 없음 | `valid` 유지 |
| 본문 변경, 해시 변경 | `suspect` | 재판정 큐 |
| 시그니처 이름만 변경, 타입 동일 | `satisfies` 유지 | `valid` |
| 시그니처 타입 변경 | `constrains` 재검토 | `suspect` |
| 청크 분할 | 옛 링크를 두 새 IRI로 복제 | 후보 재판정 |
| 청크 병합 | 두 링크를 합집합, 중복 제거 | `candidate` |
| 청크 폐기 | 링크 `invalid`, 대체 청크로 후보 생성 | 후보 재판정 |
| 상위 결정 `supersedes` | 옛 결정의 `satisfies` 전부 `suspect` | 재판정 큐 |
