from dependency_injector import containers, providers

from .database import Database
from .config import configs
from app.repo import *
from app.service import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
        ]
    )
    # base
    db = providers.Singleton(Database, db_uri=configs.dbcfg.database_uri)

    # repo
    question_repo = providers.Factory(QuestionRepo, session=db.provided.session)
    answer_repo = providers.Factory(AnswerRepo, session=db.provided.session)

    # service
    question_service = providers.Factory(QuestionService, repo=question_repo)
    answer_service = providers.Factory(AnswerService, repo=answer_repo)
