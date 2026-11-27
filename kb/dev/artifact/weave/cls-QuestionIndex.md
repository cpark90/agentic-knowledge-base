---
id: https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721
type: artifact
level: executable
title_ko: 클래스 QuestionIndex (tools/weave.py)
title: class QuestionIndex in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0b1ee795-6889-4c66-86b1-2a77ac3ee4d6, https://agentic-knowledge-base.dev/id/chunk/4787cbe7-b43d-4db2-b609-c25540fe1afc, https://agentic-knowledge-base.dev/id/chunk/8f15c2bb-62bb-4e9f-98dc-e86d7e0436b2]
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**클래스** — `class QuestionIndex` 다. 질문지 · 옛 질문지 · 본문 인용 · 유저 결정 증거를 질문 번호와 옛 질문지 파일 이름으로 모은다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
class QuestionIndex:
    """질문지 · 옛 질문지 · 본문 인용 · 유저 결정 증거를 질문 번호와 옛 질문지 파일 이름으로 모은다 — 네 절이 같은 색인을 읽는다."""

    def __init__(self, sheet_paths: list[str], legacy_paths: list[str], citing: list, evidence: list):
        self.questions: dict = {}  # 번호 → 질문지 · 열림 여부 · created · 제목 · 답
        self.sheets: dict = {}     # 질문지 → 열림 여부
        self.dups: list = []       # (번호, 앞 질문지, 뒤 질문지) — 번호는 질문지 사이에서 겹치지 않아야 한다
        for p in sorted(sheet_paths, key=lambda p: SHEET_FILE.search(p).group(2)):
            sm = SHEET_FILE.search(p)
            meta, qs = read_sheet(p)
            self.sheets[sm.group(2)] = not sm.group(1)
            for q in qs:
                if q["n"] in self.questions:
                    self.dups.append((q["n"], self.questions[q["n"]]["sheet"], sm.group(2)))
                    continue
                self.questions[q["n"]] = dict(q, sheet=sm.group(2), created=meta.get("created") or kb_lib.NONE_MARK)
        self.legacy: dict = {}
        for p in sorted(legacy_paths):
            text = Path(p).read_text(encoding="utf-8")
            title = next((ln[2:].strip() for ln in text.splitlines() if ln.startswith("# ")), "")
            self.legacy[LEGACY_FILE.search(p).group(1)] = {"title": title, "status": front_fields(text).get("status", "")}
        self.cites: dict = defaultdict(lambda: defaultdict(set))  # 번호 → 무리 → 표기
        self.legacy_cites: dict = defaultdict(set)                # 옛 질문지 → 인용한 파일 경로
        self.unresolved: list = []                                # (인용, 인용처, 사유)
        self.bare: Counter = Counter()                            # 답 문자 없는 꼴의 번호 → 곳 수
        for rel, kind, body in citing:
            self._scan(rel, kind, body)
        self.evidence: dict = defaultdict(list)  # 번호 또는 옛 질문지 이름 → 증거 자리
        for ref, where in evidence:
            self._evidence(ref, where)

    def _scan(self, rel: str, kind: str, body: str) -> None:
        group, ref = citing_ref(rel, kind)
        found: set = set()
        for sheet, n in ((f"Q-{a}", int(b)) for a, b in CITE_LONG.findall(body)):
            if self.questions.get(n, {}).get("sheet") == sheet:
                found.add(n)
            else:
                self.unresolved.append((f"{sheet}#Q{n}", rel, "질문지에 이 번호가 없다" if sheet in self.sheets else "질문지가 없다"))
        for hit in CITE_SHORT.finditer(body):
            n = int(hit.group(1))
            if n in self.questions:
                found.add(n)
            else:
                self.unresolved.append((hit.group(0), rel, "질문지에 없는 번호다"))
        for n in found:
            self.cites[n][group].add(ref)
        self.bare.update(map(int, CITE_BARE.findall(CITE_SHORT.sub(" ", CITE_LONG.sub(" ", body)))))
        for name in CITE_LEGACY.findall(body):
            if name in self.legacy:
                self.legacy_cites[name].add(rel)
            else:
                self.unresolved.append((f"legacy/{name}", rel, "옛 질문지에 없는 파일이다"))

    def _evidence(self, ref: str, where: str) -> None:
        m = re.fullmatch(r"(Q-\d{4})#Q(\d+)", ref)
        if m and self.questions.get(int(m.group(2)), {}).get("sheet") == m.group(1):
            self.evidence[int(m.group(2))].append(where)
        elif ref.startswith("legacy/") and ref[len("legacy/"):] in self.legacy:
            self.evidence[ref[len("legacy/"):]].append(where)
        else:
            self.unresolved.append((ref, f"유저 결정 증거 {where}", "질문지나 옛 질문지로 풀리지 않는다"))

    def cited(self) -> list[int]:
        return sorted(n for n, groups in self.cites.items() if any(groups.values()))

    def reversals(self) -> list[tuple[str, list[int]]]:
        """같은 결정을 인용한 질문이 둘 이상인 결정 → 질문 번호를 질문지 created 순(같은 날은 번호 순)으로 (orchestrator 판정, task 0374)."""
        by_decision: dict = defaultdict(set)
        for n, groups in self.cites.items():
            for d in groups.get("decision", ()):
                by_decision[d].add(n)
        return [(d, sorted(ns, key=lambda n: (self.questions[n]["created"], n))) for d, ns in sorted(by_decision.items()) if len(ns) >= 2]
```
<!-- 인용 끝 -->
