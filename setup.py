from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt', 'r') as f:
    required_libraries = f.read().splitlines()

setup(
    name='Galaxy',  
    version='0.1.0',  
    description='Description of your project',# Write a proper description 
    author='Prashanth',
    author_email='prashanth01071995@gmail.com',
    packages=find_packages(),
    install_requires=required_libraries,
)
