from setuptools import setup,find_packages

def get_requirements(file_path):
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.strip() for req in requirement]
    
    return requirement

setup(
    name='ChatBot',
    version='0.0.1',
    author='Reyan',
    author_email='reyanalam115@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
)