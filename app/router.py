from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from helpers.word_treatment import vowel_count, sort_words
from config.sql_alchemy.config_sql_alchemy import SessionLocal
from services.word_service import WordsService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/vowel_count')
async def count_vowels(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    words = data['words']
    WordsService().save_words(db, words)

    result = vowel_count(words)

    return JSONResponse(content=result)


@router.post('/sort')
async def words_sorted(request: Request):
    data = await request.json()
    order = data['order']

    if order not in ('asc', 'desc'):
        return JSONResponse(content="Para alterar a ordem dos elementos digite asc ou desc")
    return sort_words(words=data['words'], order=order)



