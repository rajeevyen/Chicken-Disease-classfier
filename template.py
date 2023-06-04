import os
from pathlib import Path
import logging 

#logs
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# project name as cnnClassifier: using generic name cause want to use for another project
project_name = "cnnClassifier"


#creatting folders:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",#Constructor
    f"src/{project_name}/components/__init__.py", # another folder called components, so created another constructor
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    #need some more files
    "config/config.yaml",
    "dvc.yaml",#Mlops tool:dvc
    "params.yaml",#parameters
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)#tuple: one is folder and another one is file name

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #file exists or nor || may be readme files have less size but not 0
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}") #logs


    else:
        logging.info(f"{filename} is already exists")
