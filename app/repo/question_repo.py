from typing import Callable
from contextlib import AbstractContextManager
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.model import Question
from .base import BaseRepo



class QuestionRepo(BaseRepo):
    def __init__(self, session:Callable[...,AbstractContextManager[Session]]) -> None:
        super().__init__(Question, session)