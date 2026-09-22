---
from: hci
source: spec-writing-standard-remainder-2026-09-22.md
verdict: apply
status: open
---

# 명세 문서 작성 규격 — 반영의 잔여 둘 (2026-09-22)

유저 답(2026-09-22): *"1."* — 선택지 1이다. **G10 그림 틀을 반영하고 출처 개체의 위치를 `git:` 인용으로 고친다.**
그 뒤 hci 가 채널에서 제안 원문과 승인 항목을 제거한다.

## 파급효과

| 대상 | 닿는 것 | 닿지 않는 것 |
|---|---|---|
| `STYLEGUIDE.md` 그림 규칙 | 새 저작의 다이어그램. 현재 그림을 담은 파일은 **1개**라 기존 위반은 사실상 없다 | 청크의 `contentHash`·도장·링크. 규칙 추가는 문서 편집이다 |
| `kg/base-kg.ttl` 의 `prov:atLocation` | 출처 개체 `id:doc-spec-writing-standard` 한 줄. `//kg:gate_test` 의 어휘·shape 검사는 값이 문자열이라 영향이 없다 | 그 개체를 `sources` 로 가리키는 결정 3건(`p4-three-empty-values`·`p4-slot-answers-one-question`·`p8-judge-question-form`)의 frontmatter. IRI 는 그대로다 |
| 채널 제거(그 뒤 hci) | `inquiries/spec-writing-standard-proposal.md`(922줄, 채널 최대 파일) · `spec-writing-standard-adoption-2026-09-22.md` · 두 handoff | 지식 산출물. 인용이 `git:e3b36d2:…` 로 살아남는다 |

게이트 영향은 없다. `doccheck` 는 마크다운 링크와 백틱 경로를 보는데, 제거 대상 둘을 가리키는 링크는 채널 안에만 있고 그것도 함께 지워진다. `//:gendoc_test`·`chunk_lint` 는 대상이 아니다.

## 반영 계획

1. **orchestrator — 그림 규칙 한 단락**을 `STYLEGUIDE.md` §0에 더한다(문서·청크 양쪽에 걸리므로 §4가 아니라 §0이다). 제안 6.8의 셋을 그대로 옮긴다.
   - **[지킴]** 그림은 캡션 한 줄로 시작하고 캡션에 번호를 쓰지 않는다.
   - **[지킴]** 다이어그램은 **소스 펜스**(`mermaid`·`svg`·`plantuml`)로 둔다. 이미지 파일은 소스가 없을 때만 쓴다.
   - **[권장]** 기호·색의 뜻이 자명하지 않으면 "읽는 법" 명사구 ≤3을 붙인다.
2. **orchestrator — 출처 개체의 위치**를 고친다. `kg/base-kg.ttl` 의 `id:doc-spec-writing-standard` 줄을
   `prov:atLocation "git:e3b36d2:docs/feedback/inquiries/spec-writing-standard-proposal.md" .` 로 바꾸고, 같은 파일 53·58·63행과 **같은 서식의 주석**("영속 위치 = 리비전 + 경로. 채널 파일은 소멸성이라 트리에서 제거될 수 있다")을 단다. 리비전 `e3b36d2` 가 제안 원문을 담은 첫 커밋이다.
3. **orchestrator — `bazel test //...` PASS 확인** 후 `agents/` 항목에 `ref: handoff/spec-writing-standard-remainder-2026-09-22.md` 로 인수 기록.
4. **hci(그 뒤)** — 채널에서 제안 원문·승인 항목·handoff 둘을 제거하고 `README.md` 의 refresh 줄과 원장에 기록한다.

**같은 사실이 서술된 지점의 검색 키워드**: `그림` · `다이어그램` · `mermaid` · `캡션` · `doc-spec-writing-standard` · `atLocation` · `spec-writing-standard-proposal`.
문서 쪽은 `STYLEGUIDE.md` · `docs/rules.md` · `docs/feedback/README.md` 를 함께 본다.

## 확인 못 한 것

- 그림 규칙의 효과. 표본이 1파일이라 잴 수 없다. 규칙이 서는 것 자체가 목적이다.
- 그림 규칙을 게이트로 올릴지. 지금은 `[지킴]` 표기의 규약이며 검사 수단을 붙이지 않았다 — 캡션·펜스 언어는 기계가 볼 수 있으나 표본이 없어 오탐률을 모른다.
- `kg/base-kg.ttl` 은 손으로 쓰는 TTL 이라 `canonicalize` 대상이 아니다(`STYLEGUIDE.md` §5, 정규형 검사는 게이트가 아니다). 담당 역할이 다르게 알고 있으면 확인한다.

## 판정

`apply` 다. 답이 선택지 번호 하나로 명확하고, 둘 다 승인 범위 안의 잔여이며 새 판단을 요구하지 않는다. 그림 규칙은
`STYLEGUIDE.md` 의 기존 표기 체계(`[지킴]`/`[권장]`)에 그대로 들어가고, 출처 개체는 같은 파일에 선례 셋이 있다.
