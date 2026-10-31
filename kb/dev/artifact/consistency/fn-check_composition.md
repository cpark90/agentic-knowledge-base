---
id: https://agentic-knowledge-base.dev/id/chunk/004314d0-b3f3-4281-9fdf-7c7454babcad
type: artifact
level: executable
title_ko: 함수 check_composition (tools/consistency.py)
title: function check_composition in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/378dc204-7474-4a47-ab11-c9fc4cb5c778, https://agentic-knowledge-base.dev/id/chunk/a133095c-86c0-4a59-9f2d-22259a6708f4, https://agentic-knowledge-base.dev/id/chunk/ccb3c961-ba27-4c5b-968c-d35f8cb91fb4, https://agentic-knowledge-base.dev/id/chunk/cd5413ed-eaa2-466b-b701-bb182e0a5377, https://agentic-knowledge-base.dev/id/chunk/cfb0a4b8-f534-4e19-875d-07dfe88eb9b4]
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `check_composition(text)` 다. 한 파일의 문장 구성 대리 → {규칙: [(줄 번호, 표현)…]}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_composition(text: str) -> dict[str, list[tuple[int, str]]]:
    """한 파일의 문장 구성 대리 → {규칙: [(줄 번호, 표현)…]}. 결정 p0-sentence-composition 의 규칙 3·4·5·6 이다.

    - 기호: 산문 조각(코드·따옴표·링크 대상 밖)의 `=`·`+`·`→`·`×`. 목록 표지 `+ ` 는 지운 뒤 센다
    - 명사형 끝맺음: 마침표로 끝난 문장의 끝 음절(끝 괄호·굵게·따옴표를 걷어 낸 뒤)이 한글이고 서술어 종결(다·까·라·자)이
      아니다. 제목은 보지 않고, 목록 항목과 표 셀이 문장 하나뿐이면 명사구 불릿·셀로 보아 세지 않는다(STYLEGUIDE 허용)
    - 가운뎃점 연쇄: 쉼표·마침표·괄호·대시 따위로 끊기지 않은 한 구 안에서 가운뎃점으로 비지 않은 셋 이상을 이은 것
    - 문장 가운데 괄호: 괄호 뒤에 같은 문장의 말이 이어진다. 괄호 뒤가 문장 끝(마침표·느낌표·물음표·셀 경계·단위 끝)이면
      세지 않고, 번호 괄호("(a)")와 앞말에 붙은 영문 병기("정제 수준(refinement level)", 규칙 8)도 세지 않는다.
      `규약:` 줄의 줄 끝과 표 칸 경계(` | `)도 문장 끝이다(_convention_stops)
    """
    hits: dict[str, list[tuple[int, str]]] = {"symbol": [], "noun_end": [], "chain": [], "paren": []}
    for kind, pieces in composition_units(text):
        unit, starts = _joined(pieces)
        stops = _convention_stops(pieces)
        for m in COMPOSITION_SYMBOL.finditer(unit):
            hits["symbol"].append((_line_at(starts, m.start()), unit[max(0, m.start() - 16):m.end() + 16].strip()))
        for piece in COMPOSITION_CHAIN_BREAK.split(unit):
            run: list[str] = []
            for part in piece.split("·") + [""]:
                if part.strip():
                    run.append(part.strip())
                    continue
                if len(run) >= 3:
                    expr = "·".join([run[0].split()[-1]] + run[1:-1] + [run[-1].split()[0]])
                    hits["chain"].append((_line_at(starts, unit.find(piece)), expr))
                run = []
        if kind == "제목":
            continue
        ends = [m.start() for m in COMPOSITION_PERIOD.finditer(unit)]
        single = len(ends) == 1 and not unit[ends[0] + 1:].strip(" *\"”」'’")
        if not (kind in ("항목", "셀") and single):
            prev = 0
            for e in ends:
                sentence = COMPOSITION_TRAILING.sub("", unit[prev:e])
                prev = e + 1
                last = sentence[-1:] if sentence else ""
                if sentence.rsplit(" — ", 1)[-1].strip(" *") in kb_lib.EMPTY_VALUE:
                    continue  # "**검증 대응물** — 없음." — 세 빈 값(p4-three-empty-values)은 값 표기이지 문장이 아니다
                if "가" <= last <= "힣" and last not in COMPOSITION_PREDICATE_END:
                    hits["noun_end"].append((_line_at(starts, e), "…" + sentence[-24:].lstrip() + "."))
        for a, b in _paren_groups(unit):
            inner = unit[a + 1:b - 1]
            if COMPOSITION_ENUM_PAREN.match(inner):
                continue
            if a and not unit[a - 1].isspace() and re.search(r"[A-Za-z]", inner) and COMPOSITION_GLOSS_PAREN.match(inner):
                continue
            rest = unit[b:].lstrip(" *\"”」'’")
            if not rest or rest[0] in ".!?。" or any(b <= x <= len(unit) - len(rest) for x in stops):
                continue
            hits["paren"].append((_line_at(starts, a), unit[max(0, a - 12):b + 12].strip()))
    return hits
```
<!-- 인용 끝 -->
