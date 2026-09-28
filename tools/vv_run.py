#!/usr/bin/env python3
"""V&V executor — 케이스의 실행 명령 중 허용 목록의 양성 명령을 실행하고 결과를 실행 기록으로 남긴다 (노트 8.20절 executor,
r-026 관측은 append-only 실행 기록, p0-run-as-observation `agt:Run`, p8-vv-plane-instances memory = 실행 기록, p8-reproducibility).

케이스(`kb/vv/case/*.md`)마다 본문의 `**실행 명령**` 줄(코드 스팬 하나가 명령이다)을 읽어 명령을 `;`·`&&` 로 나눈다. **허용 목록(`bazel test`·`bazel build`·`bazel query`·
`python3 tools/gen_build.py --check`)으로 시작하는 읽기 전용 검증기만 실행한다**. 그 밖(그 밖의 `python3 …` · `bazel run …`)은 실행하지 않고
SKIP 으로 적는다. **SKIP 은 PASS 가 아니다** (docs/tools.md 실패 종류 3).

**기계가 읽는 자극·기대** (결정 p8-machine-readable-case): 케이스는 `**자극**`·`**기대**` 산문 옆에 `yaml` 펜스를 두고 키 둘을 적는다.
`files` 는 `이름: 내용` 매핑이고 검증기가 명령 앞에 임시 디렉토리로 쓰고 뒤에 지운다 — **임시 파일의 경로는 검증기가 정한다.** 케이스는 명령
안에서 그 파일을 `{{이름}}` 으로 가리키고 검증기가 실제 경로로 바꾼다. `expect` 는 명령 순서마다 `exit`(기대 종료 코드)와 `contains`(출력에서
찾을 문구)를 적는다. **판정은 둘 다 맞아야 pass** 다 — 종료 코드만 보면 "실패했는가" 는 알아도 "무엇이 거부되는가" 는 모른다. 자극과 기대를
갖춘 케이스는 저장소의 읽기 전용 검증기를 직접 부르는 음성 명령(`python3 tools/<검증기>.py`)까지 실행한다. **`bazel run //tools:<검증기>` 형태는
허용 목록 밖이다** — `bazel run` 은 runfiles 트리에서 돌아 워크스페이스 상대 경로 인자를 자극이 아닌 runfiles 의 없는 파일로 풀고, 그때 나오는
입력 단계 오류가 기대한 거부와 같은 종료 코드·문구를 내 케이스를 거짓 pass 로 만든다.
읽기 전용 검증기 목록에는 `assume_check`(가정 판정·전파, `--break <조건>` 은 호스트 상태를 읽고 ODD 판정을 가상으로
바꾸는 실험 플래그일 뿐 저장소를 쓰지 않아 안전하다)를 포함한다. 그래도 검증기 자신이 파일을 쓰는 인자
(`--record`·`{{이름}}` 자극이 아닌 저장소 안 경로의 `--out`)를 가진 호출은 허용 목록 안이어도 실행하지 않고 SKIP 한다 —
허용 목록은 명령의 진입점이 아니라 무엇을 할 수 있는가의 경계다(`unsafe()`).
**점진 도입이다** — 펜스가 없거나 규약 키가 없는 케이스는 지금처럼 양성 명령만 돌고 판정도 그대로다.
케이스 형식은 `FAIL [vv-case]` 로 거부한다 — 규약 밖 키, `expect` 항목 수 ≠ 명령 수, `files` 에 없는 `{{이름}}`, 경로를 담은 이름,
검증기를 `bazel run //tools:<검증기>` 로 부르는 명령.
면제는 `docs/waivers.md` 가 같은 게이트 id 로 선언한다(축 `파일`·`stem`).
케이스 판정: 실행한 명령이 하나라도 기대와 어긋나면 fail · **명령 전부를 실행해** 전부 기대와 맞으면 pass · 그 밖(건너뛴 명령이 있거나 실행한
명령이 없음)은 skip. 건너뛴 쪽이 "게이트가 거부한다" 를 보이는 절반이므로 절반만 실행한 케이스는 pass 가 아니다. 판정 어휘는 셋
그대로이고(kb_lib.RUN_VERDICTS) 명령 단위 실행·건너뜀·기대 대조 수를 보고와 실행 기록의 요약에 따로 적는다.
재현성 기록 (p8-reproducibility 초기 상태·환경): 리비전(`git rev-parse --short HEAD`, 워킹트리 변경 여부) · 시각(UTC) · bazel·python 버전 ·
명령마다 종료 코드·소요. 난수 seed 는 없다 — 명령은 결정적이다. 명령은 워크스페이스 루트를 cwd 로, 실행기 자신의 bazel 파이썬 문맥
(`PYTHONSAFEPATH`·`PYTHONPATH`·`RUNFILES_*`)을 뺀 환경에서 돈다 — 실행기를 어떻게 불렀는가가 판정을 바꾸면 그 판정은 재현되지 않는다.

--record 는 실행 기록을 관측(memory plane, concrete, append-only)으로 kb/vv/run/run-<UTC>.md 에 쓴다 — generated.by 는 역할이 아닌
`process:vv_run` 이라 writer 검사 밖이다(카탈로그의 executor 하위 역할을 도구가 맡는 첫 형태). 이미 있는 파일은 덮지 않는다.
생성 뒤 python3 tools/gen_build.py --root . 로 BUILD 를 갱신하고 bazel test //... 를 돌린다.
케이스가 `bazel test` 를 부르므로 `bazel run` 안에서는 중첩 실행이 된다 — odd_check 의 language_policy 와 같은 형태다. 문제가 나면
`bazel run` 밖에서 python3 tools/vv_run.py 로 돌린다.

사용: bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--out report.md] [--waivers docs/waivers.md]
      python3 tools/vv_run.py [--record] [--case <슬러그>…]
종료: fail 있음 1 (EXIT_FAIL) · 전부 pass 0 (EXIT_OK) · pass 없이 skip 만 3 (EXIT_SKIP) · 입력·케이스 형식 문제 2 (EXIT_CONFIG)
"""
from __future__ import annotations

import argparse
import difflib
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import yaml  # 케이스 본문의 `yaml` 펜스(자극·기대) — space2kg·odd2kg 와 같은 잠금

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 네임스페이스·종료 코드·실행 기록 규약의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402 — 케이스의 frontmatter(라벨)는 chunk2kg 의 파서로 읽는다

ID = kb_lib.ID
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
CASE_DIR = kb_lib.KB_VV + "/case"
RUN_DIR = kb_lib.VV_RUN_DIR
GENERATOR = kb_lib.RUN_GENERATOR
ODD_IRI = str(ID["odd-agentic-knowledge-base"])  # 관측의 출처 — ODD 개체 (assume_check 와 같은 sources)
ASSUMPTIONS = [str(ID["asm-bazel-toolchain"]), str(ID["asm-chunk-conventions"])]  # 실행은 bazel 툴체인과 청크 규약을 전제한다
WAIVERS = "docs/waivers.md"  # 면제 선언의 원본 — 코드에 숨기지 않고 표 하나에 적는다 (kb_lib.load_waivers)
MAX_BODY_LINES = 42
# 케이스 본문의 실행 명령 줄 — `**실행 명령**` 뒤 대시, 그 뒤 코드 스팬 하나. 스팬 안의 전부가 명령이다
COMMAND_LINE = re.compile(r"^\*\*실행 명령\*\*\s*—\s*`(.+)`\s*$")
SPLIT = re.compile(r"\s*(?:;|&&)\s*")  # 순차 연산자 — 각 조각을 따로 판정한다
# 실행하는 양성 명령의 허용 목록 — 전부 읽기 전용 검증기다. 그 밖(bazel run · 다른 python3)은 SKIP
POSITIVE_PREFIXES = ("bazel test ", "bazel build ", "bazel query ", "python3 tools/gen_build.py --check")
EXECUTED = re.compile(r"Executed (\d+) out of (\d+) tests?")  # bazel test 요약 — 실행 수 / 전체 수. 나머지는 캐시 재사용 (재현성의 근거)

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


def unsafe(cmd: str) -> str | None:
    """허용 목록 안이어도 실행하지 않는 사유 — 안전하면 None. 검증기의 진입점만 허용 목록이 정하므로 인자 쪽도 본다."""
    if RECORD_FLAG.search(cmd):
        return "`--record` 는 관측을 쓴다 — 케이스의 검증기는 읽기 전용이어야 한다. 인자를 뺀다"
    m = OUT_FLAG.search(cmd)
    if m and not m.group(1).startswith("{{"):
        return "`--out` 이 저장소 안 경로에 쓴다 — 케이스의 검증기는 읽기 전용이어야 한다. 인자를 빼거나 `{{이름}}` 자극으로 가리킨다"
    if UNSAFE.search(cmd):
        return "리다이렉션·파이프·백틱 — 검증기의 출력을 파일이나 다른 명령으로 보내지 않는다"
    for inner in SUBSTITUTION.findall(cmd):
        if not inner.strip().startswith(SUBSTITUTION_HEADS):
            return f"명령 치환 `$({inner.strip()[:40]})` — 치환 안은 목록 조회(`ls`·`find`·`git rev-parse`)뿐이다"
    return None


def classify(cmd: str, spec: dict) -> str | None:
    """명령 하나의 SKIP 사유 — 실행 대상이면 None. 자극·기대를 갖춘 케이스는 읽기 전용 검증기를 직접 부르는 음성 명령까지 실행한다."""
    if cmd.startswith(POSITIVE_PREFIXES):
        return None
    if cmd.startswith(VERIFIER_PREFIXES):
        if not spec:
            return "기계가 읽는 자극·기대가 없다 — 케이스에 `yaml` 펜스(`files`·`expect`)를 둔다 (p8-machine-readable-case)"
        return unsafe(cmd)
    if "/tmp/" in cmd:
        return "케이스가 임시 파일 경로를 적었다 — 경로는 검증기가 정한다. `files` 의 이름을 `{{이름}}` 으로 가리킨다"
    head = " ".join(cmd.split()[:2])
    return f"`{head}` — 실행 대상은 허용 목록의 읽기 전용 검증기뿐"


def yaml_blocks(body: str) -> list[str]:
    """본문의 언어 태그 `yaml` 인 펜스 내용 목록 — 다른 언어의 펜스는 건드리지 않는다 (space2kg 와 같은 스캐너)."""
    out, cur, fence, tag = [], None, None, ""
    for line in body.split("\n"):
        m = kb_lib.MD_FENCE.match(line)
        if fence is None:
            if m:
                fence, tag, cur = m.group(1), line.strip()[len(m.group(1)):].strip(), []
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            if tag == "yaml":
                out.append("\n".join(cur))
            fence, cur = None, None
            continue
        cur.append(line)
    return out


def phrases(value) -> list[str]:
    """`contains` 의 값 → 문구 목록. 문구 하나는 문자열로도 적는다."""
    return [value] if isinstance(value, str) else list(value or [])


def case_spec(body: str) -> tuple[dict, list[str]]:
    """본문의 규약 `yaml` 펜스 → ({files, expect}, 형식 오류 목록). 규약 키가 없는 펜스는 산문의 예시라 읽지 않는다 (점진 도입)."""
    spec: dict = {}
    errs: list[str] = []
    for raw in yaml_blocks(body):
        if not SPEC_HEAD.search(raw):
            continue
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError as e:
            errs.append(f"`yaml` 펜스를 읽을 수 없다 — {e}")
            continue
        if not isinstance(data, dict):
            errs.append(f"`yaml` 펜스는 매핑이어야 한다 — 키는 {' · '.join(SPEC_KEYS)} 다")
            continue
        for k in data:
            if k not in SPEC_KEYS:
                errs.append(f"`yaml` 펜스의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(SPEC_KEYS)} 뿐이다")
            elif k in spec:
                errs.append(f"키 `{k}` 가 펜스 둘에 있다 — 한 케이스에 하나다")
            else:
                spec[k] = data[k]
    files = spec.get("files")
    if files is not None:
        if not isinstance(files, dict) or not files:
            errs.append("`files` 는 비어 있지 않은 `이름: 내용` 매핑이어야 한다")
            spec.pop("files")
        else:
            for name, content in files.items():
                if not isinstance(name, str) or not FILE_NAME.fullmatch(name):
                    errs.append(f"`files` 의 이름 `{name}` 이 단순 파일 이름이 아니다 — 경로는 검증기가 정한다 (영숫자·`.`·`_`·`-`)")
                elif not isinstance(content, str):
                    errs.append(f"`files` 의 `{name}` 내용이 문자열이 아니다 — 파일 내용을 그대로 적는다")
    expect = spec.get("expect")
    if expect is not None:
        if not isinstance(expect, list) or not expect:
            errs.append("`expect` 는 명령 순서대로의 비어 있지 않은 목록이어야 한다")
            spec.pop("expect")
        else:
            for i, e in enumerate(expect, start=1):
                if not isinstance(e, dict):
                    errs.append(f"`expect` {i}번째 항목이 매핑이 아니다 — 키는 {' · '.join(EXPECT_KEYS)} 다")
                    continue
                for k in e:
                    if k not in EXPECT_KEYS:
                        errs.append(f"`expect` {i}번째의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(EXPECT_KEYS)} 뿐이다")
                if e.get("exit") is not None and not isinstance(e["exit"], int):
                    errs.append(f"`expect` {i}번째의 `exit` 는 정수여야 한다 — 실제 `{e['exit']}`")
                c = e.get("contains")
                if c is not None and not (isinstance(c, str) or (isinstance(c, list) and all(isinstance(x, str) for x in c))):
                    errs.append(f"`expect` {i}번째의 `contains` 는 문구 하나 또는 문구 목록이어야 한다")
    return spec, errs


def check_case(spec: dict, cmds: list[str]) -> list[str]:
    """케이스 형식 검사 — 펜스와 실행 명령의 대조. 메시지가 곧 수정 안내다 (STYLEGUIDE §7)."""
    errs = []
    expect = spec.get("expect")
    if expect is not None and len(expect) != len(cmds):
        errs.append(f"`expect` 항목 {len(expect)}개가 실행 명령 {len(cmds)}개와 다르다 — 명령 순서마다 하나를 적는다")
    for c in cmds:
        m = BAZEL_RUN_VERIFIER.match(c.strip())
        if m and m.group(1) in READ_ONLY_VERIFIERS:
            errs.append(f"`bazel run //tools:{m.group(1)}` 는 runfiles 트리에서 돌아 워크스페이스 상대 경로 인자를 자극이 아닌 "
                        f"runfiles 의 없는 파일로 푼다 — `python3 tools/{m.group(1)}.py` 로 바꾼다 (실행의 cwd 가 워크스페이스 루트다)")
    names = set(spec.get("files") or {})
    used = {m for c in cmds for m in PLACEHOLDER.findall(c)}
    for ph in sorted(used - names):
        errs.append(f"명령의 `{{{{{ph}}}}}` 가 `files` 에 없다 — 자극의 이름과 같아야 한다")
    for name in sorted(names - used):
        errs.append(f"`files` 의 `{name}` 을 명령이 가리키지 않는다 — 쓰이지 않는 자극은 케이스의 절반이 빈 것이다")
    return errs


def load_cases(root: Path, only: list[str], waivers: list[dict]) -> tuple[list[dict], list[str]]:
    """케이스 파일 → [{slug, path, label, iri, spec, errors, commands: [{cmd, skip}]}], 실행 명령 줄이 없는 케이스 목록.

    형식 오류(`FAIL [vv-case]`)를 가진 케이스는 오류를 달아 돌려준다 — 판정은 main 이 한다. waivers.md 가 게이트 id
    `vv-case` 로 면제를 선언한 케이스는 오류를 집계에서 빼되 목록에 남기고, 펜스를 읽지 않은 것으로 본다(점진 도입과 같은 자리).
    """
    files = sorted((root / CASE_DIR).glob("*.md"))
    if only:
        files = [f for f in files if f.stem in only]
    cases, missing = [], []
    for f in files:
        meta, _ = parse_chunk(str(f))
        body = kb_lib.chunk_body(f.read_text(encoding="utf-8"))
        line = next((m for ln in body.splitlines() if (m := COMMAND_LINE.match(ln.strip()))), None)
        if line is None:
            missing.append(f.stem)
            continue
        cmds = [c for c in SPLIT.split(line.group(1).strip()) if c]
        spec, errs = case_spec(body)
        errs += check_case(spec, cmds)
        waived = bool(errs) and (kb_lib.waived(waivers, CASE_GATE, f.as_posix(), "파일") or kb_lib.waived(waivers, CASE_GATE, f.stem, "stem"))
        if waived:
            spec = {}
        cases.append({"slug": f.stem, "path": f.as_posix(), "label": meta["title_ko"], "iri": meta["id"], "status": meta["status"],
                      "spec": spec, "errors": errs, "waived": waived,
                      "commands": [{"cmd": c, "skip": classify(c, spec), "mismatch": []} for c in cmds]})
    return cases, missing


def clean_env() -> dict[str, str]:
    """실행기 자신의 bazel 파이썬 문맥을 뺀 환경 — 케이스의 검증기는 워크스페이스 셸에서 부른 것과 같아야 한다.

    `bazel run //tools:vv_run` 의 스텁은 `PYTHONSAFEPATH=1` 을 두고, 그러면 하위 프로세스의 `python3 tools/validate.py` 가
    스크립트 디렉토리를 sys.path 에 얹지 못해 `import kb_lib` 에서 죽는다 — 자극에 닿기 전이다. runfiles 쪽 변수도 뺀다.
    실행기를 어떻게 불렀는가가 케이스의 판정을 바꾸면 그 판정은 재현되지 않는다 (p8-reproducibility).
    """
    return {k: v for k, v in os.environ.items() if k not in BAZEL_PY_ENV}


def run_command(cmd: str, root: Path) -> dict:
    """셸로 실행 — 워크스페이스 루트에서. 종료 코드·소요·출력 꼬리를 남긴다."""
    t0 = time.monotonic()
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, env=clean_env())
    out = r.stdout + r.stderr
    tail = "\n".join(out.strip().splitlines()[-6:])
    m = EXECUTED.search(out)
    tests = (int(m.group(2)), int(m.group(1))) if m else None  # (전체, 실행) — 없으면 요약 줄이 없는 실패
    return {"rc": r.returncode, "secs": time.monotonic() - t0, "tail": tail, "out": out, "tests": tests}


def tests_note(commands: list[dict]) -> str:
    """케이스의 실행 명령이 돌린 테스트 수와 캐시 재사용 수 — `테스트 3 · 캐시 3`. 요약 줄이 없으면 빈 문자열."""
    ran = [c for c in commands if c["skip"] is None and c.get("tests")]
    if not ran:
        return ""
    total = sum(c["tests"][0] for c in ran)
    executed = sum(c["tests"][1] for c in ran)
    return f"테스트 {total} · 캐시 {total - executed}"


def materialize(spec: dict, slug: str) -> tuple[Path | None, dict[str, str]]:
    """`files` 를 임시 디렉토리에 쓴다 → (디렉토리, 이름 → 절대 경로). 경로는 검증기가 정한다 — 케이스는 이름만 준다.

    워크스페이스 밖(`tempfile`)에 두는 까닭은 둘이다. 케이스가 부르는 `bazel test //...` 가 새 파일을 지식 파일로 읽으면
    양성 명령이 자극 때문에 실패하고, 케이스가 절대 경로를 적으면 병렬 실행이 서로를 덮는다 (p8-machine-readable-case).
    내용은 케이스가 적은 그대로 쓴다 — 줄 수가 자극인 케이스가 있어 검증기가 줄을 더하지 않는다.
    """
    files = spec.get("files") or {}
    if not files:
        return None, {}
    d = Path(tempfile.mkdtemp(prefix=f"vv-{slug}-"))
    subs = {}
    for name, content in files.items():
        (d / name).write_text(content, encoding="utf-8")
        subs[name] = (d / name).as_posix()
    return d, subs


def substitute(cmd: str, subs: dict[str, str]) -> str:
    """명령의 `{{이름}}` 을 실제 경로로 바꾼다. 이름이 `files` 에 있음은 형식 검사(check_case)가 이미 보장한다."""
    return PLACEHOLDER.sub(lambda m: subs.get(m.group(1), m.group(0)), cmd)


NEAR_LINES = 40      # 근접 줄을 찾는 범위 — 출력의 마지막 40줄. 게이트의 FAIL 줄은 끝에 모인다
NEAR_RATIO = 0.4     # 이 아래면 근접 줄이라 부르지 않는다 — 무관한 줄을 "가장 가까운" 이라 적으면 수정 방향이 아니다


def near_miss(out: str, phrase: str) -> str:
    """기대 문구에 가장 가까운 출력 줄 — 없으면 마지막 줄. 문구가 어긋났을 때 무엇이 대신 나왔는지가 수정 방향이다."""
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()][-NEAR_LINES:]
    if not lines:
        return "(출력 없음)"
    best = max(lines, key=lambda ln: difflib.SequenceMatcher(None, phrase, ln).ratio())
    return best if difflib.SequenceMatcher(None, phrase, best).ratio() >= NEAR_RATIO else lines[-1]


def judge(c: dict, exp: dict | None) -> list[str]:
    """명령 하나의 기대 대조 — 어긋남 목록(빈 목록이면 맞다). 메시지에 기대와 실제를 함께 적어 수정 방향이 되게 한다."""
    want = 0 if not exp or exp.get("exit") is None else exp["exit"]
    bad = []
    if c["rc"] != want:
        bad.append(f"종료 코드 — 기대 {want} · 실제 {c['rc']}")
    for ph in phrases(exp.get("contains") if exp else None):
        if ph not in c["out"]:
            bad.append(f"기대 문구가 출력에 없다 — 기대 `{ph}` · 실제로 가장 가까운 줄 `{near_miss(c['out'], ph)}`")
    return bad


def expect_of(spec: dict, i: int) -> dict | None:
    """명령 i 번째의 기대 — `expect` 가 없으면 None(종료 0 만 본다, 점진 도입)."""
    exp = spec.get("expect") or []
    return exp[i] if i < len(exp) and isinstance(exp[i], dict) else None


def execute(cases: list[dict], root: Path) -> None:
    """케이스마다 자극을 쓰고 실행 대상 명령을 순서대로 돌린 뒤 기대와 대조한다 (제자리 갱신). 자극은 실행 뒤 지운다."""
    for case in cases:
        tmp, subs = materialize(case["spec"], case["slug"])
        try:
            for i, c in enumerate(case["commands"]):
                if c["skip"] is None:
                    c["run"] = substitute(c["cmd"], subs)
                    c.update(run_command(c["run"], root))
                    c["expect"] = expect_of(case["spec"], i)
                    c["mismatch"] = judge(c, c["expect"])
        finally:
            if tmp is not None:
                shutil.rmtree(tmp, ignore_errors=True)  # 커밋하지 않는다 — 자극은 실행 동안만 있다
        ran = [c for c in case["commands"] if c["skip"] is None]
        skipped = len(case["commands"]) - len(ran)
        # 건너뛴 명령이 하나라도 있으면 케이스는 pass 가 아니다 — 음성 자극이 건너뛰어진 케이스는 "게이트가 거부한다" 를
        # 보이는 절반이 빈 채로 남는다. 판정 어휘는 셋 그대로다(kb_lib.RUN_VERDICTS): 실행한 명령이 기대와 어긋나면 fail,
        # 명령 전부를 실행해 전부 기대와 맞으면 pass, 그 밖(건너뜀이 있거나 실행한 명령이 없음)은 skip 이다. SKIP 은 PASS 가 아니다.
        # 기대는 둘이다 — 종료 코드와 `contains` 의 문구. 둘 다 맞아야 pass 다 (p8-machine-readable-case)
        case["verdict"] = "fail" if any(c["mismatch"] for c in ran) else "pass" if ran and not skipped else "skip"
        case["secs"] = sum(c["secs"] for c in ran)


def revision(root: Path) -> tuple[str, bool]:
    """(짧은 리비전, 워킹트리에 추적 파일 변경이 있는가). git 밖이면 ('없음', False)."""
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"], cwd=root, capture_output=True, text=True,
                                    check=True).stdout.strip())
        return rev, dirty
    except (OSError, subprocess.CalledProcessError):
        return "없음", False


def environment(root: Path) -> str:
    """환경 한 줄 — bazel·python 버전과 OS. p8-reproducibility 의 환경 구성."""
    try:
        bazel = subprocess.run(["bazel", "--version"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        bazel = "bazel 없음"
    return f"{bazel} · python {platform.python_version()} · {platform.system().lower()}"


def counts(cases: list[dict]) -> dict:
    """케이스 판정별 수 + 명령 단위 집계. 명령 단위를 따로 내는 까닭은 케이스 판정 하나가 절반만 실행된 사실을 감추기 때문이다."""
    out = {v: sum(1 for c in cases if c["verdict"] == v) for v in kb_lib.RUN_VERDICTS}
    out["실행"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is None)
    out["건너뜀"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is not None)
    out["명령"] = out["실행"] + out["건너뜀"]
    out["대조"] = sum(1 for c in cases for x in c["commands"] if x["skip"] is None and x.get("expect"))
    out["어긋남"] = sum(1 for c in cases for x in c["commands"] if x["mismatch"])
    return out


def observation(now: datetime, cases: list[dict], rev: str, dirty: bool, env: str) -> str:
    """실행 기록 본문 — 시각·행동·situation 요약 (STYLEGUIDE §4 memory). frontmatter 는 assume_check 의 관측과 같은 형식이다."""
    stamp = kb_lib.utc_stamp(now)  # G3 표기 하나 — frontmatter 와 본문이 같은 꼴을 쓴다 (유저 승인 2026-09-23)
    n = counts(cases)
    ko = f"V&V 실행 {stamp}: pass {n['pass']} · fail {n['fail']} · skip {n['skip']}"
    en = f"V&V run {stamp}: {n['pass']} pass, {n['fail']} fail, {n['skip']} skip"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: memory", "level: concrete", f"title_ko: {ko}", f"title: {en}",
            "status: stable", f"sources: [{{resource: {ODD_IRI}}}]", f"assumes: [{', '.join(ASSUMPTIONS)}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    body = [f"**관측** — {stamp} 에 `vv_run` 이 케이스 {len(cases)}건의 실행 명령 {n['명령']}건 중 "
            f"허용 목록의 검증기 {n['실행']}건을 실행하고 그중 {n['대조']}건을 케이스의 기대(`exit`·`contains`)와 대조했다. "
            f"리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else '없음'}) · {env} · seed 없음.", "",
            kb_lib.RUN_CASE_TABLE_HEADER, "|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        skipped = len(c["commands"]) - ran
        note = tests_note(c["commands"])
        body.append(f"| `{c['slug']}` | {ran} 실행 · {skipped} 건너뜀{' (' + note + ')' if note else ''} | {c['verdict']} | {c['secs']:.1f}s |")
    skips = [(c["slug"], x) for c in cases for x in c["commands"] if x["skip"] is not None]
    if skips:
        body += ["", "| 케이스 | 건너뛴 명령 | 사유 |", "|---|---|---|"]
        rows = [f"| `{slug}` | `{x['cmd'][:60]}{'…' if len(x['cmd']) > 60 else ''}` | {x['skip']} |" for slug, x in skips]
        budget = MAX_BODY_LINES - len(body) - 3  # 남는 줄 — 요약 2줄과 여유
        if len(rows) > budget:
            rows = rows[:max(budget - 1, 0)] + [f"| … | 외 {len(rows) - max(budget - 1, 0)}건 | 보고(`vv_run` 출력)에 전부 있다 |"]
        body += rows
    body += ["", f"판정 요약 — 케이스 pass {n['pass']} · fail {n['fail']} · skip {n['skip']} · 명령 실행 {n['실행']} · 건너뜀 {n['건너뜀']} · "
             f"기대 대조 {n['대조']} · 어긋남 {n['어긋남']}. SKIP 은 PASS 가 아니다 — 건너뛴 명령이 있는 케이스는 skip 이다. "
             f"기대를 적은 명령은 종료 코드와 `contains` 문구가 둘 다 맞아야 맞은 것이고, 적지 않은 명령은 종료 0 만 본다."]
    return "\n".join(head + body) + "\n"


def expect_note(exp: dict | None) -> str:
    """보고의 `기대` 칸 — 기대를 적지 않은 명령은 종료 0 만 본다 (점진 도입)."""
    if not exp:
        return "종료 0 (기대 없음)"
    bits = [f"종료 {exp['exit']}"] if exp.get("exit") is not None else ["종료 0"]
    if phrases(exp.get("contains")):
        bits.append("문구 " + " · ".join(f"`{ph}`" for ph in phrases(exp["contains"])))
    return " · ".join(bits)


def report(now: datetime, cases: list[dict], missing: list[str], rev: str, dirty: bool, env: str) -> str:
    n = counts(cases)
    verdict = ("**fail 있음**" if n["fail"] else "pass 없음 — 전부 skip" if not n["pass"] else "pass" + (" (skip 있음)" if n["skip"] else ""))
    skip_note = (f"- 건너뛴 명령: **{n['건너뜀']}** / 명령 {n['명령']} — 건너뛴 명령이 있는 케이스는 pass 가 아니라 skip 이다 "
                 f"(음성 자극이 건너뛰어지면 \"게이트가 거부한다\" 를 보이는 절반이 빈다)")
    expect_line = (f"- 기대 대조: **{n['대조']}** / 실행 {n['실행']} — 기대(`exit`·`contains`)를 적은 명령은 종료 코드와 문구가 둘 다 맞아야 "
                   f"맞은 것이다. 어긋난 명령 {n['어긋남']}건 (`yaml` 펜스가 없는 케이스는 종료 0 만 본다 — 점진 도입)")
    rep = kb_lib.gendoc_header(
        "vv_run", "V&V 케이스 실행 판정", "tools/vv_run.py",
        "V&V 케이스 청크(`kb/vv/case/`)의 실행 명령 중 허용 목록의 읽기 전용 검증기만 실제로 돌려 케이스의 기대와 대조해 "
        "케이스마다 pass·fail·skip 을 — SKIP 은 PASS 가 아니다 (8.20절)",
        "bazel run //tools:vv_run", [c["path"] for c in cases],
        f"케이스 {len(cases)} (pass {n['pass']} · fail {n['fail']} · skip {n['skip']}) · 명령 {n['명령']} "
        f"(실행 {n['실행']} · 건너뜀 {n['건너뜀']})",
        kb_lib.gendoc_view_notice("V&V 케이스 청크의 본문"), input_kind="케이스 파일",
        extra=[f"- 결과: {verdict}", skip_note, expect_line,
               f"- 초기 상태: 리비전 `{rev}` (워킹트리 추적 파일 변경 {'있음' if dirty else kb_lib.NONE_MARK}) · {env}"])
    body = ["## 케이스 — 실행 대상은 허용 목록의 읽기 전용 검증기뿐. SKIP 은 PASS 가 아니다", "",
            "| 케이스 | 라벨 | 명령 | 자극·기대 | 결과 | 소요 |", "|---|---|---|---|---|---|"]
    for c in cases:
        ran = sum(1 for x in c["commands"] if x["skip"] is None)
        spec = c["spec"]
        machine = " · ".join(filter(None, [f"자극 {len(spec['files'])}" if spec.get("files") else "",
                                           f"기대 {len(spec['expect'])}" if spec.get("expect") else ""])) or kb_lib.NONE_MARK
        body.append(f"| `{c['slug']}` | {c['label']} | {ran} 실행 · {len(c['commands']) - ran} 건너뜀 | {machine} | **{c['verdict']}** | {c['secs']:.1f}s |")
    body += ["", "## 명령", "", "| 케이스 | 명령 | 종료 | 기대 | 소요 | 비고 |", "|---|---|---|---|---|---|"]
    for c in cases:
        for x in c["commands"]:
            if x["skip"] is None:
                t = x.get("tests")
                note = (f"테스트 {t[0]} · 실행 {t[1]} · 캐시 {t[0] - t[1]}" if t else "요약 줄 없음" if x["cmd"].startswith("bazel test ") else "") + \
                       ("" if not x["mismatch"] else " · **어긋남**")
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | {x['rc']} | {expect_note(x.get('expect'))} | {x['secs']:.1f}s | {note or kb_lib.NONE_MARK} |")
            else:
                body.append(f"| `{c['slug']}` | `{x['cmd']}` | SKIP | {kb_lib.NONE_MARK} | {kb_lib.NONE_MARK} | {x['skip']} |")
    off = [(c["slug"], x) for c in cases for x in c["commands"] if x["mismatch"]]
    if off:
        body += ["", "## 어긋난 명령 — 기대와 실제", ""]
        for slug, x in off:
            body += [f"### `{slug}` — `{x['cmd']}` (종료 {x['rc']})", ""] + [f"- {b}" for b in x["mismatch"]] + ["", "```text", x["tail"], "```", ""]
    if missing:
        body += ["", f"실행 명령 줄이 없는 케이스 {len(missing)}건: " + ", ".join(f"`{m}`" for m in missing) + " — 케이스 본문에 `**실행 명령**` 줄(대시 뒤 코드 스팬 하나)이 있어야 한다"]
    return kb_lib.gendoc_assemble(rep, body, [c["path"] for c in cases], input_kind="케이스 파일")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", action="append", default=[], metavar="SLUG", help="이 케이스(파일 stem)만 — 반복 가능")
    ap.add_argument("--record", action="store_true", help=f"결과를 실행 기록으로 {RUN_DIR}/run-<UTC>.md 에 append-only 로 쓴다")
    ap.add_argument("--out", default="", help="보고를 파일로도 쓴다")
    ap.add_argument("--waivers", default=WAIVERS, metavar="FILE",
                    help=f"docs/waivers.md — 게이트 id `{CASE_GATE}`(축 파일·stem)로 면제된 케이스의 형식 오류는 집계에서 빼되 목록에 남긴다")
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 워크스페이스 루트 기준")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    if not (root / CASE_DIR).is_dir():
        print(f"FAIL [vv_run] {CASE_DIR}: 케이스 디렉토리가 없다 — 워크스페이스 루트에서 돌린다")
        return EXIT_CONFIG
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [vv_run] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    waiver_path = root / a.waivers
    try:
        waivers = kb_lib.load_waivers(waiver_path) if waiver_path.is_file() else []
    except ValueError as e:  # 표의 열·축이 규약 밖이면 설정 문제다 — 판정 실패가 아니다
        print(f"FAIL [vv_run] waiver 표 — {e}")
        return EXIT_CONFIG
    try:
        cases, missing = load_cases(root, a.case, waivers)
    except ValueError as e:  # parse_chunk 의 frontmatter 규칙 — 케이스가 청크가 아니면 실행할 수 없다
        print(f"FAIL [vv_run] {e}")
        return EXIT_CONFIG
    unknown = sorted(set(a.case) - {c["slug"] for c in cases} - set(missing))
    if unknown:
        print(f"FAIL [vv_run] --case 대상이 {CASE_DIR} 에 없다: {', '.join(unknown)}")
        return EXIT_CONFIG
    if not cases:
        print(f"SKIP [vv_run] {CASE_DIR}: 실행할 케이스가 없다")
        return EXIT_SKIP
    # 케이스 형식 검사 — 규약 펜스를 둔 케이스만 대상이다. 형식이 깨진 케이스는 실행 전에 거부한다. 자극·기대가
    # 명령과 어긋난 채 도는 실행은 판정이 아니라 소음이다 (STYLEGUIDE §7 — 메시지가 곧 수정 안내다)
    for c in cases:
        if c["errors"] and c["waived"]:
            for e in c["errors"]:
                print(f"WAIVED [{CASE_GATE}] {c['path']}: {e} (waivers.md — 집계에서 뺐고 펜스를 읽지 않았다)")
    broken = [c for c in cases if c["errors"] and not c["waived"]]
    if broken:
        for c in broken:
            for e in c["errors"]:
                print(f"FAIL [{CASE_GATE}] {c['path']}: {e}")
        print(f"FAIL [{CASE_GATE}] 케이스 {len(broken)}건의 형식이 규약 밖이다 — 규약은 결정 `p8-machine-readable-case` 다. "
              f"면제는 `{a.waivers}` 에 게이트 id `{CASE_GATE}` 로 선언한다")
        return EXIT_CONFIG

    now = datetime.now(timezone.utc).replace(microsecond=0)
    rev, dirty = revision(root)
    env = environment(root)
    execute(cases, root)
    text = report(now, cases, missing, rev, dirty, env)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")

    if a.record:
        run_dir = root / RUN_DIR
        run_dir.mkdir(parents=True, exist_ok=True)
        target = run_dir / f"run-{now.strftime('%Y%m%dT%H%M%SZ')}.md"
        if target.exists():
            print(f"FAIL [vv_run] {target.relative_to(root)}: 이미 있다 — 실행 기록은 append-only 다 (r-026)")
            return EXIT_CONFIG
        target.write_text(observation(now, cases, rev, dirty, env), encoding="utf-8")
        print(f"실행 기록: {target.relative_to(root)} — python3 tools/gen_build.py --root . 로 BUILD 를 갱신한 뒤 bazel test //... 를 돌린다")
    n = counts(cases)
    return EXIT_FAIL if n["fail"] else EXIT_OK if n["pass"] else EXIT_SKIP


if __name__ == "__main__":
    raise SystemExit(main())
