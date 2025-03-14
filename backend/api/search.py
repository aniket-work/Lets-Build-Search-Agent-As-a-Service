from fastapi import APIRouter
from backend.core.agent import search_agent
from pydantic import BaseModel
import logging

# Initialize Logger
logger = logging.getLogger("SearchAPI")
logging.basicConfig(level=logging.INFO)

router = APIRouter()


class Body(BaseModel):
    text: str


@router.post("/search")
async def generate_response(body: Body):
    """Handles search queries via the Search Agent."""
    logger.info(f"Received search request: {body.text}")

    try:
        result = await search_agent.run(body.text)
        logger.info("Search query processed successfully")
        return {"response": result}
    except Exception as e:
        logger.error(f"Search query failed: {str(e)}")
        return {"error": "Search failed. Please try again later."}
