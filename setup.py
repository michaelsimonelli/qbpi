#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'sortedcontainers>=1.5.9',
    'requests>=2.13.0',
    'six>=1.10.0',
    'websocket-client>=0.40.0',
    'pymongo>=3.5.1',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qoinbase',
    version='0.0.1',
    author='Michael Simonellli',
    author_email='michael@simo.live',
    license='MIT',
    url='https://github.com/michaelsimonelli/qoinbase-python',
    packages=find_packages(),
    install_requires=install_requires,
    description='Python client for the Coinbase Pro API - integrates with qoinbase-q',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
