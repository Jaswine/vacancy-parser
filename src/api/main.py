import logging

from fastapi import FastAPI
from src.api.routes import auth_routes, account_routes, collection_routes


logger = logging.getLogger(__name__)


app = FastAPI(
    title="Vacancy parser",
    version="1.0.0",
    root_path="/api",
)


@app.on_event("startup")
async def startup():
    logger.info("🚀 App starting...")


app.include_router(auth_routes.router)
app.include_router(account_routes.router)
app.include_router(collection_routes.router)
