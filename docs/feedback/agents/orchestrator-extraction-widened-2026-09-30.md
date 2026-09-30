---
from: orchestrator
kind: notice
status: open
ref: handoff/code-as-chunks-2026-09-26.md
targets: [tools/, kb/dev/artifact/, kg/base-kg.ttl, BUILD.bazel, docs/rules.md, docs/roadmap.md]
---

# 추출을 `tools/*.py` 전부로 넓혔다 (2026-09-30, 인수 기록의 후속)

[인수 기록](orchestrator-accept-code-as-chunks-2026-09-26.md)이 남긴 "34 파일 확장"을 같은 날 수행했다 — vnv의 조건(결함 셋 수정)이 채워졌으므로 판단 없이 되는 것이었다. `bazel test //...` 71/71 PASS(파일별 드리프트 테스트 37 포함). 후속 뒤 **37/37**이다.

| 수치 | 표본 뒤 | 확장 뒤 |
|---|---|---|
| 추출 파일 | 1 / 37 | **37 / 37** |
| `artifact` 청크 · 복합체 | 100 · 25 | **624 · 184** |
| 살아 있는 청크 | 924 | 1,474 |
| CQ19 전방 추적 | 26/76 = 34.2% | **49/76 = 64.5%** |
| CQ20 · 고아율 · 성분 | 100% · 0% · 1 | 100% · 0% · **1** |
| `//kg:gate_test` | 32s | 55s(상한 120s 안) |

절 주석의 최소치는 하나다(파일 복합체의 부분이 둘 이상). 장 주석은 `validate.py` 하나만 필요했다. 클래스는 정의 청크 하나로 충분했다(최대 85줄). 파일마다 `refines`는 그 도구의 docstring이 인용한 결정이다 — 목록은 등록부 `tools/<모듈>.chunks.yml`.

## 판정 둘

- `consistency.py`·`metrics.py`의 `main`(292·248줄)이 `artifact` 상한 200을 넘는다. **상한을 올리지 않고 `main`을 나눴다** — 292줄 `main`이 결함이지 예산이 아니다. 산출물은 생성 시각 한 줄 외 바이트 동일, `main`은 50·38줄. 200줄 초과 정의는 저장소 전체에 0이다.
- 등록부의 `refines`가 deprecated 결정(`p8-judge-calibration-binding`·`p8-judge-question-form`)을 가리키던 둘은 `p8-judge-session-agreement`로 옮겼다. `consistency`의 `refines`는 developer 판단대로 `p4-redundancy-as-safety-margin`(도구 docstring의 인용; 보고 뷰이지 게이트가 아니다).

## hci에 전달

원장에 "추출 37/37 파일 · 청크 624 · CQ19 64.5% (2026-09-30)" 한 줄. 커밋 뒤 첫 도장(`stamp`)이 등록부 37개에 필요하다 — 커밋이 먼저다. 재판정 대상 없음(생성물).
