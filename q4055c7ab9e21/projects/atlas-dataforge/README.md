# Atlas DataForge

Atlas DataForge is an open-source toolkit for analytics engineering teams.
It bundles parsers, connectors and transformation helpers that plug into modern
data platforms through a shared component manifest format.

## Headline module

The flagship component is **parquet-bridge** (`modules/parquet_bridge`), a
high-throughput Parquet reader and writer. Most of the project's adoption comes
from that module.

## Module tree

| Module | Path | Notes |
|---|---|---|
| parquet-bridge | modules/parquet_bridge | Parquet reader and writer (headline) |
| kafka-loader | modules/kafka_loader | Kafka ingestion sink |
| nql-adapter | modules/nql_adapter | Adapter for the Nebula Query Language (NQL) v2 engine |
| json-flatten | modules/json_flatten | Nested JSON flattening transforms |

Each module ships its own component_manifest.json so that platform teams can
vendor only the pieces they need. Component metrics are per module; they are
not reported at the project level.

## License

Repository code is Apache-2.0 unless a module states otherwise.
