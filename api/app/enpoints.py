from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from api.helpers.word_treatment import vowel_count, sort_words, validate_words
from api.config.schemas import VowelCountRequest, SortRequest
router = APIRouter()


@router.post('/vowel_count')
async def count_vowels(request: Request, data: VowelCountRequest):
    data_words = data.words
    if request.headers.get('Content-Type') != 'application/json':
        raise HTTPException(status_code=415, detail="Content-Type deve ser application/json")

    validate_words(data_words)
    result = vowel_count(data_words)
    return JSONResponse(content=result)


@router.post('/sort')
async def words_sorted(request: Request, data: SortRequest):
    data_words = data.words
    if request.headers.get('Content-Type') != 'application/json':
        raise HTTPException(status_code=415, detail="Content-Type deve ser application/json")

    validate_words(data_words)
    order = data.order
    if order not in ('asc', 'desc'):
        return JSONResponse(content="Para alterar a ordem dos elementos digite asc ou desc")

    result = sort_words(words=data_words, order=order)
    return JSONResponse(content=result)
