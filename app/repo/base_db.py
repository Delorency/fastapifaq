from sqlalchemy.orm import scoped_session



class BaseRepo:
    def __init__(self, model, sc_session:scoped_session):
        self._scoped_session = sc_session
        self._model = model