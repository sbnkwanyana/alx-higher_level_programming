#!/usr/bin/python3
"""
Module contains the SQLAlchemy ORM model mapping
with Base and Cities model
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class contains the table mapping for cities in database
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("states.id"), nullable=False)
