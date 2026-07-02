import os
import sys
import dill
import yaml
import numpy as np

from us_visa.exception import USvisaException
from us_visa.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USvisaException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes data to a YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise USvisaException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    """
    Saves any Python object using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        raise USvisaException(e, sys) from e


def load_object(file_path: str) -> object:
    """
    Loads a pickled Python object.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise USvisaException(e, sys) from e
    

import dill
import numpy as np

from us_visa.exception import USvisaException
from us_visa.logger import logging


def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Load NumPy array data from a file.

    Args:
        file_path (str): Path of the file to load.

    Returns:
        np.ndarray: Loaded NumPy array.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise USvisaException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Save NumPy array data to a file.

    Args:
        file_path (str): Path where the NumPy array will be saved.
        array (np.ndarray): NumPy array to save.

    Returns:
        None
    """
    try:
        logging.info("Entered the save_numpy_array_data method of utils")

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)

        logging.info("NumPy array saved successfully.")

    except Exception as e:
        raise USvisaException(e, sys) from e   

from pandas import DataFrame

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Drop specified columns from a DataFrame.

    Args:
        df (DataFrame): Input DataFrame.
        cols (list): List of columns to drop.

    Returns:
        DataFrame: DataFrame after dropping the specified columns.
    """
    logging.info("Entered drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Columns dropped successfully.")
        return df

    except Exception as e:
        logging.error("Exception occurred while dropping columns.")
        raise USvisaException(e, sys) from e    


