---
id: https://agentic-knowledge-base.dev/id/chunk/84dbc611-a7b9-4944-a6d8-0b8b4716f9f3
type: decision
level: concrete
title_ko: 같은 한글 단어를 두 개념에 쓰지 않는다
title: No Korean word carries two concepts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0025]
part_of: https://agentic-knowledge-base.dev/id/composite/727e4644-52bb-4880-bb4b-ba11d36469f1
composite: {id: https://agentic-knowledge-base.dev/id/composite/727e4644-52bb-4880-bb4b-ba11d36469f1, title_ko: 한 단어에 한 개념 — 동음 충돌 회피, title: One word, one concept}
---
**결론** — 같은 한글 단어를 두 개념에 쓰지 않는다. 충돌하는 자리마다 한쪽에
**다른 단어를 할당**해 1:1로 고정한다.

주요 할당 — 온톨로지는 T-Box(개체 집합은 "지식그래프"), 어휘는 개념 이름
집합(공리·규칙은 "형식화"), ODD는 운영 조건 명세 문서(에이전트 권한은
"스코프", 항목별 전제는 "가정"), 영역은 ODD가 정한 대상 영역(논의 범위는
"범위", 분야는 "분야"), 제약은 후보 링크 간 양립 조건(논리적 제한은 "공리",
요구사항은 "요구"), 요구는 `requirement` plane 청크(체계에 대한 요구는
"입력"), 기준은 logical의 합격 기준, 검증은 명세 대비 확인(기계적인 것은
"검사"), 링크는 추적성 관계(문서 내 참조는 "참조"), 청크는 42줄 최소
단위, 복합체는 `part-of` 묶음이다.

두 KB를 가르는 자리도 이 규칙로 고정한다 — **시나리오·검증 목표·verifier는
V&V KB 전용**이고, 개발 KB의 대응물은 결정·요구·구현이라고 부른다. 상태를
가리키는 말도 갈라진다 — 전체 스냅샷은 "리비전", 스코프 × level 창으로 거른
청크 집합은 "작업 집합", 관측 기록은 "실행 기록"이다 (0.5절).
