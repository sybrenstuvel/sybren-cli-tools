#!/usr/bin/env python

__author__ = 'Sybren A. Stüvel'
__version__ = '0.1'


# Check the Python version
import sys

if sys.version_info[:2] < (3, 4):
    raise SystemExit("Sorry, Python 3.4 or newer required")

from setuptools import setup

setup(
    name='mkv-edit',
    version=__version__,
    author='Sybren A. Stüvel',
    author_email='sybren@stuvel.eu',
    maintainer='Sybren A. Stüvel',
    maintainer_email='sybren@stuvel.eu',
    description='Simple CLI scripts to do stuff.',
    packages=['sybren_cli_tools'],
    license='Python',
    classifiers=[
        'License :: OSI Approved :: Python License (CNRI Python License)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'enzyme>=0.4.1',  # for mkvedit
    ],
    zip_safe=True,
    entry_points={'console_scripts': [
        'mkv-edit-deactivate-subtitles = sybren_cli_tools.mkvedit:deactivate_subtitles',
    ]},
)
