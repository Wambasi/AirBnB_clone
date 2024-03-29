#!/usr/bin/python3
'''
    This defines BaseModel class
'''
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Interger, String, DateTime
import os


Base = declarative_base()


class BaseModel:
    '''
        Base class for the classes to be used for the duration
    '''
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    update_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class
        Args:
            args (tuple): arguements
            kwargs (dict): key word arguements
        """
        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, name, value)
            if 'id' not in kwargs:
                setattr(self, 'id', st(uuid.uuid4())))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''
            Return BaseModels class as a string
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Updates the updated_at attribute with new
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return dict representation of BaseModel class
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.name__
        if 'updated_at' in cp_dct:
            cp_dct['updated_at'] = self.updated_at.strftime(
                    "%Y-%m-%dT%H:%M:%S.%f")
        if 'created_at' in cp_dct:
            cp_dct['created_at'] = self.created_at.strftime(
                    "%Y-%m-%dT%H:%M:%S.%f")
        if '_sa_instance_state' in cp_dct:
            del cp_dct['_sa_instance_state']
        return (cp_dct)

    def delete(self):
        """
        to delete the current instance from the storage
        """
        models.storage.delete(self)
