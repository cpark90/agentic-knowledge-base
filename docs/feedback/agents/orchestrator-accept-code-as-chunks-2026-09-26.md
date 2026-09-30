---
from: orchestrator
kind: notice
status: open
ref: handoff/code-as-chunks-2026-09-26.md
targets: [kb/dev/decision/p7-code-extraction-direction/, kb/dev/decision/p7-code-links-on-file-composite/, kb/dev/decision/p10-function-identity-registry/, tools/extract.py, tools/stamp.py, tools/kb_lib.chunks.yml, kb/dev/artifact/kb_lib/, tools/revalidate.py, kb/vv/verifier/, kb/vv/verdict/code-chunk-churn-cycle.md, STYLEGUIDE.md, docs/rules.md, docs/roadmap.md, AGENTS.md]
---

# 인수 기록 — `code-as-chunks-2026-09-26` (2026-09-30)

승인 항목 [`code-as-chunks-2026-09-26`](../code-as-chunks-2026-09-26.md)의 반영 계획 여섯을 전부 수행했다. 유저 답 "권고대로" — **추출**(코드가 원본)·**`kb_lib.py` 표본 먼저**. `bazel test //...` 34/34 PASS, 드리프트 검사 셋 PASS.

| 계획 | 수행 |
|---|---|
| 1 orchestrator — 결정 | 셋을 저작했다: `p7-code-extraction-direction`(추출, 드리프트 게이트, `artifact` 도장 = 테스트 통과, 줄 상한은 프로파일 파라미터), `p7-code-links-on-file-composite`(링크는 파일 복합체, 함수는 `part_of`만, 절 복합체로 7±2), `p10-function-identity-registry`(등록부 `이름 → uuid`가 원본, 개명·삭제는 등록부 편집, 해시는 개명을 **제안**만) |
| 2 developer — 추출기 | `tools/extract.py`(`bazel run //tools:extract -- <소스>`), 게이트 `extract`·`extract-drift`. 파일 → 장 → 절 → 정의 복합체(`composite.part_of` 중첩 — 이 자리의 첫 사용), `ordered` = 소스 순서. 소스의 절 주석(`# ══ 장`·`# ── 절`)이 구조의 원본 |
| 3 developer — uuid 안정성 | 사이드카 등록부 `tools/kb_lib.chunks.yml`. 개명은 정규화 본문 해시로 제안(`FAIL [extract]` 안내) → 사람이 키를 고친다; 신설만 자동 |
| 4 developer — 드리프트 게이트 | `//:extract_drift_test`(바이트 동일). `--check` 멱등 |
| 5 orchestrator — 규칙 셋 | `STYLEGUIDE.md` §4 `artifact` 도장·상한, `docs/rules.md` §1·§2·§7, `docs/roadmap.md` tangle → 추출, `AGENTS.md` 셀프체크 |
| 6 vnv — churn 실측 | 자극 다섯(수정·개명·신설·삭제·순서). **uuid 정체성 전부 성립**(개명·순서 0/0, 신설·삭제 1/1). 결함 셋을 드러냈고 developer가 고쳤다: `revalidate`가 경로로 비교(개명 → 삭제+신규 30) → uuid 비교; 하류 라벨이 함수 파일 경로(`rdeps` 0/0) → `iri_to_label` + `kb_composite`; 불변 청크의 `generated.at` 갱신(100 파일 잡음) → 본문 변경 시만. 게이트 시간 불변(`extract_drift` ~1s, `gate_test` ~32s) |

## 표본 실측

| 수치 | 전 | 후 |
|---|---|---|
| `artifact` plane 청크 | 3 | 103(표본 100 + 검증기 3) |
| 복합체 | 253 | 278(표본 25) |
| CQ19 전방 추적 | 24/76 = 31.6% | 26/76 = 34.2% |
| TIM 채움 | 10/15 | 13/17(칸 둘 추가 — `refines: artifact→decision`·`artifact→contract`) |
| 42줄 초과 함수 | — | 4(최대 185줄) → `artifact` 상한 **200**(게이트 `line-budget`이 `kb_lib`·shape 동일성 강제) |
| 검증기의 `verifies` 대상 | 없음 | 파일 청크 `module`(TIM `verifies: artifact→artifact` 채움) |

도장 도구 `stamp`(등록부 `tested` — `bazel test` PASS 뒤, 커밋된 소스만; 소스가 바뀌면 `verified`가 빠진다)는 있고 **첫 도장은 커밋 뒤**다.

## 계획과 다르게 읽은 것

- `serves`를 쓰지 않는다 — 정의역이 `agt:DecisionChunk`라 artifact가 요구를 직접 `serves`하면 shape가 거부한다(56건 실측). 코드는 결정을 `refines`하고 결정이 요구에 닿는다.
- 34 파일 확장의 실제 비용은 소스에 장·절 주석을 넣는 일이다(대부분 절 주석이 없다). vnv 판정: 결함 셋을 고친 뒤 조건부 진행 — 셋이 고쳐졌으므로 다음 회차의 developer 작업이다.

## 남긴 것 · 유저에게 되돌릴 것

- **코드베이스 churn**(호출부 파손 — 개명 하나에 36곳)은 잡지 못한다. developer 초안: AST 호출 관계를 references 족 잎 `usesDefinition`(함수 청크 → 함수 청크, deps 아님, `dangling`·`revalidate`가 판정)으로 — **어휘 확장이라 승인이 필요하다**(별 항목).
- `cites: artifact→decision`(코드 주석의 결정 인용)은 TIM에 넣지 않는다(권고 수용). 클래스 규칙은 표본에 클래스가 없어 미실측.

## hci에 전달

원장에 "코드 → 청크 = 추출(2026-09-30), 표본 kb_lib 100 청크·CQ19 34.2%, uuid 정체성 성립" 한 줄. 유저 질문 하나 — `usesDefinition` 어휘 잎 추가 승인. 재판정 대상 없음(생성 청크는 미검증, 결정 셋은 orchestrator 저작).
