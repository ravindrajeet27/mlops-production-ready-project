import os
from datetime import date
DATABASE_NAME = "Us_Visa"

COLLECTION_NAME = "Visa_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME = "usvisa"

ARTIFACT_DIR = "artifact"

MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constants
"""

DATA_INGESTION_COLLECTION_NAME = "Visa_data"

DATA_INGESTION_DIR_NAME = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_INGESTION_INGESTED_DIR = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2