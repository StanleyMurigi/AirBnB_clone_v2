#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialize State """
        super().__init__(*args, **kwargs)

        if storage.__class__.__name__ == 'DBStorage':
            self.setup_db_storage()
        elif storage.__class__.__name__ == 'FileStorage':
            self.setup_file_storage()

    def setup_db_storage(self):
        """Setup for DBStorage"""
        self.cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def setup_file_storage(self):
        """Setup for FileStorage"""
        pass  # You can implement this if needed

