import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name="text_summarizer"
folder="Text_Summarizer"
list_file=[
    f"{folder}/.github/worlflows/.gitkeep",
    f"{folder}/src/{project_name}/__init__.py",
    f"{folder}/src/{project_name}/components/__init__.py",
    f"{folder}/src/{project_name}/utils/__init__.py",
    f"{folder}/src/{project_name}/utils/common.py",
    f"{folder}/src/{project_name}/logging/__init__.py",
    f"{folder}/src/{project_name}/config/configuration.py",
    f"{folder}/src/{project_name}/pipeline/__init__.py",
    f"{folder}/src/{project_name}/entity/__init__.py",
    f"{folder}/src/{project_name}/constants/__init__.py",
    f"{folder}/config/config.yaml",
    f"{folder}/params.yaml",
    f"{folder}/app.py",
    f"{folder}/main.py",
    f"{folder}/Dockerfile",
    f"{folder}/requirements.txt",
    f"{folder}/setup.py",
    f"{folder}/research/trials.ipynb"
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

