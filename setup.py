# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in income_statement/__init__.py
from income_statement import __version__ as version

setup(
	name='income_statement',
	version=version,
	description='Report to generate gross profit and net profit',
	author='Anju Prasannan',
	author_email='anjuprasannan321@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
