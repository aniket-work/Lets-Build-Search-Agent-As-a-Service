from fastapi import APIRouter
import logging

# Initialize Logger
logger = logging.getLogger("InfoAPI")
logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/info")
def get_info():
    """Returns API service information."""
    logger.info("Info request received")

    try:
        info = {
            "service": "Search Agent Service",
            "version": "1.0",
            "features": ["AI-powered search", "Real-time information retrieval"],
            "upcoming_features": ["Advanced AI filtering", "User preferences support"]
        }
        logger.info("Info request processed successfully")
        return info
    except Exception as e:
        logger.error(f"Failed to retrieve info: {str(e)}")
        return {"error": "Unable to fetch service information"}
