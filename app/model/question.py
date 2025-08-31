from typing import List

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel



class Question(BaseModel):
    __tablename__= "question"
    text: Mapped[str] = mapped_column(Text)

    answers: Mapped[List["Answer"]] = relationship(back_populates="question")