from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np



class USvisaData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e,sys)

    def export_collection_as_dataframe(
    self,
    collection_name: str,
    database_name: Optional[str] = None
) -> pd.DataFrame:
        try:
            """
            Export entire collection as a pandas DataFrame.
            """

            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            print("Database:", self.mongo_client.database.name)
            print("Collection:", collection_name)

            documents = list(collection.find())

            print("Number of documents:", len(documents))
            print("First document:", documents[:1])

            df = pd.DataFrame(documents)

            if "_id" in df.columns:
                df = df.drop(columns=["_id"])

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise USvisaException(e, sys)