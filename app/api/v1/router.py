from fastapi import APIRouter
from .endpoints import que_router
from .endpoints import ans_router



router = APIRouter()

routers = [
    que_router,
    ans_router
]

for rou in routers:
    router.include_router(rou) 