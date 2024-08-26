from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPEN_E_DOT]
       


    return requirements




setup(
name = "ML Project",
version = "0.0.1",
author = "Santhosh Kumar M",
author_email = "santhoshkumar082003@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")
)
