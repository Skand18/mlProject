from setuptools import find_packages, setup
from typing import List

hypne = '-e.'


def get_requirements(file_path: str) -> List[str]:
    '''
     get requirements from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if hypne in requirements:
            requirements.remove(hypne)


setup(
    name='mlproject',
    version='0.0.1',
    author='skand',
    author_email='skandk61@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
