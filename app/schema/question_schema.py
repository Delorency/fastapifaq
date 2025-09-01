from datetime import datetime
from pydantic import BaseModel, RootModel, field_validator

from app.core.exceptions import BadRequestError


class QuestionSchema(BaseModel):
    id:int
    text:str
    created_at:datetime

class GetQuestionsResponse(RootModel):
    root:list[QuestionSchema]

class CreateQuestionRequest(BaseModel):
    text:str

    @field_validator('text')
    @classmethod
    def validate_text(cls, value):
        if len(value) < 10:
            raise BadRequestError("The text must be at least 10 characters long")
        return value