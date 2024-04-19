#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize the file path to Json"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            my_dict[key]["__class__"] = value.__class__.__name__
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the file path to JSON"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    if "__class__" in value: # checks if '__class__ attribute exists
                        class_name = value["__class__"]
                        cls = getattr(models, class_name)
                        obj = cls(**value)
                        self.__objects[key] = obj
                    else:
                        print(f"Error: Missing '__class__' attribute for object with key '{key}'")
        except FileNotFoundError:
            print("Error: JSON file not found")
        except json.decoder.JSONDecodeError:
            print("Error: Invalid JSON data in the file")

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
