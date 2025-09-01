from typing import Optional
from datetime import datetime
from pydantic import BaseModel, field_validator, Field

from app.core.exceptions import BadRequestError


class AnswerSchema(BaseModel):
    id:int
    text:str
    user_id:str
    created_at:datetime


class CreateAnswerRequest(BaseModel):
    text:str 
    user_id:str
    question_id: Optional[int] = Field(default=None, exclude=False)

    @field_validator('text')
    def validate_text(cls, value):
        if len(value) < 10:
            raise BadRequestError("The text must be at least 10 characters long")
        return value
    
    @field_validator('user_id')
    def validate_user_id(cls, value):
        if len(value) < 8:
            raise BadRequestError("User id must be at least 8 characters long")
        return value