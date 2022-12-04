#!/usr/bin/python3
"""
Module contains the SQLAlchemy ORM State model mapping
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class contains the table mapping for states in database
    """
    __table__ = "states"

    id = Column("id", Integer, primaryKey=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
