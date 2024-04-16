#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    # For DBStorage
    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    
    # For FileStorage
    if storage_type == 'fs':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            from models import storage
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

