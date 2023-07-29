from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt', 'r') as f:
    required_libraries = f.read().splitlines()

setup(
    name='Galaxy',  # Replace with your project name
    version='0.1.0',  # Replace with the desired version number
    description='Description of your project',
    author='Prashanth',
    author_email='prashanth01071995@gmail.com',
    packages=find_packages(),
    install_requires=required_libraries,
    # Add other metadata such as license, url, etc. if needed
)
