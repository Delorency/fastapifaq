from typing import Callable, List
from contextlib import AbstractContextManager
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.model import Question
from .base import BaseRepo



class QuestionRepo(BaseRepo):
    def __init__(self, session:Callable[...,AbstractContextManager[Session]]) -> None:
        super().__init__(Question, session)

    def _get_list(self) -> List[Question]:
        with self._session() as session:
            objs = session.query(self._model).order_by(desc(self._model.created_at)).all()

            # if objs is None:
            #     return
            
            return objs