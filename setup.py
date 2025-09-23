" defines configuration of our project"

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    "this func returns list of requiremenets"
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # reading lines from file
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                # ignore empty lines and -e .
                if requirements and requirements!= '-e .':
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network Securirty",
    version="0.0.1",
    author="Aishwarya Mishra",
    author_email="2k23.csaiml2313622@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
