import os #used for files and directory management
import sys  #used for exception handling and system-specific parameters

from pandas import DataFrame
from sklearn.model_selection import train_test_split
from streamlit import dataframe

from us_visa.entity.config_entity import DataIngestionConfig 
# contains the configuration for data ingestion, such as file paths  and test size
from us_visa.entity.artifact_entity import DataIngestionArtifact
# Stores the output of the Data Ingestion stage
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USvisaData
# It separates database logic from pipeline logic.

class DataIngestion:
    

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:

            dataframe = self.export_data_into_feature_store()

            
            print(dataframe.shape)
            print(dataframe.head())
            self.split_data_as_train_test(dataframe)

            data_ingestion_artifact = DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                training_file_path=self.data_ingestion_config.training_file_path,
                testing_file_path=self.data_ingestion_config.testing_file_path
            )

            logging.info("Data Ingestion completed successfully.")

            return data_ingestion_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e

    def export_data_into_feature_store(self) -> DataFrame:
        """
        Fetches data from the database and saves it to the feature store.

        Returns:
            DataFrame: The fetched data as a pandas DataFrame.
        """
        try:
            # Fetch data from MongoDB
            usvisa_data = USvisaData()
            df = usvisa_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )

            logging.info("Successfully exported data from MongoDB.")

            # Create feature store directory
            feature_store_dir = os.path.dirname(
                self.data_ingestion_config.feature_store_file_path
            )
            os.makedirs(feature_store_dir, exist_ok=True)

            # Save dataframe to feature store
            df.to_csv(
                self.data_ingestion_config.feature_store_file_path,
                index=False,
                header=True
            )

            logging.info(
                f"Feature store file saved at: "
                f"{self.data_ingestion_config.feature_store_file_path}"
            )

            return df

        except Exception as e:
            raise USvisaException(e, sys) from e
        



    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )

            dir_path = os.path.dirname(
                self.data_ingestion_config.training_file_path
            )
            os.makedirs(dir_path, exist_ok=True)

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False,
                header=True
            )

            logging.info("Train and Test files saved successfully.")

        except Exception as e:
            raise USvisaException(e, sys) from e   
        try:
        # Fetch data from MongoDB
            usvisa_data = USvisaData()
            df = usvisa_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )

            logging.info("Successfully exported data from MongoDB.")

            # Create feature store directory
            feature_store_dir = os.path.dirname(
                self.data_ingestion_config.feature_store_file_path
            )
            os.makedirs(feature_store_dir, exist_ok=True)

            # Save dataframe to feature store
            df.to_csv(
                self.data_ingestion_config.feature_store_file_path,
                index=False,
                header=True
            )

            logging.info(
                f"Feature store file saved at: "
                f"{self.data_ingestion_config.feature_store_file_path}"
            )

            return df

        except Exception as e:
            raise USvisaException(e, sys) from e
        
    def run_pipeline(self) -> DataIngestionArtifact:
        try:
            return self.initiate_data_ingestion()

        except Exception as e:
            raise USvisaException(e, sys) from e