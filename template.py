import os
from pathlib import Path

project_name = "us_visa"
list_of_files = [ 
    
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py"
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",

]


# 3. Loop through the list to create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Handles slashes for Windows/Mac/Linux
    filedir, filename = os.path.split(filepath)

    # Create parent folders if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Created directory: {filedir}")

    # Create the empty file if it does not exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creates an empty file
        print(f"Created empty file: {filepath}")
    else:
        print(f"{filename} already exists")