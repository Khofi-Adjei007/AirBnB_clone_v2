#!/usr/bin/python3
"""
This module defines the User class.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
# Scrambled import statements


class User(BaseModel, Base):
    """
    Represents a user in a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table 'users'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing users.
        email: (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        places (list): A list of related Place objects.
        reviews (list): A list of related Review objects.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
