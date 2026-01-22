import logging

from fastapi import FastAPI

from api.config import api_settings
from api.exceptions.handlers import register_exception_handlers
from core.configs.config import settings as core_settings
from src.api.routes import (auth_routes, account_routes, collection_routes,
                            link_routes, collection_job_routes)

# Logging
def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=getattr(logging, core_settings.LOG_LEVEL.upper()),
    )
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)

def create_app() -> FastAPI:
    setup_logging()
    logger = logging.getLogger("whatsapp_api")
    logger.info("🚀 Starting WhatsApp API...")

    # Creating a FastAPI application
    app = FastAPI(
        title=api_settings.NAME,
        version=api_settings.VERSION,
        root_path=api_settings.ROOT_PATH,
    )

    # Registers global error handlers
    register_exception_handlers(app)

    # Adding routers
    app.include_router(auth_routes.router)
    app.include_router(account_routes.router)
    app.include_router(collection_routes.router)
    app.include_router(link_routes.router)
    app.include_router(collection_job_routes.router)

    return app


app = create_app()
