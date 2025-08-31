from sqlalchemy import Text, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Answer(BaseModel):
    __tablename__= "answer"
    text: Mapped[str] = mapped_column(Text)
    
    user_id: Mapped[str] = mapped_column(String(128))

    question_id: Mapped[int] = mapped_column(ForeignKey('question.id', ondelete="CASCADE"))
    question: Mapped["Question"] = relationship(back_populates="answers")