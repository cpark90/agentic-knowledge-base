---
iri: https://agentic-knowledge-base.dev/id/chunk-d0057
plane: decision
level: concrete
label_ko: 프로파일은 골격을 확장만 하는 온톨로지 모듈이다
label_en: A profile is an extension-only ontology module
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 프로파일은 별도 장치가 아니라 온톨로지 모듈이다. `profile/<domain>`
에 두고 골격 모듈을 import하며, **골격 클래스의 하위 클래스와 shape만
추가한다.** 골격을 수정하는 프로파일은 검사 실패다. 한 프로젝트는 프로파일을
여럿 가질 수 있다.

**근거** (노트 2.11절)
- 개발 프로젝트에도 문서 작성 작업이 있다. development(함수=청크, 심볼 앵커,
  ODC 결함 유형)·writing(문단=청크, 문체 규약=contract)·operations(절차
  단계=청크, SLA=contract)처럼 프로파일이 한 프로젝트에 공존한다.
- 청크는 프로파일 클래스 하나에 속하되 **링크는 프로파일을 넘는다** — 문서
  청크가 코드 청크를 `targets`할 수 있다. 링크 타입이 골격에 있기 때문에
  가능한 일이다.
- 골격 수정을 막아야 프로파일이 늘어도 판정 방식·사다리·링크 타입이 모든
  프로파일에서 같은 뜻을 유지한다.
