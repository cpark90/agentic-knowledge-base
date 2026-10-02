---
from: orchestrator
kind: notice
status: open
ref: handoff/unification-program-2026-10-01.md
targets: [defs/kb.bzl, tools/gates2kg.py, tools/kb_lib.py, tools/validate.py, tools/doccheck.py, kb/ontology/related/harness/, kb/ontology/shapes/gate-shapes.ttl, kg/BUILD.bazel, docs/rules.md, docs/tools.md]
---

# 통일 기획 2단계 — 첫 조각: 게이트 id의 단일 정의처와 그래프 개체 (2026-10-02)

산발 목록의 첫 행(게이트 id가 넷으로 갈림)을 닫았다. `bazel test //...` 75/75 PASS(새 검사 둘 포함).

| 항목 | 결과 |
|---|---|
| 대조 | 상수 25 · 코드 태그 51 · 총람 28 · 하네스 문단 25 → 합집합 **56**. 넷에 다 있던 id는 **10**뿐, 한 목록에만 있던 id 12, 태그만 있고 상수 없던 것 22, 총람에만 있던 것 2 |
| 정리 | 삭제 2(`space2kg` — 하네스 문단의 오기, 생성기의 게이트 id는 `space`; `line-budget` — 줄 상한 폐지의 잔재) · **게이트 아님 분리 9**(`consistency`·`judge`·`link`·`open`·`propose`·`revalidate`·`tokens`·`validate`·`weave` — 입력 문제·보고 태그, `TOOL_TAGS`) · 신설 2(`gate-registry`·`gates2kg`) · 리터럴 태그였던 15에 파생 상수. **게이트 49 · 도구 태그 9** |
| 단일 정의처 | `defs/kb.bzl`의 `GATES`(id → 계층·판정 도구·ko 라벨·설명) — `RESIDENCY`·`EXTRACTED_SOURCES`와 같은 해법. `kb_lib`의 손 상수 26을 지우고 리터럴 읽기로 파생. 예외 둘(rdflib 없이 도는 생성기의 지역 리터럴·`getattr` 폴백)은 `gate-registry`가 대조 |
| 그래프 개체 | `//kg:gates_kg`(생성, 트리플 341) — `id:gate-<id> a agt:Gate ; agt:inLayer processLayer ; agt:gateTier <shape|verify|analysis|test|human> ; agt:enforcedBy <판정 도구의 파일 복합체>`. 어휘 `gate-ontology`·`gate-tier-ontology`(harness 모듈), shape `gate-shapes` |
| 검사 | `gate-registry`(`//tools:gate_registry_test`): 코드 태그 ⊆ 등록부 · 손 상수 없음 · 폴백 일치 · 등록 id가 코드에 닿음. 로드 시점 `check_gates`. `doccheck --gates`: 총람 `id` 열 ⊆ 등록부(게이트), 총람에 없는 등록 게이트는 보고(15 → 문단에 적어 0) |
| CQ-38 | 프로세스 층 716 → **773**(코드 청크 724 + 게이트 49). 종류 절을 `VALUES ?kind { agt:Gate }`로 열어 뷰·skill이 더해질 자리를 만들었다 |

developer가 브리핑과 다르게 한 둘을 받는다: `agt:gateLayer` → `agt:gateTier`(서비스 층 `inLayer`와 이름이 겹친다), `agt:judgedBy` 재사용 대신 `agt:enforcedBy`(`judgedBy`의 정의역이 `agt:Chunk`라 게이트 49가 청크가 되어 위반 188건 — 실측).

## 남은 것 (2단계)

뷰 13·skill 21의 개체(같은 꼴 — `agt:View`·`agt:Skill`) · 테스트 타깃 16 · **원본 결정 없는 규약 113**(orchestrator 저작 — 주제별 묶음으로 결정 수를 줄이는 것이 설계 변수) · `AGENTS.md` 황금률의 원본 결정(3단계 투영의 선행 조건) · 총람 표의 생성 뷰 전환(3단계).

## hci에 전달

원장에 "게이트 id 단일 정의처 `GATES`(49 + 도구 태그 9), 개체 `id:gate-*` 49, 검사 `gate-registry` (2026-10-02)" 한 줄. 재판정 대상 없음. 유저 판단 불필요 — 다음 조각(뷰·skill 개체, 규약의 원본 결정)도 판단 없이 된다.
