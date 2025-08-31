from app.repo.base import BaseRepo
from .base import BaseService



class QuestionService(BaseService):
    def __init__(self, repo:BaseRepo) -> None:
        super().__init__(repo)

    def get_list(self):
        return self._repo._get_list()