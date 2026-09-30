---
id: https://agentic-knowledge-base.dev/id/chunk/39dbbbb7-da94-41af-8686-75a75ac62baa
type: artifact
level: executable
title_ko: 절 exit-ok (tools/kb_lib.py)
title: section exit-ok in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ff9d354a-d261-44a5-b7cd-7dd050de0370
---
**절** — `tools/kb_lib.py` 의 절 `exit-ok` 다. 종료 코드 — 실패 종류를 구분한다 (agrtls-practices-review-2026-09-12 A)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 종료 코드 — 실패 종류를 구분한다 (agrtls-practices-review-2026-09-12 A) ──────────────────
# 판정 실패 / 설정·입력 문제 / 미실행을 하나의 1 로 뭉개지 않는다. **SKIP 은 PASS 가 아니다** —
# 입력이 0건이라 검사가 돌지 않은 것은 통과가 아니라 미실행이다. 모든 게이트·뷰 도구가 같은 상수를 쓴다.
EXIT_OK = 0
EXIT_FAIL = 1      # 판정 실패 — 산출물을 고친다
EXIT_CONFIG = 2    # 설정·입력 문제 — 파일 없음·인자 오류·파싱 불가. 배선을 고친다
EXIT_SKIP = 3      # 검사가 실행되지 않음 — 입력 0건 등. 통과로 세지 않는다
```
<!-- 인용 끝 -->
