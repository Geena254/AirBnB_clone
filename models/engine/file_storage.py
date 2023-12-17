#!/usr/bin/python3
"""The module for FileStorage class."""
import datetime
import json
import os


class FileStorage:
    """This serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """This serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            slzd_objs = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(slzd_objs, file, ensure_ascii=False)

    def reload(self):
        """
        This deserializes the JSON file to __objects
        Only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {l: self.classes()[w["__class__"]](**w)
                        for l, w in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def classes(self):
        """This returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        return classes

    def attributes(self):
        """This returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
                     }
        return attributes
