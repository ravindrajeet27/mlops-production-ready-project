import os
import sys
import certifi
import pymongo

from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.exception import USvisaException
from us_visa.logger import logging


ca = certifi.where()


class MongoDBClient:
    """
    Class Name : MongoDBClient

    Description :
        This class establishes a connection to the MongoDB database.

    Output :
        MongoDB database connection

    On Failure :
        Raises USvisaException
    """

    client = None

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is None:
                    raise Exception(
                        f"Environment variable '{MONGODB_URL_KEY}' is not set."
                    )

                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )

                logging.info("MongoDB connection established successfully.")

            self.client = MongoDBClient.client
            self.database = self.client[database_name]

        except Exception as e:
            raise USvisaException(e, sys) from e