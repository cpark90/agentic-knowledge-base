# 다른 프로젝트의 하네스 부트스트랩 — 2026-11-01 smartbelley_vnv

- 유저가 이 세션(원형 interpreter)에 `~/git/smartbelley_vnv` 하네스 구축을 지시했다. 파일 수정 경계는 원형 저장소 안의 규칙이므로 다른 저장소의 부트스트랩은 경계 밖이라고 읽고 직접 세웠다. 원형에는 질문지(Q-0075)와 역할 메모리만 썼다. 이 읽기는 Q-0075 Q171 의 `hci의 읽기`에 적었다.
- 같은 저장소가 2026-10-31에 한 번 세워졌다가 커밋 없이 지워졌다. 유저가 답한 질문지 여섯의 답은 원형 프로젝트의 세션 전사(`~/.claude/projects/-home-cpark-git-smartbelley-vnv/*.jsonl`)에서 `Q<n>-<x>` 참조 빈도와 tool_result 의 `답:` 줄로 복구했다. 전사는 Write 입력과 Bash heredoc 에만 본문이 남고, dispatch 가 쓴 파일(기획안 원문)은 남지 않는다.
- 복제의 골격: `lib.sh`·`inbox.sh`·`read-msg.sh`·`mark.sh`·`watch.sh`·`reset.sh`·`run-hci.sh` 는 그대로(환경 변수 접두만), `send.sh` 는 발신 전 검사를 bazel 바이너리 대신 `python3 -I harness/channel_lint.py --message` 로, `channel_lint.py` 는 rdflib 없는 표준 라이브러리 판(이름 원천은 결정 slug 뿐), `scripts_test.py` 는 runfiles 의존 시험 하나를 결정 기록 fixture 로 바꿨다. `check.sh` = channel + scripts + prose.
- 다른 저장소의 질문지에서 원형 결정 slug 를 적으면 원형 게이트는 안 걸리지만, 원형 질문지에 같은 줄을 옮길 때 `composite.title_ko` 정확 일치가 필요하다 — 풀이말을 괄호에 넣었다가 6건 거부됐다. 이름은 `kb/dev/decision/<slug>/conclusion.md` 의 `composite.title_ko` 에서 그대로 복사한다.

관련: [session-start-cycle](session-start-cycle.md) · [review-discipline](review-discipline.md)
