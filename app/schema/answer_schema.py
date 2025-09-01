from pydantic import BaseModel


class AnswerSchema(BaseModel):
    id:int
    text:str
    user_id:str


class GetAnswerRequest(BaseModel):
    id:int
    text:str 
    user_id:str