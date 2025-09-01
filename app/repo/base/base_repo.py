from typing import Callable, List
from contextlib import AbstractContextManager
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.model.base import BaseModel
from app.schema import Pagination



class BaseRepo:
    def __init__(self, model:BaseModel, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model


    def _get_list(self, pag:Pagination) -> List[BaseModel]:
        with self._session() as session:
            objs = session.query(self._model).order_by(desc(self._model.created_at)).offset((pag.page-1)*pag.limit).limit(pag.limit).all()
            
            return objs