# setup.py

# built-in packages
import os
from setuptools import setup

setup(
    name='branchapi',
    version='1.0.0',
    description='Download data in csv format',
    author='Kartik Shandilya',
    packages=['branchapi'],
    author_email="kartik.shandilya@branch.io",
    include_package_data = True,
    install_requires = ['requests']
    )