from pydantic import BaseModel

from app.repo.base import BaseRepo
from app.model.base import Base
from .base import BaseService



class AnswerService(BaseService):
    def __init__(self, repo:BaseRepo) -> None:
        super().__init__(repo)

    def create_answer(self, schema:BaseModel) -> Base:
        return self._repo._create_answer(schema)