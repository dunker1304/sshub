import sys
from setuptools import setup, find_packages

VERSION='0.0.1'
DESCRIPTION='A command line tool to manage your ssh connections'

setup(
  name='sshub',
  version=VERSION,
  author='Dunk',
  author_email='dunker1304@gmail.com',
  description=DESCRIPTION,
  license='MIT',
  packages=find_packages(),
  install_requires=[],
  keywords=['python', 'sshub', 'ssh connections'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: MIT License',
    'Topic :: System :: Systems Administration',
  ]
)