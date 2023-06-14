#!/usr/bin/python3
"""
This module defines a class to manage file storage for the HBNB clone
"""

import json


class FileStorage:
    """This class manages storage of HBNB models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        return {
            k: v for k, v in self.__objects.items() if isinstance(v, cls)
        }

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes the storage dictionary to a JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                class_dict = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name in class_dict:
                        self.__objects[key] = class_dict[class_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
