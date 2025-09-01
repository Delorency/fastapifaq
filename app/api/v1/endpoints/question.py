from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core import Container
from app.schema import GetQuestionsResponse, Pagination


router = APIRouter(prefix='/question', tags=['Questions'])



@router.get("/", summary='Get list questions', response_model=GetQuestionsResponse, status_code=200)
@inject
async def get_list(pag = Depends(Pagination), service=Depends(Provide[Container.question_service])):
    return service.get_list(pag)