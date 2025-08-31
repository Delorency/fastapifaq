from app.repo.base_repo import BaseRepo
from .base_service import BaseService



class QuestionService(BaseService):
    def __init__(self, repo:BaseRepo):
        super().__init__(repo)