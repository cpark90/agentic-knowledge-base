---
from: hci
source: link-model-robustness-cde-2026-09-19.md
verdict: apply
status: open
---

# 링크 견고성 — 남은 선택지 C·D·E (2026-09-19 항목, 2026-09-23 승인)

유저 답: *"1."* — **D → E 순으로 연다. C(selector 층)는 보류다.**
유저는 항목 `nl-ambiguity-adoption-2026-09-22` 의 답에서 **"link-model-robustness부터 수행하고"** 라고 순서를 지정했다.
이 항목이 먼저다.

## 파급효과

- **D 는 자연어 항목의 M2·M3 과 같은 일이다.** `when` 실물 0 · `suspect` 실물 0 · `agt:linkState` 는 `confirmed` 646 단일이다. D 가 켜지면 그 둘이 함께 닫힌다 — 두 항목이 같은 코드를 건드리므로 **따로 수행하지 않는다.**
- `agt:supersedes` 의 정의문이 이미 "대체가 일어나면 옛 결정을 충족하던 링크가 전부 suspect 가 된다"고 적는다. `supersedes` 134쌍이 그 규칙의 첫 대상이다. **정의문에 있으나 한 번도 실행되지 않은 규칙**이 D 의 첫 시험이다.
- E 는 `relatedTo` 아래 약한 잎 하나를 더한다. `//kg:link_candidates` 의 후보 11이 전부 `relatedTo` 라 링크 키가 없어 채택되지 못하는 상태가 풀린다.
- 닿지 않는 것: 청크 본문·라벨·`contentHash`·도장. D·E 는 frontmatter 키와 그래프 층의 일이다.

## 반영 계획

1. **developer — `when` 평가기.** ODD 조건 판정(`assume_check`)을 재사용한다. 링크의 `when` 이 거짓이면 그 링크를 `suspect` 로 유도한다. 상태는 저장하지 않고 생성물(`bazel-out`)에만 물질화한다 — 노트 9.11 의 "상태는 저장값이 아니라 평가 결과".
2. **developer — 트리거를 링크 타입별로 좁게 선언한다.** 외부 실무의 경고(추적 매트릭스가 suspect 로 포화)를 받아 `supersedes` 의 대체 전파부터 켜고, 나머지 타입은 선언된 것만 돈다. **suspect 포화율을 `metrics` 의 한 줄로 관측**한다.
3. **developer — `revalidate` 확장.** 본문 해시 변경 → 링크 재판정까지 잇는다.
4. **orchestrator — E 의 어휘.** `agt:relatedTo` 아래 약한 잎 하나(관계는 있으나 이름이 아직 없다)를 온톨로지에 더하고, 링크 키로 쓸 수 있게 `chunk2kg` 에 등록한다. 확장 규칙 한 절(새 관계는 기존 네 족 아래 잎으로만, 게이트가 부모 트리플을 함께 생성)을 `docs/rules.md` 에 적는다.
5. **vnv — 검증.** `when` 이 거짓인 링크가 `suspect` 로 유도되는 음성 시험 하나, 후보 채택이 복원 비율에 드는지 확인.

**검색 키워드**: `when` · `suspect` · `linkState` · `relatedTo` · `coUpdatesWith` · `link_candidates` · `복원 비율` · `트리거`.

## 확인 못 한 것

- 트리거를 어느 타입까지 켤지. 실측 없이는 포화율을 모른다. `supersedes` 하나로 시작해 수치를 보고 넓힌다.
- `when` 의 식 언어. CEL 실물이 0이라 ODD 판정과 같은 형(명령 문자열)으로 시작할지, 식 언어를 먼저 정할지는 developer 판단이다.
- E 의 잎 이름. 어휘 제안 워크플로(`term_propose`)를 거친다.

## 판정

`apply` 다. 답이 선택지 번호 하나이고 순서까지 지정됐다. **자연어 항목의 M2·M3 은 이 항목으로 흡수한다** — 같은 코드를 두 번 건드리지 않기 위해서다.
