---
from: hci
status: approved
targets: [kb/dev/decision/p4-all-knowledge-is-composite/, tools/chunk2kg.py, defs/kb.bzl, kg/composite-kg.ttl]
---

# 결정이 요구하는 복합체를 도구가 만들지 못한다 (2026-09-26 중계)

원본: [`agents/orchestrator-verdict-and-verifier-2026-09-22.md`](agents/orchestrator-verdict-and-verifier-2026-09-22.md) §1

## 질문

결정 `p4-all-knowledge-is-composite` 는 검증기를 "케이스 열의 `co:List`" 복합체로 정한다. vnv 가 검증기 셋을 복합체로 묶으려다
`FAIL [chunk2kg] … part_of 대상 복합체가 이 묶음 안에 선언되지 않았다` 를 받았다. **결정이 요구하는 것을 도구가 만들지 못한다.**

어려운 이유는 원인이 도구의 우연한 제약이라는 데 있다. `chunk2kg --fragment` 가 **파일 하나를 묶음으로 보므로** 복합체는
`kb_decision` 처럼 여러 파일을 한 액션으로 묶는 규칙에서만 성립한다. 즉 규칙의 모양이 지식의 모양을 제한하고 있다.

## 이미 정해진 것

- `p4-all-knowledge-is-composite` — 모든 plane 의 지식은 복합체를 이룬다. 결정은 결론·근거·대안, 요구는 관심사별, 합격 기준은 기준 집합, 시나리오는 세 청크다.
- 복합체의 부분은 순서를 갖고(`co:List`) 부분의 plane·level 은 전체와 같다(`composite-heterogeneous.rq`, 결정 복합체는 예외).
- 한 청크는 한 파일이고 복합체는 그 자체가 지식 항목이다.

## 현재 상태 (실측 2026-09-26, hci 확인)

- 복합체 **246** 가운데 청크 frontmatter 로 생성된 것은 **결정 242** 뿐이다. 요구 쪽 4건은 손으로 쓴 `kg/composite-kg.ttl` 의 것이다.
- `hasDirectPart` 선언이 `kg/composite-kg.ttl` 에 42건 있다 — 손으로 쓰면 되지만 **생성 경로가 없다.**
- 같은 제약이 결정 표의 다른 줄 전부에 걸린다 — 요구의 관심사별 복합체, 합격 기준의 기준 집합, 시나리오의 세 청크.
- `artifact` plane 3(검증기)이 방금 섰고 그 셋이 첫 피해자다.

## 답이 가르는 것

- **도구를 고치면** `kb_chunk` 단위 청크끼리 복합체를 만들 수 있다. 결정의 표가 전부 성립하고 요구·기준·시나리오·검증기가 같은 형식을 얻는다. 비용은 묶음 규칙 하나를 새로 만드는 것이다.
- **결정을 좁히면** 복합체가 결정 전용이 된다. 다른 plane 은 단일 청크로 남고 `co:List` 의 순서 보장을 포기한다. 결정 하나를 `supersedes` 로 개정한다.
- **그냥 두면** 결정과 실물이 어긋난 채 남는다. `r-009`(모든 산출물은 요구로 거슬러 오른다)와 감사에 불리하고, 2026-09-26 의 정의문 판정(규칙은 실행 자리를 이름 짓는다)과 정면으로 어긋난다 — **규칙이 있고 실행이 없는 것**이 바로 그 판정이 없애려던 상태다.

## 선택지

1. **도구를 고친다** (권고). `kb_chunk` 여러 개를 한 묶음으로 보는 규칙(`kb_composite` 또는 `--fragment` 의 확장)을 만든다. 비용: `defs/kb.bzl` 규칙 하나 + `chunk2kg` 의 묶음 인식 + 생성 BUILD 재생성. 근거는 결정 표의 네 줄이 전부 이것을 기다린다는 것이다.
2. **결정을 좁힌다.** 복합체를 결정 전용으로 하고 다른 plane 은 단일 청크로 둔다. 비용: 결정 개정 1. `co:List` 순서와 부분-전체 질의를 다른 plane 에서 포기한다.
3. **손으로 쓴 복합체를 공식 경로로 인정한다.** `kg/composite-kg.ttl` 에 적는 것을 규약으로 정한다. 비용: 규약 한 줄. 다만 생성물과 손 기록이 갈려 드리프트 가드가 없다.

## 답
1.
