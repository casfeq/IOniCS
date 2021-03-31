from setuptools import setup


setup(
	name='IOniCS',
	version='0.0.1',
	author='Carlos A. S. Ferreira',
	author_email='casf.eq@gmail.com',
	description=('This package intends to provide tools for FEniCS and multiphenics problem solving environments.'),
	long_description=open('ionics/README.md', 'r').read(),
	packages=['ionics'],
	license='BSD',
	url='https://github.com/casfeq/IOniCS'
)