#!/usr/bi/python3
"""This is the script for the base model of the AirBnB clone."""

import uuid
from datetime import datetime


class BaseModel:
    """This is the base class from which all other classes will inherit."""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the official string representation"""

        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """This returns a dictionary containing all keys/values of __dict__"""

        own_dict = self.__dict__.copy()
        own_dict["__class__"] = self.__class__.__name__
        own_dict["created_at"] = own_dict["created_at"].isoformat()
        own_dict["updated_at"] = own_dict["updated_at"].isoformat()
        return own_dict
