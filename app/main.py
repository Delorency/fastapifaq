from fastapi import FastAPI 
from starlette.middleware.cors import CORSMiddleware

from app.core import Container
from app.core.config import configs
from app.api import v1_router



class AppIni:
    def __init__(self):
        self.app = FastAPI(
            title=configs.projectcfg.project_name,
        )

        self.container = Container()

        # db
        self.database = self.container.database()

        # routers / mounts
        self.app.include_router(v1_router)


app = AppIni().app