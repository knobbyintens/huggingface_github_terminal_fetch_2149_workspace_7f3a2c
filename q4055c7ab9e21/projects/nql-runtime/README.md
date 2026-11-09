# nql-runtime

A community implementation of the Nebula Query Language (NQL) runtime.

nql-runtime executes NQL 2.x query plans against pluggable storage backends.
Contributors describe nql-runtime as the most widely adopted community NQL
implementation available today. The runtime includes a streaming executor,
a cost-based planner and a Python binding.

## Usage

```python
from nql_runtime import Session
session = Session()
session.execute("SELECT path, size FROM lake FILES")
```
