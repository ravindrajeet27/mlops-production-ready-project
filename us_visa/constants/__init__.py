import os
from datetime import date
DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME = "usvisa"

ARTIFACT_DIR = "artifact"

MODEL_FILE_NAME = "model.pkl"


TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
Data Ingestion related constants
"""

DATA_INGESTION_COLLECTION_NAME = "visa_data"

DATA_INGESTION_DIR_NAME = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_INGESTION_INGESTED_DIR = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

"""
Data Validation related constants
"""
DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR_NAME = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"
