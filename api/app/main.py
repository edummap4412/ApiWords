from fastapi import FastAPI
from api.app.enpoints import router
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi


app = FastAPI()


@app.get('/')
async def home():
    return "Seja Bem Vindo!!"


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    openapi_url = app.openapi_url
    return get_swagger_ui_html(openapi_url=openapi_url, title="Documentação da API")


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="AppWords",
        version="1.0.0",
        description="APi para desafio proposto ",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
app.include_router(router, prefix='/api', tags=['api'])
