from datetime import datetime

from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())