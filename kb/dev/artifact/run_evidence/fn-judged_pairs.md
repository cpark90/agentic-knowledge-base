---
id: https://agentic-knowledge-base.dev/id/chunk/6df5b1b2-44cf-407f-94c2-73b8f6e9093c
type: artifact
level: executable
title_ko: 함수 judged_pairs (tools/run_evidence.py)
title: function judged_pairs in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07748717-33f2-409f-8b8d-9c1a2fc37bc4, https://agentic-knowledge-base.dev/id/chunk/9ba49f50-c949-45ae-816e-d24210ec8af6, https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2]
part_of: https://agentic-knowledge-base.dev/id/composite/ed156a01-76a8-4195-b32e-c9096b040444
---
**함수** — `judged_pairs(meta_of, path_of)` 다. 판정 로그의 쌍 행 → ((앵커, 종류, 대상) → [(판정 로그, 판정자, 극성, 확신도)], 판정 로그들, 낡은 판정 수, 끝이 없는 쌍 행 수).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judged_pairs(meta_of: dict, path_of: dict) -> tuple[dict, list[str], int, int]:
    """판정 로그의 쌍 행 → ((앵커, 종류, 대상) → [(판정 로그, 판정자, 극성, 확신도)], 판정 로그들, 낡은 판정 수, 끝이 없는 쌍 행 수).

    낡은 판정(입력 해시값이 지금 두 파일의 sha256 과 다름)과 끝이 없는 행은 세고 건너뛴다. 확신도는 판정 로그의 `확신도` 칸('예'의 확률)이고
    읽지 못하면 None 이다. 판정 증거(judgement_lines)와 믿음 정도(belief_lines)가 이 한 읽기를 쓴다."""
    judged: dict[tuple[str, str, str], list[tuple[str, str, str, float | None]]] = defaultdict(list)
    judge_logs = sorted(i for i, m in meta_of.items()
                        if f"{kb_lib.JUDGE_LOG_DIR}/" in path_of[i] and Path(path_of[i]).name.startswith(kb_lib.JUDGE_LOG_PREFIX)
                        and isinstance(m.get("generated"), dict) and m["generated"].get("by") == kb_lib.JUDGE_GENERATOR)
    stale = gone_pair = 0
    for log in judge_logs:
        for row in kb_lib.judge_log_rows(Path(path_of[log]).read_text(encoding="utf-8")):
            pair = kb_lib.parse_pair_target(row["대상"])
            pol = kb_lib.JUDGE_NOUL_POLARITY.get(row["값"])
            if pair is None or pol is None:
                continue
            a, b, kind = pair
            if a not in meta_of or b not in meta_of or kind not in LINK_KEYS:
                gone_pair += 1
                continue
            if kb_lib.pair_record_fingerprint(Path(path_of[a]).read_bytes(), Path(path_of[b]).read_bytes()) != row["입력 해시값"]:
                stale += 1
                continue
            conf = float(row["확신도"]) if kb_lib.JUDGE_CONFIDENCE.match(row.get("확신도", "")) else None
            judged[(a, kind, b)].append((log, row["판정자 식별자"], pol, conf))
    return judged, judge_logs, stale, gone_pair
```
<!-- 인용 끝 -->
