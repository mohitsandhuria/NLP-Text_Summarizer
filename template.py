import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name="text_summarizer"
list_file=[
    f".github/worlflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"config/config.yaml",
    f"params.yaml",
    f"app.py",
    f"main.py",
    f"Dockerfile",
    f"requirements.txt",
    f"setup.py",
    f"research/trials.ipynb"
]



for files in list_file:
    file_path=Path(files)
    print(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating files:{filename} and directories: {filedir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating files:{file_path}")
    
    else:
        logging.info(f"file already exist:{file_path}")

# Set-ExecutionPolicy RemoteSigned -Scope Process
