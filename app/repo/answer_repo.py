from typing import Callable
from pydantic import BaseModel
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.exceptions import DuplicatedError, BadRequestError
from app.model import Answer
from app.model.base import Base
from .base import BaseRepo



class AnswerRepo(BaseRepo):
    def __init__(self, que_repo:BaseRepo, session:Callable[...,AbstractContextManager[Session]]) -> None:
        super().__init__(Answer, session)
        self._que_repo = que_repo


    def _create_answer(self, schema:BaseModel) -> Base:
        if self._que_repo._get_by_id(schema.question_id): 
            with self._session() as session:
                query = self._model(**schema.model_dump(exclude_none=True))
                try:
                    session.add(query)
                    session.commit()
                    session.refresh(query)
                except IntegrityError as e:
                    raise DuplicatedError(str(e.orig))
                
                return query
            
        raise BadRequestError(f'Not found with id={schema.question_id}')