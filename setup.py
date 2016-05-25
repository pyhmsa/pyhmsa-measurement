#!/usr/bin/env python

# Standard library modules.
import os
import codecs

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
import versioneer

# Globals and constants variables.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

packages = find_packages()

cmdclass = versioneer.get_cmdclass()

setup(name='pyHMSA-measurement',
      version=versioneer.get_version(),
      description='Additional condition for pyHMSA',
      long_description=long_description,

      author='Philippe Pinard',
      author_email='philippe.pinard@gmail.com',
      maintainer='Philippe Pinard',
      maintainer_email='philippe.pinard@gmail.com',

      url='http://pyhmsa.readthedocs.org',
      license='MIT',
      keywords='microscopy microanalysis hmsa file format',

      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Physics',
        ],

      packages=packages,

      install_requires=['pyhmsa'],
#       tests_require=['Pillow', 'nose', 'coverage'],

      zip_safe=False,

      test_suite='nose.collector',

    entry_points=\
      {'pyhmsa.fileformat.xmlhandler.condition':
          ['MeasurementPeak = pyhmsa_measurement.fileformat.xmlhandler.condition.measurement:MeasurementPeakXMLHandler',
           'MeasurementBackground = pyhmsa_measurement.fileformat.xmlhandler.condition.measurement:MeasurementBackgroundXMLHandler',
           'MeasurementNet = pyhmsa_measurement.fileformat.xmlhandler.condition.measurement:MeasurementNetXMLHandler',]
      },

      cmdclass=cmdclass,
     )
