from typing import Callable, List
from contextlib import AbstractContextManager
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel

from app.core.exceptions import DuplicatedError, NotFoundError, ServerSideError
from app.model.base import Base
from app.schema import Pagination



class BaseRepo:
    def __init__(self, model:Base, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model

    def _get_list(self, pag:Pagination) -> List[Base]:
        with self._session() as session:
            objs = session.query(self._model).order_by(desc(self._model.created_at)).offset((pag.page-1)*pag.limit).limit(pag.limit).all()
            
            return objs
        
    def _create(self, schema:BaseModel) -> None:
        with self._session() as session:
            query = self._model(**schema.model_dump(exclude_none=True))
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedError(str(e.orig))
            
    def _delete(self, id:int) -> None:
        with self._session() as session:
            obj = session.query(self._model).filter(self._model.id==id).first()

            if obj is None:
                raise NotFoundError(f'Not found with id={id}')
            
            try:
                session.delete(obj)
                session.commit()
            except:
                raise ServerSideError("Delete error")
