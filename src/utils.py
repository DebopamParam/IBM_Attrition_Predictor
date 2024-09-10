# Anything that maybe used in the entire application is written here
# For example: 
# - if we want to read from a MongoDB database, we can write the mongo 
# connection here and use it in the entire application
# - Save a model to the Cloud we can do it over here

import os, sys
import dill


from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file:
            dill.dump(obj, file)

    except Exception as e:
        raise CustomException(e, sys) from e

def load_object(file_path):
    try:
        with open(file_path, "rb") as file:
            obj = dill.load(file)
        return obj

    except Exception as e:
        raise CustomException(e, sys) from e