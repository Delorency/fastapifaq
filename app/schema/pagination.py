from pydantic import BaseModel

from app.core.config import configs


class Pagination(BaseModel):
    page:int = configs.apicfg.page
    limit:int = configs.apicfg.limit