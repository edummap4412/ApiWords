from fastapi import FastAPI
from app.router import router


app = FastAPI()


@app.get('/')
async def home():
    return "Welcome Home"


app.include_router(router, prefix='/api', tags=['api'])
