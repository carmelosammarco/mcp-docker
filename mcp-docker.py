import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Demo",
    host="0.0.0.0",  # only used for SSE transport
    port=8050,  # only used for SSE transport (set this to any port)
)


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")  # or SSE protocol