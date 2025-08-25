# mcp_server.py
import os
import httpx
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("movies-api-mcp")

# Base URL for your FastAPI app
BASE_URL = os.getenv("MOVIE_API_URL", "http://localhost:8000/v1")


# Tools wrappes your routers


@mcp.tool()
def list_movies() -> List[Dict[str, Any]]:
    """
    List all movies (calls GET /v1/movies).
    """
    resp = httpx.get(f"{BASE_URL}/movies")
    resp.raise_for_status()
    return resp.json()

@mcp.tool()
def get_movie(movie_id: int) -> Dict[str, Any]:
    """
    Get details of a single movie by ID (calls GET /v1/movies/{id}).
    """
    resp = httpx.get(f"{BASE_URL}/movies/{movie_id}")
    if resp.status_code == 404:
        return {"error": f"Movie {movie_id} not found"}
    resp.raise_for_status()
    return resp.json()

@mcp.tool()
def create_movie(
    title: str,
    description: str,
    language: str,
    duration: float,
    rating: float
) -> Dict[str, Any]:
    """
    Create a new movie (calls POST /v1/movies).
    """
    payload = {
        "title": title,
        "description": description,
        "language": language,
        "duration": duration,
        "rating": rating,
    }
    resp = httpx.post(f"{BASE_URL}/movies", json=payload)
    resp.raise_for_status()
    return resp.json()


# Run stdio MCP server

if __name__ == "__main__":
    mcp.run() 





