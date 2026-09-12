# 인수인계 lane — hci → 담당 역할

유저가 승인한(`approved`) 유저 lane 항목마다 hci 가 **하나의 인수인계 항목**을 쓴다 (agrtls F, 유저 채택 2026-09-12).
담당 역할(orchestrator·developer·vnv)은 이 항목을 읽고 수행한 뒤 **자기 lane(`agents/`)에** `ref: handoff/<이 파일>` 로
인수 기록을 남긴다 — 유저 lane 항목에는 hci 외 누구도 쓰지 않는다. `channel_lint` 가 handoff ↔ agents 쌍을 대조한다:
짝 없는 handoff 항목 = 아직 되돌아오지 않은 것. 형식 원본: `kg/catalog-kg.ttl` `id:chan-handoff`.

- 파일명: `{원본 유저 lane 항목의 파일명}` 그대로 (예: `agrtls-practices-review-2026-09-12.md`)
- 작성은 `.wip.md` → 완료 시 rename. placeholder 가 남은 항목은 처리 대상이 아니다.
- `verified` 라는 이름은 쓰지 않는다 (OKF 필드명과 충돌).

```markdown
---
from: hci
source: {유저 lane 파일명}          # 실재해야 한다
verdict: apply                     # apply | apply-with-changes | needs-decision
status: open                       # open → closed (담당 역할의 agents 항목이 돌아온 뒤 hci 가)
---

# (제목 — 원본 항목과 같게)

## 파급효과
(`bazel run //tools:impact -- <타깃>` 출력 + "무엇에 닿지 않는가")

## 반영 계획
(구체 편집 목록 + 같은 사실이 서술된 지점의 **검색 키워드 목록** — 중복을 안전율로 용인하므로 전수 grep 이 유일한 방어)

## 확인 못 한 것
(자료로 확인하지 못해 계획에 넣지 않은 것 — "없음"도 적는다)

## 판정
(verdict 의 근거 한 단락. needs-decision 이면 유저 lane 항목으로 되돌린다)
```
