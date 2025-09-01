from app.repo.base import BaseRepo

from app.schema import Pagination


class BaseService:
    def __init__(self, repo:BaseRepo) -> None:
        self._repo = repo

    def get_list(self, pag:Pagination):
        return self._repo._get_list(pag)