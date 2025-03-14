from fastapi import FastAPI
from backend.api.search import generate_response
from backend.api.health import health_check
from backend.api.info import get_info

import uvicorn

app = FastAPI(title="Search Agent Service", description="A REST API for Search Agent as a Service", version="1.0")

app.add_api_route("/", health_check, methods=["GET"])
app.add_api_route("/search", generate_response, methods=["POST"])
app.add_api_route("/info", get_info, methods=["GET"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
