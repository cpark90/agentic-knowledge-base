---
id: https://agentic-knowledge-base.dev/id/chunk/41141de0-6fa2-4b92-802c-3816ac5936ef
type: artifact
level: executable
title_ko: 절 case-gate (tools/vv_run.py)
title: section case-gate in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296, https://agentic-knowledge-base.dev/id/chunk/b8d74a2d-f94b-4fe7-8b3b-13dca638d338, https://agentic-knowledge-base.dev/id/chunk/36a0b6fa-ac60-47db-a769-b49d067f6854]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
composite: {id: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f, title_ko: 절 복합체 case-gate (tools/vv_run.py), title: section composite case-gate in tools/vv_run.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/41141de0-6fa2-4b92-802c-3816ac5936ef, https://agentic-knowledge-base.dev/id/chunk/b43bbf0b-8cd2-4a3c-9acb-56a1fa9e8a63, https://agentic-knowledge-base.dev/id/chunk/2c7856fb-c6fb-42fb-bc34-c18e19362e57, https://agentic-knowledge-base.dev/id/chunk/f1c79e23-8146-427e-83da-3d62ae01bb20, https://agentic-knowledge-base.dev/id/chunk/13d0468f-ac80-47c0-9d27-cafd3ef8ffaf, https://agentic-knowledge-base.dev/id/chunk/4fa89da6-040b-46a2-8dda-692155b66811, https://agentic-knowledge-base.dev/id/chunk/fad9cc7c-a705-42d5-adcc-e124bff2c57c, https://agentic-knowledge-base.dev/id/chunk/4819f0e8-1ed9-43cb-b206-366b65a7f00f], part_of: https://agentic-knowledge-base.dev/id/composite/5fc8dfb1-4583-4c27-8266-44c34557e4c1}
---
**절** — `tools/vv_run.py` 의 절 `case-gate` 다. 기계가 읽는 자극·기대 (결정 p8-machine-readable-case)

**정의** — `unsafe` · `classify` · `yaml_blocks` · `phrases` · `case_spec` · `check_case` · `load_cases` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 기계가 읽는 자극·기대 (결정 p8-machine-readable-case) ──────────────────────────────────────────────
# 케이스는 산문 옆에 `yaml` 펜스를 두고 키 둘(files·expect)을 적는다. 그 밖의 `yaml` 펜스는 산문의 예시이므로 읽지 않는다 —
# 점진 도입이라 옮기지 않은 케이스가 거부되면 안 된다. SPEC_HEAD 가 규약 펜스인지를 가른다
CASE_GATE = "vv-case"  # 케이스 형식 검사의 게이트 id — FAIL [vv-case]. docs/waivers.md 가 이 이름으로 면제를 선언한다 (축 파일·stem)
SPEC_KEYS = ("files", "expect")
EXPECT_KEYS = ("exit", "contains")
SPEC_HEAD = re.compile(r"^(files|expect)\s*:", re.M)
# 자극 파일의 치환 표기 — 케이스는 이름만 주고 검증기가 실제 경로로 바꾼다. 케이스가 절대 경로를 적으면 병렬 실행이 서로를 덮는다.
# 이중 중괄호를 고른 까닭: 셸 메타문자가 아니라(`{{x}}` 는 쉼표가 없어 brace expansion 이 아니다) 치환에 실패해도 셸이 조용히
# 빈 문자열로 펴지 않고, 미해결 이름을 형식 검사가 잡는다. `$이름` 은 셸이 먼저 먹어 그 검사가 불가능하다
PLACEHOLDER = re.compile(r"\{\{\s*([^{}\n]+?)\s*\}\}")
FILE_NAME = re.compile(r"[A-Za-z0-9._][A-Za-z0-9._-]*")  # 자극 이름은 단순 파일 이름이다 — 디렉토리도 `..` 도 없다
# 자극과 기대를 갖춘 케이스에서만 더 도는 음성 명령의 허용 목록 — 저장소 자신의 읽기 전용 검증기를 직접 부르는 형태다.
# 허용 목록은 여전히 보안 경계다. `files` 가 임의 명령의 실행을 허가하지는 않는다 — 바뀌는 것은 자극을 기계가 읽는다는 사실뿐이다.
# `python3 tools/<검증기>.py` 하나만 둔다. 실행은 워크스페이스 루트가 cwd 이므로(run_command) 케이스가 적는 상대 경로가 자극에 닿는다
READ_ONLY_VERIFIERS = ("validate", "chunk_lint", "chunk2kg", "doccheck", "gendoc", "channel_lint", "odd2kg", "taxonomy", "space2kg",
                       "assume_check")
VERIFIER_PREFIXES = tuple(f"python3 tools/{v}.py " for v in READ_ONLY_VERIFIERS)
# 같은 검증기를 `bazel run //tools:<검증기>` 로 부르는 형태는 허용 목록 밖이고 케이스 형식 검사가 실행 전에 거부한다. 까닭은 셋이다.
# `bazel run` 의 cwd 는 runfiles 트리라 워크스페이스 상대 경로가 자극이 아닌 없는 파일로 풀리고, 그 입력 단계 오류가 기대한 거부와 같은
# 종료 코드·문구를 내 케이스를 거짓 pass 로 만들며, 상대 경로는 `$(ls …)`·glob 으로 실행 시점에 생겨 실행 전 판별이 불가능하다.
# 허용 목록에서 빼기만 하면 SKIP 사유가 "허용 목록의 읽기 전용 검증기뿐" 이 되어 읽기 전용 검증기를 부른 저자에게 수정 방향이 아니다
BAZEL_RUN_VERIFIER = re.compile(r"^bazel\s+run\s+//tools:([A-Za-z0-9_]+)\b")
# 같은 함정이 실행기 자신에게도 있다 — `bazel run //tools:vv_run` 의 파이썬 문맥이 하위 프로세스로 새면 케이스가 자극에 닿지 못한다
BAZEL_PY_ENV = ("PYTHONSAFEPATH", "PYTHONPATH", "PYTHONHOME", "RUNFILES_DIR", "RUNFILES_MANIFEST_FILE")
UNSAFE = re.compile(r"[>|`]")  # 리다이렉션·파이프·백틱은 검증기의 출력을 임시 디렉토리 밖으로 내보낸다
SUBSTITUTION = re.compile(r"\$\(([^()]*)\)")
SUBSTITUTION_HEADS = ("ls ", "find ", "git rev-parse")  # 명령 치환 안은 목록 조회만 — 인자를 넓히는 용도다
# 허용 목록의 검증기라도 자신이 저장소에 파일을 쓰는 인자는 실행하지 않는다 — 허용 목록은 진입점이 아니라 "무엇을 할 수
# 있는가" 의 경계다(p8-machine-readable-case 반영, `assume_check` 허용 목록 추가 시의 판단). `assume_check --record` 는
# 관측을 `kb/dev/memory/` 에 쓴다 — 케이스가 그것을 부르면 실행마다 저장소에 파일이 생긴다. `--out` 은 `{{이름}}` 자극으로
# 가리키면 materialize() 가 이미 만든 임시 디렉토리 안에 쓰여 안전하다 — 그 밖의 값은 워크스페이스 상대 경로라 저장소 안이다
RECORD_FLAG = re.compile(r"(?<!\S)--record(?!\S)")
OUT_FLAG = re.compile(r"(?<!\S)--out(?:=|\s+)(\S+)")
```
<!-- 인용 끝 -->
