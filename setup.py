from setuptools import setup, find_packages
import sys, os

version = '0.2.1'

setup(name='provtool',
      version=version,
      description="Utility for working with iOS Provisioning Profiles",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ios provisioning',
      author='Andy Mroczkowski',
      author_email='andy@mindsnacks.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points= {
          'console_scripts': [
              'provtool = provtool:main',
              ],
          }
      )
