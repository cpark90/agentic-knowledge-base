---
from: hci
source: generated-requirements-stable-2026-09-21.md
verdict: apply
status: open
---

# 요구 `r-027`·`r-028` 의 stable 전이 (2026-09-21 항목, 2026-09-23 승인)

유저 답: *"1."* — **둘 다 stable 로 올린다.** 근거는 규약이 이미 게이트로 강제되고 근거가 전부 외부 표준이라는 것이다.

## 파급효과

- 요구 35건 중 draft 는 이 둘뿐이다. 전이 뒤 **draft 0** 이 된다.
- 항목 작성 시점에 "검증 대응물 비율이 17/35 로 표시된다"고 적었으나 **그 사이 vnv 가 요구 17건의 사슬을 저작해 35/35 = 100%** 가 됐다(2026-09-21). 두 요구에도 목표·기준이 이미 있으므로 **전이가 비율을 낮추지 않는다.** 항목의 그 줄은 낡았다.
- 편집은 frontmatter `status` 한 줄이다. 본문·링크·`contentHash` 는 그대로이고 두 요구에는 `verified` 도장이 없다 — 재판정이 없다.
- 요구의 stable 전이는 유저 승인 사항이므로(AGENTS 역할 표) 이 승인이 그 조건을 채운다.

## 반영 계획

1. **orchestrator — `status: draft` → `status: stable`** 을 `kb/dev/requirement/r-027-generated-documents-carry-provenance.md` 와 `r-028-generated-documents-share-one-form.md` 에 적용한다.
2. **orchestrator — `bazel test //...` PASS 확인.** `//kg:gate_test` 의 상태 어휘 검사와 `chunk2kg` 의 `STATES` 를 지난다.
3. **orchestrator — 원장 인용.** 이 승인이 요구 두 건의 전이 근거다.

**검색 키워드**: `r-027` · `r-028` · `draft` · `stable` · `documents-are-generated`.

## 확인 못 한 것

- 없음. 편집이 두 줄이고 검사는 기존 게이트가 한다.

## 판정

`apply` 다. 승인이 곧 전이 조건이고 다른 판단이 걸려 있지 않다.
