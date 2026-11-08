---
license: other
tags:
- code
- multi-language
- large
---

# megacode-corpus

The largest code corpus in this registry, aggregating permissively licensed
source files from public repositories across more than twenty languages.

The corpus is distributed as per-language directories (for example
`python/`, `javascript/`, `rust/`).  There is no single flat archive: each
language directory contains monthly parquet shards named
`train-000XX-of-000NN.parquet`.

Licensing is a mixture of permissive licences that cannot be represented by a
single standard identifier, hence the generic `other` licence tag.
