---
id: https://agentic-knowledge-base.dev/id/chunk/af38a092-1ea7-41f2-a032-e31c6ff0168d
type: decision
level: concrete
title_ko: 저장은 kb/{ontology,odd,dev,vv}이고 vv만 dev를 참조하며 각 디렉터리의 index.md가 라벨 목록이다
title: Storage is kb/{ontology,odd,dev,vv}; only vv references dev; each directory index.md is the label list
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
composite: {id: https://agentic-knowledge-base.dev/id/composite/6d696b3f-6d63-476e-bb56-65f27d8d2ed5, title_ko: 저장 구조, title: Storage layout}
part_of: https://agentic-knowledge-base.dev/id/composite/6d696b3f-6d63-476e-bb56-65f27d8d2ed5
---
**결론** — 저장 구조 (노트 부록 E.7):

```
kb/
├── kb/ontology/    Turtle. related/condition → kb/odd/taxonomy.yml 생성
├── kb/odd/         OpenODD YAML
├── dev/         OKF 번들 — requirement/ decision/ contract/ schema/ artifact/ + *.space.md
└── vv/          OKF 번들 — goal/ scenario/ criteria/ case/ verifier/ + domain.osc
```

`vv/`만 `dev/`를 참조한다. 각 디렉터리의 `index.md`가 라벨 목록이다. 이 저장소: `kb/dev`·`kb/vv`는 있고(같은 저장소 별도 패키지, 유저 결정 2026-09-10), `ontology/`·`odd/`의 `kb/` 이동은 완료(2026-09-10, 순서 (b)), `index.md`는 생성물로만 (Q4).
