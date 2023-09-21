#!/usr/bin/python3
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv

# Check the 'HBNB_TYPE_STORAGE' environmental variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()  # Instantiate a database storage engine
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()  # Instantiate a file storage engine

storage.reload()  # Reload data into the storage engine
