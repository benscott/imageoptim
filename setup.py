"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='image_optim',
  version='0.0.1',
  description='Access Image Optim API Python',
  long_description=long_description,
  url='https://github.com/benscott/image_optim_api',
  author='Ben Scott',
  author_email='ben@benscott.co.uk',
  license='MIT',
  keywords='image image_optim',
  packages=find_packages(exclude=['tests']),
  install_requires=['requests', 'Pillow'],
)
