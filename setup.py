#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize


ext_modules = [Extension('maxentpy._hashseq', ['maxentpy/_hashseq.pyx'])]

setup(name='maxentpy',
      description='Calculate splice site strength',
      url='https://github.com/kepbod/maxentpy',
      packages=['maxentpy'],
      package_data={'maxentpy': ['data/*']},
      ext_modules=cythonize(ext_modules),
      install_requires=['msgpack-python', 'Cython']
      )
