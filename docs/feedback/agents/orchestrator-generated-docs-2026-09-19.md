---
from: orchestrator
kind: notice
status: open
targets: [tools/weave.py, tools/gen_skills.py, .claude/skills/, INTENT.md, docs/method.md, docs/tools.md]
---

# 6단계 첫 형태 — 지식에서 문서·skill 생성 (2026-09-19)

유저 "계속해서 진행해줘"에 따라 로드맵 다음 산출 6을 첫 형태로 만들었다(developer). 근거는 요구 `documents-are-generated`와 결정 `p12-documents-are-generated`(생성물마다 생성 시각과 질의를 적는다).

- **`weave`** — 세 뷰(`bazel-bin`에만): `//kb/dev:adr`(결정 복합체 188 + 옛 단일 파일 결정 27, 본문 그대로, refines 요구·supersedes 연쇄·출처·가정) · `//kb/dev:requirements`(요구 33: EARS 패턴 분포 ubiquitous 16·event-driven 12·unwanted-behaviour 3·complex 1·state-driven 1, 정제 도달 수준 concrete 33, 정제 결정 없는 요구 0) · `//kb/dev:changelog`(supersedes 134쌍; `prov:wasRevisionOf`는 0 — 개정이 아직 새 IRI로만 기록됐다는 실측).
- **`gen_skills`** — 도구 docstring과 `kb_lib.SKILLS`(12항목: 도구·절 앵커·언제·대표 명령)에서 `.claude/skills/<도구>/SKILL.md` 12개를 생성한다. 생성 트리 파일이라 커밋하고 `//:skills_drift_test`가 재생성과 비교한다(손으로 쓴 skill도 드리프트로 거부). 생성 시 자기검사: 도구·타깃·절 앵커 실재, 단정 서술형.
- **INTENT.md** — 손으로 쓴 요구 33건의 IRI 표기를 지우고 생성 뷰를 가리킨다. 이해관계자별 묶음(손으로 정한 소속)만 남았다 — 이해관계자를 데이터로 올리는 것은 어휘가 없어 후속.
- 문서: method §9 뷰 표에 ADR·요구 색인·변경 이력·skill 행, tools.md 활용·development 층 행, STYLEGUIDE §6 생성 트리 파일 예외(BUILD·skills), AGENTS 셀프체크에 재생성 명령. 게이트 17.
- 남긴 것: tangle(코드 파일 — `artifact` 항목 뒤), API 문서·감사 증적 뷰(계약·V&V 항목 뒤), 생성 시각이 Bazel 캐시로 고정되는 성질(입력이 바뀌지 않으면 시각도 그대로 — 사실은 참).

## hci에 전달
- 원장에 "6단계 첫 형태(2026-09-19)" 한 줄. 재판정 대상 없음.
- 세션 시작 표에 `python3 tools/gen_skills.py --check`(또는 `bazel test //:skills_drift_test`)를 넣을 값어치가 있다 — skill을 손으로 고치는 사고를 잡는다.

## 답
(hci가 채움)
