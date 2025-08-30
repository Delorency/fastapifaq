from dependency_injector import containers, providers

from .database import Database
from .config import configs


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
        ]
    )

    db = providers.Singleton(Database, db_uri=configs.dbcfg.database_uri)