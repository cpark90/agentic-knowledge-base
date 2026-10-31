---
id: https://agentic-knowledge-base.dev/id/chunk/474fdd6f-fa92-45e7-b6b0-8f53e655a16e
type: artifact
level: executable
title_ko: 절 coedit-max-files (tools/kb_lib.py)
title: section coedit-max-files in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb
composite: {id: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb, title_ko: 절 복합체 coedit-max-files (tools/kb_lib.py), title: section composite coedit-max-files in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/474fdd6f-fa92-45e7-b6b0-8f53e655a16e, https://agentic-knowledge-base.dev/id/chunk/f5c8131e-c94d-4c0b-82fe-9e7ad9d36c69, https://agentic-knowledge-base.dev/id/chunk/12124054-d49f-44e2-be10-6fbdb102b578, https://agentic-knowledge-base.dev/id/chunk/33676d8e-31ee-4546-8550-deab439480eb, https://agentic-knowledge-base.dev/id/chunk/67eb756b-e7f0-4da2-af55-90f4bc3058e9], part_of: https://agentic-knowledge-base.dev/id/composite/cd5a8ce9-a52a-40c7-89b0-b41f163cfde2}
---
**절** — `tools/kb_lib.py` 의 절 `coedit-max-files` 다. 동시 편집 관측 (결정 p10-co-edit-evidence-from-small-commits, 유저 답 Q96-a)

**정의** — `coedit_short` · `coedit_pairs` · `case_verifiers` · `co_cover` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 동시 편집 관측 (결정 p10-co-edit-evidence-from-small-commits, 유저 답 Q96-a) ──
# 동시 편집 쌍은 `bazel run //tools:run_evidence -- --coedit-record` 가 git 에서 뽑아 개발 KB 의 관측 하나로 고정한다. git 은 밀폐 빌드
# 밖이므로 증거 기록(run_evidence)과 링크 후보 뷰(link)는 git 을 읽지 않고 가장 늦은 이 관측만 읽는다 — 같은 리비전에서 같은 후보가 나온다.
COEDIT_MAX_FILES = 20                       # 쌍을 뽑는 커밋의 상한 — 바뀐 단위 지식 파일 수. 이 값의 단일 정의 위치는 여기 하나다
COEDIT_GENERATOR = "process:run_evidence"   # 동시 편집 관측의 generated.by — 역할이 아니라 writer 검사 밖이다
COEDIT_PREFIX = "obs-coedit-"               # 파일명 obs-coedit-<UTC>.md — 같은 디렉토리의 가정 판정 관측과 접두로 갈린다
COEDIT_ITEM_PATH = re.compile(r"^(kb/.+|space/[^/]+|chunks/.+)\.md$")  # 단위 지식 파일 — 단위 지식·설계 공간 (id 가 없는 파일은 쌍에서 뺀다). `chunks/` 는 git 이력의 경로라 남긴다(트리에서는 지시 0192 로 지웠다)
COEDIT_TABLE_HEADER = "| 커밋 | 시각 | 항목 수 | 쌍 수 | 함께 바뀐 항목 |"  # 행마다 항목들의 모든 두 조합이 쌍이다
_COEDIT_UUID = re.compile(r"^chunk/([0-9a-f]{8})-[0-9a-f-]{27}$")
_COEDIT_ITEM = re.compile(r"`([^`]+)`")
```
<!-- 인용 끝 -->
