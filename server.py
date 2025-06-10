from mcp.server.fastmcp import FastMCP
import click
import httpx
import base64
import sys

@click.command()
@click.option("--port", default=8085, help="Port to listen", type=int)
def main(port: int):
    mcp = FastMCP(
        "mcp-tools",
        debug=True,
        log_level="INFO",
        port=port,
        host="0.0.0.0",
    )

    @mcp.tool()
    def decode_content(content: str):
        """
        Decode base64 content.

        :param content: The base64 content to decode
        :returns: The decoded content
        """
        try:
            # Try to decode as base64 first
            decoded = base64.b64decode(content).decode('utf-8')
            return decoded
        except Exception:
            # If decoding fails, return original content
            return content

    mcp.run(transport='sse')
    return 0

if __name__ == "__main__":
    sys.exit(main())
