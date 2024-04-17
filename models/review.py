#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = Column(String(1024), nullable=False)
    user_id = Column(String(60),
            ForeignKey("place.id", ondelete="CASCADE"),
            nullable=False)
    text = Column(String(60),
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False)
