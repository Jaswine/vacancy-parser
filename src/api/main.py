from fastapi import FastAPI
from src.api.routes import account_routes
from src.core.utils.logger import logger

app = FastAPI(
    title='Vacancy parser',
    version='1.0.0'
)

@app.on_event("startup")
async def startup():
    logger.info("🚀 App starting... DB engine initialized")


app.include_router(account_routes.router, prefix='/accounts', tags=['Accounts'])