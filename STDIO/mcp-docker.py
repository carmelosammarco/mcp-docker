from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DEMO")


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")  # or SSE protocol