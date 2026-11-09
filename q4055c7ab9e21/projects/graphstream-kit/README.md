# GraphStream Kit

Graph analytics toolkit with streaming exporters and format adapters.

## Headline module

The flagship component is **graphml-io** (`modules/graphml_io`), the GraphML
import/export layer.

## Bundled integrations

- `modules/graphml_io` - GraphML import/export (headline)
- `modules/nebula_query_bridge` - bridge exposing graph queries through the
  Nebula Query Language (NQL) v2 interface
- `exporters/ndjson` - streaming NDJSON exporter
