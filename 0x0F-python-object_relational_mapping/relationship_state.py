#!/usr/bin/python3
# relationship_state.py
from sqlalchemy import Column, Integer, String
from base import Base
from relationship_city import City

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
