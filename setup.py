#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import eulasees
version = eulasees.__version__

setup(
    name='eulasees',
    version=version,
    description="Django project for eulasees koding hackathon project",
    author='Johnny Gill',
    author_email='swfiua@gmail.com',
    packages=[
        'eulasees',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['eulasees/manage.py'],
)
