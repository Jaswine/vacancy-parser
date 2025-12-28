import logging

from fastapi import FastAPI
from src.api.routes import auth_routes


logger = logging.getLogger(__name__)


app = FastAPI(title="Vacancy parser", version="1.0.0")


@app.on_event("startup")
async def startup():
    logger.info("🚀 App starting... DB engine initialized")


app.include_router(auth_routes.router)
