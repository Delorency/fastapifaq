from app.model import Question
from .base import BaseRepo


class QuestionRepo(BaseRepo):
    def __init__(self, session):
        super().__init__(Question, session)