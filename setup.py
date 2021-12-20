# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in saiotx/__init__.py
from saiotx import __version__ as version

setup(
	name='saiotx',
	version=version,
	description='Saiotes',
	author='MiM',
	author_email='mismail@datavaluenet.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
