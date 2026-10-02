---
id: https://agentic-knowledge-base.dev/id/chunk/63cf4a6b-7be3-4c38-8be4-9a039b8d5aec
type: artifact
level: executable
title_ko: 함수 render (tools/tokens.py)
title: function render in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T11:12:02Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/88215097-083d-4315-8983-eff5433360ad, https://agentic-knowledge-base.dev/id/chunk/93603726-5c98-4055-96e5-fb41e9f77347, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/9dca3dba-bb72-415b-a4cb-bcf5058e807f, https://agentic-knowledge-base.dev/id/chunk/aac10f80-c526-4fab-ad8f-e93b193438f3, https://agentic-knowledge-base.dev/id/chunk/f58f73d7-95e7-4d7a-8bb5-687eaf43cb31]
part_of: https://agentic-knowledge-base.dev/id/composite/bb329900-d369-44b7-88d4-5e3996dc0aa5
---
**함수** — `render(rows, inputs, vocab)` 다. 보고 전체 — 생성 문서 규약의 머리 블록 + 네 절이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(rows: list[dict], inputs: list[Path], vocab: Path) -> str:
    """보고 전체 — 생성 문서 규약의 머리 블록 + 네 절이다."""
    head = kb_lib.gendoc_header(
        "tokens", "청크 본문의 토큰 수 분포", "tools/tokens.py",
        f"청크 {len(rows)}개의 본문을 고정된 어휘 `{kb_lib.TOKENIZER_NAME}` 로 세면 분포와 42의 배수별 초과 수가 얼마인가",
        "bazel run //tools:tokens", [], f"청크 {len(rows)}개",
        kb_lib.gendoc_view_notice("각 청크의 본문") + " " + kb_lib.GENDOC_DETERMINISTIC_NOTE,
        input_kind="청크 파일", stamped=False,
        input_note=f"청크 디렉토리 {len(CHUNK_ROOTS)}개: "
                   f"{' · '.join('`' + d + '/`' for d in CHUNK_ROOTS)} 의 frontmatter 있는 `.md` 와 저작 접미"
                   f"({' · '.join('`' + s + '`' for s in TTL_CHUNK_SUFFIXES)})의 `.ttl` 전부 — 분모는 게이트가 "
                   f"판정하는 전 청크다 (2026-10-01 정정: `kb/ontology/` 의 TTL 청크가 빠져 있었다)",
        extra=[f"- 계수기: `{kb_lib.TOKENIZER_PACKAGE} {kb_lib.TOKENIZER_PACKAGE_VERSION}` · 어휘 "
               f"`{kb_lib.TOKENIZER_NAME}` · 어휘 지문 `sha256:{kb_lib.TOKENIZER_VOCAB_SHA256[:12]}` "
               f"(고정처는 `MODULE.bazel` 의 `http_file({kb_lib.TOKENIZER_VOCAB_REPO})`)",
               f"- 입력 지문: `{kb_lib.input_fingerprint(inputs)}`"])
    body = ["## plane 별 분포", "",
            f"단위는 토큰이다. 줄 수는 같은 본문에서 센 값이고 둘의 비가 줄당 토큰이다. `.ttl` 청크는 plane 이 "
            f"없어 `{kb_lib.NONE_MARK}` 행이고 기본 상한 {kb_lib.MAX_BODY_TOKENS} 를 받는다.", ""]
    body += plane_table(rows)
    body += ["## 42의 배수별 초과", "",
             f"상한을 42의 배수로 두면(유저 결정 2026-10-01) 그 값마다 초과 청크가 분할 대상이다. 분모는 청크 {len(rows)}개다.", ""]
    body += multiple_table(rows)
    body += ["## 컨텍스트 예산의 환산", "",
             f"42줄의 근거는 컨텍스트 예산의 1/5 이었다(d-0002). 그 근거를 토큰으로 옮긴 값이 확정 상한 "
             f"{kb_lib.MAX_BODY_TOKENS}(42×26)이고 예산은 {kb_lib.CONTEXT_TOKEN_BUDGET}(42×129)이다 "
             f"(p1-chunk-unit-is-tokens). 아래는 그 환산을 지금 입력에서 다시 잰 것이다.", ""]
    body += budget_lines(rows)
    body += [f"## 상위 {TOP_N} 청크", ""]
    body += top_table(rows)
    return kb_lib.gendoc_assemble(head, body, [], input_kind="청크 파일")
```
<!-- 인용 끝 -->
