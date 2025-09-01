from typing import Callable, List
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session, selectinload

from app.model import Question
from app.core.exceptions import NotFoundError
from .base import BaseRepo



class QuestionRepo(BaseRepo):
    def __init__(self, session:Callable[...,AbstractContextManager[Session]]) -> None:
        super().__init__(Question, session)

    def _get_by_id(self, id:int) -> List[Question]:
        with self._session() as session:
            obj = session.query(self._model).options(
                selectinload(self._model.answers)).filter(self._model.id==id).first()
            
            if obj is None:
                raise NotFoundError(f'Not found with id={id}')
            
            return obj
                