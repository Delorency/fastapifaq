from dependency_injector import containers, providers

from .database import Database
from .config import Configs


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
        ]
    )

    cfg = providers.Singleton(Configs)
    db = providers.Singleton(Database, db_uri=cfg.dbcfg.database_uri)