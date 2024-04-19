#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews"
    __table_args__ = {'extend_existing': True}
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60),
            ForeignKey("places.id", ondelete="CASCADE"),
            nullable=False)
    user_id = Column(String(60),
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False)
