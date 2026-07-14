import os

print("MONGODB_URL =", os.getenv("MONGODB_URL"))

from us_visa.pipeline.training_pipeline import TrainingPipeline
obj = TrainingPipeline()
obj.run_pipeline()