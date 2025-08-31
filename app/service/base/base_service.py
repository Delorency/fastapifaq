from app.repo.base import BaseRepo



class BaseService:
    def __init__(self, repo:BaseRepo) -> None:
        self._repo = repo