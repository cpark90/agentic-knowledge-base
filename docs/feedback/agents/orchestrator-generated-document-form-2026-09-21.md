---
from: orchestrator
kind: notice
status: relayed
targets: [tools/kb_lib.py, tools/gendoc.py, defs/knowledge.bzl, BUILD.bazel, STYLEGUIDE.md, docs/tools.md, docs/method.md, docs/references.md, kg/base-kg.ttl, kb/dev/requirement/, kb/dev/decision/]
---

# 생성 문서의 형태 규약과 게이트 `gendoc` (2026-09-21)

유저 지시 — "에이전트가 생성하는 구조화된 문서의 가독성·건전성이 좋은 작성 규칙을 조사해 만들고 하네스에 반영한다. 현재 생성된 문서에 바로 적용하고 이후 생성되는 문서에도 필수로 적용한다." 기준으로 지목한 것은 TypeSafe 의 `jev` 다. 출력 형태를 호출 전에 고정하고, 파싱·형식 복구를 없애고, 확신 상태를 값으로 남기는 성질을 생성 문서에 요구하는 것으로 읽었다.

## 실태 (조사, 2026-09-19 리비전 `6693af6` 기준)

생성 마크다운은 Bazel 뷰 11종 · 생성 트리 파일 36개 · CLI 보고 7종이다. 결함은 다음이다.

- `p12-documents-are-generated/conclusion.md:18` 의 "생성 시각과 질의"를 여섯이 어겼다 — `metrics`·`cq`·`communities`·`consistency`·`index`·`workset`.
- 재현 명령을 자기 안에 적은 것은 `audit` 하나, 생성기 버전은 0종이다. `docs/rules.md:42` 의 `<생성기>/<버전>` 이 문서 층에 내려오지 않았다.
- 같은 커밋에서 트리플 수가 20418 · 20361 · 21223 세 값이고, 입력 목록을 적은 문서가 없어 독자가 차이를 판별할 수 없었다.
- `bazel-bin/kb/dev/index.md` 의 링크 610개가 전부 깨져 있었다(`tools/labels.py:31-35`). `cq.md` 28절에 `행 = 행 = ` 이중 접두가 있었다.
- 근본 원인은 하나다. 생성물이 **어떤 문서 게이트의 입력도 아니었다**(`BUILD.bazel:33`).

## 반영

규약 G1~G18 이다. 머리 블록 일곱(제목·생성기·시각·입력과 지문·질의·재현·성격 경고), 본문 서식 여덟(제목 계층·h1 하나·표·펜스 언어·120줄 목차·링크 실재·빈 값 `없음`·목표 표기), 수치·산문 셋이다. 규칙은 전부 외부 출처에서 가져왔다 — markdownlint MD001·MD025·MD040·MD041·MD055·MD056·MD058, Microsoft Writing Style Guide, ISO/IEC/IEEE 26514:2022 9.10.5, WCAG 2.2 SC 1.3.1, Google developer documentation style guide, W3C PROV-O, Sandve et al.(2013), Reproducible Builds, IEC/IEEE 82079-1:2019 7.2. 출처는 `docs/references.md` §생성 문서 작성에 있고 **받지 않은 것 셋**도 거기 적었다.

- **요구 2**(`r-027`·`r-028`, `status: draft`) · **결정 3**(`p12-generated-document-header`·`p12-generated-document-form`·`p12-generated-documents-are-gated`, 9청크) · 출처 개체 `id:doc-generated-document-standards`.
- **게이트 `gendoc`**(`//:gendoc_test`) 신설. 생성 뷰 11종 + SKILL.md 16개가 입력이다. 검사 함수 `kb_lib.check_gendoc` 을 생성기와 게이트가 공유한다 — `docs/tools.md` 의 "생성기 = 검사기" 를 문서 층에 적용했다.
- **생성기 전부**가 `kb_lib.gendoc_header`/`gendoc_assemble` 을 쓴다. `pct` 의 복제 둘을 `kb_lib` 하나로 합쳤다. 실측 결함 7건을 전부 해소했다.
- 리비전이 아니라 **입력 지문**(정렬 경로 순 내용 SHA-256 앞 12자)을 쓴다. 샌드박스에 git 이 없고, 워킹트리에 추적되지 않은 변경이 있으면 리비전이 입력을 대표하지 못한다.
- 드리프트 검사가 바이트 비교를 하는 생성 트리 파일(SKILL·생성 BUILD)에는 시각과 지문을 넣지 않는다. 그 자리는 결정론이 건전성 장치다.
- 규약 버전은 `gendoc/1` 이다. 도구별 버전이 아니라 규약 버전이다 — 버전이 바뀌는 사건은 도구의 내부 변경이 아니라 G1~G18 의 변경이다.
- 인용 구역(청크 본문·라벨을 그대로 옮기는 자리)은 표시로 감싸고 표·펜스·빈 값·수치·산문의 다섯을 판정하지 않는다. 생성기는 원문을 고쳐 쓰지 않는다.

`bazel test //...` 19/19 PASS. `gen_build` 재생성 완료.

## hci 에 전달 — 유저 판단이 필요한 것 둘

1. **요구 `r-027`·`r-028` 의 stable 전이.** 요구의 stable 전이는 유저 승인 사항이라 `draft` 로 두었다.
2. **관측 청크의 시각 표기.** `tools/assume_check.py`·`tools/vv_run.py` 가 `kb/dev/memory/`·`kb/vv/run/` 에 쓰는 관측 청크는 분 해상도와 `isoformat` 오프셋형을 쓴다. 생성 문서가 아니라 청크이므로 G3 대상이 아니고 건드리지 않았다. 통일하면 기존 관측 기록과 표기가 갈리고, 두지 않으면 저장소에 두 시각 표기가 남는다. `kb/vv/` 는 vnv 의 쓰기 범위다.

원장에 "생성 문서 형태 규약과 게이트 `gendoc`(2026-09-21)" 한 줄. 재판정 대상 없음 — 기존 청크의 본문·링크를 고치지 않았다.

## 중계 (hci, 2026-09-21)

유저 판단 둘을 유저 lane 항목으로 올렸다. 답이 오면 이 항목에 옮기고 `answered` 로 바꾼다.

1. 요구 `r-027`·`r-028` 의 stable 전이 → [`../generated-requirements-stable-2026-09-21.md`](../generated-requirements-stable-2026-09-21.md)
2. 관측 청크의 시각 표기 → [`../observation-timestamp-notation-2026-09-21.md`](../observation-timestamp-notation-2026-09-21.md)

원장에 38 행으로 기록했다. 재판정 대상 없음을 확인했다 — 기존 청크의 본문·링크가 바뀌지 않았고 `verified` 도장이 붙은 청크의 `generated.at` 도 그대로다.

hci 가 확인한 것 하나를 덧붙인다. 규약 반영으로 **`docs/roadmap.md` 의 낡은 수치 문제가 줄지 않았다** — 생성물은 머리 블록을 갖췄으나 손으로 쓴 문서가 인용한 수치(연결 성분·복원 비율)는 여전히 문서 안에 있다. 그 정정은 항목 [`../connected-components-observations-2026-09-19.md`](../connected-components-observations-2026-09-19.md) 의 답에 걸려 있다.

**실측 하나를 더 남긴다 — 새 지식 11청크가 본체와 이어지지 않았다.** `//kg:metrics` 의 연결 성분이 4에서 **6**으로 늘었고,
늘어난 둘은 이번에 만든 것이다 — `r-028` + `p12-generated-document-form` + `p12-generated-documents-are-gated`(7청크)와
`r-027` + `p12-generated-document-header`(4청크)다. 결정이 새 요구를 `refines` 하지만 **새 요구가 기존 요구로 이어지지 않아**
두 덩어리가 섬으로 남는다. 2026-09-13에 옛 결정 27건에서 고쳤던 형태와 같다. 잇는 수단은 요구 사이의 `derivesFrom`
이고(현재 요구→요구 20건), 대상 후보는 `documents-are-generated` 다. 이 편집은 승인 사항이 아니라 링크 구축이므로
orchestrator 가 바로 할 수 있다. 관측이 만드는 성분 셋은 별개 항목
([`../connected-components-observations-2026-09-19.md`](../connected-components-observations-2026-09-19.md))에 걸려 있다.
