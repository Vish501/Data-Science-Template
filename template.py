import os
import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files and directories that need to be created or amended with new files
list_of_files = [
    "data/.gitkeep",
    "docs/.gitkeep",
    "models/.gitkeep",
    "notebooks/.gitkeep",
    "references/.gitkeep",
    "reports/figures/.gitkeep",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/make_dataset.py",
    "src/features/__init__.py",
    "src/features/build_features.py",
    "src/models/__init__.py",
    "src/models/predict_model.py",
    "src/models/train_model.py",
    "src/visualization/__init__.py",
    "src/visualization/plot_settings.py",
    "src/visualization/visualize.py",
    "app.py",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # If the directory does not exist create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir}')
    
    # If the file within the directory does not exist 
    # or the size of the file is 0, then create the file
    # Else if the file already exists within the specified path, log that it already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
        