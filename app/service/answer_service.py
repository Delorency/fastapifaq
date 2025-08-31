from .base_service import BaseService



class AnswerService(BaseService):
    def __init__(self, repo):
        super().__init__(repo)