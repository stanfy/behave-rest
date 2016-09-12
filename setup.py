#!/usr/bin/env python

from setuptools import setup
import behave_rest


long_description = open('README.rst', 'r').read()

install_requires = [
    'behave>=1.2.5',
    'nose>=1.3.7',
    'requests>=2.10.0',
    'trafaret>=0.7.1',
    'jpath>=1.5'
]

setup(
    name='behave-rest',
    version=behave_rest.__version__,
    packages=['behave_rest', 'behave_rest.steps'],
    install_requires=install_requires,
    description="BDD-style Rest API testing tool",
    long_description=long_description,
    url='https://github.com/stanfy/behave-rest',
    license='Apache Software License',
    author='Oleg Nikiforov',
    author_email='nikiphor@hotmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
