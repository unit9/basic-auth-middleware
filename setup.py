"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='basic-auth-middleware',
    version='1.0.1',
    description='A WSGI middleware providing HTTP Basic Auth',
    long_description=long_description,
    url='https://github.com/unit9/basic-auth-middleware',
    author='UNIT9',
    author_email='root@unit9.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['basic_auth_middleware'],
    install_requires=[
        'netaddr>=0.7.19',
    ],
)
