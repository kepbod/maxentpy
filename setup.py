#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.extension import Extension


ext_modules = [Extension('maxentpy._hashseq', ['maxentpy/_hashseq.c'])]

setup(name='maxentpy',
      version='0.0.2',
      description='Calculate splice site strength',
      url='https://github.com/kepbod/maxentpy',
      packages=['maxentpy'],
      package_data={'maxentpy': ['data/*']},
      ext_modules=ext_modules,
      install_requires=['msgpack-python']
      )
