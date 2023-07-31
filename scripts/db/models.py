from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config import Base


class result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    items = relationship("Result", back_populates="owner")


class Result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    error_category = models.PositiveSmallIntegerField(
       choices=[],
   )


class ErrorCategory(Base):
    STATUS = ('high','medium','low')

    status = models.PositiveSmallIntegerField(
      choices=STATUS,
      default=1,
   )