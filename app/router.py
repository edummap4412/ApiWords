from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from helpers.word_treatment import vowel_count, sort_words

router = APIRouter()


@router.post('/vowel_count')
async def count_vowels(request: Request):
    data = await request.json()
    words = data['words']

    result = vowel_count(words)

    return JSONResponse(content=result)


@router.post('/sort')
async def words_sorted(request: Request):
    data = await request.json()
    order = data['order']

    if order not in ('asc', 'desc'):
        return JSONResponse(content="Para alterar a ordem dos elementos digite asc ou desc")
    return sort_words(words=data['words'], order=order)



