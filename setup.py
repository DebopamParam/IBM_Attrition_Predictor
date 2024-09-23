from typing import List
from setuptools import setup, find_packages

# -e . is an indication to install the package in editable mode, 
# which means that the package is installed in such a way that changes to
# the source files will immediately affect the installed package without needing to reinstall it.

# Setup.py will automatically build the package when the version number is changed/requirements are updated.
MINUS_E_DOT = "-e ."


def get_requirements(filepath: str) -> List[str]:
    """Reads the requirements file and returns a list of requirements."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"Content of {filepath}:\n{content}")
            requirements = content.splitlines()
            # Removes the '\n' at the end of each line
            
            requirements = [requirement.strip() for requirement in requirements]
            if MINUS_E_DOT in requirements:
                requirements.remove(MINUS_E_DOT)
        print(f"Requirements: {requirements}")
        return requirements
    except UnicodeDecodeError as e:
        print(f"Error reading {filepath}: {e}")
        raise


setup(
    name="IBM Attrition Prediction",
    version="0.0.1",  # version number, we can change it in the future, & it will trigger automatic build of the package
    author="Debopam Chowdhury",
    author_email="debopamwork@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
