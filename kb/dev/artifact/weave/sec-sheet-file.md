---
id: https://agentic-knowledge-base.dev/id/chunk/1ae33e03-d177-4448-941d-38d9d265c292
type: artifact
level: executable
title_ko: 절 sheet-file (tools/weave.py)
title: section sheet-file in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
composite: {id: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa, title_ko: 절 복합체 sheet-file (tools/weave.py), title: section composite sheet-file in tools/weave.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/1ae33e03-d177-4448-941d-38d9d265c292, https://agentic-knowledge-base.dev/id/chunk/0b1ee795-6889-4c66-86b1-2a77ac3ee4d6, https://agentic-knowledge-base.dev/id/chunk/8f15c2bb-62bb-4e9f-98dc-e86d7e0436b2, https://agentic-knowledge-base.dev/id/chunk/fc1144d8-e0cf-4dc0-a8f5-0d9822fb0334, https://agentic-knowledge-base.dev/id/chunk/4787cbe7-b43d-4db2-b609-c25540fe1afc, https://agentic-knowledge-base.dev/id/chunk/ef9472b8-59c4-47b6-91eb-b0532f4403de, https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721, https://agentic-knowledge-base.dev/id/chunk/f04f26e1-a284-4a1d-a16a-a9ba90bde65e, https://agentic-knowledge-base.dev/id/chunk/07201b14-1b46-4994-8d76-3f7334f06262], part_of: https://agentic-knowledge-base.dev/id/composite/d4819604-90cc-4d20-9aa3-25160d68c333}
---
**절** — `tools/weave.py` 의 절 `sheet-file` 다. 재료 — 질문지와 본문의 인용을 읽는다

**정의** — `front_fields` · `read_sheet` · `load_citing` · `citing_ref` · `user_decision_evidence` · `QuestionIndex` · `_cell` · `_names_cell` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 재료 — 질문지와 본문의 인용을 읽는다 ────────────────────
SHEET_FILE = re.compile(r"(?:^|/)user/(archive/)?(Q-\d{4})\.md$")     # 질문지 — 열림(user/)과 보관(user/archive/)
LEGACY_FILE = re.compile(r"(?:^|/)user/archive/legacy/([^/]+\.md)$")  # 옛 질문지 — 2026-10-03 이전 유저 lane 의 파일, 질문 번호가 없다
QUESTION_HEADING = re.compile(r"^## Q(\d+)\.\s*(.*?)\s*$")            # 질문 절의 제목 (harness/README.md 유저 채널 절의 양식)
ANSWER_LINE = re.compile(r"^답\s*:\s*(.*?)\s*$")                      # 질문 절 안의 답 줄 — 콜론 없는 산문 줄(`답이 가르는 것`)은 걸리지 않는다
# 인용 꼴 둘 — 긴 꼴은 질문지와 번호(`#` 또는 공백으로 잇는다), 짧은 꼴은 번호와 답 문자다. 한글이 낱말 문자라 `\b` 대신 영숫자 둘레를 본다
CITE_LONG = re.compile(r"(?<![A-Za-z0-9_])Q-(\d{4})(?:#|\s+)Q(\d+)(?![0-9])")
CITE_SHORT = re.compile(r"(?<![A-Za-z0-9_#-])Q(\d+)-[a-z](?![A-Za-z0-9_])")
# 답 문자 없는 꼴은 세지 않는다 — 질문지 번호 체계(2026-10-01~)보다 앞선 2026-09-10 세션의 유저 결정이 같은 꼴이라 질문지로 풀 수 없다
CITE_BARE = re.compile(r"(?<![A-Za-z0-9_#-])Q(\d+)(?![0-9A-Za-z_-])")
CITE_LEGACY = re.compile(r"(?<!channel/archive/)legacy/([A-Za-z0-9._-]+\.md)")  # 옛 질문지 인용 — 옛 채널 기록(channel/archive/legacy/)은 아니다
QUESTION_CELL_SHOW = 5  # 인용처 칸에 이름을 보이는 수 — 넘으면 수와 앞의 이름만 적는다 (상한 뷰는 라벨로 자르지 않고 수를 함께 낸다)
QUESTION_GROUPS = (("decision", "결정"), ("space", "설계 공간"), ("other", "그 밖의 단위 지식"))
```
<!-- 인용 끝 -->
