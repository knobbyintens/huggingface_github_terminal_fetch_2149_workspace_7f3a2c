"""Batch inference pipeline for the Lattice-Exec-Reasoning corpus."""

import json
from pathlib import Path
from typing import Iterable, Iterator


def stream_rows(path: Path) -> Iterator[dict]:
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def filter_by_quality(rows: Iterable[dict], threshold: float = 0.5) -> Iterator[dict]:
    for row in rows:
        if float(row["quality_score"]) >= threshold:
            yield row


def batched(rows: Iterable[dict], size: int = 32) -> Iterator[list]:
    batch: list = []
    for row in rows:
        batch.append(row)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def main(source: str = "data/sample_rows.jsonl") -> None:
    path = Path(source)
    kept = list(filter_by_quality(stream_rows(path), threshold=0.4))
    for batch in batched(kept, size=16):
        print(json.dumps({"batch_size": len(batch), "first": batch[0]["blob_key"]}))


if __name__ == "__main__":
    main()
