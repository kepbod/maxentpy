#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='maxentpy',
      description='Calculate splice site strength',
      url='https://github.com/kepbod/maxentpy',
      packages=['maxentpy'],
      package_data={'maxentpy': ['data/*.txt']}
      )
