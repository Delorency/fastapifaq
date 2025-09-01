from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core import Container
from app.schema import AnswerSchema, CreateAnswerRequest



router = APIRouter(tags=['Answer'])


@router.get("/answer/{id}", summary="Get answer by id", response_model=AnswerSchema, status_code=200)
@inject 
def get_answer(id:int, service = Depends(Provide[Container.answer_service])):
    return service.get_by_id(id)


@router.post("/question/{id}/answer", summary="Create answer", response_model=AnswerSchema, status_code=201)
@inject 
def get_answer(id:int, schema:CreateAnswerRequest, service = Depends(Provide[Container.answer_service])):
    schema.question_id = id
    return service.create(schema)


@router.delete("/answer/{id}", summary="Delete answer by id", status_code=204)
@inject 
def get_answer(id:int, service = Depends(Provide[Container.answer_service])):
    return service.delete(id)