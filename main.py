from fastapi import FastAPI

from dotenv import load_dotenv
from routes import account_routes

load_dotenv()

app = FastAPI(
    title='Vacancy Parser',
    version='1.0.0',
    openapi_prefix='/api'
)

app.include_router(account_routes.router, prefix='/account', tags=['Account'])
