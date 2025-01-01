#!/usr/bin/python3
"""
This module defines the City class for SQLAlchemy, inheriting from Base
and linking to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that maps to the 'cities' table in the database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship with the State class
    state = relationship('State', back_populates='cities')
