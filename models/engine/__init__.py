#!/usr/bin/python3
'''
    Package initializer
'''

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Explicitly import FileStorage
from models.engine.file_storage import FileStorage

# Define the classes dictionary
classes = {
    "User": User,
    "BaseModel": BaseModel,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

# Create an instance of FileStorage
storage = FileStorage()

# Reload data from the file, if available
storage.reload()
