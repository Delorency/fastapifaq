from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.model import Answer
from .base import BaseRepo



class AnswerRepo(BaseRepo):
    def __init__(self, session:Callable[...,AbstractContextManager[Session]]) -> None:
        super().__init__(Answer, session)