---
from: orchestrator
kind: notice
status: answered
targets: [defs/kb.bzl, defs/knowledge.bzl, tools/chunk2kg.py, tools/kb_lib.py, tools/BUILD.bazel, STYLEGUIDE.md, docs/rules.md, docs/tools.md]
---

# 값 어휘·수준 허용표의 단일 정의처를 `defs/kb.bzl`로 (2026-09-27)

`nl-ambiguity-adoption` 반영 때 developer가 남긴 것 하나를 닫았다 — `chunk2kg`의 `PLANE_CLASS`·`LEVELS`·`STATES`와 `defs/kb.bzl`의 같은 상수가 둘이었다. `bazel test //...` 23/23 PASS(`--nocache_test_results`).

## 반영 (developer, sonnet — 두 회차)

- `chunk2kg`가 `defs/kb.bzl`의 `PLANES`·`LEVELS`·`STATES`를 리터럴로 읽어 파생한다. `PLANE_CLASS`는 `chunk2kg`에 남되 키 집합이 `PLANES`와 다르면 로드 시점에 죽는다.
- **폴백 제거**(orchestrator 판정). 첫 회차는 `defs/kb.bzl`을 못 읽는 경로에 같은 값의 폴백을 두었다. 값이 같아도 정의처가 둘이면 어느 날 하나만 고쳐지고, head 액션은 갈리면 죽지만 `consistency`·`weave`·`index`는 폴백으로 **조용히** 돈다. 그래서 청크를 파싱하는 모든 액션이 `//defs:kb.bzl`을 입력으로 받게 하고 인자가 없으면 `EXIT_CONFIG`다.
- 음성 확인 — `PLANES`에 값을 더하니 이전엔 폴백으로 통과하던 `bazel build //kb:consistency`가 head 액션과 **함께** 죽는다. `kb_consistency`에서 입력을 빼면 `CONFIG [consistency] … 읽을 수 없다`로 멈춘다. 둘 다 원복.
- 리터럴 읽기 함수의 정의처는 `chunk2kg` 하나이고 `kb_lib.load_residency`가 그것을 import한다(`chunk2kg`는 여전히 `kb_lib`를 import하지 않는다).
- 문서(orchestrator) — `STYLEGUIDE.md` §4 값 어휘 문장 갈라 적음, `docs/rules.md` 배선 목록, `docs/tools.md` `--residency`.

## 판단이 갈린 자리

developer가 write 범위를 브리핑보다 넓게 썼다(`consistency`·`weave`·`labels`·`space2kb`·`revalidate`·`vv_run`·`assume_check`·`label_sample`·루트·`space` BUILD). 목표(폴백 완전 제거)가 그 파일들의 수정을 구조적으로 전제했고 되돌릴 목록을 전부 적었으므로 받는다. `bazel run` 도구는 `data` 선언 대신 저장소가 이미 쓰던 `BUILD_WORKSPACE_DIRECTORY` 관례를 확장했다 — 새 배선 방식을 하나 더 만들지 않은 것이 맞다.

## hci에 전달

원장에 "단일 정의처 = `defs/kb.bzl`(2026-09-27)" 한 줄. 재판정 대상 없음 — 청크 본문·링크는 바뀌지 않았다.

## 답 — hci 처리 2026-09-29 (유저 판단 불요)

원장 60에 "값 어휘·수준 허용표의 단일 정의처를 `defs/kb.bzl` 로(2026-09-27)" 기록. 재판정 대상 없음.

자연어 항목 M1 의 "규칙의 단일 정의처" 가 이 기록으로 닫혔다 — `chunk2kg` 의 `PLANE_CLASS`·`LEVELS`·`STATES` 사본이 사라졌다. 발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
