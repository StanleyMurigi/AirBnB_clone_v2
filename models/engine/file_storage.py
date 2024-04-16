#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serialize the file path to Json"""

        param_dict = {}
        for key, value in self._objects.items():
            param_dict[key] = value.to_edit()
        with open(FileStorage.__file_path, 'w', encoding= "UTF-8") as f:
            json.dump(param_dict, f)

    def reload(self):
        """serialize the file path to JSON"""

        try:
            with open(self.__file_path, 'r', encoding= "UTF-8") as f:
                for key, val in (json.load(f)).items():
                        value = eval(value['__class__']](**value)
                        self._objects[key] = value
        except FileNotFoundError:
            pass
