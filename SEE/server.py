from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="MCP Server SSE",
    # host="0.0.0.0",  # only used for SSE transport in localhost
    port=8050,  # only used for SSE transport (set this to any port=exposed port in Dockerfile)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Run the server
if __name__ == "__main__":
    print("Running server with SSE transport")
    mcp.run(transport="sse")