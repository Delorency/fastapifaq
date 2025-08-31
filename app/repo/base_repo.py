from app.model.base import BaseModel



class BaseRepo:
    def __init__(self, model:BaseModel, session):
        self._session = session
        self._model = model