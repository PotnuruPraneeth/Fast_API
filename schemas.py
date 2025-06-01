"""This module will have database models
"""
from sqlalchemy import Column, Integer, String, Float
from database_conn import Base
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker


class Movie(Base):
    __tablename__="Movies"
    id :Mapped[int] =mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255), nullable=False)
    description:Mapped[str]=mapped_column(String(1000))
    language:Mapped[str]=Column(String(50))
    duration:Mapped[Float]=Column(Float)
    rating:Mapped[Float]=Column(Float)

