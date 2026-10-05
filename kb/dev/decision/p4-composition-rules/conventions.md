---
id: https://agentic-knowledge-base.dev/id/chunk/8cc565dd-bfd6-45b3-8422-409d454bb56b
type: decision
level: concrete
title_ko: 규범 문서 규약 — 구성 규칙은 비순환·7±2·동질성·참조 재사용이며 shape으로 쓴다
title: Normative-document conventions — Composition rules are acyclicity, 7±2, homogeneity and reference reuse, written as shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/27157a50-048e-4b31-835f-ce91abcb93a8
---
**규약** — `p4-composition-rules`의 결론을 규범 문서에 싣는 문장이다.

규약: 동질성 | 부분의 plane 클래스가 전체와 같다. level도 같되 결정 복합체는 예외다 — 결론 concrete·근거/대안 logical(`p7-decision-spans-three-levels`). plane·level을 넘는 관계는 전부 링크다. verify 질의 `composite-heterogeneous`가 검사한다 (2026-09-13)
규약: 크기 | 직접 부분 최대 9개(7±2). 넘는 묶음은 **중첩**으로 담는다 — 선언 청크의 `composite.part_of`가 그 복합체를 상위 복합체의 직접 부분으로 만들고(`p4-composite-as-part-of`), 중첩된 복합체 전부는 한 액션(= 한 Bazel 타깃)이 뿌리부터 잎까지 받는다. 코드의 추출이 이 자리를 처음 쓴다 — 파일 → 장·절 복합체 → 정의 청크이고 소스의 절 주석(`# ══ 장` · `# ── 절`)이 구조의 원본이다. 절 주석이 없어 9를 넘는 파일은 `FAIL [extract]`로 절 주석을 요구한다 — 9개씩 자르지 않는다(순서에 뜻이 없는 묶음)
규약: 비순환 | `part-of`의 반대칭 공리로 추론된다
규약: 상태 | 부분에서 추론된다 — 부분 하나가 `invalidated`면 복합체는 `suspect`
