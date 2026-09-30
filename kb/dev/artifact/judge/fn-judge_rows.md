---
id: https://agentic-knowledge-base.dev/id/chunk/136a10e2-560c-4817-b3e1-630cbe303a57
type: artifact
level: executable
title_ko: 함수 judge_rows (tools/judge.py)
title: function judge_rows in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/8f3b4eaf-dced-410d-98cc-6771157e17c6
---
**함수** — `judge_rows(root, paths, q, name, th, resp_sets, sheet)` 다. 청크 × 응답 집합마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_rows(root: Path, paths: list[str], q: dict, name: str, th: dict, resp_sets: list[dict],
              sheet: dict[str, dict] | None = None) -> list[dict]:
    """청크 × 응답 집합마다 판정 행을 만든다.

    지문은 **둘**이다(2026-09-30 vnv 결함 보고 ①) — 로그의 `입력 지문` 열에 실리는 **기록 지문**(청크 파일
    바이트의 sha256, 추적·재현의 열쇠)과, 응답을 찾는 **대조 지문**(`kb_lib.label_fingerprint`, 판정자에게
    실제로 보인 라벨+본문의 sha256)이다. 세션 판정자는 파일을 읽지 않고 `label_sample.py --judge-sheet`가 보인
    것만 보므로 대조는 그 지문으로 해야 한다 — 파일 바이트 지문으로 대조하면 응답이 전부 안 잡힌다(실측 결함).
    `sheet`(선택)는 `--decoys`의 key.json 전체(실표본+미끼)를 경로로 색인한 것이다 — 있으면 그 항목의
    라벨·본문(판정자에게 보인 그대로)으로 대조 지문을 내고, 없으면 청크를 다시 읽어(label_sample.body_of와
    같은 추출) 낸다. 상대 경로는 워크스페이스 루트 기준으로 푼다 — `bazel run`의 작업 디렉토리는 runfiles
    트리라 그대로는 닿지 못한다.
    """
    sheet = sheet or {}
    rows = []
    now = kb_lib.utc_stamp(datetime.now(timezone.utc))
    for data in resp_sets:
        used: set = set()
        for p in paths:
            path = at(root, p)
            posix = Path(p).as_posix()
            try:
                raw = path.read_bytes()
                meta, _ = parse_chunk(str(path))
            except (OSError, ValueError) as e:
                raise JudgeError(f"{p}: 청크로 읽을 수 없다 — {e}")
            record_fp = hashlib.sha256(raw).hexdigest()
            shown = sheet.get(posix) or sheet.get(p)
            item = shown if shown else {"title_ko": meta.get("title_ko", ""), "title": meta.get("title", ""),
                                        "body": sample_body_of(str(path))}
            match_fp = kb_lib.label_fingerprint(item)
            answer = take_response(data, used, q, name, match_fp)
            rows.append({"path": posix, "iri": meta["id"], "level": meta["level"],
                         "verdict_stem": f"{path.parent.name}-{path.stem}",
                         "label": meta.get("title_ko", ""), "fingerprint": record_fp, "at": now,
                         "route": route(answer["confidence"], th), **answer})
    return rows
```
<!-- 인용 끝 -->
