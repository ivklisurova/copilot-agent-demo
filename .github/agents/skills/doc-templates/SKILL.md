---
name: doc-templates
description: Documentation templates for data models and pipelines. Use when writing or updating data engineering documentation.
---
# Documentation templates

Pick the template by task and copy its headings exactly:
- Table or model docs: templates/data-model.md, saved to docs/models/<name>.md
- Pipeline or job docs: templates/pipeline.md, saved to docs/pipelines/<name>.md

## Procedure
1. Read the matching template file before writing.
2. Check whether the target file already exists. If it does, edit it and keep
   its existing content. Never overwrite it.
3. Fill every section from the code, DDL or configs. Do not skip sections.
   Write "TBD: confirm with owner" for anything not found.
4. Cite the source file for each statement.

## Rules
- Never create README.md or index files inside docs/. The root README.md is the
  only README, and the agent updates its Documentation section.
- If the task fits neither template, say so and use a simple structure:
  Purpose, Inputs and outputs, Details, Source files.