from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from helpers.word_treatment import vowel_count, sort_words

router = APIRouter()


@router.post('/vowel_count')
async def count_vowels(request: Request):
    if request.headers.get('Content-Type') != 'application/json':
        raise HTTPException(status_code=415, detail="Content-Type deve ser application/json")

    data = await request.json()

    words = data['words']
    result = vowel_count(words)
    return JSONResponse(content=result)


@router.post('/sort')
async def words_sorted(request: Request):
    if request.headers.get('Content-Type') != 'application/json':
        raise HTTPException(status_code=415, detail="Content-Type deve ser application/json")

    data = await request.json()
    order = data['order']
    if order not in ('asc', 'desc'):
        return JSONResponse(content="Para alterar a ordem dos elementos digite asc ou desc")
    return sort_words(words=data['words'], order=order)
