---
license: cc-by-4.0
tags:
- code
- reasoning
- filtered
---

# reason-code-raw

We release the raw data for our processed reasoning corpus, adapted from the
original corpus produced by the Halcyon group.

The repository ships the filtered coding subset of the upstream reasoning
records together with its original artefact listing (see `files.json`).

## Record layout

Each line is one reasoning record with the following fields:

- `problem_statement`
- `io_spec`
- `reference_code`
- `source`
- `difficulty`

Some records carry empty IO specifications because their input/output payload
exceeded the extraction budget; they are kept for completeness.

*Note: the conversion pipeline is LLM-assisted, so a small number of problem
statements are under-specified.  We leave this for future work.*
