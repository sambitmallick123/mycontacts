#!/usr/bin/env python
from setuptools import setup

with open("README.md", 'r') as f:
   long_description = f.read()
version='1.0'

setup(
   name='mycontacts',
   version='1.0',
   description='mycontacts - add new contacts, show contact details, display contact list',
   long_description=long_description,
   license='Sambit',
   url='https://github.com/sambitmallick123/mycontacts',
   author='Sambit Mallick',
   author_email='sambitmallick123@gmail.com',
   packages=['mycontacts'],
   package_dir={'mycontacts': 'mycontacts'},
   package_data={'mycontacts': ['data/test.yaml'],}
)
