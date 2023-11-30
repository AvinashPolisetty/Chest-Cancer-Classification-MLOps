from setuptools import setup,find_packages
from typing import List


Hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements

setup(
    name="chest-cancer-classifier",
    version="0.0.0",
    author="avinash",
    author_email="avinashpolisetty456@gmail.com",
    description="a project that is used to classify the chest cancer",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)