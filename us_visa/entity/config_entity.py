import os
from dataclasses import dataclass, field
from datetime import datetime

from us_visa.constants import *

TIMESTAMP = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


@dataclass
class DataIngestionConfig:
    training_pipeline_config: TrainingPipelineConfig

    data_ingestion_dir: str = field(init=False)
    feature_store_file_path: str = field(init=False)
    training_file_path: str = field(init=False)
    testing_file_path: str = field(init=False)

    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME

    def __post_init__(self):
        self.data_ingestion_dir = os.path.join(
            self.training_pipeline_config.artifact_dir,
            DATA_INGESTION_DIR_NAME
        )

        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_FEATURE_STORE_DIR,
            "usvisa.csv"
        )

        self.training_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_INGESTED_DIR,
            "train.csv"
        )

        self.testing_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_INGESTED_DIR,
            "test.csv"
        )