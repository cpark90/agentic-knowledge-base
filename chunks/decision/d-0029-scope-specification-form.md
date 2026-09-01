---
iri: https://agentic-knowledge-base.dev/id/chunk-d0029
plane: decision
level: concrete
label_ko: 스코프 명세는 네 문장으로 쓴다
label_en: Scope is written as four statement kinds
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 스코프는 네 종류의 문장으로 쓴다. **mode**(기본 모드:
`restrictive` = 명시 포함만 허용 / `permissive` = 명시 제외만 금지),
**include**(스코프 안의 조건·개념), **exclude**(스코프 밖의 조건·개념),
**conditional**(include/exclude에 붙는 부가 조건, "X이면 Y를 포함").
write scope의 기본 모드는 `restrictive`이고, read scope는 하네스별로 정한다.

**근거** (노트 0.4절)
- mode를 명시해야 **적히지 않은 것의 의미**가 결정된다. mode 없이
  include/exclude만 있으면 목록에 없는 조건을 허용으로 볼지 금지로 볼지가
  에이전트의 추측에 맡겨진다(1.2절).
- **conditional이 프로세스 규칙의 기계적 강제 수단이다.** 아래 문장은
  9.1절 "구현 전 상세 설계"를 문서 규칙이 아니라 하네스 검사로 만든다 —
  관련 결정이 확정된 뒤에만 인터페이스 수정을 허용한다.

```
scope :developer-scope
  mode restrictive
  include plane source          (write)
  include plane interface       (read)
  conditional: include write plane interface
               if design-decision(target).level = concrete
```

- 스코프가 참조하는 조건은 ODD 속성이어야 한다 — ODD에 없는 속성을
  참조하는 스코프는 검사 게이트가 거부한다(d-0008).
