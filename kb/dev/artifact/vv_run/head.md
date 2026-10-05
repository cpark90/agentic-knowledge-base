---
id: https://agentic-knowledge-base.dev/id/chunk/663886da-0e72-42f0-ba6b-3dfbf495e462
type: artifact
level: executable
title_ko: 모듈 머리 id (tools/vv_run.py)
title: module head id in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5fc8dfb1-4583-4c27-8266-44c34557e4c1
---
**모듈 머리** — `tools/vv_run.py` 의 모듈 머리 `id` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 네임스페이스·종료 코드·실행 기록 규약의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk, tokenizer_vocab_path  # noqa: E402
# 케이스의 frontmatter(라벨)는 chunk2kg 의 파서로 읽고, 토큰 계수기 어휘 경로는 chunk2kg.tokenizer_vocab_path 가 단일 정의처다

ID = kb_lib.ID
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
CASE_DIR = kb_lib.KB_VV + "/case"
VERIFIER_DIR = kb_lib.KB_VV + "/verifier"
# 실행 명령을 읽는 항목의 종류 → 자리. 두 종류는 같은 줄 꼴(`**실행 명령**`)·같은 허용 목록·같은 판정 규칙을 쓴다 (유저 답 Q29-a)
KINDS = {"case": CASE_DIR, "verifier": VERIFIER_DIR}
RUN_DIR = kb_lib.VV_RUN_DIR
GENERATOR = kb_lib.RUN_GENERATOR
ODD_IRI = str(ID["odd-agentic-knowledge-base"])  # 관측의 출처 — ODD 개체 (assume_check 와 같은 sources)
ASSUMPTIONS = [str(ID["asm-bazel-toolchain"]), str(ID["asm-chunk-conventions"])]  # 실행은 bazel 툴체인과 청크 규약을 전제한다
WAIVERS = "docs/waivers.md"  # 면제 선언의 원본 — 코드에 숨기지 않고 표 하나에 적는다 (kb_lib.load_waivers)
# 실행 기록 한 파일의 행 수 상한 — 읽는 비용을 위한 생성기의 자기 제한이다. 청크 크기의 상한이 아니다:
# 그것은 토큰이고 정의처는 kb_lib.BODY_TOKEN_LIMITS 다 (결정 p1-chunk-unit-is-tokens)
MAX_RECORD_LINES = 42
# 케이스 본문의 실행 명령 줄 — `**실행 명령**` 뒤 대시, 그 뒤 코드 스팬 하나. 스팬 안의 전부가 명령이다
COMMAND_LINE = re.compile(r"^\*\*실행 명령\*\*\s*—\s*`(.+)`\s*$")
SPLIT = re.compile(r"\s*(?:;|&&)\s*")  # 순차 연산자 — 각 조각을 따로 판정한다
# 실행하는 양성 명령의 허용 목록 — 전부 읽기 전용 검증기다. 그 밖(bazel run · 다른 python3)은 SKIP
POSITIVE_PREFIXES = ("bazel test ", "bazel build ", "bazel query ", "python3 tools/gen_build.py --check")
EXECUTED = re.compile(r"Executed (\d+) out of (\d+) tests?")  # bazel test 요약 — 실행 수 / 전체 수. 나머지는 캐시 재사용 (재현성의 근거)
```
<!-- 인용 끝 -->
