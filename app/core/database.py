from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Database:
    def __init__(self, db_uri: str) -> None:
        self._engine = create_engine(url=db_uri, echo=True)
        self._session_factory = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)
        self.session = scoped_session(self._session_factory)
