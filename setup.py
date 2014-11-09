#!/usr/bin/env python

from distutils.core import setup

setup(name='threeplot',
      description='Browser-based 3D plotting, with zero dependencies',
      version='0.1',
      author='Alex Flint',
      author_email='alex.flint@gmail.com',
      url='http://alexflint.github.io/threeplot/',
      packages=['threeplot'],
      package_data={'threeplot': ['templates/*.html']}
      )
