"""This module will have database models
"""
from sqlalchemy import Column, Integer, String, Float
from database_conn import Base
from sqlalchemy.orm import Mapped,mapped_column,sessionmaker
''' | Module           | Description                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sqlalchemy`     | The **core SQLAlchemy module**. It includes low-level SQL building blocks like `Column`, `Integer`, `String`, `create_engine`, etc.                                                                                      |
| `sqlalchemy.orm` | The **ORM (Object-Relational Mapping) module**. It provides high-level tools like `DeclarativeBase`, `mapped_column`, `Mapped`, `Session`, etc., used for defining models and interacting with DBs using Python classes. |
'''

class Movie(Base):
    __tablename__="Movies"
    id :Mapped[int] =mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255), nullable=False)
    description:Mapped[str]=mapped_column(String(1000))
    language:Mapped[str]=Column(String(50))
    duration:Mapped[Float]=Column(Float)
    rating:Mapped[Float]=Column(Float)

