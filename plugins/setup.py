import os
from setuptools import setup, find_packages

setup(
    name='sdns',
    version='1.0',
    description='A Netbox plugin that brings Dns informations',
    url='https://github.com/netsinfoo/plugin-dns',
    author='Manoel Bezerra',
    license='GNU General Public License v3.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    )