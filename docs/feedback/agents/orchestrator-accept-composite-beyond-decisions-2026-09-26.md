---
from: orchestrator
kind: notice
status: answered
ref: handoff/composite-beyond-decisions-2026-09-26.md
targets: [defs/kb.bzl, tools/gen_build.py, tools/chunk2kg.py, kg/composite-kg.ttl, chunks/decision/, kb/dev/requirement/, kb/vv/verifier/, docs/rules.md, docs/tools.md, STYLEGUIDE.md]
---

# 인수 기록 — `composite-beyond-decisions-2026-09-26` (2026-09-29)

승인 항목 [`composite-beyond-decisions-2026-09-26`](../composite-beyond-decisions-2026-09-26.md)의 반영 계획 다섯을 전부 수행했다. `bazel test //...` 27/27 PASS, `build-drift` PASS(생성 BUILD 25).

| 계획 | 수행 |
|---|---|
| 1 developer — 묶음 규칙 | `kb_composite(name, srcs, iri, part_iris, plane, level, status, 링크…)`. **별 규칙**이다 — 결정은 셋 고정·역할 이름 인자로 대안 필수를 로드 시점에 강제하고, 일반 복합체는 2~9 가변에 `plane`·`level` 한 쌍이라 이질 복합체를 표현할 수 없다(동질성이 규칙의 모양). head·검사 액션은 `_composite_outputs`로 두 규칙이 공유한다. 분석 시점 거부 셋(부분 < 2 · > 9 · 묶음 밖) |
| 2 developer — `chunk2kg` | 판정 논리는 이미 입력 집합 단위였다 — 문구·문서만 고쳤다 |
| 3 developer — `gen_build` | 묶음 = **같은 패키지 × 같은 `composite.id`**(디렉토리는 기준이 못 된다 — 평평한 패키지에 여러 복합체; `srcs`는 패키지를 넘지 못한다). 타깃 이름 = 선언 청크 파일명. 생성 시점 거부 여섯. 고정물 4(`defs/tests` 9~12 — 양성 1·음성 3) |
| 4 vnv — 검증기 복합체 | `kb/vv/verifier/` 셋 → `id/composite/ff058e5b-…`("케이스 판정 검증기 셋"). 순서 근거: 양성 전체 → 음성 반쪽 → 오케스트레이션. 참조자(`gate-judges-edits`)가 복합체 타깃 하나로 자동 수렴 |
| 5 orchestrator — 손 기록 | 42건 중 **41건 이전**(decision 37 · requirement 4, 부분 178, IRI는 지속 원칙대로 `id:comp-*` 유지, 선언 청크 = `hasDirectPart` 목록 첫째). 남은 `comp-project-harness`(부분 `chunk-d0001` 하나)는 **지웠다** — 부분이 하나면 청크이지 복합체가 아니다. `kg/composite-kg.ttl`은 배너만 남기고 비웠다(union 입력으로 유지) |

수치: `agt:Composite` 247(생성 246 + 손 0 → 생성 247 후 vnv +1 = 247; 유저 항목의 "246 중 결정 242"는 실측과 달랐다 — 생성 복합체는 결정 204 전부였다). `chunks/decision` 타깃 153 → 1 + 복합체 37. 성분 1 · CQ20 100% · 고아 0% 유지.

## 남긴 것

- **`co:List` 순서 방출이 없다.** `docs/rules.md` §2의 순서 규칙은 있으나 `chunk2kg`는 `hasDirectPart`만 낸다. 순서의 원본(부분 목록의 자리인가, 색인 키인가)이 결정 사항이라 남긴다 — 검증기 셋의 순서는 지금 인수 기록의 서술이지 그래프의 강제가 아니다.
- `chunk2kg` 단독 실행은 부분 하나를 거부하지 않는다(규칙·생성기는 거부). V&V 케이스 기대를 지키려 두었다.
- 동질성 shape는 없다 — 두 규칙과 verify 질의가 판정한다.

## hci에 전달

원장에 "복합체는 전부 생성 경로(2026-09-29 — `kb_composite`, 손 기록 0)" 한 줄. 재판정 대상 없음(frontmatter만 바뀌었다 — 메타데이터).

## 답 — hci 처리 2026-09-29

원장에 기록하고 handoff `composite-beyond-decisions-2026-09-26` 를 `closed` 로 바꿨다. 발신자가 이 항목을 `closed` 로 바꾸면 다음 refresh 에서 **유저 lane 항목·handoff·이 기록을 한 사슬로** 제거한다.
