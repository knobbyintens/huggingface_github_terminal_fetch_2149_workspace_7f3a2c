"""Validate that released rows match the documented schema."""

import json
import sys

EXPECTED = {
    "blob_key": str,
    "owner_repo": str,
    "file_path": str,
    "size_bytes": int,
    "quality_score": float,
    "rounded_score": int,
}


def validate(path: str) -> int:
    failures = 0
    with open(path, "r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if list(row.keys()) != list(EXPECTED.keys()):
                print(f"row {lineno}: unexpected fields {list(row.keys())}")
                failures += 1
                continue
            for key, typ in EXPECTED.items():
                if not isinstance(row[key], typ):
                    print(f"row {lineno}: {key} is not {typ.__name__}")
                    failures += 1
    return failures


if __name__ == "__main__":
    sys.exit(1 if validate(sys.argv[1]) else 0)
