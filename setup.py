from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filename:str) -> List[str]:
    '''
        requirement List
    '''

    requirements = []

    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'dsproject',
    version = '0.0.1',
    author = 'sid',
    author_email = 'naiksiddhesh110@gmil.com',
    packages = find_packages(),
    install_required = get_requirements("requirements.txt")
)