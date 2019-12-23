# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in practiceapp/__init__.py
from practiceapp import __version__ as version

setup(
	name='practiceapp',
	version=version,
	description='For Practice Purpose',
	author='kushal.shah',
	author_email='kushal.shah@finbyz.tech',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
