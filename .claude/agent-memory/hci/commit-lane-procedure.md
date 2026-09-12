# hci 커밋 절차 — 자기 작업분만, 전후 같은 검사 (2026-09-12)

전제: 같은 트리에 orchestrator 세션이 붙어 있다. 오늘 두 번(645 파일·44 파일) 남의 작업 중간 상태를 만났다 —
빌드가 깨진 중간 상태(`//kb/vv:bodies` 빈 glob)와 refresh 중 상태가 바뀐 항목(`git rm` 거부).

1. **유저 요청이 있을 때만** 커밋한다 (AGENTS: git 은 inspection/유저; hci 는 요청 시 대행). 대화의 요청은 커밋 메시지에 남는다.
2. `git status --short` 로 무엇이 바뀌었는지 본다. **남의 변경이 섞여 있으면**:
   - 게이트가 초록이면 통째로 담되 커밋 메시지에 역할별로 갈라 적는다(오늘 `10c75e6` 방식).
   - 게이트가 빨강이면 커밋하지 않는다 — 남의 중간 상태다. `git add docs/feedback/` 로 채널만 따로 담는 것도 빌드 깨진 리비전을 남기므로 유저에게 둘 중 하나를 묻는다.
3. 커밋 전 검사 셋: `bazel test //...` (전역 스코프 — `--changed` 류 금지) · `channel_lint` · doccheck(`//...` 에 포함). **초록을 본 기억이 아니라 종료 코드**.
4. `git add -A` 뒤 `git diff --cached --stat` 로 검산 — 의도 밖 파일(scratch·`.wip.md`)이 없는지.
5. 메시지: 무엇을(역할별) · 왜 · 남은 것. 끝에 하네스 지침의 trailer(모델명 하드코딩 금지).
6. `git push origin main` → `git log --oneline -1` · `git status --short | wc -l` = 0 확인.
7. **커밋 뒤 같은 검사 셋을 다시 본다**(다른 세션이 그 사이 썼을 수 있다) — 바뀌었으면 보고만.
