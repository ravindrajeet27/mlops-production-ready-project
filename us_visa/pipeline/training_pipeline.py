import sys

from us_visa.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
)

from us_visa.components.data_ingestion import DataIngestion
from us_visa.exception import USvisaException
from us_visa.logger import logging


class TrainingPipeline:
    """
    Training Pipeline Class
    """

    def __init__(self):
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise USvisaException(e, sys) from e

    def start_data_ingestion(self):
        """
        Starts the Data Ingestion Component
        """
        try:
            logging.info("Starting Data Ingestion...")

            data_ingestion_config = DataIngestionConfig(
                training_pipeline_config=self.training_pipeline_config
            )

            data_ingestion = DataIngestion(
                data_ingestion_config=data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.run_pipeline()

            logging.info("Data Ingestion completed successfully.")

            return data_ingestion_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e

    def run_pipeline(self):
        """
        Runs the complete training pipeline.
        """
        try:
            logging.info("Training Pipeline Started")

            data_ingestion_artifact = self.start_data_ingestion()

            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

            logging.info("Training Pipeline Completed Successfully")

        except Exception as e:
            raise USvisaException(e, sys) from e