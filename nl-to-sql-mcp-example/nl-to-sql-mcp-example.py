from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("nl-to-sql-mcp-example")

@mcp.tool()
async def get_player_data(query: str) -> str:
    """Get player data.

    Args:
        query: a natural requests asking for specific player data.
    """
    
    return "to be implemented"