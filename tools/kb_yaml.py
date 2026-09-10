"""YAML 부분집합 로더 — OpenODD 문서(kb/odd/*.yml)와 생성 택소노미를 읽는다.

잠금 파일(tools/requirements_lock.txt)의 정책("순수 파이썬 휠만")에 맞춰 PyYAML을 넣지 않았다
(ODD 조건 cond-dependency-lock). rules_python은 sdist 빌드를 지원하고 PyYAML ≥ 6.0.1은 sdist에서 빌드되므로
정책을 바꾸면 relock으로 넣을 수 있다 (2026-09-11 확인). 이 로더는 그 자리를 메우는 **부분집합**이다:
블록 매핑·블록 시퀀스·흐름 매핑 `{}`·흐름 시퀀스 `[]`·따옴표 스칼라·주석. 앵커·다중 문서·
블록 스칼라(`|`, `>`)는 지원하지 않는다. 진짜 YAML 파서로 읽어도 같은 결과가 나오는
문서만 쓴다 — 잠금에 PyYAML이 들어오면 이 파일은 삭제 대상이다 (open-questions §3).
"""
from __future__ import annotations

import re


def load(text: str):
    lines = []
    for raw in text.splitlines():
        s = _strip_comment(raw)
        if s.strip():
            lines.append((len(s) - len(s.lstrip(" ")), s.strip()))
    val, i = _block(lines, 0, lines[0][0] if lines else 0)
    if i != len(lines):
        raise ValueError(f"YAML: {i+1}번째 항목 뒤가 해석되지 않았다: {lines[i][1]!r}")
    return val


def _strip_comment(line: str) -> str:
    out, q = [], None
    for ch in line:
        if q:
            out.append(ch)
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch; out.append(ch)
        elif ch == "#" and (not out or out[-1] in " \t"):
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def _block(lines, i, indent):
    if i >= len(lines):
        return None, i
    ind, s = lines[i]
    if ind != indent:
        raise ValueError(f"YAML: 들여쓰기 불일치 {s!r}")
    return (_seq if s.startswith("- ") or s == "-" else _map)(lines, i, indent)


def _seq(lines, i, indent):
    out = []
    while i < len(lines) and lines[i][0] == indent and (lines[i][1].startswith("- ") or lines[i][1] == "-"):
        item = lines[i][1][1:].strip()
        if not item:
            v, i = _block(lines, i + 1, lines[i + 1][0]); out.append(v); continue
        key, val, is_map = _split_key(item)
        if is_map:  # "- key: value" — 매핑의 첫 항목이 시퀀스 항목 줄에 온다
            sub = [(indent + 2, item)]
            j = i + 1
            while j < len(lines) and lines[j][0] > indent:
                sub.append(lines[j]); j += 1
            base = sub[0][0]
            sub = [(base if k == 0 else ind, t) for k, (ind, t) in enumerate(sub)]
            v, _ = _map(sub, 0, base); out.append(v); i = j
        else:
            out.append(_scalar(item)); i += 1
    return out, i


def _map(lines, i, indent):
    out = {}
    while i < len(lines) and lines[i][0] == indent and not lines[i][1].startswith("- "):
        key, val, is_map = _split_key(lines[i][1])
        if not is_map:
            raise ValueError(f"YAML: 'key: value' 가 아니다: {lines[i][1]!r}")
        if val == "":
            if i + 1 < len(lines) and lines[i + 1][0] > indent:
                v, i = _block(lines, i + 1, lines[i + 1][0])
            else:
                v, i = None, i + 1
        else:
            v, i = _scalar(val), i + 1
        out[key] = v
    return out, i


def _split_key(s):
    """'key: value' / 'key:' 를 나눈다. 키 안의 ':'(예: id:cond-x)는 뒤에 공백이 없으면 구분자가 아니다."""
    if s[0] in "\"'":
        q = s[0]; end = s.index(q, 1)
        rest = s[end + 1:]
        if rest.startswith(":") and (len(rest) == 1 or rest[1] == " "):
            return s[1:end], rest[1:].strip(), True
        return None, s, False
    if s.startswith(("{", "[")):
        return None, s, False
    m = re.match(r"^([^\s\"'{}\[\],]+?):(?:\s+(.*))?$", s)
    if m:
        return m.group(1), (m.group(2) or "").strip(), True
    return None, s, False


def _scalar(s: str):
    s = s.strip()
    if s.startswith("{"):
        return _flow_map(s)
    if s.startswith("["):
        return _flow_list(s)
    if s and s[0] in "\"'":
        return _unquote(s)
    if s in ("true", "True"): return True
    if s in ("false", "False"): return False
    if s in ("null", "~", ""): return None
    if re.fullmatch(r"-?\d+", s): return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s): return float(s)
    return s


def _unquote(s):
    q = s[0]
    if s[-1] != q:
        raise ValueError(f"YAML: 따옴표가 닫히지 않았다: {s!r}")
    body = s[1:-1]
    return body.replace('\\"', '"').replace("\\\\", "\\") if q == '"' else body.replace("''", "'")


def _split_flow(inner: str):
    parts, depth, q, cur = [], 0, None, []
    for ch in inner:
        if q:
            cur.append(ch)
            if ch == q: q = None
        elif ch in "\"'":
            q = ch; cur.append(ch)
        elif ch in "{[":
            depth += 1; cur.append(ch)
        elif ch in "}]":
            depth -= 1; cur.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(cur)); cur = []
        else:
            cur.append(ch)
    if "".join(cur).strip():
        parts.append("".join(cur))
    return [p.strip() for p in parts]


def _flow_map(s):
    assert s.endswith("}"), f"YAML: 흐름 매핑이 닫히지 않았다: {s!r}"
    out = {}
    for part in _split_flow(s[1:-1]):
        key, val, ok = _split_key(part)
        if not ok:
            raise ValueError(f"YAML: 흐름 매핑 항목이 'k: v' 가 아니다: {part!r}")
        out[key] = _scalar(val)
    return out


def _flow_list(s):
    assert s.endswith("]"), f"YAML: 흐름 시퀀스가 닫히지 않았다: {s!r}"
    return [_scalar(p) for p in _split_flow(s[1:-1])]
