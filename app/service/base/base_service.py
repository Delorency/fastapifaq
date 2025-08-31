from app.repo.base import BaseRepo



class BaseService:
    def __init__(self, repo:BaseRepo):
        self._repo = repo