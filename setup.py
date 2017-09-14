import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='yetanotherhackernews',
      version='0.0.1',
      packages=['yetanotherhackernews'],
      install_requires=required,
      zip_safe=False)