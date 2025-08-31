from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.model.base import BaseModel



class BaseRepo:
    def __init__(self, model:BaseModel, session:Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session
        self._model = model