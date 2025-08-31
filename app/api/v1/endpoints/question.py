from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.core import Container


router = APIRouter(prefix='/question', tags=['Questions'])



@router.get("/", summary='Get list questions', status_code=200)
@inject
async def get_list(service=Depends(Provide[Container.question_service])):
    return service.get_list()