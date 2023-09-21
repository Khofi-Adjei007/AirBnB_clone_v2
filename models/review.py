#!/usr/bin/python3

"""
This module defines the Review class.
"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Represents a review in a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table 'reviews'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing Reviews.
        text (str): The description of the review.
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who created the review.
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
