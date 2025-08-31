from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject



router = APIRouter(prefix='/answer', tags=['Answer'])