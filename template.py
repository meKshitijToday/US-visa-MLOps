# To create structure of files using script

import os
from pathlib import Path

project_name="us_visa"

# constructor file is required in every folder as this is modular coding, so, we have to 
# use component in some other file by importing that file and folder using constructor package
# Every folder should have constructor file

list_of_files=[
    f"{project_name}/__init__.py",
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
    f"{project_name}/entity/artificat_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=filepath.parent, filepath.name
    print("filedir: ", filedir,"; filename: ", filename)
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write("")
    print(f"Created {filepath}")
print("All files created successfully")
