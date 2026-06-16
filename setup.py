#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize


ext_modules = cythonize(
    [Extension('maxentpy._hashseq', ['maxentpy/_hashseq.pyx'])],
    language_level='3',
)

setup(name='maxentpy',
      version='0.0.3',
      description='Calculate splice site strength',
      url='https://github.com/kepbod/maxentpy',
      packages=['maxentpy'],
      package_data={'maxentpy': ['data/*']},
      ext_modules=ext_modules,
      install_requires=['msgpack-python']
      )
