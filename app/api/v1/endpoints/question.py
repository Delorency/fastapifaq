from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core import Container
from app.schema import *


router = APIRouter(prefix='/question', tags=['Questions'])



@router.get("/", summary='Get list questions', response_model=GetQuestionsResponse, status_code=200)
@inject
async def get_questions(pag = Depends(Pagination), service=Depends(Provide[Container.question_service])):
    return service.get_list(pag)

@router.post("/", summary='Create question', status_code=201)
@inject
async def create_question(schema:CreateQuestionRequest, service=Depends(Provide[Container.question_service])):
    return service.create(schema)

@router.delete("/{id}", summary="Delete question by id", status_code=204)
@inject
async def delete_question(id:int, service=Depends(Provide[Container.question_service])):
    return service.delete(id)