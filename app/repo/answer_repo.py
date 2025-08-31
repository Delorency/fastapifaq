from app.model import Answer
from .base import BaseRepo



class AnswerRepo(BaseRepo):
    def __init__(self, session):
        super().__init__(Answer, session)