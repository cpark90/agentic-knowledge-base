#!/usr/bin/env python3
"""게이트 등록부(`defs/kb.bzl` 의 `GATES`) → 게이트 그래프(-kg.ttl) 생성기 (M1 단일 정의처, 2026-10-02).

게이트는 프로세스 층의 **항목**이다(결정 p0-service-is-a-three-layer-wiki) — 어느 청크의 투영으로도 환원되지
않으므로 그래프에 개체가 서야 층별 집계(CQ-38)가 셀 자리를 갖는다. 2026-10-01 실측에서 같은 목록이 넷으로
갈려 있었고(상수 26 · 코드의 태그 · 총람의 `id` 열 · 하네스 목록) 단일 정의처가 없다는 것이 그 진단이었다.

원본은 `GATES`·`TOOL_TAGS` 리터럴이고 TTL 은 생성물이다 — `kg/` 에 손으로 쓰지 않는다(`odd2kg`·`space2kg` 와
같은 자리). 개체 하나가 게이트 하나이고 IRI 는 `id:gate-<게이트 id>` 다. 도구 태그(`TOOL_TAGS`)는 게이트가
아니므로 개체를 받지 않는다.

생성 = 검사:
  - 항목마다 네 키(`tier`·`tool`·`ko`·`desc`)가 있고 `tier` 는 `GATE_TIERS` 안이다
  - 판정 도구가 파이썬 안이면 등록부 사이드카(`tools/<도구>.chunks.yml`)의 `ids: file:` 이 실재한다 —
    `agt:enforcedBy` 의 대상이 그 파일 복합체이고, 없으면 끊긴 링크를 내는 대신 여기서 거부한다
  - 파이썬 밖(`starlark`·`bazel`)인 게이트는 가리킬 코드 청크가 없어 `agt:enforcedBy` 를 갖지 않는다

사용: gates2kg.py --out gates-kg.ttl --gates defs/kb.bzl [--registry tools/<도구>.chunks.yml ...]
출력·종료: 위반은 `FAIL [gates2kg] <원본>: <메시지>` + EXIT_FAIL. 읽을 수 없는 입력은 EXIT_CONFIG.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:  # 리터럴 읽기와 종료 코드 규약의 단일 정의처는 kb_lib 다
    from tools import kb_lib
except ImportError:
    import kb_lib

EXIT_FAIL = kb_lib.EXIT_FAIL
EXIT_CONFIG = kb_lib.EXIT_CONFIG
TAG = "gates2kg"
ID_BASE = str(kb_lib.ID)
TIER_INDIVIDUAL = "agt:%sTier"  # 실행 계층 → 개체 (gate-tier-ontology)
LAYER_INDIVIDUAL = "agt:%sLayer"  # 서비스 층 → 개체 (layer-ontology)
HEADER = (
    "# 게이트 그래프 — 생성물이다. 손으로 쓰지 않는다 (tools/gates2kg.py).\n"
    "# 원본은 defs/kb.bzl 의 GATES 리터럴이고 개체 하나가 게이트 하나다 (id:gate-<게이트 id>).\n"
    "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n"
    "@prefix id: <%s> .\n"
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n" % ID_BASE
)


# ── 판정 도구의 개체 — 등록부 사이드카의 파일 복합체 IRI ────────────────────

def tool_composites(registries: list[str]) -> dict[str, str]:
    """등록부 사이드카들 → 도구 이름 → 파일 복합체 IRI (`ids: file:`).

    사이드카는 손이 원본인 등록부이고 파일 복합체가 도구 하나의 개체다 (p7-code-links-on-file-composite).
    YAML 파서를 싣지 않는다 — 필요한 것은 `ids:` 블록의 `file:` 한 줄뿐이고 이 생성기는 타깃마다 돈다.
    """
    out: dict[str, str] = {}
    for path in registries:
        p = Path(path)
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except OSError as e:
            print(f"FAIL [{TAG}] {path}: 읽을 수 없다 — {e}", file=sys.stderr)
            raise SystemExit(EXIT_CONFIG)
        name = p.name[: -len(".chunks.yml")] if p.name.endswith(".chunks.yml") else p.stem
        for line in lines:
            if line.startswith("  file:"):
                out[name] = line.split(":", 1)[1].strip()
                break
    return out


def escape(text: str) -> str:
    """TTL 문자열 리터럴의 이스케이프 — 역슬래시와 따옴표만 나온다 (설명은 한 줄이다)."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


# ── 그래프 방출 ────────────────────

def emit(gates: dict, tiers: tuple, layer: str, tools: dict[str, str], outside: tuple, where: str) -> str:
    """게이트 등록부 → TTL. 키·계층의 위반과 판정 도구의 부재는 생성 시점에 거부한다."""
    errors = []
    blocks = []
    for gate_id in sorted(gates):
        spec = gates[gate_id]
        missing = [k for k in ("tier", "tool", "ko", "desc") if not spec.get(k)]
        if missing:
            errors.append(f"{where}: 게이트 {gate_id!r} 에 {', '.join(missing)} 가 없다")
            continue
        if spec["tier"] not in tiers:
            errors.append(f"{where}: 게이트 {gate_id!r} 의 계층 {spec['tier']!r} 이 어휘 밖이다 — {list(tiers)} 중 하나다")
            continue
        props = [
            "a agt:Gate",
            f'rdfs:label "{escape(gate_id)}"@en , "{escape(spec["ko"])}"@ko',
            f'skos:definition "{escape(spec["desc"])}"@ko',
            f"agt:inLayer {LAYER_INDIVIDUAL % layer}",
            f"agt:gateTier {TIER_INDIVIDUAL % spec['tier']}",
        ]
        if spec["tool"] not in outside:
            iri = tools.get(spec["tool"])
            if not iri:
                errors.append(f"{where}: 게이트 {gate_id!r} 의 판정 도구 {spec['tool']!r} 의 파일 복합체를 찾을 수 없다 — "
                              f"tools/{spec['tool']}.chunks.yml 의 `ids: file:` 가 agt:enforcedBy 의 대상이다")
                continue
            props.append(f"agt:enforcedBy <{iri}>")
        head = f"id:{kb_lib.GATE_ID_PREFIX}{gate_id} {props[0]}"
        blocks.append(" ;\n    ".join([head] + props[1:]) + " .")
    if errors:
        print("\n".join(f"FAIL [{TAG}] {e}" for e in errors), file=sys.stderr)
        raise SystemExit(EXIT_FAIL)
    return HEADER + "\n" + "\n\n".join(blocks) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="게이트 등록부 → 게이트 그래프 (-kg.ttl)")
    ap.add_argument("--out", required=True, help="출력 TTL 경로 (접미사 규약 0.2절의 `-kg`)")
    ap.add_argument("--gates", required=True, help="게이트 등록부의 원본 defs/kb.bzl")
    ap.add_argument("--registry", nargs="*", default=[], help="등록부 사이드카들 (tools/<도구>.chunks.yml) — agt:enforcedBy 의 대상")
    a = ap.parse_args()
    try:
        gates = kb_lib.load_gates(a.gates)
        tiers = kb_lib.load_bzl_list(a.gates, "GATE_TIERS")
        outside = kb_lib.load_bzl_list(a.gates, "GATE_TOOLS_OUTSIDE_PYTHON")
        layer = kb_lib.load_bzl_scalar(a.gates, kb_lib.GATE_LAYER_NAME)
    except (OSError, ValueError) as e:
        print(f"FAIL [{TAG}] {a.gates}: 게이트 등록부를 읽을 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    ttl = emit(gates, tiers, layer, tool_composites(a.registry), outside, a.gates)
    try:
        Path(a.out).write_text(ttl, encoding="utf-8")
    except OSError as e:
        print(f"FAIL [{TAG}] {a.out}: 쓸 수 없다 — {e}", file=sys.stderr)
        return EXIT_CONFIG
    print(f"PASS [{TAG}] — 게이트 {len(gates)}개, 판정 도구 개체 {len(tool_composites(a.registry))}개", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
