# fast-mcp-tools

To test using `mcp dev server.py` move mcp out of main:

```python
port=8000
mcp = FastMCP(
    "mcp-tools",
    debug=True,
    log_level="INFO",
    port=port,
)
```

```bash
podman build --no-cache -t quay.io/eformat/fast-mcp-tools:latest -f Containerfile
```
