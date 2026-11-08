# Lattice-DataSync

**Lattice-Exec-Reasoning-Raw** and **Lattice-Exec-Reasoning** are a released
corpus pair for executable reasoning research.

We release the raw data for our processed Lattice-Exec-Reasoning corpus.
The rows were adapted from an earlier public corpus; the upstream archive
cited by the release card is:

`seg_091244_filt_v3_q27.coded.jsonl`

The processed sibling is produced by `src/batched_inference.py`.

## Row schema

`data/sample_rows.jsonl` contains 50 sample rows with the following columns:

| column | type |
| --- | --- |
| `blob_key` | string |
| `owner_repo` | string |
| `file_path` | string |
| `size_bytes` | int64 |
| `quality_score` | float64 |
| `rounded_score` | int64 |

## Licence

The licence of the upstream archive must be recorded before this release can
be distributed.  See the repository's provenance record once it has been
filed.
