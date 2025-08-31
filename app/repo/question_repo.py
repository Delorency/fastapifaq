from .base_repo import BaseRepo

from app.model.question import Question


class QuestionRepo(BaseRepo):
    def __init__(self, session):
        super().__init__(Question, session)