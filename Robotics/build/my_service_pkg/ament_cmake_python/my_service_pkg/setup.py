from setuptools import find_packages
from setuptools import setup

setup(
    name='my_service_pkg',
    version='0.0.0',
    packages=find_packages(
        include=('my_service_pkg', 'my_service_pkg.*')),
)
