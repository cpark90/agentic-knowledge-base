---
iri: https://agentic-knowledge-base.dev/id/chunk-d0154
plane: decision
level: concrete
label_ko: 청크 편집기의 최소 요구
label_en: Minimum requirements for the chunk editor
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 청크를 만드는 도구가 만족해야 할 최소 요구를 다섯으로 고정한다.
전부 체계의 규칙을 **저장 시점에** 강제하기 위한 것이다.

**근거** (노트 11.4절)
- **42줄 초과 시 즉시 경고하고 저장 시 분할을 제안한다** — shape 위반을
  저장 전에 잡는다 (4.1절).
- **라벨 없이 저장 불가** — 라벨링 원칙. 라벨 없는 청크는 라벨 목록으로
  읽히지 않으므로 사실상 없는 것이다.
- **plane·level 선택 필수** — head 그래프가 요구한다.
- **참조한 청크를 provenance에 자동 기록** — 구축에 의한 링크(8.3절).
  사람이 나중에 적는 provenance는 빠진다.
- **본문 편집과 링크 편집을 다른 화면에 둔다** — 청크는 자기 링크를
  모른다(4.3절). 한 화면에 두면 그 분리가 곧 무너진다.
