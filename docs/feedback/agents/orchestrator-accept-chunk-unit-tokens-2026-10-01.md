---
from: orchestrator
kind: notice
status: open
ref: handoff/chunk-unit-tokens-2026-10-01.md
targets: [kb/dev/decision/p1-chunk-unit-is-tokens/, kb/dev/decision/p1-context-budget-breakdown/, kb/dev/requirement/r-014-42-line-chunk.md, MODULE.bazel, tools/tokens.py, tools/chunk_lint.py, tools/validate.py, kb/ontology/shapes/token-budget-shapes.ttl, kb/odd/project-odd.yml, docs/agent-knowledge-system-notes.md, AGENTS.md, STYLEGUIDE.md, docs/rules.md, docs/waivers.md]
---

# 인수 기록 — `chunk-unit-tokens-2026-10-01` (2026-10-01)

승인 항목 [`chunk-unit-tokens-2026-10-01`](../chunk-unit-tokens-2026-10-01.md)의 반영 계획 여섯을 전부 수행했다. 유저 답 — 단위는 토큰, 42의 배수, 공개 토크나이저 하나를 의존성으로 고정.

| 계획 | 수행 |
|---|---|
| 1 developer — 토크나이저 | 후보 넷을 이 저장소 청크 100개로 실측(혼합 표본 문자/토큰: `o200k_base` 2.35 · `cl100k` 1.84 · XLM-R SP 2.13 · `p50k` 1.01). **`tiktoken 0.12.0` + `o200k_base`** — 어휘 파일은 `MODULE.bazel` `http_file`(sha256 고정, 오프라인), 패키지는 lock 가산. ODD 조건 **`cond-tokenizer-lock`**(등급 A, 세 자리의 해시·버전 대조) — 임베딩을 제외한 것과 반대 경로로 조건을 먼저 세웠다. 계수기 `bazel run //tools:tokens` |
| 2 vnv — 실측 | 청크 1,648(뒤에 TTL 포함 1,782): 저작 산문 줄당 토큰 중앙 **27**, 예산 200줄 = **5,418 = 42×129**. 관측 주석 `chunk-token-distribution-first-measurement` |
| 3 orchestrator — 숫자 | **1,092 = 42×26**(예산 ÷ 5 — 42줄의 원래 도출을 토큰으로 옮김), 인용(`artifact`·`memory`) **2,856 = 42×68**(200줄 환산). 근사(3,200)와 실측의 차 1.7배 — hci 표의 630은 근사의 산물이었다. 참조 저장소의 260은 도출과 무관하고 저작 산문 43%를 쪼갠다 → 기각. 결정 `p1-chunk-unit-is-tokens`(`p1-context-budget-breakdown`을 supersede), 요구 `r-014` 개정, **노트 938·949·641·975·1001·1010행 정정**(유저 의도 대 노트 — 통일 기획 1-②의 첫 실행), 황금률 4·STYLEGUIDE·rules·method·INTENT·CLAUDE |
| 4 developer — 게이트 | `agt:lineCount` → **`agt:tokenCount`**, `token-budget-shapes`, `kb_lib.BODY_TOKEN_LIMITS`(단일 정의처 — 게이트 `token-budget`이 shape와 어휘 해시까지 대조), 본문 판정처 하나(`body_text`), 어휘 파일을 head·검사 액션·lint·gate·workset·space에 배선. 비용은 프로세스당 어휘 적재 0.43s(콜드 전체 ~12분) |
| 5 역할별 분할 | 초과 12 → 코드 6(소스 분할, 산출물 바이트 동일 — `render_audit` 4,686 → 1,023 등)·TTL 2(파일 하나 = 청크 하나)·케이스 3(`p10` 분할, uuid 승계)·memory 로그 1 = **면제**(append-only — `docs/waivers.md`의 `chunk`·`shacl`; 새 로그는 `judge`가 토큰 안에서 나눈다) |
| 6 vnv·developer — 음성 | 고정물 `//defs/tests:token_budget_test`(1,092 통과 · 1,093 FAIL · 어휘 변조 거부·`token-budget` FAIL), 케이스 `token-budget` |

측정이 드러낸 것: `tokens`의 첫 분모가 `kb/ontology` TTL 청크를 빠뜨려 2건을 놓쳤다(정정 — 분모는 게이트가 판정하는 전 청크). `vv_run`의 bare `python3`에 `tiktoken`이 없어 검증기가 죽었다 → 하네스 인터프리터 + pip 폐포만 넘기는 것으로(격리 대상은 도구 모듈이지 서드파티가 아니다).

## hci에 전달

원장에 "청크 단위 = 토큰: 1,092(42×26) · 인용 2,856 · 예산 5,418, 계수기 o200k_base 고정 (2026-10-01)" 한 줄. 노트 여섯 줄을 정정했다 — 동결 전의 유저 의도 정정이고 각 줄에 표시했다. 재판정 대상: 라벨·본문을 고친 결정 넷(`p4-plane-subclass-level-property`·`p4-chunk-rules-as-shacl-shapes`·`p4-chunk-as-ontology-class` — orchestrator 재검토 표시 완료; `d-0071`·`d-0072`는 deprecated).
