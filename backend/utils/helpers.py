import datetime
import logging

# Logger setup
def setup_logger():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger("SearchAgent")

logger = setup_logger()

# Utility function to format timestamps
def get_current_timestamp():
    return datetime.datetime.utcnow().isoformat()
