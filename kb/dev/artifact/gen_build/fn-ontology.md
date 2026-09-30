---
id: https://agentic-knowledge-base.dev/id/chunk/9cf3ed9e-81a6-4add-97ba-b933477041ad
type: artifact
level: executable
title_ko: 함수 ontology (tools/gen_build.py)
title: function ontology in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `ontology(root)` 다. 모듈 디렉토리 → BUILD, project-ontology.ttl 의 owl:imports → modules.bzl

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def ontology(root: Path):
    """모듈 디렉토리 → BUILD, project-ontology.ttl 의 owl:imports → modules.bzl"""
    text = (root / "kb/ontology/project-ontology.ttl").read_text(encoding="utf-8")
    imports = re.findall(r"<" + re.escape(ONTO_BASE) + r"([\w/-]+)>", text)
    imports = [i for i in imports if i != "project" and not i.startswith("project/")]
    outputs = {}
    mod_dirs = sorted(p for p in root.glob("kb/ontology/*/*") if p.is_dir() and list(p.glob("*.ttl")))
    for d in mod_dirs:
        rel = d.relative_to(root / "kb/ontology").as_posix()
        outputs[str(d / "BUILD.bazel")] = (HEADER.replace("각 청크의 frontmatter", "모듈 디렉토리의 온톨로지 TTL")
                                           + 'load("//defs:kb.bzl", "kb_ontology_module")\n\n'
                                           'package(default_visibility = ["//visibility:public"])\n\n'
                                           f'# 모듈 = 디렉토리, 청크 = 파일 (2.3절). IRI {ONTO_BASE}{rel}\n'
                                           f"kb_ontology_module(\n    name = {q(d.name)},\n    srcs = glob([\"*.ttl\"]),\n    iri = {q(ONTO_BASE + rel)},\n)\n")
    labels = [f"//kb/ontology/{i}" for i in imports]
    outputs[str(root / "kb/ontology/modules.bzl")] = (HEADER.replace("각 청크의 frontmatter", "project-ontology.ttl 의 owl:imports")
                                                      + '"""project-ontology.ttl 이 가져오는 모듈 — owl:imports 에서 생성."""\n\nPROJECT_IMPORTS = [\n'
                                                      + "".join(f"    {q(l)},\n" for l in sorted(labels)) + "]\n")
    return outputs
```
<!-- 인용 끝 -->
