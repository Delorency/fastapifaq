from typing import Callable
from contextlib import AbstractContextManager, contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session


class Database:
    def __init__(self, db_uri: str) -> None:
        self._engine = create_engine(url=db_uri, echo=True)
        self._session_factory = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)
        self._scoped_session = scoped_session(self._session_factory)

    @contextmanager 
    def session(self):
        session: Session = self._scoped_session()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()