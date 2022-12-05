#!/usr/bin/python3
"""
Module contains the SQLAlchemy ORM model mapping
with Base and State model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
"""
Base declarative documentation
"""


class State(Base):
    """
    State class contains the table mapping for states in database
    """
    __tablename__ = "states"

    id = Column(Integer, primaryKey=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
