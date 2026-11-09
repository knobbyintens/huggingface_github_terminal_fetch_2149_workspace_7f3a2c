# SQLBridge

Compatibility middleware for legacy SQL dialects.

## Headline component

The core SQL rewriter (`component_manifest.json` at the project root) is the
flagship component.

## Layers

- `modules/nql_compat` - compatibility layer that translates NQL 2.0 queries
  to SQLBridge's internal representation (beta)
