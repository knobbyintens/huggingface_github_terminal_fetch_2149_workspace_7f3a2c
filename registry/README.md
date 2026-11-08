# Public dataset registry snapshot

Read-only metadata snapshot of the public corpus registry used by the QLab
provenance team.

Every dataset is stored under `datasets/<owner>/<dataset>/` and contains:

- `card.json` -- machine-readable metadata (licence, tags, downloads, configurations and their column schemas)
- `files.json` -- the artefact listing (`rfilename` entries published by the registry)
- `README.md` -- the human-readable dataset card

Licences are declared per dataset in `card.json` under the `license` key.
