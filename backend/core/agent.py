from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
from tavily import AsyncTavilyClient
import os

load_dotenv()

search_agent = Agent(
    "openai:gpt-4",
    result_type=str,
    system_prompt="Use the talivy_tool function to find the latest information"
)

@search_agent.tool
async def talivy_tool(ctx: RunContext, query: str):
    """Fetch the latest information from the internet."""
    tavily_client = AsyncTavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = await tavily_client.search(query, max_results=3)
    return response["results"]
