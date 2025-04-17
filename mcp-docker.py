import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-docker")


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport='stdio')