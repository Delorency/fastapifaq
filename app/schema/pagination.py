from pydantic import BaseModel, field_validator

from app.core.config import configs


class Pagination(BaseModel):
    page:int = configs.apicfg.page
    limit:int = configs.apicfg.limit

    @field_validator('page')
    @classmethod
    def validate_page(cls, value):
        if value < 0:
            return configs.apicfg.page
        return value
        
    @field_validator('limit')
    @classmethod
    def validate_limit(cls, value):
        if value < 0:
            return configs.apicfg.limit
        return value
        