---
from: hci
source: nl-ambiguity-adoption-2026-09-22.md
verdict: apply
status: open
---

# 지식을 형식으로 옮기기 — M1·M5 (2026-09-23 승인)

유저 답: *"link-model-robustness부터 수행하고 1.로 수행"* — **선행은 링크 항목**이고, 그 뒤 선택지 1(**M1 관계의 대수 공리 + M5 값의 형과 단위**)이다.
M2·M3 은 링크 항목의 D 와 같은 일이므로 그쪽 handoff 가 맡는다. M4·M6 은 이번 범위 밖이다.

## 파급효과

- **M1 의 대상은 셋이다.** ① 성질 공리 — `owl:TransitiveProperty`·`IrreflexiveProperty`·`FunctionalProperty`·`inverseOf` 가 전부 **0**이다(있는 것은 `SymmetricProperty` 4 · `AsymmetricProperty` 1 · `subPropertyOf` 18). ② 규칙의 단일 정의처 — `refines` 비순환·수준 한 단계·plane 단방향이 `defs/kb.bzl` 의 조건문과 verify 질의에만 있다. ③ **정의문에 갇힌 규칙** — `skos:definition` 154개 중 **36개(23%)** 가 규칙 문장을 품는다.
- **판정이 필요한 표본 둘이 이미 드러나 있다.** `supersedes` 의 "전부 suspect 가 된다"(링크 항목 D 가 실행한다) · `refines` 의 "후보 상한도 1"(실제 분포는 1개 148 · **2개 119 · 3개 19**).
- 둘째 표본은 **정의문이 두 가지로 읽힌다** — "전이 시점에 하나"가 한 전이당인지 청크당인지 갈리지 않는다. 판정 없이 공리로 옮기면 138청크가 한꺼번에 위반이 되거나 규칙이 공허해진다.
- M5 의 대상은 shape 다. 지금 `sh:datatype` **1** · `sh:in` 17 · `sh:class` 10 이고 범위·단위 표기가 없다.
- 닿지 않는 것: 청크 본문·도장. 공리 선언과 shape 보강은 T-Box 층이다. 다만 **공리를 켜면 기존 데이터가 위반으로 드러날 수 있다** — 그것이 이 작업의 목적이다.

## 반영 계획

1. **developer — 성질 공리 선언.** `refines` 비순환(`owl:IrreflexiveProperty` + 순환 금지 질의 유지) · `supersedes` 이행 · `part_of` 비순환을 온톨로지에 적는다. 수준 한 단계처럼 OWL 로 표현되지 않는 것은 SHACL 또는 질의에 두되 **어느 층이 원본인지 정의문에 적는다.**
2. **developer — 단일 정의처.** `defs/kb.bzl` 의 조건문이 선언을 읽거나, 선언에서 파생된 상수를 읽게 한다. 두 곳에 같은 규칙을 적지 않는다.
3. **orchestrator — 정의문 36건 판정.** 각 규칙 문장을 셋으로 가른다 — **공리·shape·질의로 옮길 것 / 이미 실행되는 것(그 자리를 정의문에 명시) / 실행되지 않고 옮길 수도 없는 것(정의문에서 뺀다).** `refines` 상한 1은 **읽기를 먼저 정한 뒤** 옮긴다.
4. **developer — M5.** 본문 슬롯 shape 4종의 값에 `sh:datatype` 과 범위·단위를 단다. 값이 닫힌 집합이면 `sh:in` 을 쓴다.
5. **vnv — 검증.** 공리를 어기는 고정물로 음성 시험을 더한다. 기존 `defs/tests` 7개와 같은 형이다.

**검색 키워드**: `TransitiveProperty` · `IrreflexiveProperty` · `subPropertyOf` · `skos:definition` · `refines` · `상한` · `sh:datatype` · `sh:in` · `단일 정의처`.

## 확인 못 한 것

- 정의문 36건 가운데 몇 건이 실제로 실행되지 않는지. hci 는 표본 둘만 확인했다. 전수 판정은 3번의 산출이다.
- `refines` 상한 1의 올바른 읽기. 유저 판단이 필요해지면 항목으로 되돌린다.
- 공리를 켰을 때 기존 데이터에서 나올 위반 수. 선언 전에 질의로 먼저 세는 것을 권한다.

## 판정

`apply` 다. 순서 지정(링크 항목 선행)이 명확하고 범위가 M1·M5 로 좁다. **3번(정의문 판정)이 이 작업의 값어치가 가장 큰 부분**이다 — 규칙이 산문에 갇혀 데이터와 어긋난 사례가 이미 둘 확인됐다.
