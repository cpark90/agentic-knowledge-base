---
id: https://agentic-knowledge-base.dev/id/chunk/01222bd2-207a-4927-af92-878cc4e516f8
type: artifact
level: executable
title_ko: 절 vv-run-dir (tools/kb_lib.py)
title: section vv-run-dir in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2
---
**절** — `tools/kb_lib.py` 의 절 `vv-run-dir` 다. 실행 기록과 관측 (r-026 append-only · p0-run-as-observation · p8-vv-plane-instances memory = 실행 기록)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 실행 기록과 관측 (r-026 append-only · p0-run-as-observation · p8-vv-plane-instances memory = 실행 기록) ──────────────
# 관측은 도구가 쓴다 — 생성자는 역할이 아닌 `process:<도구>` 라 writer 검사 밖이다 (validate check_writer). 카탈로그의 executor
# 하위 역할을 도구가 맡는 첫 형태다. V&V 실행 기록은 V&V KB 의 memory plane 디렉토리(kb/vv/run — gen_build VV_PKGS), 가정 판정
# 관측은 개발 KB 의 memory 디렉토리(kb/dev/memory — assume_check)에 놓인다. weave audit 이 두 곳의 최신 관측을 그대로 요약한다
VV_RUN_DIR = KB_VV + "/run"
DEV_MEMORY_DIR = KB_DEV + "/memory"
RUN_GENERATOR = "process:vv_run"                # V&V 실행 기록의 generated.by (tools/vv_run.py --record)
ASSUME_CHECK_GENERATOR = "process:assume_check"  # 가정 판정 관측의 generated.by (tools/assume_check.py GENERATOR · metrics · weave audit 의 정의처)
RUN_CASE_TABLE_HEADER = "| 케이스 | 실행 명령 | 결과 | 소요 |"  # 실행 기록 본문의 케이스 표 — audit 이 이 헤더로 표를 찾는다
ASSUME_CHECK_TABLE_HEADER = "| 가정 | 판정 유형 | 등급 | 상태 | 직접 영향 | suspect 후보(전이) |"  # 가정 판정 관측의 가정 표 (assume_check.observation)
RUN_VERDICTS = ("pass", "fail", "skip")          # 케이스 판정 — SKIP 은 PASS 가 아니다 (docs/tools.md 실패 종류 3)
```
<!-- 인용 끝 -->
