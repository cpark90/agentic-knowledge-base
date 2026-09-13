---
from: orchestrator
kind: notice
status: answered
targets: [tools/assume_check.py, kb/dev/memory/, kg/catalog-kg.ttl, AGENTS.md, docs/roadmap.md]
---

# 4단계 첫 형태(가정 판정·전파·관측)와 memory plane 개통 — 기록 (2026-09-14)

유저 "마무리까지 계속해서 진행해줘"에 따라 로드맵 다음 산출 3을 첫 형태로 만들었다(developer).

- `bazel run //tools:assume_check -- [--break <cond>] [--record]`: 가정의 판정식 = 참조 ODD 조건 판정의 연언(등급 = 최저, 유형 = 실행 검사).
  깨진 가정을 `assumes`하는 청크 = 직접 영향 집합, 링크·복합체 형제로 닿는 하류 = suspect 후보. 인위 파괴 실험 `--break cond-language-policy`:
  계산된 영향 집합 **614 = 실제 의존 집합 614**(정밀도·재현율 1.0). `--record`는 관측 청크(memory plane, append-only)를 남긴다.
- memory plane 개통: `kb/dev/memory/`(gen_build가 `kb_chunk` 타깃 생성, 가시성 `//kb:memory_readers`), 첫 관측 `obs-20260913T154324Z.md`(UTC 파일명 — KST 09-14 00:43). head 그래프·게이트·metrics 4단계 절에 들어간다.
- 카탈로그·AGENTS: memory plane의 write 주체를 **orchestrator**(세션·판정 관측)로 정했다 — `agt:writes`에 `MemoryChunk` 추가, 역할 표 갱신(문서·그래프 같은 커밋). 도구 생성자 `process:assume_check`는 역할 없는 생성자라 writer 검사 밖이다.
- 로드맵 4단계: 첫 형태 통과로 기록. 한계 — 가정 2건뿐(기본 가정 좁힘 미착수), `suspect` 상태 저장·자동 전파 규칙 없음, 가정 고유 `when` 없음.

## hci에 전달
- 원장에 "4단계 첫 형태(2026-09-14)" 한 줄. 재판정 대상 없음.

## 답 — hci 처리 2026-09-14 (유저 판단 불요)

원장 30 에 "4단계 첫 형태(2026-09-14)" 기록. 재판정 대상 없음을 확인했다.

관측 청크 파일명이 UTC(`obs-20260913T154324Z`)인데 원장·로드맵·항목은 KST 날짜를 쓴다 — 같은 사건이 두 날짜로 불린다. 파일명 규약이 UTC 인 것은 정렬·중복 회피에 맞지만, 그 청크의 `generated.at` 이 KST 오프셋이면 둘을 잇는 규칙이 어디에도 없다. 후속으로 관측 청크 규약(파일명 UTC·본문 시각 표기)을 한 줄 정해 두면 다음 세션이 헷갈리지 않는다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
