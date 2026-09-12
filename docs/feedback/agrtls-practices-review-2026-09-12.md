---
from: hci
status: open
targets: [docs/feedback/README.md, tools/channel_lint.py, .claude/agents/hci.md, docs/tools.md, docs/glossary.md, tools/consistency.py, tools/validate.py, tools/chunk2kg.py, docs/methodology.md, AGENTS.md, kg/catalog-kg.ttl, docs/agent-knowledge-system-notes.md]
---

# agrtls 하네스에서 가져올 것 — 열 후보 (2026-09-12, 4판: 하위 9 repo 포함)

원문 요청: [`inquiries/suggestion.md`](inquiries/suggestion.md) — "`~/git/agrtls`에서 에이전트를 위한 문서 활용을 참고해서
내용을 채우려고 해. 현재 정리하고 있는 내용보다 통일성 있고 유연성 있으면서 실질적인 효과가 있는 개선점이 될 만한
부분만 반영해줘."

## 검토 이력

| 판 | 읽은 것 | 결과 |
|---|---|---|
| 1차 | `agrtls_common` 표준 일부 · LEXICON | 후보 5 |
| 2차 | + `COMMUNICATION.md` 전문 · 규칙 색인 · 설계 표준 전문 · 설계 repo `lpranging` 실물 | 후보 7 — 우리 채널 규약의 모순 발견(F) |
| 3차 | + R7·R10 · lane README · `docs_review`·`handoffs`·worker · **우리 노트 12.2·13.5, 채널 온톨로지, 카탈로그, OKF, 도구 실물** | 후보 8 — F·A 를 우리 설계에 맞춤, N 신설 |
| **4차** | **하위 9 repo 전수** — 설계 `system_design`·`design_webservice`, 구현 `ranging_module`·`weight_device`·`webservice`·`device_installation`, 실험 `rlsim`·`upgrade/ranging_module`·`upgrade/weight_device` (CLAUDE.md·역할 정의·skill·lane README·도구 docstring·lesson 전부) | 후보 10 — P·Q 신설, F·A·C·E·K·M 보강, V&V 설계 입력 별도 절 |

## 질문

`agrtls`는 여러 repo를 가로지르는 하네스다. 이 저장소(단일 repo, 온톨로지 중심)와 구조가 달라 대부분은 가져올 것이 없다.
골라야 할 것은 **이 저장소가 실제로 겪은 문제에 답이 되면서 우리 설계(노트·온톨로지)와 어긋나지 않는 것**뿐이다.
어느 것을 채택할지가 유저 판단이다. 후보는 **지금 채택할 것(열)**과 **V&V 착수 시 설계 입력(별도 절, 지금은 채택 대상 아님)**으로 나눴다.

## 이미 정해진 것 (가져올 필요가 없는 것)

| agrtls | 이 저장소의 대응 |
|---|---|
| 비관여·읽기 전용 · 승인 게이트 · 블로킹 프롬프트 금지 · 구두 답은 항목에 옮겨 적기 · verify-then-proceed refresh | hci 역할 규약 + `channel_lint`·writer 검사 |
| SSOT 배너 + 사본 드리프트 검사 | 생성 파일 머리말 + `//:build_drift_test` |
| ID 증가·재사용 금지 · 폐기는 상태+사유+대체 | `supersedes`·`deprecated`·`owl:deprecated` |
| 역할 메모리 — 자기 폴더만, 일회성은 쓰지 않는다 | `.claude/agent-memory/README.md` |
| 채널은 그래프 밖 · 채널마다 담당 하나 | 온톨로지 `agt:Channel`·`agt:ownedBy`, 카탈로그 `chan-user-feedback` |
| "완결된 피드백만 채널을 통과한다" | 노트 12.2 [확정] |
| 게이트에 등록되지 않은 산출물 금지 (ranging DEC-005 — 깨진 채 초록 5주) | 지식은 `gen_build` + drift 검사로 전수 등록 — 구조로 충족 |
| append-only 판정 원장 + last-wins 뷰 (weight `results.tsv`) | `verified` 누적 · run-kg · 뷰 비저장 — 설계 일치 |
| raw 산출물과 문서 노드 분리, `.scratch`는 증거 아님 (rlsim) | 관측 저장소 / 지식 분리 — 설계 일치 |
| 게이트 밖 목록을 사유와 함께 명시 (weight BUILD 머리말) | `tools.md` "게이트 밖" 절 |

## 하위 9 repo 에서 수렴한 것 (셋 이상의 repo 가 독립적으로 같은 규칙에 도달)

| 수렴 규칙 | 어디서 | 우리 실물 |
|---|---|---|
| **규칙·근거의 거처는 영속 지식 — 소멸성 채널 경로를 인용원으로 쓰지 않는다** | `design_webservice` 온톨로지 제약 10 + L1("채널에만 적힌 근거는 refresh 와 함께 사라진다") · `webservice` 판정 체크리스트 7("드리프트를 고치면서 해법을 다시 소멸성 문서에 두는 것이 가장 흔한 재발 경로") · `ranging` DEC 규약 | **위반 1건 실재** — `p14-stage-pass-conditions/conclusion.md` 가 `docs/feedback/stage-pass-conditions.md` 를 "원본"으로 인용. 어제 발견, 그 항목을 지우지 못하는 원인 → **P** |
| **게이트 계층화 — 판정 실패(exit 1) / 설정·배선 문제(exit 2) / 미실행·SKIP(exit 3) 을 구분하고, 미실행은 통과가 아니다** | `webservice`·`ranging` tracecheck(ERROR/WARN/exit 2) · `rlsim` 3상태(parity/divergence/**NOT RUN**) · `upgrade` `fw_build` exit 3 SKIP("SKIP 을 PASS 로 보고하지 않음") | 우리 도구는 실패 종류를 구분하지 않는다 → **A 보강** |
| **판정 리포트에 스코프·시점·증거 등급을 결론과 같은 절에** — "0건"이 아니라 "무엇을 대상으로 쟀는가" | `design_webservice` L12(리포트에 실행 명령·스코프 축자, `--changed` 금지, vnv 재실행) · `webservice` 체크리스트 2("언제·어느 버전으로") · `upgrade` 4-필드 판정(결론/스코프/미확인/재개) | hci 항목·inspection 답에 형식 없음 → **F 보강**, V&V 입력 |
| **자기 작업분만 커밋, 커밋 전후 같은 검사 셋** | `webservice`·`weight`·`upgrade/weight_device` hci 정의·메모리(`commit-lane-procedure`) | 오늘 다른 세션의 645 파일을 통째로 담았다(유저 지시) → **M′** |
| **면제는 선언으로, 상태 축 포함(`deprecated` 는 길이 면제 등)** | 전 repo `harness.toml` 3축(파일·stem·상태) · common "오탐은 침묵이 아니라 선언으로" | 면제가 코드에 숨어 있다(`channel_lint.EXEMPT`, `consistency` "검증" 예외) → **C 보강** |
| **판정자는 self-test 재실행이 아니라 독립 재유도; 자기 하네스가 1차 용의자** | `ranging`·`weight` vnv("구현의 self-test 재실행은 검증이 아니다") · `rlsim` vnv("워커의 게이트 보고를 믿지 않고 직접 재실행") · `weight` "파일에 남은 숫자는 재실행 없이는 증거가 아니다" | 우리 vnv = "`bazel test` PASS 확인 + 주석" — 정확히 self-test 재실행. **vnv 역할 정의 파일이 없다**(`.claude/agents/`엔 `hci.md` 뿐) → V&V 입력 |
| **하네스 문서도 생성물** | `upgrade/ranging_module` — CLAUDE.md·agents·skills·tools 가 TTL recipe 생성물, 손으로 고치면 다음 빌드에 덮어씀 | 우리 요구 "문서는 저장하지 않고 생성한다"의 **실현 선례** → K 의 방향 |

## 현재 상태 — 이 저장소가 실제로 겪은 문제 (실측 2026-09-12)

| 겪은 일 | 남은 것 |
|---|---|
| 채널 규약의 모순 — README 32행(유저 lane 은 타 에이전트에게 읽기 전용) vs `channel_lint` 23행(그 항목 안의 `인수:` 줄 요구). orchestrator 가 유저 lane 5개 항목에 8줄 | hci → orchestrator lane 이 없다 |
| 결정 청크가 채널 파일을 "원본"으로 인용 | 위반 1건, 게이트 없음 |
| 문서의 죽은 링크·앵커·경로 게이트 없음 — 깨진 앵커 이틀째, hci 의 `/tmp` 스크립트로만 확인, 백틱 경로 부재 5 | 게이트 없음 |
| 게이트 이름 세 체계(결정 한글명+절 · 총람 한글명 · 도구 kebab) | 잇는 열 없음 |
| `consistency` ⑥ "프로파일" 28건 → 용어집에서 빼서 해결, `verifier/` 1건 소음 | 검사 약화, 면제 하드코딩 |
| 라벨 형식 197건 FAIL → 범위 좁힘 | 판단 기준 미기록, "게이트를 추가할 때" 절 없음 |
| 유저가 답은 줬으나 태깅 안 한 항목이 `open` 으로 영원히 | `rejected` 없음 |
| 42줄 상한 게이트 — 노트 4.10 분할 신호에 "압축 반복"은 없다 | 압축으로 버티는 청크를 셀 수 없다 |
| 역할 정의 파일 `hci.md` 하나 · skill 0 · 세션 시작 절차 없음 · `impact.py` 를 hci 절차가 안 씀 | — |

## 답이 가르는 것

- 채택하면 위 문제들이 구조로 막힌다. 채택하지 않으면 다음 개정·치환·인수·문서 검토에서 반복된다.
- 열은 **따로 고를 수 있다.** 의존은 C→A 하나. **F·Q 는 규칙·노트 편집이라 유저 태깅 좌석**, M′ 은 hci 자기 메모리라 좌석 없음.

## 선택지 — 지금 채택할 것 (열)

### F. hci → orchestrator lane `handoff/` + verdict + `rejected` — 통일성 (**1순위 권고**)

1. `docs/feedback/handoff/` — hci 가 쓰는 lane(담당 hci, 카탈로그 `chan-handoff`). 항목: `source:`(원본 항목) · `verdict: apply | apply-with-changes | needs-decision` · **파급효과**(`bazel run //tools:impact` 출력 + "무엇에 닿지 않는가") · **반영 계획**(구체 편집 + 같은 사실이 서술된 지점의 **검색 키워드 목록** — 우리는 중복을 안전율로 용인하므로(`p4-redundancy-as-safety-margin`) 전수 grep 이 유일한 방어) · **확인 못 한 것**(`upgrade` lesson 의 "자료로 확인하지 못해 쓰지 않은 것" 절) · 판정.
2. orchestrator 의 인수 기록은 **자기 lane(`agents/`)에** `ref: handoff/<항목>` 로. 유저 lane 은 읽기 전용으로 복귀, `channel_lint` 는 `handoff`↔`agents` 쌍을 대조. 짝 없는 `handoff/` 항목 = 되돌아오지 않은 것.
3. 유저 lane 에 `rejected`. refresh 는 승계 확인 뒤 제거.
4. hci 가 쓰는 항목도 `.wip.md → rename`, placeholder 남은 항목은 처리 대상 아님.
- `verified` 이름은 쓰지 않는다(OKF 필드명). `ownedBy` 와 정합. 노트 12.2 의 "완결된 피드백만 통과"가 `needs-decision` 으로 기계 표현된다.
- 비용: 디렉토리 + README + hci.md + `channel_lint` + 카탈로그 한 개체. **유저 좌석.**

### P. 소멸성 경로 인용 금지 게이트 — 통일성 (권고, 신설 · 실재 위반 1)

살아 있는 청크 본문이 `docs/feedback/` 경로를 인용하면 FAIL (`chunk2kg` 한 줄). 근거는 세 repo 수렴 규칙. 고칠 것:
`p14-stage-pass-conditions/conclusion.md` 의 인용을 노트 14.1 로만(orchestrator). 그러면 `stage-pass-conditions` 항목도 refresh 가능.
- 비용: 검사 한 줄 + 청크 한 곳.

### N. 문서 현행성 게이트 — 죽은 링크·앵커·경로 — 통일성 (권고)

hci 의 임시 `linkcheck.py` 를 `tools/doccheck.py` 로 들이고 백틱 경로 검사를 더해 `//docs:doccheck_test`. 원칙은 `docs_review` 의
"게이트는 기계적으로 참·거짓이 갈리는 것만, 나머지는 검토 재료". 생성물 경로는 표지가 아니라 규칙("`bazel-bin/` 접두로 적는다").
- 비용: 도구 하나(프로토타입 있음) + 타깃 하나.

### A. 게이트 식별자 통일 + 해소 절차 열 + 실패 종류 — 통일성 (권고)

총람에 `id` 열(= 도구의 kebab 이름) 과 "해소 절차(누가·어디서)" 열. 결정 `p6-gate-catalogue` 의 표기 뒤에 같은 id. 도구 출력을
`FAIL [<id>] …` 로 통일하고 **실패 종류를 구분** — 판정 실패 / 설정·입력 문제 / 미실행(SKIP 은 PASS 가 아니다). 번호(`G{n}`)는 불필요.
- 비용: 총람 두 열 + 결정 청크 한 곳 + 도구 출력 형식.

### B. 용어집에 tier — 유연성 (권고)

`tier` 열(1 기계 치환 · 2 유저 결정 · 3 문맥 공존, 바꾸지 않음). `consistency` ⑥ 은 tier 1 만 위반. "프로파일"·"검증"을 tier 3 으로.
- 비용: 용어집 한 열 + `consistency` 의 열 읽기.

### C. waiver 선언 — 유연성 (A 선행)

`docs/waivers.md` 에 `게이트 id · 대상 · 사유 · 판정자 · 날짜`, 축은 파일·stem·**상태**(예: `deprecated` 는 길이 면제). 도구는 집계에서
빼되 목록에 남긴다. 코드 속 면제 둘(`channel_lint.EXEMPT`, `consistency` "검증")과 `verifier/` 1건을 첫 항목으로. ODD 의
`EXCLUSIONS_REVIEWED` 가 같은 패턴의 선례.
- 비용: 파일 하나 + 도구 조회.

### E. "대량 FAIL 이면 규칙을 의심한다" + 게이트 vs 보고 + 비-초록 기준선 선언 — 방법론

`tools.md` 에 "게이트를 추가할 때" 절(이름 → 총람 행 → 도구 → 첫 실행 실태 → 대량 FAIL 이면 판정을 총람 행에 기록), "게이트 vs 보고"
기준, 그리고 **아직 배선 안 된 검사를 정상으로 선언하는 문장**(`device_installation` "trace-check exit 2 가 정상이다" — 다음
세션이 고치러 오지 않게). 결정으로 올릴 값어치 있음.
- 비용: 세 문단.

### Q. 상한 압축 반복 = 분할 신호 — 방법론 (신설, L18)

`design_webservice` L18: 42줄 같은 상한에 걸려 **압축으로 버틴 횟수** 자체가 분할 신호(1회 유예 · 2회 경고 · 3회 부채); 분할은 조항
번호(우리는 IRI·라벨) 보존 + 원 청크에 포인터. 노트 4.10 의 분할 신호(라벨 둘·재사용·가정·suspect 입도)에 이것이 없다 —
압축 대응을 반복하면 가장 최근 개정이 가장 근거가 얇아지는 역전이 생긴다. 계수는 git 이력(같은 청크의 줄 수가 42 근처에서 오르내린 횟수)으로 잴 수 있다.
- 노트 4.10 개정이라 **유저 좌석**. 결정 한 건.

### K. 정형 작업을 skill 로 — 문서 활용 (조건부)

절차가 `method.md` 14개 절에 흩어져 있고 skill 은 0. 채택 조건은 "원본 절 + 명령 순서 열 줄 이내". 4차 보강: `upgrade/ranging_module` 은
하네스 문서 전체(CLAUDE.md·agents·skills·tools)를 **TTL recipe 에서 생성**한다 — 채택한다면 손으로 쓰는 것이 아니라 그 방향(6단계 문서 생성)이
우리 요구와 맞다. 지금 손으로 쓰면 이중 원본.
- 비용: 생성이면 6단계 작업, 손으로 쓰면 SKILL.md 4~5개(드리프트 위험).

### M′. 세션 시작·커밋 절차를 역할 메모리에 — 문서 활용 (작음, hci 즉시 가능)

3차의 M(CLAUDE.md 명령 블록)을 바꾼다. `webservice`·`weight` 는 절차를 **hci 역할 메모리**에 둔다 — "명령 / 정상(수치 기준선)" 2열 표,
없는 것도 없다고 적기(`verified/` 폴더는 이 repo 에 없다. 정상이다), 커밋 전 검사 셋 → `git diff --cached` 검산 → **자기 작업분만** →
커밋 후 같은 셋 재실행. 진입점 편집이 아니므로 좌석 없이 hci 가 지금 쓸 수 있다.
- 비용: 메모리 파일 둘. `upgrade` G1 원칙("판정·규약은 자동 주입 문서에, 서사·수치는 조회형으로")에 따라 CLAUDE.md 는 그대로 둔다.

## V&V 착수 시 설계 입력 — 지금 채택 대상 아님 (`kb/ontology/vv` 부재, `kb/vv/` 비어 있음)

구현·실험 repo 가 V&V 에서 실제로 겪고 성문화한 것. 노트 8장(8.3 검증 대응물 · 8.6 세 방향 · 8.11 합격 기준 · 8.14 판정자 · 8.20 역할 ·
8.23 케이스 생성)과의 대조는 V&V 착수 항목에서 한다. 여기서는 목록만.

| 규칙 | 출처 | 우리 설계와의 관계 |
|---|---|---|
| 판정 어휘 3~4상태 — pass / fail / **SKIP·NOT RUN**(미실행은 통과가 아님) / HIL(환경 밖 대장) / OBSERVE(관측만, 판정 아님) | `rlsim` 3상태 · `weight` SKIP("NOT scored, NOT quietly passed") · `ranging` OBSERVE | 어휘 없음 — 신설 필요 |
| **부재의 가시화** — 행 없음 ≠ 판정할 것 없음; clean 이어도 행을 만든다 | `ranging` run.sh("Silent absence is the failure mode this guards against") | 커버리지 분모 설계(8장)와 결합 |
| 4-필드 판정(결론 / 스코프 / 미확인 / 재개) + **증거 등급 4단**(정적 독해 · 이상 입력 실행 · 손실·경계 입력 실행 · 실기) + 결론 어휘 분리(기각·관측 불가·미결) | `upgrade/ranging_module` review-dispatch · C4 | 판정 노드 속성 후보 |
| **premise 행 + CONTROL 축** — 판정마다 전제 성립을 행으로, 조건을 뒤집으면 판정도 뒤집힘을 값으로 | `weight` manifest 2026-09-02 | Evidence `polarity` 로 표현 가능 — 폐기한 `counterfactualTest` 의 재도입이 아니라 증거 기록 종류 |
| **계획 선등록** — 실행 전에 seed·규모·tolerance·합격 기준 고정, 결과 본 뒤 조정 금지; baseline 없는 측정은 기록하지 않는다 | `rlsim` sim-parity · experiments README | r-024(기준 먼저) + `p8-reproducibility` 와 방향 일치 |
| 지표 세트를 **확정 결정**으로 + 축 역할(주장 / 하한 제약 / 회귀 감시) + 프록시 분리 + 최악 seed 병기 + "각 축이 실제 결함을 잡은 실적" | `upgrade/weight_device` D8·D3 | 14.1 세 축("단일 축 개선이 다른 축을 깨면 채택 불가")과 같은 구조 |
| **독립 재유도** — self-test 재실행은 검증이 아님; 판정자가 자기 하네스를 1차 용의자로 | `ranging`·`weight`·`rlsim` vnv | 8.20 기준 저자 ≠ 검증기 저자와 같은 방향. vnv 역할 정의 파일 신설 시 반영 |
| 기준 부재는 결함이 아니라 **⚙ 확정 요청**으로 승격(측정값을 채택 후보로) · 증거 문서 / 판정 문서 분리 | `ranging` EVIDENCE_*.md → F19 | 채널 항목 형식 |
| 실행 기록 골격 — 컬럼 계약 · 실행 조건 · 입력 건전성 counter · GT 유무와 대체 sanity · `<!-- historical -->` | `upgrade/weight_device` 캡처 노트 | 관측 청크 템플릿 |
| 상류 소비 — frozen/active 정책 · **이식 관계 선언**(언어·형식이 바뀐 이식은 내용 비교로 안 잡힘) · verbatim/diverged/local | `upgrade/ranging_module` upstream_guard | 참조 저장소 `sources` 가 선언; 신선도 pin 은 없음 — 지금은 동결에 가까워 보류 |

## 가져오지 않기를 권하는 것 (4차 확정)

- **레지스트리·배선·채널 프로토콜·vendoring·`harness.toml`·work order/conductor** — 여러 repo 전제.
- **상주 세션 인프라·인가 3형태(`user_approval`/`ref`/`work_order`)** — 전자는 agrtls 도 미설치·미검증, 후자는 단일 사용자 repo 에서 비용 대비 낮다.
- **lesson(`L{n}`)·교차 지식(`K{n}`)** — 세 repo 가 L 을 쓰지만 우리는 `memory` plane + 일반화(0.5·6.3절). 4부 형식(증상/믿은 원인 → 근본원인 → 일반화 규칙 → 이력)은 관측 청크의 본문 골격으로만 참고.
- **파생물 sha256 무결성(`MODIFIED` exit 1)** — 노트→청크 재도출을 손으로 하는 지금은 해당 없음(6단계 뒤).
- **markdown frontmatter 온톨로지 · 200줄 상한 · `docs_review` 의 orphans/removed_refs** — 지난 단계이거나 hci 스캔이 이미 잰다.

## 답
권장대로.
