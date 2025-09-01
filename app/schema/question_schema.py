from datetime import datetime

from pydantic import BaseModel, RootModel


class QuestionSchema(BaseModel):
    id:int
    text:str
    created_at:datetime



class GetQuestionsResponse(RootModel):
    root:list[QuestionSchema]