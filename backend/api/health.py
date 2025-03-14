from fastapi import APIRouter
import logging

# Initialize Logger
logger = logging.getLogger("HealthCheck")
logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/health")
def health_check():
    """Health check endpoint."""
    logger.info("Health check request received")

    try:
        status = {"status": "healthy", "message": "Service is running!"}
        logger.info("Health check passed")
        return status
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy", "message": "Service is down"}
