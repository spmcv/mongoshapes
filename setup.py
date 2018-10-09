#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


packages = find_packages(
    exclude=['tests']
)

install_requirements = [
    'pymongo>=3.7.1',
    'mongoengine>=0.15.3',
    'shapely>=1.6.4',
    'pyproj'
]

setup_requirements = [
    'pyyaml>=3.13',
    'pytest>=3.8',
    'pytest-pep8',
    'pytest-mypy',
    'pytest-cov'
]

classifiers = [
    "Development Status :: 4 - Beta"
    "Intended Audience :: Developers"
    "Intended Audience :: Science/Research"
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
    "Topic :: Database",
    "Topic :: Scientific/Engineering :: GIS"
]

setup(
    name='mongoshapes',
    version='0.1.1',
    packages=packages,
    url='https://github.com/phuntimes/mongoshapes',
    license='MIT License',
    author='Sean McVeigh',
    author_email='spmcveigh@gmail.com',
    description='Shapely integration for MongoEngine',
    install_requires=install_requirements,
    setup_requires=setup_requirements,
    classifiers=classifiers
)
