#!/usr/bin/env python
import os.path
from pathlib import Path

import setuptools

def long_description():
    """Return the contents of the readme."""
    r_path=Path('readme.md')
    with r_path.open('r', encoding='utf-8') as r_fh:
        r_str = r_fh.read()
    return r_str

def get_version():
    """Return the current version of the package."""
    with Path('version').open('r', encoding='utf-8') as v_fh:
        version = v_fh.read()
    return version

setuptools.setup(
    author_email='daveshawley+python@gmail.com',
    author='Dave Shawley',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Sphinx :: Extension',
    ],
    description='Describe JSON document structures in sphinx',
    install_requires=[
        'faker'
        'sphinx',
    ],
    license='BSD',
    long_description=long_description(),
    name='sphinx-jsondomain',
    py_modules=['sphinxjsondomain'],
    url='https://github.com/edwardtheharris/sphinx-jsondomain',
    version=get_version(),
)
