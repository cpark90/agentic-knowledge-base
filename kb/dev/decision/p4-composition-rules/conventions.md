---
id: https://agentic-knowledge-base.dev/id/chunk/8cc565dd-bfd6-45b3-8422-409d454bb56b
type: decision
level: concrete
title_ko: 규범 문서 규약 — 구성 규칙은 비순환, 7±2, 동질성, 참조 재사용의 넷이며 shape으로 쓴다
title: Normative-document conventions — Composition rules are acyclicity, 7±2, homogeneity and reference reuse, written as shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/27157a50-048e-4b31-835f-ce91abcb93a8
---
**규약** — `p4-composition-rules`의 결론을 규범 문서에 싣는 문장이다.

규약: 동질성 | 부분의 지식 종류 클래스가 전체와 같다. 정제 수준도 같아야 하지만 결정 기록은 예외여서 결론은 구체 수준이고 근거와 대안은 논리 수준이다(`p7-decision-spans-three-levels`). 지식 종류나 정제 수준을 넘는 관계는 전부 링크이고, verify 질의 `composite-heterogeneous`가 이를 검사한다 (2026-09-13).
규약: 크기 | 직접 부분은 최대 9개다(7±2). 9개를 넘는 묶음은 **중첩**으로 담는다. 선언하는 단위 지식의 `composite.part_of`가 그 복합체를 상위 복합체의 직접 부분으로 만들고, 중첩된 복합체 전부는 한 액션, 곧 한 Bazel 타깃이 뿌리부터 잎까지 받는다(`p4-composite-as-part-of`). 코드 추출이 이 자리를 처음 쓰며, 파일 아래 장·절 복합체를 두고 그 아래 정의 단위 지식을 두는 구조의 원본은 소스의 절 주석인 `# ══ 장`과 `# ── 절`이다. 절 주석이 없어 9를 넘는 파일은 `FAIL [extract]`로 절 주석을 요구하고, 순서에 뜻이 없는 묶음이 되므로 9개씩 자르지 않는다
규약: 비순환 | `part-of`의 반대칭 공리로 추론된다
규약: 상태 | 부분에서 추론되며, 부분 하나가 `invalidated`면 복합체는 `suspect`다
