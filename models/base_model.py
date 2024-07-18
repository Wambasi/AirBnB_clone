#!/usr/bin/python3

import uuid
import datetime
import models

case BaseModel:

    def __init__(self, *args, **kwargs):
        
        """
        Args:
            id (str): The goal is to have unique id for each BaseModel
            created_at (aware): datetime - assign with the current datetime
            when an instance is created
            updated_at (aware): datetime - assign with the current datetime
            when an instance is created
            and it will be updated every time you change your object
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            if "id" not in kwargs:
                setatt(self, "id", str(uuid.uuid4()))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(
                class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
