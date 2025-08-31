from .base_repo import BaseRepo

from app.model.answer import Answer


class AnswerRepo(BaseRepo):
    def __init__(self, session):
        super().__init__(Answer, session)