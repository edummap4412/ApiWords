from fastapi import FastAPI
from config.sql_alchemy import models
from config.sql_alchemy.config_sql_alchemy import engine
from app.router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def home():
    return "Welcome Home"


app.include_router(router, prefix='/api', tags=['api'])
