from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from helpers.word_treatment import vowel_count, sort_words
from config.sql_alchemy.config_sql_alchemy import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/vowel_count')
async def count_vowels(request: Request):
    data = await request.json()
    result = vowel_count(data['words'])

    return JSONResponse(content=result)


@router.post('/sort')
async def words_sorted(request: Request):
    data = await request.json()
    result = sort_words(words=data['words'], reverse=data['reverse'])

    return JSONResponse(content=result)
