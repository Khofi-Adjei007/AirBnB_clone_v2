#!/usr/bin/python3
"""
This module defines the State class.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):

    """
    Represents a state in a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table 'states'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing States.
        name (str): The name of the State.
        cities (list): A list of related City objects.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
