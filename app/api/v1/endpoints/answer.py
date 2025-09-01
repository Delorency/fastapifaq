from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core import Container
from app.schema import GetAnswerRequest



router = APIRouter(prefix='/answer', tags=['Answer'])


@router.get("/{id}", summary="Get answer by id", response_model=GetAnswerRequest, status_code=200)
@inject 
def get_answer(id:int, service = Depends(Provide[Container.answer_service])):
    return service.get_by_id(id)


@router.delete("/{id}", summary="Delete answer by id", status_code=204)
@inject 
def get_answer(id:int, service = Depends(Provide[Container.answer_service])):
    return service.delete(id)