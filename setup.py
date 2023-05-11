from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #to read line by line
        requirements=[req.replace("\n","")for req in requirements] #replacing \n with space

        if HYPHEN_E_DOT in requirements: #whenever we use -e. the setup.py will start running (trigger setup.py)
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Akanksh',
    author_email='akankshs.01@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)