#!/usr/bin/python3
'''
    Initializing Packages
'''

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.usr import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

classes = {"User": User, "BaseModel": BaseModel,
            "Place": Place, "State": State,
            "City": City, "Amenity": Amenity,
            "Review": Review}

if os.getenv('HBNH_TYPE_STORAGE') == 'db':
    from models.engine.db_stroage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
