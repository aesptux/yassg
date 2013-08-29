#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.md').read()

setup(
    name='yassg',
    version='0.0.1',
    description='Yet Another Static Site Generator',
    long_description=readme + '\n\n' + history,
    author='Adrian Espinosa Moreno',
    author_email='aespinosamoreno@gmail.com',
    url='https://github.com/aesptux/yassg',
    packages=[
        'yassg',
    ],
    package_dir={'yassg': 'yassg'},
    include_package_data=True,
    install_requires=[
    ],
    license="Apache 2.0",
    zip_safe=False,
    keywords='yassg',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)