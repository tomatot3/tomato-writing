# Tomato Writing

[中文说明](README.zh-CN.md)

A self-contained skill for revising research arguments and prose without flattening technical meaning, evidence, or the author's voice.

The package currently contains **research-writing-editor**. Its short entrypoint selects among seven focused guides rather than loading a complete editing workflow for every sentence.

## What it helps with

- A motivation that describes the proposed task instead of establishing a research problem.
- Related work that lists studies, or becomes incomprehensible after excessive compression.
- Methods that read like implementation notes rather than a scientific explanation.
- Results dominated by numbers without a clear finding.
- Discussion that repeats procedures or argues with imagined reviewers.
- Unstable terminology, bilingual meaning drift, and revision/version mistakes.

It is intended for computational, empirical, theoretical, qualitative, and humanities research. Examples are synthetic. The package contains no manuscript, private research data, or project-specific results.

## Install in Codex

Copy the entire folder at [skills/research-writing-editor](skills/research-writing-editor/SKILL.md) into your Codex skills directory, preserving its references and agents subdirectories. The usual location is ~/.codex/skills/research-writing-editor. If you use a different CODEX_HOME, use its skills directory. Open a new Codex session if the new skill is not discovered in the current one.

Then invoke:

~~~text
Use $research-writing-editor to revise this Introduction for a first-time reader.
Preserve concrete explanations of prior methods and already-approved wording.
Explain material changes briefly.
~~~

Automatic invocation remains enabled by default. Existing writing skills can stay installed. This skill is a self-contained alternative for the requested edit; do not automatically chain every writing skill on the same passage. It can use document-formatting or source-retrieval tools when the actual task requires them, but those tools are not bundled or required for plain-text revision.

## Package structure

- [SKILL.md](skills/research-writing-editor/SKILL.md): task boundaries, routing, editing decisions, delivery.
- [Argument and literature](skills/research-writing-editor/references/argument-and-literature.md).
- [Section writing](skills/research-writing-editor/references/section-writing.md).
- [Evidence and claim strength](skills/research-writing-editor/references/evidence-and-claims.md).
- [Prose and terminology](skills/research-writing-editor/references/prose-and-terminology.md).
- [Bilingual revision](skills/research-writing-editor/references/bilingual-revision.md).
- [Revision integrity](skills/research-writing-editor/references/revision-integrity.md).
- [Worked examples](skills/research-writing-editor/references/worked-examples.md).

## Validation

~~~sh
python scripts/validate_package.py
~~~

This checks package structure, local links, UI metadata, and evaluation-case completeness. It does not measure prose quality or scientific validity.

Behavioural evaluation uses [synthetic cases](evaluation/cases.json) and a [review rubric](evaluation/README.md). Inspect the actual revised text. A valid package or a favourable model self-assessment is not evidence of successful writing.

## Scope

The skill edits the presentation of research. It does not invent evidence, run new experiments, replace statistical analysis, assume current journal rules, or authorize publication. It does not treat confidence intervals, passive voice, long sentences, or technical nouns as inherently undesirable.

Licensed under the [MIT License](LICENSE). Reuse and modification are permitted with the copyright and license notice retained.
