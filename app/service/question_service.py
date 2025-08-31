from .base_service import BaseService



class QuestionService(BaseService):
    def __init__(self, repo):
        super().__init__(repo)